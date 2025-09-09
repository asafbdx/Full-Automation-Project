from selenium.webdriver.common.by import By


# Page Object Model for the application’s main page.
#
# This file defines:
# - Locator for the main page title.
# - The MainPage class with a method to access the title element.
#
# Purpose:
# Provide a reusable interface for validating the main page’s title,
# keeping automation tests simple, organized, and maintainable.


main_title = (By.CLASS_NAME,"css-1ti7uft")

class MainPage():
    def __init__(self,driver):
        self.driver = driver


    def get_name_title(self):
        return self.driver.find_element(main_title[0],main_title[1])

