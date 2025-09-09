import allure

from extensions.db_actions import DBActions
from workflows.web_flows import WebFlows

# Database flow layer for the Automation Project.
#
# This file defines:
# - login_grafana_via_db → Retrieves user credentials from the database and performs a Grafana login.
#
# Purpose:
# Integrate database queries with web flows, enabling data-driven testing
# by logging into Grafana using credentials stored in the DB.

class DBFlows:
    @staticmethod
    @allure.step("Login to Grafana via Database Flow")
    def login_grafana_via_db():
        columns = ["name", "password"]
        result = DBActions.get_query_result(columns, "Students", "comments","correct")
        WebFlows.login_flow(result[0][0], result[0][1])
