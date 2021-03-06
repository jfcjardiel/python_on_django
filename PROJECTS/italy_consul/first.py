from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os
from selenium.webdriver.common.keys import Keys
import time
import winsound


#setting basic configurations
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"   #  undefined

#login 
driver = webdriver.Chrome()
#setting load timeout
driver.set_page_load_timeout(60)
driver.get("https://prenotami.esteri.it/")
email_box = driver.find_elements(By.ID, "login-email")
password_box = driver.find_elements(By.ID, "login-password")
email_box[0].send_keys('pamela_pasinato@hotmail.com')
time.sleep(2)
password_box[0].send_keys('Eweiquie1!')

button = driver.find_elements(By.XPATH, "//button[contains(@class,'button primary g-recaptcha')]")
button[0].click()

time.sleep(30)

#enter in the page to submit the informations
driver.get("https://prenotami.esteri.it/Services/Booking/751")

tentativa = 0
i=0
while(True):
    print(tentativa, 'tentativa')
    #sending file the pdf
    file_location = os.path.join('C:\\Users\\jfcjardiel', 'Downloads', 'Fatura_Claro_unlocked.pdf')
    choose_file = driver.find_elements(By.ID, "File_0")
    choose_file[0].send_keys(file_location)

    #checking the privacy check
    privacy_check = driver.find_elements(By.ID, "PrivacyCheck")
    privacy_check[0].click()

    try:
        #submit form
        submit = driver.find_elements(By.ID, "btnAvanti")
        submit[0].click()
        time.sleep(60)
        test = driver.find_elements(By.ID, "ServizioDescrizione")
        if test:
        while(i<50):
                winsound.Beep(400,500)
                i = i+1
        break
    except:
        driver.get("https://prenotami.esteri.it/Services/Booking/751")
        print('tentando novamente')
        time.sleep(1)
    tentativa = tentativa + 1
