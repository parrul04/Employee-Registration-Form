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
class EmployeeDetail(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):

        self.emp_reg_page = EmployeeRegistrationPage(self.driver)
        self.verifyTest = VerificationStatus(self.driver)
        self.emp_detail = EmployeeDetailPage(self.driver)

        # verify Emp detail

    @pytest.mark.run(order=2)
    @data(*getCsvData("/Users/parulagarwal/Documents/workspace_python/Employee_Registration/testData.csv"))
    @unpack
    def test_emp_detail(self, empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License):


        emp_detail = self.emp_detail.verify_emp_detail(empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License)

        if False in emp_detail:
            self.verifyTest.markFinal('test_emp_detail', False, " Employee data doesn't match")
            # print("Employee detail doesn't match with test data")

        else:
            self.verifyTest.markFinal('test_emp_detail', True, " Employee data matchs")

    # verify Header name
    @pytest.mark.run(order=1)
    @data(*getCsvData("/Users/parulagarwal/Documents/workspace_python/Employee_Registration/testData.csv"))
    @unpack
    def test_verify_header(self, empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License):

        self.emp_reg_page.fillForm(empName, Summary, Department, Salary, lat, long, workLocation,
                               JoningDate, isStillActive, CubicalLength, Lengthmwasure, CubicalWidth, widthMeasure, cubicalColor,
                               car1Brand, car1Model, car1ModelYear, car1Trim, car1color, car1License,
                               car2Brand, car2Model, car2ModelYear, car2Trim, car2color, car2License)

        headerName = self.emp_detail.verifyHeader(empName)
        # assert headerName == True
        if headerName == True:
            self.verifyTest.markFinal('test_verify_header', headerName,
                                      'Employee Name is displayed as a header of detail page')
        else:
            self.verifyTest.markFinal('test_verify_header', headerName,
                                      'Employee Name is not displayed as a header of detail page')
