"""
AMC Reporting Engine
HTML Report Generator
"""

import os
from jinja2 import Environment, FileSystemLoader

from config import COMPANY_NAME
from config import REPORT_TITLE
from config import OUTPUT_HTML

from report_generator import ReportGenerator


class HTMLReport:

    def generate(self):

        report = ReportGenerator()

        workflow = report.get_latest_run()

        jobs = report.get_jobs(workflow["id"])

        env = Environment(
            loader=FileSystemLoader("../templates")
        )

        template = env.get_template("daily_health.html.j2")

        html = template.render(
            company=COMPANY_NAME,
            report_title=REPORT_TITLE,
            workflow=workflow,
            jobs=jobs
        )

        os.makedirs(OUTPUT_HTML, exist_ok=True)

        filename = os.path.join(
            OUTPUT_HTML,
            "daily_report.html"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

        report.close()

        return filename
