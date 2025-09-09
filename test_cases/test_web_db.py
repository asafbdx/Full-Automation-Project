import allure
import pytest

from extensions.verifiactions import Verifications
from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


# Automated web test integrated with database for Grafana.
#
# This file defines:
# - Login verification using credentials retrieved from the database.
#
# Purpose:
# Validate end-to-end functionality by combining database-driven test data
# with web automation flows, ensuring seamless integration between DB and UI.


@pytest.mark.usefixtures("init_web_driver")
@pytest.mark.usefixtures("init_db_connection")

class Test_Web_DB:
    @allure.title("Test01: Login to Grafana via DB")
    @allure.description("This test verify login using elements taken from database")
    def test_verify_login_db(self):
        DBFlows.login_grafana_via_db()
        WebFlows.verify_grafana_title