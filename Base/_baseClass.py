import splinter
from splinter import *
from splinter.exceptions import *
from Splinter_Project.loggingPackage.custom_logger import customlogger as cl
import inspect
from datetime import datetime
import os
from traceback import print_stack
from urllib3.exceptions import *
import socket

class baseClass():
    browser = Browser()
    log = cl(loglevel='DEBUG')

    def _BG_broswerLanunch(self, broswerType, url):
        self.browser = Browser(broswerType)
        
        if broswerType == 'chrome':
                self.browser.visit(url)
                self.browser.driver.maximize_window()
                self.log.info("[PASS] Method: '{0}{1}'".format(__name__,inspect.currentframe().f_code.co_name)
                              + "Browser {} is successfully launched".format(broswerType))
        elif broswerType == 'firefox':
            self.browser.visit(url)
            self.browser.driver.maximize_window()
            self.log.info("[PASS] Method: '{0}{1}'".format(__name__, inspect.currentframe().f_code.co_name)
                          + "Browser {} is successfully launched".format(broswerType))
        else:
            print("Invalid browser")
            self.log.error("[FAIL] Method: '{0}{1}'".format(__name__,inspect.currentframe().f_code.co_name) + "Invalid Browser")

    def _BG_getType(self, locatorType):
        if locatorType == 'id':
            return self.browser.find_by_id
        elif locatorType == 'value':
            return self.browser.find_by_value
        elif locatorType == 'text':
            return self.browser.find_by_text
        elif locatorType == 'name':
            return self.browser.find_by_name
        elif locatorType == 'tag':
            return self.browser.find_by_tag
        elif locatorType == 'xpath':
            return self.browser.find_by_xpath
        elif locatorType == 'css':
            return self.browser.find_by_css
        else:
            self.log.error("[FAIL] Method: {0}{1}".format(__name__,inspect.currentframe().f_code.co_name) + "Invalid locatorType:{}".format(locatorType))
            return False


    def _BG_getElement(self, locator, locatorType):
        try:
            type = self._BG_getType(locator)
            element = type(locatorType)
            if element:
                self.log.info("[PASS] Method: '{}{}'".format(__name__, inspect.currentframe().f_code.co_name) + "Element found successfully using locator {0} and locatorType {1}".format(locator, locatorType))
            return element
        except:
            self.log.error("[FAIL] Method: '{}{}'".format(__name__,inspect.currentframe().f_code.co_name) + "Element not found using locator {0} and locatorType {1}".format(locator, locatorType))

    def _BG_checkBoxSelect(self, locator, *args):
            for arg in args:
                try:
                    self.browser.choose(locator, arg)
                    print('Checkbox "{}" is successfully selected'.format(arg))
                    self.log.info("[PASS] Method: '{0}-->{1}'".format(__name__, inspect.currentframe().f_code.co_name) + "Checkbox {} is successfully selected".format(arg))
                except ElementDoesNotExist:
                    print('Checkbox with value {} is not present, please select valid and available checkbox'.format(arg))
                    self.log.error("[FAIL] Method: '{}{}'".format(__name__,inspect.currentframe().f_code.co_name) + "Checkbox with value {} is not present, please select a valid checkbox".format(arg))


    def _BG_dropDownElementSection(self, locator, *args):
        for arg in args:
            try:
                element = self.browser.select(locator, arg)
                if element:
                    self.log.info("[PASS] Method: '{0}-->{1}'".format(__name__,inspect.currentframe().f_code.co_name)
                                  + "An item {} is successfully selected from dropdown".format(arg))
                return element
            except ElementDoesNotExist:
                print('Element: {} is not present in the drop down'.format(arg))
                self.log.error("[FAIL' Method: '{}-->{}'".format(__name__,inspect.currentframe().f_code.co_name) + "An element/item '{}' is not present in the dropdpwn".format(arg))

    def _BG_switchWindowExample(self, locator, locatorType):
        #self.browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")
        btnOpenWin = self._BG_getElement(locator, locatorType)
        btnOpenWin.click()
        window = self.browser.windows
        if window:
            self.log.info("[PASS] Method '{}-->{}'".format(__name__,inspect.currentframe().f_code.co_name)+ "All the active windows are returned")
        return window

    def _BG_navigateToNewTab(self):
        window = self.browser.windows
        return window

    def _BG_closeBrowser(self):
        self.browser.quit()
        self.log.info("[PASS] Method: '{}-->{}'".format(__name__,inspect.currentframe().f_code.co_name) + "Driver {} is successfully close".format(self.browser))

    def _B_screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        now = datetime.now()
        fileName = resultMessage + "." + str(now.strftime("%Y%m%d%H:%M:%S")) + ".png"
        screenshotDirectory = "../screenshots/{0}{1}{2}".format("screenshots","_",str(now.strftime("%Y%m%d")))
        relativeFileName =  fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(screenshotDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.browser.driver.save_screenshot(destinationFile)
            self.log.info("[PASS] Test method: '{0}-->{1}'".format(__name__,inspect.currentframe().f_code.co_name) + ":" + " Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("[FAIL] Test method: '{0}-->{1}'".format(__name__,inspect.currentframe().f_code.co_name) + "### Exception Occurred when taking screenshot")
            #print_stack()