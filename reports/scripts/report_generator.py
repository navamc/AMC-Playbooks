"""
AMC Reporting Engine
Report Generator
Reads data from SQLite
"""

import sqlite3

from config import DATABASE


class ReportGenerator:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

    def get_latest_run(self):

        self.cursor.execute("""
            SELECT *
            FROM report_runs
            ORDER BY id DESC
            LIMIT 1
        """)

        return self.cursor.fetchone()

    def get_jobs(self, run_id):

        self.cursor.execute("""
            SELECT *
            FROM report_jobs
            WHERE run_id=?
            ORDER BY id
        """, (run_id,))

        return self.cursor.fetchall()

    def close(self):

        self.conn.close()
