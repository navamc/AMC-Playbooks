from awx_api import AWXAPI

api = AWXAPI()

events = api.get_job_events(284)

print(f"Total Events : {len(events)}")
print()

for event in events:
    if event["host_name"]:
        print(
            event["event"],
            "|",
            event["host_name"],
            "|",
            event["task"]
        )
