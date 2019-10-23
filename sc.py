from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
browser.get('http://www.gmail.com')
time.sleep(2)
email = browser.find_element_by_class_name('whsOnd.zHQkBf')
email.send_keys('sender gmail id')
push = browser.find_element_by_id('identifierNext') 
#time.sleep(50)
push.click()


time.sleep(5)

password = browser.find_element_by_class_name('whsOnd.zHQkBf')

# own password in keys
password.send_keys('My_password')
push1 = browser.find_element_by_id('passwordNext') 
push1.click()

time.sleep(5)

compose_msg = browser.find_element_by_class_name('z0') 
compose_msg.click()

time.sleep(10)
#reciever address in send keys
reciever = browser.find_element_by_class_name("vO")
reciever.send_keys('Reciever email id ')

time.sleep(2)
#enter your suject for mail "hi" in this case
subject = browser.find_element_by_class_name("aoT")
subject.send_keys("hi")

time.sleep(2)
#enter ody of your mail(take as "hello" in this case)
body=browser.find_element_by_class_name("Am.Al.editable.LW-avf.tS-tW")
body.send_keys("hello")

time.sleep(2)

send = browser.find_element_by_class_name("T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
send.click()
#mail sent succesfully
