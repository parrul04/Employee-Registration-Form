from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilites.custom_log import CustomLogger
import logging
from traceback import print_stack
from datetime import datetime
import os
import time
import inspect

class SeleniumDriver:

    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType='id'):

        try:
            locatorType = locatorType.lower()

            if locatorType == 'id':
                return By.ID

            elif locatorType == 'xpath':
                return By.XPATH

            elif locatorType == 'class':
                return By.CLASS_NAME

            elif locatorType == 'name':
                return By.NAME

            elif locatorType == 'linktext':
                return By.LINK_TEXT

            elif locatorType == 'partiallinktext':
                return By.PARTIAL_LINK_TEXT

            elif locatorType == 'tag':
                return By.TAG_NAME

            elif locatorType == 'cssselector':
                return By.CSS_SELECTOR

            else:
                print("No locator Type found using locator type: " + locatorType)
        except:
            print("  Exception occoured : No locator Type found using locator type: " +locatorType)
            return False


    def getElement(self, locator, locatorType='id'):

        element = None

        try:
            ByType = self.getByType(locatorType)
            element = self.driver.find_element(ByType, locator)
            self.log.info("  Element found using locator Type: " + locatorType + " and locator : " + locator)


        except:
            self.log.error("  Exception Occoured : Element found using locator Type: " + locatorType + " and locator : " + locator)


        return element

#             ELEMENT CLICK

    def elementClick(self, locator='', locatorType='id', element = None):


    # if element is already give click on it otherwise find element using locator first
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("  Element click using locatorType: " + locatorType + " and locator : " + locator)


        except:
            self.log.error("  Exception Occoured : Element cannot click using locator Type: "
                           + locatorType + "and locator : " + locator)
            print_stack()


    def sendData(self, data, locator='', locatorType='id', element= None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)

            self.log.info(" Data sent to en element using locator Type: "+ locatorType + " and locator : "  + locator)


        except:

            self.log.error(" Exception occoured : Data cannot sent with locator Type: " + locatorType + " and locator" + locator)

            print_stack()



    def DropDown(self, locator='', locatorType='id', index='', value='', visible_text='', element=None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            sel = Select(element)

            if index:
                sel.select_by_index(index)
                self.log.info(" Element seleced by index:: " + str(index))


            if value:
                sel.select_by_value(value)
                self.log.info(" Element seleced by value:: " + str(value))


            if visible_text:
                sel.select_by_visible_text(visible_text)
                self.log.info(" Element seleced by visible text:: " + str(visible_text))


        except:
            self.log.error(" Exception occured element not selected from dropdown")

            print_stack()

#*************      Title     *******

    def getTitle(self):
        return self.driver.title



#   Get url of current page



    def getUrl(self):

        return self.driver.current_url

#  get text

    def getText(self, locator='', locatorType='id', element=None):
        text = None
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            self.log.info("get element text using locator Type:" + locatorType + " and locator : " +locator)


        except:
            self.log.error(" Exception Occoured :cannot get element text using locator Type:", locatorType +  " and locator : " + locator)

        return text



# date format

    def dateFmt(self,date):
        d = datetime.strptime(date, '%b %d, %Y')
        return d.strftime('%m/%d/%Y')


#       TAKE SCREENSHOTS of current open webpage


    def screenShots(self, resultMessage):


        FileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"

        # now goto screenshoot dir for that go out from current base dir so use ..

        screenshotdir = "../screenshots/"

         # now the file path
        RelativeFilepath =  screenshotdir + FileName

        # current dir

        currentdir = os.path.dirname(__file__)

        # Destinationdir relative to current dir

        destinationfilePath = os.path.join( currentdir , RelativeFilepath)

        destinationdirpath = os.path.join( currentdir, screenshotdir )

        try:
            if not os.path.exists(destinationdirpath):
                os.makedirs(destinationdirpath)
            self.driver.save_screenshot(destinationfilePath)
            self.log.info(" ##Screenshot Saved to directory " + destinationdirpath)

        except:
            self.log.error("### EXCEPTION OCCOURED!!!")
            print_stack()


    # validate actual result with exected result

    def validateResult(self, actual, expected, testName=''):

        try:

            if actual == expected:
                self.log.info(testName + " : Matchs "  + " the actual value is : " + actual + " and expected value is: " + expected )
                return True

            else:
                self.log.error(testName + " : doesn't match." + " The actual value is : " + actual +" and expected value is: " +
                              expected)
                return False

        except:
            self.log.error(testName + " : doesn't match" + " the actual value is : " + actual + " and expected value is: " + expected )
            print_stack()
