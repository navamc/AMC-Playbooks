"""
AMC Reporting Engine
Global Configuration File
"""

# --------------------------------------------------
# Company Information
# --------------------------------------------------

COMPANY_NAME = "Al Hayat Medical Center"

REPORT_TITLE = "Daily Infrastructure Health Report"

TIMEZONE = "Asia/Qatar"

# --------------------------------------------------
# AWX Configuration
# --------------------------------------------------

AWX_URL = "https://awx.amc.com"

AWX_VERIFY_SSL = False

# Paste your AWX API token below
AWX_TOKEN = "chpjcnLn6GqRZG4phywk96zOLBPEIu"

# --------------------------------------------------
# SQLite Database
# --------------------------------------------------

DATABASE = "/opt/amc-reports/database/amc_reports.db"

# --------------------------------------------------
# Output Directories
# --------------------------------------------------

OUTPUT_HTML = "/opt/amc-reports/output/html"

OUTPUT_JSON = "/opt/amc-reports/output/json"

OUTPUT_PDF = "/opt/amc-reports/output/pdf"

ARCHIVE = "/opt/amc-reports/archive"

LOGS = "/opt/amc-reports/logs"

# --------------------------------------------------
# Report Settings
# --------------------------------------------------

WORKFLOW_NAME = "Daily Windows Infrastructure Health Check"

MAX_WORKFLOWS = 1
