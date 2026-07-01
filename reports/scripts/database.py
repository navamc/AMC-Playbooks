"""
AMC Reporting Engine
SQLite Database Library
"""

import sqlite3

from datetime import datetime
from zoneinfo import ZoneInfo

from config import DATABASE
from config import TIMEZONE


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

    def save_report_run(self, workflow_name, status):

        run_date = datetime.now(
            ZoneInfo(TIMEZONE)
        ).strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute(
            """
            INSERT INTO report_runs
            (
                run_date,
                workflow_name,
                status
            )
            VALUES
            (?, ?, ?)
            """,
            (
                run_date,
                workflow_name,
                status
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def close(self):

        self.conn.close()

    def save_job(self, run_id, hostname, playbook, status):

        self.cursor.execute(
            """
            INSERT INTO report_jobs
            (
                run_id,
                hostname,
                playbook,
                status
            )
            VALUES
            (?, ?, ?, ?)
            """,
            (
                run_id,
                hostname,
                playbook,
                status
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def save_host_result(
        self,
        run_id,
        job_id,
        hostname,
        task_name,
        event,
        changed,
        failed
    ):

        self.cursor.execute(
            """
            INSERT INTO host_results
            (
                run_id,
                job_id,
                hostname,
                task_name,
                event,
                changed,
                failed
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                run_id,
                job_id,
                hostname,
                task_name,
                event,
                changed,
                failed
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def save_host_summary(
        self,
        run_id,
        hostname,
        successful_tasks,
        failed_tasks,
        unreachable_tasks,
        changed_tasks,
        health_status
    ):

        self.cursor.execute(
            """
            INSERT INTO host_summary
            (
                run_id,
                hostname,
                successful_tasks,
                failed_tasks,
                unreachable_tasks,
                changed_tasks,
                health_status
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                run_id,
                hostname,
                successful_tasks,
                failed_tasks,
                unreachable_tasks,
                changed_tasks,
                health_status
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid
