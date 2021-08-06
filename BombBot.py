from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
import time
import string
from typing import Text
from selenium.webdriver.common.action_chains import ActionChains
import random

code = input("Code: ")
name = input("Name: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://jklm.fun/")
driver.delete_all_cookies()

time.sleep(3)

code_box = driver.find_element_by_css_selector(".joinRoom input[type=text]")
code_box.send_keys(code)
code_box.send_keys(Keys.RETURN)

time.sleep(3)

name_box = driver.find_element_by_css_selector(".setNickname.page .nickname")
name_box.send_keys(name)
name_box.send_keys(Keys.RETURN)

time.sleep(3)

iframe = driver.find_element_by_css_selector("iframe")
driver.switch_to.frame(iframe)



while True:
    button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/button")
    if(button.is_displayed()):
        time.sleep(1)
        button.click()
        time.sleep(1)
    
    player = driver.find_element_by_class_name("player").text
    input_box = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
      
    if(player == "" and input_box.is_displayed()):
        time.sleep(0.25)
        syl = driver.find_element_by_class_name("syllable").text
        syl = syl.lower()
        print("It's your turn with syllable: " + syl )

        f= open('wordlist.txt',mode='r')
        my_list = [line.rstrip('\n') for line in f]
        words = []
        
        x = 0
        for i in my_list:   
            if syl in my_list[x]:
                words.append(my_list[x])
            x = x + 1

        print("Words found: ")
        y = len(words)
        print(y)

      
        while input_box.is_displayed():
            q = 0
            final = words[random.randint(0, y)]
            z = len(final)
            time.sleep(random.uniform(0.3, 1))
            for i in range(z):
                input_box.send_keys(final[q])
                q = q + 1
                time.sleep(random.uniform(0.01, 0.25))

            input_box.send_keys(Keys.RETURN)
            y = y + 1
            time.sleep(0.5)

        words.clear()
        
        f.close()
