"""
AMC Reporting Engine
Health Analyzer
"""

from collections import defaultdict

from database import Database


class HealthAnalyzer:

    def __init__(self):

        self.db = Database()

    def analyze(self, run_id):

        self.db.cursor.execute(
            """
            SELECT
                hostname,
                event,
                changed,
                failed
            FROM host_results
            WHERE run_id=?
            """,
            (run_id,)
        )

        rows = self.db.cursor.fetchall()

        hosts = defaultdict(
            lambda: {
                "successful": 0,
                "failed": 0,
                "unreachable": 0,
                "changed": 0
            }
        )

        for hostname, event, changed, failed in rows:

            if event == "runner_on_ok":
                hosts[hostname]["successful"] += 1

            elif event == "runner_on_failed":
                hosts[hostname]["failed"] += 1

            elif event == "runner_on_unreachable":
                hosts[hostname]["unreachable"] += 1

            if changed:
                hosts[hostname]["changed"] += 1

        #
        # Save summary into SQLite
        #

        for hostname, stats in hosts.items():

            if stats["unreachable"] > 0:

                health = "Critical"

            elif stats["failed"] > 0:

                health = "Warning"

            else:

                health = "Healthy"

            self.db.save_host_summary(
                run_id=run_id,
                hostname=hostname,
                successful_tasks=stats["successful"],
                failed_tasks=stats["failed"],
                unreachable_tasks=stats["unreachable"],
                changed_tasks=stats["changed"],
                health_status=health
            )

        return hosts

    def close(self):

        self.db.close()
