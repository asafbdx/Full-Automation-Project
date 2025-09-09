import allure
import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.mobile_actions import MobileActions
from extensions.verifiactions import Verifications
from utilities.common_ops import get_data


# Flow layer for automating the Mortgage Calculator mobile app.
#
# This file defines:
# - mortgage_flow → Fills in mortgage details, calculates repayment, and optionally saves results.
# - verify_mortgage_repayment → Validates repayment amount against the expected value.
# - swipe_screen → Performs swipe gestures in all four directions.
# - verify_rate_delete_transaction → Verifies saved transaction rate and deletes the entry.
#
# Purpose:
# Provide reusable mobile automation flows for mortgage calculation and saved transaction handling,
# encapsulating UI actions to keep mobile test cases clean and maintainable.



class MobileFlows:
    @staticmethod
    @allure.step("Fill in mortgage details flow")
    def mortgage_flow(amount,term,rate,save):
        MobileActions.update_text(page.mobile_calculator.get_amount(),amount)
        MobileActions.update_text(page.mobile_calculator.get_term(),term)
        MobileActions.update_text(page.mobile_calculator.get_rate(),rate)
        MobileActions.click(page.mobile_calculator.get_calculate())
        if save:
            MobileActions.click(page.mobile_calculator.get_save())


    @staticmethod
    @allure.step("Verify mortgage flow")
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        Verifications.verify_equals(actual,"£" + expected)


    @staticmethod
    @allure.step("Swipe screen flow")
    def swipe_screen(direction):
        width = conf.mobile_size["width"]
        height = conf.mobile_size["height"]

        start_x = None
        start_y = None
        end_x = None
        end_y = None

        if direction == "left":
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height * 0.5

        if direction == "right":
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5

        if direction == "up":
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5

        if direction == "down":
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5

        MobileActions.swipe(start_x,start_y,end_x,end_y,int(get_data("Swipe_Duration")))

    @staticmethod
    @allure.step("Verify and delete saved transactions flow")
    def verify_rate_delete_transaction(expected):
        actual = page.mobile_saved.get_rate().text
        Verifications.verify_equals(actual,expected + "%")
        MobileActions.tap(page.mobile_saved.get_delete(),1)
        MobileActions.tap(page.mobile_saved.get_confrim_delete(),1)

