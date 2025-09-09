import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

import test_cases.conftest as conf

import test_cases


#Web UI interaction utility module for the Automation Project.

#This file provides reusable actions for working with web elements:
#- Click, right-click, clear, update text.
#- Mouse over / hover interactions.
#- Drag and drop operations.
#- Get attributes from elements.

#Purpose:
#Centralize Selenium-based UI actions to keep test cases simple, readable,
#and consistent across the project.


class UiActions:
    @staticmethod
    @allure.step("Click on element")
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("Update text")

    def update_text(elem: WebElement,value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Mouse over")

    def mouse_over(elem1: WebElement,elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()


    @staticmethod
    @allure.step("Mouse hover tooltip")
    def mouse_hover_tooltip(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform()


    @staticmethod
    @allure.step("Right click on element")

    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step("Drag and Drop")

    def drag_and_drop(elem1: WebElement,elem2: WebElement):
        conf.drag_and_drop(elem1,elem2).perform()

    @staticmethod
    @allure.step("Clear text in element")

    def clear(elem: WebElement):
        elem.clear()


    @staticmethod
    @allure.step("Get attribute from element")

    def get_attribute(elem: WebElement, attribute_name: str):
        return elem.get_attribute(attribute_name)