import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


#Assertion and verification utilities for the Automation Project.

#This file provides reusable methods to validate test results:
#- Equality checks (verify_equals).
#- Element visibility (is_displayed, is_element_displayed_safe).
#- Count verification (verify_number_of_elements).
#- Soft assertions for multiple elements.

#Purpose:
#Centralize verification logic to keep test cases clean, readable,
#and ensure consistent reporting in Allure.



class Verifications:
    @staticmethod
    @allure.step("Verify equals")

    def verify_equals(actual, expected):
        assert actual == expected, "Verify Equals Failed, Actual :" + str(actual) + "is not equals to Expected" + str(expected)

    @staticmethod
    @allure.step("Verify element is displayed")

    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "Verify Is Displayed Failed, Element :" + elem.text + "is not displayed"


    #@staticmethod
    #def verify_number_of_elements(elements: list[WebElement], expected_count: int):
        #actual_count = len(elements)
        #assert actual_count == expected_count , f"Expected{expected_count} elements , but found{actual_count}"

    # Verify Menu Buttons Flow Using Smart Assertions
    @staticmethod
    @allure.step("Soft verification(assert) of elements using smart assertions")

    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
            verify_expectations()

    # Verify Menu Buttons Flow Using My Implementation
    @staticmethod
    @allure.step("Soft verification(assert) of elements using my implementation")

    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute("aria-label"))

        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print("Soft Displayed Failed, Elements which failed: " +str(failed_elem))

            raise AssertionError("Soft Displayed Failed")

    @staticmethod
    @allure.step("Verify number of elements")

    def verify_number_of_elements(elems, size):
        assert len(elems) == size, \
            f"Number of elements in list: {len(elems)} does not match expected: {size}"

    @staticmethod
    @allure.step("Verify element is displayed safe")

    def is_element_displayed_safe(get_element_func):
        try:
            return get_element_func().is_displayed()
        except:
            return False
