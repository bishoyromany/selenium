from selenium import webdriver 
from time import sleep 

usr=input('Enter Email Id / Phone Number:')  
pwd=input('Enter Account Password:')  

# add web driver path  
driver = webdriver.Chrome(executable_path="D:\web_drivers\chromedriver.exe")

# add facebook url website
driver.get('https://www.facebook.com/') 

# add email / phone
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email ID / Phone Number Entered") 

# add password
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password Entered") 

# submit the form
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

print ("Loged in to facebook") 

# quit option
input('Press anything to quit') 
driver.quit() 
print("Finished") 

  
