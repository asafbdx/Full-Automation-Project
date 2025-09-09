from selenium.webdriver.common.by import By


# Page Object Model for the application’s login screen.
#
# This file defines:
# - Locators for username, password, submit, and skip button.
# - The LoginPage class with methods to access these UI elements.
#
# Purpose:
# Provide a reusable interface for automating login actions,
# keeping web automation tests clean, organized, and maintainable.

user_name = (By.NAME,"user")
password = (By.NAME,"password")
submit = (By.CLASS_NAME,"css-1ewfzsi-button")
skip = (By.CLASS_NAME,"css-10ztfkf-button")



class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(user_name[0],user_name[1])

    def get_password(self):
        return self.driver.find_element(password[0],password[1])

    def get_submit(self):
        return self.driver.find_element(submit[0],submit[1])

    def get_skip(self):
        return self.driver.find_element(skip[0],skip[1])