from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from typing import Text
import random
import time

code = input("Code: ")
name = input("Name: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://jklm.fun/")
print("Lunching...")
driver.delete_all_cookies()
print("Deleting cookies...")

time.sleep(3)

print("Joining Room...")
code_box = driver.find_element_by_css_selector(".joinRoom input[type=text]")
code_box.send_keys(code)
time.sleep(0.5)
code_box.send_keys(Keys.RETURN)

time.sleep(3)

print("Setting up a nickname")
name_box = driver.find_element_by_css_selector(".setNickname.page .nickname")
name_box.send_keys(name)
time.sleep(0.5)
name_box.send_keys(Keys.RETURN)

time.sleep(3)

iframe = driver.find_element_by_css_selector("iframe")
driver.switch_to.frame(iframe)
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

while True:
    button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/button")
    if(button.is_displayed()):
        time.sleep(1)
        button.click()
        print("Game joined!")
        alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
        time.sleep(1)
    
    player = driver.find_element_by_class_name("player").text
    input_box = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
      
    if(player == "" and input_box.is_displayed()):
        time.sleep(0.25)
        syl = driver.find_element_by_class_name("syllable").text
        syl = syl.lower()
        print("It's your turn with syllable: " + syl )

        f= open('wordlist.txt', mode='r')
        my_list = [line.rstrip('\n') for line in f]
        words = []
        final_words = []
        
        x = 0
        for i in my_list:   
            if syl in my_list[x]:
                words.append(my_list[x])
            x = x + 1

        y = len(words)-1
        print("Words found: ", y)
      
        for x in range(len(alpa)):
            for y in range(len(words)):
                if(alpa[x] in words[y] and words[y] not in final_words):
                    final_words.append(words[y])

        if(final_words == []):
            final_words = words
            print("Most optimal word not found")
        else:
            print("Words with letters that weren't used", len(final_words) - 1)

        while input_box.is_displayed():
            q = 0
            final = final_words[random.randint(0, len(final_words) - 1)]
            print("Trying word: ", final)
            z = len(final)
            time.sleep(random.uniform(0.3, 1))
            for i in range(z):
                input_box.send_keys(final[q])
                q = q + 1
                time.sleep(random.uniform(0.1, 0.16))

            input_box.send_keys(Keys.RETURN)
            y = y + 1
            time.sleep(0.5)

        long = len(final)
        for y in range(long):
            if(final[y] in alpa):
                alpa.remove(final[y])

        print("Word used successfully")
        print("Missing letters for next life: ")
        for x in range(len(alpa)):
            print(alpa[x], end=", ")
            
        print("\n")

        if(alpa == []):
            print("All letters used")
            alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

        words.clear()
        final_words.clear()
        f.close()
