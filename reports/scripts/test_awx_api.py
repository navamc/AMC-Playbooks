import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AWX_URL = "https://awx.amc.com"
TOKEN = "chpjcnLn6GqRZG4phywk96zOLBPEIu"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

JOB_ID = 193

response = requests.get(
    f"{AWX_URL}/api/v2/jobs/{JOB_ID}/job_events/",
    headers=headers,
    verify=False,
    timeout=30
)

print("HTTP Status:", response.status_code)
print()
print(json.dumps(response.json(), indent=4))
