from selenium import webdriver
from base.selenium_driver import SeleniumDriver


class EmployeeDetailPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    # emp detail

    _header = "//h1[@class='border-bottom border-gray pb-2']"  #XPath

    _empName = "Field.500_1:ValueContainer"   #ID
    _empSummary = "Field.500_2:ValueContainer"  #ID
    _department = "Field.500_7:ValueContainer"  #ID
    _salary = "Field.500_6:ValueContainer" #ID
    _address = "Field.500_25:ValueContainer"  #ID
    _workLocation = "Field.500_8:ValueContainer"  #ID
    _dateOfJoining = "Field.500_3:ValueContainer" #ID
    _employeeStillActive = "Field.500_4:ValueContainer" #ID
    _cubicalLength = "//div[@id='Table500_9:Container']//tr[@id='Row7:Container']//td[@id='Row0.Field500_12:Container']//div[@class='TableCell--input-container']"  # xpath
    _cubicalWidth = "//div[@id='Table500_9:Container']//tr[@id='Row7:Container']//td[@id='Row0.Field500_13:Container']//div[@class='TableCell--input-container']"  #XPATH
    _cubicalColor = "//div[@id='Table500_9:Container']//tr[@id='Row7:Container']//td[@id='Row0.Field500_14:Container']//div[@class='TableCell--input-container']"  #XPATH

    # car1 Detail

    _car1Brand = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_16:Container']//div[@class='TableCell--input-container']" # Xpath
    _car1Model = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_17:Container']//div[@class='TableCell--input-container']" #XPATH
    _car1ModelYear = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_18:Container']//div[@class='TableCell--input-container']" #XPATH
    _car1Trim = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_19:Container']//div[@class='TableCell--input-container']"
    _car1Color = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_20:Container']//div[@class='TableCell--input-container']" #XPATH
    _car1License = "//div[@id='Table500_15:Container']//tr[@id='Row8:Container']//td[@id='Row0.Field500_21:Container']//div[@class='TableCell--input-container']" #XPATH


    # car2 Detail

    _car2Brand = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_16:Container']//div[@class='TableCell--input-container']"  #XPATH
    _car2Model = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_17:Container']//div[@class='TableCell--input-container']" #XPATH"
    _car2ModelYear = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_18:Container']//div[@class='TableCell--input-container']"  #XPATH
    _car2Trim = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_19:Container']//div[@class='TableCell--input-container']"  #XPATH
    _car2Color = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_20:Container']//div[@class='TableCell--input-container']"  #XPATH
    _car2License = "//div[@id='Table500_15:Container']//tr[@id='Row9:Container']//td[@id='Row1.Field500_21:Container']//div[@class='TableCell--input-container']" #XPATH



 #  METHODS
    # emp detail

    def empName(self):
        return self.getText(self._empName, locatorType='id')

    def empSummary(self):
        summaryList =  self.getText(self._empSummary, locatorType='id')
        summary = summaryList.split("\n")
        return summary[2]


    def department(self):
        return self.getText(self._department, locatorType='id')

    def empSalary(self):
        return self.getText(self._salary, locatorType='id')

    def address(self):
        return self.getText(self._address, locatorType='id')

    def workLocation(self):
        return self.getText(self._workLocation, locatorType='id')

    def joningDate(self):
        return self.getText(self._dateOfJoining, locatorType='id')

    def isStillActive(self):
        return self.getText(self._employeeStillActive, locatorType='id')

    def cubicallength(self):
        return self.getText(self._cubicalLength, locatorType='xpath')

    def cubicalWidth(self):
        return self.getText(self._cubicalWidth, locatorType='xpath')

    def cubicalColor(self):
        return self.getText(self._cubicalColor, locatorType='xpath')

    # car1 detail

    def car1Brand(self):
        return self.getText(self._car1Brand, locatorType='xpath')

    def car1Model(self):
        return self.getText(self._car1Model, locatorType='xpath')

    def car1ModelYear(self):
        return self.getText(self._car1ModelYear, locatorType='xpath')

    def car1Trim(self):
        return self.getText(self._car1Trim, locatorType='xpath')

    def car1Color(self):
        return self.getText(self._car1Color, locatorType='xpath')

    def car1License(self):
        return self.getText(self._car1License, locatorType='xpath')

    # car2 Detail

    # car1 detail

    def car2Brand(self):
        return self.getText(self._car2Brand, locatorType='xpath')

    def car2Model(self):
        return self.getText(self._car2Model, locatorType='xpath')

    def car2ModelYear(self):
        return self.getText(self._car2ModelYear, locatorType='xpath')

    def car2Trim(self):
        return self.getText(self._car2Trim, locatorType='xpath')

    def car2Color(self):
        return self.getText(self._car2Color, locatorType='xpath')

    def car2License(self):
        return self.getText(self._car2License, locatorType='xpath')



    def verifyHeader(self, empname):
        result = self.getText(self._header, locatorType='xpath')
        if result == empname:
            return True
        else:
            return False



    def verify_emp_detail(self, employeeName, summary, department, salary, lat, long, workLocation,
                 joningDate, isStillActive, cubicalLength, lengthMeasure, cubicalWidth, widthMeasure, cubicalColor,
                 car1Brand, car1Model, car1ModelYear, car1Trim, car1Color, car1License,
                 car2Brand, car2Model, car2ModelYear, car2Trim, car2Color, car2License):

        verify = []

        empName = self.validateResult(self.empName(), employeeName, ' Employee Name')
        verify.append(empName)

        summary = self.validateResult(self.empSummary(), summary, ' Summary')
        verify.append(summary)

        department = self.validateResult(self.department(), department ," Department")
        verify.append(department)

        salary = self.validateResult(self.empSalary(), salary, " Salary")

        address  = self.validateResult(self.address(), lat+', '+long+ ' Map', " Address")
        verify.append(address)

        workLocation = self.validateResult(self.workLocation(), workLocation, " WorkLocation")
        verify.append(workLocation)

        joningDate = self.validateResult(self.joningDate(), joningDate, " Date of joning")
        verify.append(joningDate)

        isStillActive = self.validateResult(self.isStillActive(), isStillActive, " Is employee still active")
        verify.append(isStillActive)

        cubicalLength = self.validateResult(self.cubicallength(), cubicalLength+lengthMeasure, " Cubical Length")
        verify.append(cubicalLength)

        cubicalWidth = self.validateResult(self.cubicalWidth(), cubicalWidth+widthMeasure, " Cubical Length")
        verify.append(cubicalWidth)

        cubicalColor = self.validateResult(self.cubicalColor(), cubicalColor, ' Cubical Color')
        verify.append(cubicalColor)


        # car1 detail

        car1Brand = self.validateResult(self.car1Brand(), car1Brand, ' Car1 Brand')
        verify.append(car1Brand)

        car1Model = self.validateResult(self.car1Model(), car1Model, ' Car1 Model')
        verify.append(car1Model)


        car1ModelYear = self.validateResult(self.car1ModelYear(), car1ModelYear, ' Car1 Model Year')
        verify.append(car1ModelYear)

        car1Trim = self.validateResult(self.car1Trim(), car1Trim, " Car1 Trim")
        verify.append(car1Trim)


        car1Color = self.validateResult(self.car1Color(), car1Color, " Car1 Color")
        verify.append(car1Color)

        car1License = self.validateResult(self.car1License(), car1License, " Car1 License")
        verify.append(car1License)

        # car2 detail

        car2Brand = self.validateResult(self.car2Brand(), car2Brand, ' Car2 Brand')
        verify.append(car2Brand)

        car2Model = self.validateResult(self.car2Model(), car2Model, ' Car2 Model')
        verify.append(car2Model)

        car2ModelYear = self.validateResult(self.car2ModelYear(), car2ModelYear, ' Car2 Model Year')
        verify.append(car2ModelYear)

        car2Trim = self.validateResult(self.car2Trim(), car2Trim, " Car2 Trim")
        verify.append(car2Trim)

        car2Color = self.validateResult(self.car2Color(), car2Color, " Car2 Color")
        verify.append(car2Color)

        car2License = self.validateResult(self.car2License(), car2License, " Car1 License")
        verify.append(car2License)

        return verify





