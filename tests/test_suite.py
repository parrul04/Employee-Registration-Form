import unittest
from tests.registration.test_employee_registration import EmployeeRegistration
from tests.registration.test_registration_detail import EmployeeDetail


# get all test from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(EmployeeRegistration)
tc2 = unittest.TestLoader().loadTestsFromTestCase(EmployeeDetail)


# create test suite

smoke_test = unittest.TestSuite([tc1, tc2])

# run testsuite

unittest.TextTestRunner(verbosity=2).run(smoke_test)
