import allure
import pytest

from extensions.verifiactions import Verifications
from workflows.desktop_flows import DesktopFlows

# Automated desktop application tests for the Windows Calculator.
#
# This file defines:
# - Adding two numbers and verifying the result.
# - Performing arithmetic actions (multiply, add, divide, subtract) and verifying results.
#
# Purpose:
# Provide automated coverage for basic calculator functions on the Windows desktop app,
# ensuring accuracy of calculations and stable UI interactions.


@pytest.mark.usefixtures("init_desktop_driver")
class TestDesktop:
    @allure.title("Test 01 : Adding 2 Numbers")
    @allure.description("This test adds a 2 numbers and verify the result")
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow("1+7")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "8" )

    @allure.title("Test 02 : Arithmetic Actions")
    @allure.description("This test does some arithmetic actions and verifies it")
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flow("2*5+50/2-25")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "5" )


    def teardown_method(self):
        DesktopFlows.clear_flow()

