from selenium import webdriver
from pages.registration.employee_registration_page import EmployeeRegistrationPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utilites.readData import getCsvData
from pages.registration.employee_detail_page import EmployeeDetailPage
from utilites.verificationStatus import  VerificationStatus

@ddt
@pytest.mark.usefixtures("oneTimeSetUp", 'setUp')
class EmployeeRegistration(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):

        self.emp_reg_page = EmployeeRegistrationPage(self.driver)
        self.verifyTest = VerificationStatus(self.driver)


    # emp_reg_page = EmployeeRegistrationPage(driver)
    # verifyTest = VerificationStatus(driver)

    @data(*getCsvData("/Users/parulagarwal/Documents/workspace_python/Employee_Registration/testData.csv"))
    @unpack


    def test_employee_register(self, empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License):

        self.emp_reg_page.fillForm(empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License)

        """
        validate after submit form user navigate to following link/page
        https://rpmsoftware.com/hiring/2020/integration-test/form.html
        """

        result = self.emp_reg_page.verifyUrl()
        #assert result == True
        if result == True:
            self.verifyTest.markFinal('test_employee_register', result, 'User is navigated to the employee detail page')
        else:
            self.verifyTest.markFinal('test_employee_register', result, 'User is not navigated to the employee detail page')



    #
    # def test_employee_register(self):
    #
    #
    #     self.emp_reg_page.fillForm('Isabel Britt', 'This is a test Employee Summary.', 'Management', '$50,000.00',
    #                                '34.833850°', '106.748580°','Headquarters', 'Jan 4, 2018', 'Yes', '47', 'in', '21', 'in', 'Brown',
    #                                'Ford', 'Taurus', '2018', 'SEL', 'Black', 'TEST-0001',
    #                                'Ford', 'F150', '2015', 'XLT', 'Red', 'Test-0002')
    #
    #     """
    #     validate after submit form user navigate to following link/page
    #     https://rpmsoftware.com/hiring/2020/integration-test/form.html
    #     """
    #
    #     result = self.emp_reg_page.verifyUrl()
    #     #assert result == True
    #     if result == True:
    #         self.verifyTest.markFinal('test_employee_register', result, 'User is navigated to the employee detail page')
    #     else:
    #         self.verifyTest.markFinal('test_employee_register', result, 'User is not navigated to the employee detail page')
    #



        #
        # self.driver.quit()





