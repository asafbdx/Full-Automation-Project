import os
import time

import allure
import pytest

from test_cases.conftest import driver
from utilities.common_ops import get_data, By
from workflows import web_flows
from workflows.web_flows import WebFlows
import test_cases.conftest as conf




@pytest.mark.usefixtures("init_web_driver")
class Test_Web:
    @allure.title("Test 01 - Verify Login Grafana")
    @allure.description("this test verifies a successfully loging to Grafana")
    def test_verify_login(self):
        WebFlows.login_flow(get_data("UserName"),get_data("Password"))
        WebFlows.verify_grafana_title("Welcome to Grafana")

    @allure.title("Test 02 - Verify Upper Menu Buttons")
    @allure.description("this test verifies upper menu buttons are displayed")
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flows_smart_assertion()
        #WebFlows.verify_menu_buttons_flows()


    @allure.title("Test 03 - Verify New User")
    @allure.description("this test creates and verifies a new user")
    def test_verify_new_user(self):
        WebFlows.open_side_menu()
        WebFlows.admin_menu_expand()
        WebFlows.users_and_access_expand()
        WebFlows.page_open_users()
        WebFlows.create_user("Asaf","asafbd1@hotmail.co.il","asaf","exsadgbv")
        WebFlows.create_user("Moshe","moshe@hotmail.co.il","moshe","ffccxxgkm")
        WebFlows.verify_number_of_users(3)


    @allure.title("Test 04 - Filtering Users")
    @allure.description("this test filters users")
    @pytest.mark.parametrize("search_value,expected_users",web_flows.testdata)
    def test_csv(self,search_value,expected_users):
        WebFlows.open_side_menu()
        WebFlows.page_open_users()
        WebFlows.search_user(search_value)
        time.sleep(2)
        WebFlows.verify_number_of_users(int(expected_users))


    @allure.title("Test 05 - Delete User")
    @allure.description("this test verifies deleted users")
    def test_delete_user(self):
        WebFlows.open_side_menu()
        WebFlows.page_open_users()
        WebFlows.delete_user(By.USER, "asaf")
        WebFlows.delete_user(By.USER,"moshe") # Option 1 / delete by username
            #WebFlows.delete_user(By.INDEX,2)  # Option 2 / delete by index
        WebFlows.verify_number_of_users(1)


    @allure.title("Test 06 - Visual Testing")
    @allure.description("this test verifies visually users table")
    @pytest.mark.skip(get_data("Execute_Aplitools").lower() == "no",reason ="run this test only on selenium 3.141&appium 1.3.0")
    def test_visual_deleted_user(self):
        conf.eyes.open(self.driver,"Grafana","Grafana Testing User Table")
        WebFlows.login_flow(get_data("UserName"),get_data("Password"))
        conf.driver.get("http://localhost:3000/admin/users")
        conf.eyes.check_window("Users Table")

    def teardown_method(self):
        WebFlows.grafana_home(self)
