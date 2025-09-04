import allure

from extensions.ui_actions import UiActions
import test_cases.conftest as conf
from test_cases.conftest import m_action


class MobileActions(UiActions):
    @staticmethod
    @allure.step("Tap on element")
    def tap(elem,times):
        conf.action.tap(elem,times).perform()

    @staticmethod
    @allure.step("Swipe screen")
    def swipe(start_x,start_y,end_x,end_y,duration):
        conf.action.swipe(start_x,start_y,end_x,end_y,duration).perform()

    @staticmethod
    @allure.step("Zoom on element")
    def zoom(element,pixels=200):
        action1 = conf.action
        action2 = conf.action2
        m_action = conf.m_action
        x_loc = element.rect["x"]
        y_loc = element.rect["y"]
        action1.long_press(x=x_loc,y=y_loc).move_to(x=x_loc,y=y_loc+pixels).wait(500)
        action2.long_press(x=x_loc,y=y_loc).move_to(x=x_loc,y=y_loc-pixels).wait(500)
        m_action.add(action1,action2)
        m_action.perform()


    @staticmethod
    @allure.step("Pinch on element")
    def zoom(element,pixels=200):
        action1 = conf.action
        action2 = conf.action2
        m_action = conf.m_action
        x_loc = element.rect["x"]
        y_loc = element.rect["y"]
        action1.long_press(x=x_loc,y=y_loc+pixels).move_to(x=x_loc,y=y_loc).wait(500)
        action2.long_press(x=x_loc,y=y_loc-pixels).move_to(x=x_loc,y=y_loc).wait(500)
        m_action.add(action1,action2)
        m_action.perform()
