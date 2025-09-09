import allure

from extensions.verifiactions import Verifications
from workflows.api_flows import APIFlows

# Automated API tests for the Grafana application.
#
# This file defines:
# - Creating a new team and verifying response status.
# - Validating team name and member details.
# - Updating a team and verifying changes.
# - Deleting a team and confirming successful removal.
#
# Purpose:
# Provide end-to-end automated API coverage for Grafana’s team management,
# ensuring correctness of CRUD operations and consistent API responses.

team_name = "Asaf"
team_email = "asaf@gmail.com"

class Test_API:
    @allure.title("Test 01 : Create Team & Verify Status Code")
    @allure.description("This test creates a new team in Grafana")
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name,team_email)
        Verifications.verify_equals(actual, 200)


    @allure.title("Test 02 : Verify Team Name")
    @allure.description("This test verify the Grafana team member name")
    def test_verify_team_member_name(self):
        nodes = ["teams",0,"name"]
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual,team_name)


    @allure.title("Test 03 : Update Team & Verify Status Code")
    @allure.description("This test update team and verify status code")
    def test_update_and_verify_team_name(self):
        nodes = ["teams",0,"id"]
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + " Ben David", team_email , id)
        Verifications.verify_equals(actual, 200)

    @allure.title("Test 04 : Verify Team Name")
    @allure.description("This test verifies team member name")
    def test_verify_team_updated_name(self):
        nodes = ["teams",0,"name"]
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual,team_name + " Ben David")


    @allure.title("Test 05 : Delete Team & Verify Status Code")
    @allure.description("This test delete team and verify status code")
    def test_delete_and_verify_team(self):
        nodes = ["teams",0,"id"]
        id = APIFlows.get_value_from_api(nodes)
        actual =  APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)
