# Employee-Registration-Form

a. Issue Heading: Employee detail doesn't match

b. Issue Description: Employee Joining date doesn't match

c. Expexted Behaivour : Actual Joining date is " Jun 4, 2018" on Employee detail page but Expected joining date is " Jan 4, 2018'.





STEPS TO RUN TEST SUIT 
 py.test -s -v tests/test_suite.py --browser chrome
 or py.test -s -v tests/test_suite.py
 

STEPS TO RUN test_registration_detail.py
py.test -s -v tests/registration/test_registration_detail.py
py.test -s -v tests/registration/test_registration_detail.py --browser chrome

STEPS TO RUN test_registration.py
 py.test -s -v tests/registration/test_employee_registration.py --browser chrome
 
 
 * NOTE:  You can write browser from firefox, chrome, ie, safari
