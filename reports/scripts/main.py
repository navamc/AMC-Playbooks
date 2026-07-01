"""
AMC Reporting Engine
Main Program
"""

from awx_api import AWXAPI
from database import Database
from health_analyzer import HealthAnalyzer
from html_report import HTMLReport

print("-------------------------------------")
print(" AMC Reporting Engine v1.0")
print("-------------------------------------")
print()

# ----------------------------------------------------
# Connect to AWX
# ----------------------------------------------------

api = AWXAPI()

print("Connecting to AWX...")

workflow = api.get_latest_workflow()

print("Connection Successful")
print()

# ----------------------------------------------------
# Display Workflow
# ----------------------------------------------------

print("Latest Workflow")
print("------------------------------")

print("ID      :", workflow["id"])
print("Name    :", workflow["name"])
print("Status  :", workflow["status"])
print()

# ----------------------------------------------------
# Connect to Database
# ----------------------------------------------------

print("Connecting to SQLite...")

db = Database()

run_id = db.save_report_run(
    workflow["name"],
    workflow["status"]
)

print("Run ID :", run_id)
print()

# ----------------------------------------------------
# Read Workflow Nodes
# ----------------------------------------------------

print("Reading workflow nodes...")

nodes = api.get_workflow_nodes(workflow["id"])

print("Nodes found :", len(nodes["results"]))
print()

# ----------------------------------------------------
# Save Each Job
# ----------------------------------------------------

for node in nodes["results"]:

    summary = node.get("summary_fields", {})

    job = summary.get("job")

    if not job:
        continue

    job_id = job["id"]

    print("Processing Job", job_id)

    details = api.get_job_details(job_id)

    hostname = details.get("inventory", "Unknown")

    playbook = details.get("playbook", "Unknown")

    status = details.get("status", "Unknown")

    db_job_id = db.save_job(
        run_id,
        str(hostname),
        playbook,
        status
    )

    events = api.get_job_events(job_id)

    for event in events:

        if not event["host_name"]:
            continue

        db.save_host_result(
            run_id=run_id,
            job_id=db_job_id,
            hostname=event["host_name"],
            task_name=event["task"],
            event=event["event"],
            changed=int(event["changed"]),
            failed=int(event["failed"])
        )

print()

db.close()

print()

print("Analyzing Host Health...")

health = HealthAnalyzer()

health.analyze(run_id)

health.close()

print("Health Analysis Completed")

print()

print("Generating HTML Report...")

html = HTMLReport()

filename = html.generate(run_id)

print("HTML Report Created")

print(filename)

print()

print("Reporting Engine Completed Successfully")
