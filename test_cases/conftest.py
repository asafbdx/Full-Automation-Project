import sqlite3
import time

import allure
import pytest
import selenium
import appium.webdriver
from appium.webdriver import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
#from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_time_stamp
from utilities.manage_pages import ManagePages

driver = None
action = None
action2 = None
m_action = None
mobile_size = None
my_db = None
eyes = Eyes() # Aplitools

# PyTest fixtures and driver management for the Automation Project.
#
# This file defines:
# - Fixtures for initializing and tearing down Web, Mobile, Electron, and Desktop drivers.
# - Database connection setup and teardown.
# - WebDriver factories (Chrome, Firefox, Edge, Android, iOS, Electron, Windows Desktop).
# - Exception handling with automatic screenshot capture and Allure reporting.
#
# Purpose:
# Centralize all environment setup, driver initialization, and global fixtures
# to keep test files clean, reusable, and maintainable.


@pytest.fixture(scope="class")
def init_web_driver(request):
    globals()["driver"] = get_web_driver()
    driver = globals()["driver"]
    #driver.maximize_window()
    driver.implicitly_wait(int(get_data("WaitTime")))
    driver.get(get_data("Url"))
    request.cls.driver = driver
    globals()["action"]  = ActionChains(driver)
    ManagePages.init_web_pages()
    if get_data("Execute_Aplitools").lower() == "yes":
        eyes.api_key = get_data("Aplitools_key")
    yield
    time.sleep(3)
    driver.quit()
    if get_data("Execute_Aplitools").lower() == "yes":
        eyes.close() #aplitools
        eyes.abort() #aplitools


@pytest.fixture(scope="class")
def init_mobile_driver(request):
    globals()["driver"] = get_mobile_driver()
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    globals()["action"] = TouchAction(driver)
    request.cls.action = globals()["action"]
    globals()["action2"] = TouchAction(driver)
    request.cls.action2 = globals()["action2"]
    globals()["m_action"] = MultiAction(driver)
    request.cls.m_action = globals()["m_action"]
    globals()["mobile_size"] = driver.get_window_size()
    request.cls.mobile_size = globals()["mobile_size"]
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_electron_driver(request):
    globals()["driver"] = get_electron_driver()
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    globals()["action"]= ActionChains(driver)
    request.cls.action = globals()["action"]
    ManagePages.init_electron_pages()

    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_desktop_driver(request):
    globals()["driver"] = get_desktop_driver()
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()

    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_db_connection(request):
    my_db = sqlite3.connect(get_data("DB_HOST"))
    globals()["my_db"] = my_db
    request.cls.my_db = my_db
    yield
    my_db.close()

def get_web_driver():
    web_driver = get_data("Browser")
    if web_driver.lower() ==  "chrome":
        driver = get_chrome()

    elif web_driver.lower() == "firefox":
        driver = get_firefox()

    elif web_driver.lower() == "edge":
        driver = get_edge()

    else :
        driver = None
        raise Exception("Wrong Input, Unrecognized Browser")
    return driver


def get_mobile_driver():
    if get_data("Mobile_Device").lower() == "android":
        driver = get_android(get_data("Udid"))
    elif get_data("Mobile_Device").lower() == "ios":
        driver = get_ios(get_data("Udid"))
    else:
        driver = None
        raise Exception("Wrong input, unrecognized mobile OS")
    return driver


def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("Electron_APP")
    driver = selenium.webdriver.Chrome(chrome_options=options,executable_path=get_data("Electron_Driver"))
    return driver


def get_desktop_driver():
    dc = {}
    dc["app"] = get_data("Application_Name")
    dc["platformName"] = "Windows"
    dc["deviceName"] = "WindowPC"
    driver = appium.webdriver.Remote(get_data("WinAppDriver_Service"), dc)
    return driver


def get_chrome():
    #srv = Service(ChromeDriverManager().install()) #selenium 4.x
    #chrome_driver = selenium.webdriver.Chrome(service=srv) #selenium 4.x
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install()) #selenium 3.x
    return chrome_driver

def get_firefox():
    #srv = Service(executable_path=GeckoDriverManager().install()) #selenium 4.x
    #ff_driver = selenium.webdriver.Firefox(service=srv) #selenium 4.x
    ff_driver = selenium.webdriver.Chrome(GeckoDriverManager().install()) #selenium 3.x
    return ff_driver

def get_edge():
    #srv = Service(EdgeChromiumDriverManager().install()) #selenium 4.x
    #edge_driver = selenium.webdriver.Edge(service=srv) #selenium 4.x
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) #selenium 3.x
    return edge_driver


def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data("App_Package")
    dc['appActivity'] = get_data("App_Activity")
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data("Appium_Server"),dc)
    return android_driver

def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data("Bundle_ID")
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data("Appium_Server"),dc)
    return ios_driver


#catch exceptions and error
def pytest_exception_interact(node,call,report):
    if report.failed:
        if globals()["driver"] is not None: #if it is None -> this is exception from API test
            image = get_data("ScreenshotPath") + "screen_" + str(get_time_stamp()) + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)