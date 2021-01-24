from selenium import webdriver
from base.selenium_driver import SeleniumDriver
from time import sleep
from utilites.custom_log import CustomLogger
import logging

class EmployeeRegistrationPage(SeleniumDriver):

    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    # locators

    _employee_name = "FL:_ctl0:_ctl3" #ID
    _summary = "FL:_ctl1:_ctl4" # ID
    _department = "FL:_ctl3:_ctl3" # ID
    _salary = "FL:_ctl4:_ctl3" #ID
    _lat = "FL_latTxt_5" # ID
    _long = "FL_longTxt_5" #ID
    _work_Location = "FL:_ctl6:_ctl3" #ID
    _joning_Date = 'FL:_ctl8:_ctl3' # ID
    _is_employee_active_yes = 'FL__ctl3_9' #ID
    _is_employee_active_no = 'FL__ctl5_9'  #ID
    _cubical_length = "//tr[@id='Row0:Container']/td[2]//span/input[@type='text']"  #XPATH
    _length_measure = "//tr[@id='Row0:Container']/td[2]//span/select"  #XPATH
    _cubical_width = "//tr[@id='Row0:Container']/td[3]//span//input[@type='text']" #XPATH
    _width_measure = "//tr[@id='Row0:Container']/td[3]//span/select" #XPATH
    _cubical_color = "//tr[@id='Row0:Container']/td[4]//input"  #XPATH


    # car1 Detail locators

    _car1_brand = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[2]//input" #XPATh
    _car1_model = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[3]//input" #XPATH
    _car1_model_Year = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[4]//input" #xpath
    _car1_trim = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[5]//input"  #XPATH
    _car1_color = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[6]//input" #XPATH
    _car1_license = "//div[@id='Table500_15:Container']//tbody//tr[2]//td[7]//input" #XPATH

    # car2 locators

    # car1 Detail locators

    _car2_brand = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[2]//input"  # XPATh
    _car2_model = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[3]//input"  # XPATH
    _car2_model_Year = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[4]//input"  # xpath
    _car2_trim = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[5]//input"  # XPATH
    _car2_color = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[6]//input"  # XPATH
    _car2_license = "//div[@id='Table500_15:Container']//tbody//tr[3]//td[7]//input"  # XPATH


    _submit = "//button[text()='Submit']" # Xpath

    _header = "//h1[@class='border-bottom border-gray pb-2']"  #XPATH


    def employeeName(self, name):

        self.sendData(name, self._employee_name, locatorType='id')

    def summary(self, summary):
        self.sendData(summary, self._summary, locatorType='id')

    def department(self, department):
        self.DropDown( self._department, locatorType='id', visible_text=department)

    def salary(self, salary):
        self.sendData(salary, self._salary, locatorType='id')

    def lat(self, lat):
        self.sendData(lat, self._lat, locatorType='id')

    def long(self, long):
        self.sendData(long, self._long, locatorType='id')

    def workLocation(self, workLocation):
        self.DropDown(self._work_Location, locatorType='id', visible_text=workLocation)

    def joningDate(self, date):
        date = self.dateFmt(date)
        self.sendData(date, self._joning_Date, locatorType='id')

    def isEmployeeActive(self,active):
        if active == 'Yes':
            self.elementClick(self._is_employee_active_yes, locatorType='id')

        if active == 'No':
            self.elementClick(self._is_employee_active_no, locatorType='id')




    # cubical data

    def  cubicalLength(self, length):
        self.sendData(length, self._cubical_length, locatorType='xpath')

    def lengthMeasure(self, measure):
        self.DropDown(self._length_measure, locatorType='xpath', visible_text=measure)

    def cubicalWidth(self, width):
        self.sendData(width, self._cubical_width, locatorType='xpath')

    def widthMeasure(self, measure):
        self.DropDown(self._width_measure, locatorType='xpath', visible_text=measure)

    def cubicalColor(self, color):
        self.sendData(color, self._cubical_color, locatorType='xpath')

    # car 1 details

    def car1Brand(self, car1_brand):
        self.sendData(car1_brand, self._car1_brand, locatorType='xpath')

    def car1Model(self, car1_model):
        self.sendData(car1_model, self._car1_model, locatorType='xpath')

    def car1ModelYear(self, car1_modelYear):
        self.sendData(car1_modelYear, self._car1_model_Year, locatorType='xpath')

    def car1Trim(self, car1_trim):
        self.sendData(car1_trim, self._car1_trim, locatorType='xpath')

    def car1Color(self, car1_color):
        self.sendData(car1_color, self._car1_color, locatorType='xpath')

    def car1License(self, car1_license):
        self.sendData(car1_license, self._car1_license, locatorType='xpath')


    # car 2 details

    def car2Brand(self, car2_brand):
        self.sendData(car2_brand, self._car2_brand, locatorType='xpath')

    def car2Model(self, car2_model):
        self.sendData(car2_model, self._car2_model, locatorType='xpath')

    def car2ModelYear(self, car2_modelYear):
        self.sendData(car2_modelYear, self._car2_model_Year, locatorType='xpath')

    def car2Trim(self, car2_trim):
        self.sendData(car2_trim, self._car2_trim, locatorType='xpath')

    def car2Color(self, car2_color):
        self.sendData(car2_color, self._car2_color, locatorType='xpath')

    def car2License(self, car2_license):
        self.sendData(car2_license, self._car2_license, locatorType='xpath')

    def submit(self):
        self.elementClick(self._submit, locatorType='xpath')


    def fillForm(self, employeeName, summary, department, salary, lat, long, workLocation,
                 joningDate, isStillActive, cubicalLength, lengthMeasure, cubicalWidth, widthMeasure, cubicalColor,
                 car1Brand, car1Model, car1ModelYear, car1Trim, car1Color, car1License,
                 car2Brand, car2Model, car2ModelYear, car2Trim, car2Color, car2License):

        self.employeeName(employeeName)
        self.summary(summary)
        self.department(department)
        self.salary(salary)
        self.driver.execute_script("window.scrollBy(1,500)")
        self.lat(lat)
        self.long(long)
        self.workLocation(workLocation)
        self.joningDate(joningDate)
        self.isEmployeeActive(isStillActive)
        self.cubicalLength(cubicalLength)
        self.lengthMeasure(lengthMeasure)
        self.cubicalWidth(cubicalWidth)
        self.widthMeasure(widthMeasure)
        self.cubicalColor(cubicalColor)

        # car1 details

        self.car1Brand(car1Brand)
        self.car1Model(car1Model)
        self.car1ModelYear(car1ModelYear)
        self.car1Trim(car1Trim)
        self.car1Color(car1Color)
        self.car1License(car1License)

        # Car2

        # car1 details

        self.car2Brand(car2Brand)
        self.car2Model(car2Model)
        self.car2ModelYear(car2ModelYear)
        self.car2Trim(car2Trim)
        self.car2Color(car2Color)
        self.car2License(car2License)
        self.submit()


    def verifyUrl(self):

        result = self.getUrl()


        if result == "https://rpmsoftware.com/hiring/2020/integration-test/form.html":
            return True
        else:
            return False






