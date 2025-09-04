import allure

import page_objects.web_objects.main_page as main
import page_objects.web_objects.users_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifiactions import Verifications
from utilities.common_ops import wait, For, get_data, read_csv
from utilities.manage_pages import web_upper_menu


class WebFlows:
    @staticmethod
    @allure.step("Login to Grafana flow")
    def login_flow(user: str,password: str):
        UiActions.update_text(page.web_login.get_user_name(),user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    @allure.step("Verify Grafana title")

    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXISTS,main.main_title)
        actual = page.web_main.get_name_title().text
        Verifications.verify_equals(actual, expected)

    # Verify Menu Buttons Flow Using Smart Assertions
    @staticmethod
    @allure.step("Verify displayed menu buttons flow using smart assertion")

    def verify_menu_buttons_flows_smart_assertion():
        elems = [page.web_upper_menu.get_new(),
                 page.web_upper_menu.get_help(),
                 page.web_upper_menu.get_profile()]

        Verifications.soft_assert(elems)

        # Verify Menu Buttons Flow Using My Implementaion
    @staticmethod
    @allure.step("Verify displayed menu buttons flow using my implementation")

    def verify_menu_buttons_flows():
        elems = [page.web_upper_menu.get_new(),
                 page.web_upper_menu.get_help(),
                 page.web_upper_menu.get_profile()]

        Verifications.soft_displayed(elems)


            #Open the side menu, if open pass to the next
    @staticmethod
    @allure.step("Open side menu flow , pass if already open")

    def open_side_menu():
        side_menu_button = page.web_left_menu.get_left_menu_open()
        aria_label = UiActions.get_attribute(side_menu_button, "aria-label")

        if "Close" in aria_label:
            pass
        else:
            UiActions.click(side_menu_button)



    @staticmethod
    @allure.step("Admin menu expand flow, pass if already open")

    def admin_menu_expand():
        admin_menu_button = page.web_admin_menu.get_administration_expand()
        aria_label = UiActions.get_attribute(admin_menu_button, "aria-label")

        if "Expand" in aria_label:
            UiActions.click(page.web_admin_menu.get_administration_expand())



    @staticmethod
    @allure.step("Users and access flow, pass if already open")

    def users_and_access_expand():
        users_and_access_button = page.web_admin_menu.get_users_and_access_expand()
        aria_label = UiActions.get_attribute(users_and_access_button, "aria-label")

        if "Expand" in aria_label:
            UiActions.click(page.web_admin_menu.get_users_and_access_expand())

    @staticmethod
    @allure.step("Open page users flow, just click on the users tab on the menu")

    def page_open_users():

        UiActions.click(page.web_admin_menu.get_users())




    @staticmethod
    @allure.step("Full open users flow")

    def open_users():
        side_menu_button = page.web_left_menu.get_left_menu_open()
        aria_label = UiActions.get_attribute(side_menu_button, "aria-label")

        if "Close" in aria_label:
            pass
        else:
            UiActions.click(side_menu_button)

        UiActions.click(page.web_admin_menu.get_administration_expand())
        UiActions.click(page.web_admin_menu.get_users_and_access_expand())
        UiActions.click(page.web_admin_menu.get_users())




    @staticmethod
    @allure.step("Create user flow")

    def create_user(name,email,user,password):
        UiActions.click(page.web_users_page.get_new_user())
        UiActions.update_text(page.web_admin_new_user.get_name(), name)
        UiActions.update_text(page.web_admin_new_user.get_email(), email)
        UiActions.update_text(page.web_admin_new_user.get_username(), user)
        UiActions.update_text(page.web_admin_new_user.get_new_password(), password)
        UiActions.click(page.web_admin_new_user.get_create_user())
        UiActions.click(page.web_left_menu.get_left_menu_open())
        UiActions.click(page.web_admin_menu.get_users())



    @staticmethod
    @allure.step("Search user flow")

    def search_user(search_value):
        UiActions.clear(page.web_users_page.get_search())
        UiActions.update_text(page.web_users_page.get_search(),search_value)

    @staticmethod
    @allure.step("Verify number of users flow")

    def verify_number_of_users(number):
        if number >0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.users_page.users_list)
            Verifications.verify_number_of_elements(page.web_users_page.get_users_list(), number)


    @staticmethod
    @allure.step("Delete user flow")

    def delete_user(by, value):
        if by == "user":
            UiActions.click(page.web_users_page.get_user_by_user_name(value))
        elif by == "index":
            UiActions.click(page.web_users_page.get_user_by_index(value))

        UiActions.click(page.web_users_page.get_delete())
        UiActions.click(page.web_users_page.get_confirm_delete())


    @staticmethod
    @allure.step("Go to home page flow")

    def grafana_home(self):
        self.driver.get(get_data("Url"))


data = read_csv(get_data("CSV_Location"))
testdata = [
    (data[0][0],data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
