"""
Using Python Selenium Automation and Actionchains visit the URl 
https://jqueryui.com/droppable/ and do a Drag and Drop operation
 of the White Rectangular Box into the Yellow Rectangular Box?
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class JqueryUI:

    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)

    def open_website(self):
        """
        Opening website https://jqueryui.com/droppable/
        """
        self.driver.get(self.url)
        sleep(4)

    def perform_drag_drop(self):
        """
        Performing drag and drop and handled exception for NoSuchElement in iframe
        """
        iframe_element = self.driver.find_element(By.CLASS_NAME,"demo-frame")
        self.driver.switch_to.frame(iframe_element)

        # Initialise element to avoid unbound local error
        draggable_element = None    
        droppable_element = None

        try:
            draggable_element = self.driver.find_element(By.ID, "draggable")
        except NoSuchElementException:
            print("Draggable element not found")
        try:
           droppable_element = self.driver.find_element(By.ID, "droppable")
        except NoSuchElementException:
            print("Droppable element not found")
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable_element,droppable_element).perform()
    
    def close_browser(self):
        self.driver.quit()

practice = JqueryUI()
practice.open_website()
practice.perform_drag_drop()
practice.close_browser()