chrome_driver = "./chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver  = webdriver.Chrome(chrome_driver)
URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url = URL)

# count = driver.find_element_by_id(id_="articlecount")
# print(count.find_element_by_tag_name("a").text)
# #you can use above or below method where you have div(name) and tag you want to add
# count = driver.find_element_by_css_selector(css_selector="#articlecount a")

#Giving the input to the website which is operating
First_Name_input = driver.find_element_by_name("fName")
First_Name_input.send_keys("Shubham")
Last_Name_Input = driver.find_element_by_name("lName")
Last_Name_Input.send_keys("Das")
Email_Input = driver.find_element_by_name("email")
Email_Input.send_keys("smtp.check.shubham@gmail.com")

# Always use if only one button is given try to give css_find object
Button_Input = driver.find_element_by_css_selector("form button")
Button_Input.send_keys(Keys.ENTER)

driver.quit()