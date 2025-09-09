from selenium.webdriver.common.by import By


# Page Object Model for the User Creation screen.
#
# This file defines:
# - Locators for name, email, username, password, and create user button.
# - The NewUsersPage class with methods to access these UI elements.
#
# Purpose:
# Provide a reusable interface for automating user creation,
# keeping web tests clean, readable, and maintainable.

name = (By.ID,"name-input")
email = (By.ID,"email-input")
username = (By.ID,"username-input")
new_password = (By.ID,"password-input")
create_user = (By.CLASS_NAME,"css-9ilz2k-button")




class NewUsersPage():
    def __init__(self,driver):
        self.driver = driver


    def get_name(self):
        return self.driver.find_element(name[0],name[1])

    def get_email(self):
        return self.driver.find_element(email[0],email[1])


    def get_username(self):
        return self.driver.find_element(username[0],username[1])


    def get_new_password(self):
        return self.driver.find_element(new_password[0],new_password[1])


    def get_create_user(self):
        return self.driver.find_element(create_user[0],create_user[1])
