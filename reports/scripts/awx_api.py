"""
AMC Reporting Engine
AWX API Library
"""

import requests
import urllib3

from config import *

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)


class AWXAPI:

    def __init__(self):

        self.base_url = AWX_URL

        self.headers = {
            "Authorization": f"Bearer {AWX_TOKEN}"
        }

    def get_latest_workflow(self):

        response = requests.get(
            f"{self.base_url}/api/v2/workflow_jobs/?order_by=-id&page_size=1",
            headers=self.headers,
            verify=AWX_VERIFY_SSL,
            timeout=30
        )

        response.raise_for_status()

        return response.json()["results"][0]

    def get_workflow_nodes(self, workflow_id):

        response = requests.get(
            f"{self.base_url}/api/v2/workflow_jobs/{workflow_id}/workflow_nodes/",
            headers=self.headers,
            verify=AWX_VERIFY_SSL,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_job_events(self, job_id):

        response = requests.get(
            f"{self.base_url}/api/v2/jobs/{job_id}/job_events/",
            headers=self.headers,
            verify=AWX_VERIFY_SSL,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_job_details(self, job_id):

        response = requests.get(
            f"{self.base_url}/api/v2/jobs/{job_id}/",
            headers=self.headers,
            verify=AWX_VERIFY_SSL,
            timeout=30
        )

        response.raise_for_status()

        return response.json()
