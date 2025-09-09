from selenium.webdriver.common.by import By

# Page Object Model for the application’s upper navigation menu.
#
# This file defines:
# - Locators for Home, Dashboards, Search, New, Help, and Profile.
# - The UpperMenuPage class with methods to access these menu items.
#
# Purpose:
# Provide a reusable interface for interacting with the upper navigation bar,
# keeping automation tests clean, organized, and maintainable.

home = (By.LINK_TEXT,"Home")
dashboard = (By.LINK_TEXT,"Dashboards")
search = (By.CSS_SELECTOR,"[class='css-1lj8xfd-input-input']")
new = (By.CSS_SELECTOR,"button[aria-label='New']")
help = (By.CSS_SELECTOR,"button[aria-label='Help']")
profile = (By.CSS_SELECTOR,"button[aria-label='Profile']")



class UpperMenuPage:
    def __init__(self,driver):
        self.driver = driver


    def get_home(self):
        return self.driver.find_element(home[0],home[1])

    def get_dashboard(self):
        return self.driver.find_element(dashboard[0],dashboard[1])

    def get_search(self):
        return self.driver.find_element(search[0],search[1])

    def get_new(self):
        return self.driver.find_element(new[0],new[1])

    def get_help(self):
        return self.driver.find_element(help[0],help[1])

    def get_profile(self):
        return self.driver.find_element(profile[0],profile[1])