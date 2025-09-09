import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


# Utility functions, enums, and constants for the Automation Project.
#
# This file defines:
# - Data helpers (get_data from XML, read_csv, get_time_stamp).
# - Wait helpers for handling element presence/displayed.
# - Enums for element lookup (For, By), mortgage save option (Save), and directions (Direction).
#
# Purpose:
# Provide common utilities and constants to support automation flows,
# keeping test logic clean, reusable, and centralized.


#Function Name : Get Data
#Function Description : This function reads data from external xml file
#Function Parameters : String - the node(tag) name
#Function Return : String - node(tag) value
def get_data(node_name):
    root = ET.parse("C:/Users/asafb/PycharmProjects/test_automation_final_project/configuration/data.xml").getroot()
    return root.find(".//"+ node_name).text

#Function Name : Wait
#Function Description : This function wait for element appears on the page by time
#Function Parameters : Element_Exists -  Waits until the element is present in the DOM.

def wait(for_element, elem):
    if for_element == "element_exists":
        WebDriverWait(conf.driver,int(get_data("WaitTime"))).until(EC.presence_of_element_located((elem[0], elem[1])))

    elif for_element == "element_displayed":
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.presence_of_element_located((elem[0], elem[1])))

#Function Name : Read CSV
#Function Description : This function reads data from CSV file
#Function Parameters : String - the CSV file name (including path if needed)
#Function Return : List - a list of rows , where each row is represented as list of strings
def read_csv(file_name):
    data = []
    with open(file_name,newline="") as file :
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data

# Enum for selecting displayed element or exist element, my wait method uses this enum.

class For:
    ELEMENT_EXISTS = "element_exists"
    ELEMENT_DISPLAYED = "element_displayed"

#Enum for selecting row from table to delete

class By:
    USER = "user"
    INDEX = "index"

#Enum for selecting whether we want to save mortgage transaction
class Save:
    Yes = True
    No = False

#Class Name : Direction
#Class Description : This class defines constants representing possible directions

class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

def get_time_stamp():
    return time.time()