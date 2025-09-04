import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page

class DesktopFlows:

    @staticmethod
    @allure.step("Calculator equation")
    def calculate_flow(equation):
        for i in equation:
            DesktopFlows.calculate_flow(i)
        UiActions.click(page.standard_calc.get_equal())


    @staticmethod
    def calculator_click(value):
        if value == "0":
            UiActions.click(page.standard_calc.get_zero())
        elif value == "1":
            UiActions.click(page.standard_calc.get_one())
        elif value == "2":
            UiActions.click(page.standard_calc.get_two())
        elif value == "3":
            UiActions.click(page.standard_calc.get_three())
        elif value == "4":
            UiActions.click(page.standard_calc.get_four())
        elif value == "5":
            UiActions.click(page.standard_calc.get_five())
        elif value == "6":
            UiActions.click(page.standard_calc.get_six())
        elif value == "7":
            UiActions.click(page.standard_calc.get_seven())
        elif value == "8":
            UiActions.click(page.standard_calc.get_eight())
        elif value == "9":
            UiActions.click(page.standard_calc.nine())
        elif value == "+":
            UiActions.click(page.standard_calc.get_plus())
        elif value == "-":
            UiActions.click(page.standard_calc.get_minus())
        elif value == "/":
            UiActions.click(page.standard_calc.get_divide())
        elif value == "*":
            UiActions.click(page.standard_calc.get_multi())
        else:
            raise Exception("Invalid Input:" + value)


    @staticmethod
    @allure.step("Get calculator result")
    def get_result_flow():
        page.standard_calc.get_result().text.replace("התצוגה היא","").strip()


    @staticmethod
    @allure.step("Clear calculator result")
    def clear_flow():
        UiActions.click(page.standard_calc.get_clear())