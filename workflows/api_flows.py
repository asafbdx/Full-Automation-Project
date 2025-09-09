import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data


# API flow layer for Grafana team management.
#
# This file defines:
# - get_value_from_api → Retrieve values from Grafana API responses.
# - create_team → Create a new Grafana team.
# - update_team → Update an existing Grafana team.
# - delete_team → Delete a Grafana team.
#
# Purpose:
# Provide reusable API flows for Grafana team management,
# encapsulating request/response handling to keep test cases simple and maintainable.


url = get_data("Url")
user = get_data("UserName")
password = get_data("Password")


class APIFlows:
    @staticmethod
    @allure.step("Get value from Grafana api flow")
    def get_value_from_api(nodes):
        response = APIActions.get(url + "api/teams/search", user,password)
        return APIActions.extract_value_from_response(response,nodes)


    @staticmethod
    @allure.step("Create new team in Grafana flow")
    def create_team(name, email):
        payload = {"name": name,"email":email}
        status_code = APIActions.post(url + "api/teams/",payload,user,password)
        return status_code

    @staticmethod
    @allure.step("Update team in Grafana flow")
    def update_team(name, email, id):
        payload = {"name": name,"email":email}
        status_code = APIActions.put(url + "api/teams/" +str(id),payload,user,password)
        return status_code


    @staticmethod
    @allure.step("Delete team in Grafana flow")
    def delete_team(id):
        status_code = APIActions.delete(url + "api/teams/"+ str(id),user,password)
        return status_code