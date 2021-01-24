from selenium import webdriver


baseurl = "https://rpmsoftware.com/hiring/2020/integration-test/form.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseurl)
driver.implicitly_wait(10)



name = driver.find_element_by_xpath("//div[@id='500_2']//span[@id='Field.500_2:ValueContainer']")
l = name.text
n = l.split("\n")

print(n[2])

driver.quit()





