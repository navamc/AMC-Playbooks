"""
AMC Reporting Engine
SQLite Database Library
"""

import sqlite3

from config import DATABASE


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

    def save_report_run(self, workflow_name, status):

        self.cursor.execute(
            """
            INSERT INTO report_runs
            (
                workflow_name,
                status
            )
            VALUES
            (?,?)
            """,
            (workflow_name, status)
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
