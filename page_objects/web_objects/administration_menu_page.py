from selenium.webdriver.common.by import By


# Page Object Model for the Administration menu.
#
# This file defines:
# - Locators for Administration, Users and Access, Provisioning, General, and Plugins.
# - The AdministrationMenuPage class with methods to access these menu items.
#
# Purpose:
# Provide a reusable interface for navigating the Administration menu,
# keeping automation tests clean, maintainable, and consistent.


administration_expand = (By.CSS_SELECTOR,"[aria-label *='Administration']")
users_and_access_expand = (By.CSS_SELECTOR,"button[aria-label*='Users and access']")
users = (By.XPATH,"//span[@class='css-uantyg' and text()='Users']")
provisioning = (By.XPATH,"//span[@class='css-uantyg' and text()='Provisioning']")
general = (By.XPATH,"//span[@class='css-uantyg' and text()='General']")
plugins = (By.XPATH,"//span[@class='css-uantyg' and text()='Plugins and data']")
usersandaccess = (By.XPATH,"//span[@class='css-uantyg' and text()='Users and access']")


class AdministrationMenuPage():
    def __init__(self,driver):
        self.driver = driver


    def get_administration_expand(self):
        return self.driver.find_element(administration_expand[0],administration_expand[1])

    def get_users_and_access_expand(self):
        return self.driver.find_element(users_and_access_expand[0],users_and_access_expand[1])

    def get_users(self):
        return self.driver.find_element(users[0],users[1])

    def get_provisioning(self):
        return self.driver.find_element(provisioning[0],provisioning[1])

    def get_general(self):
        return self.driver.find_element(general[0],general[1])

    def get_plugins(self):
        return self.driver.find_element(plugins[0],plugins[1])

    def get_usersandaccess(self):
        return self.driver.find_element(usersandaccess[0],usersandaccess[1])