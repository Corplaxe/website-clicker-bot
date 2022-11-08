from require import *
import pyautogui
import keyboard
import time
import random
a = input('aranacak şeyi girin - ')
def main():
    browser.get('https://www.google.com')
    browser.find_element(by='css selector',value='.gLFyf').send_keys(a)
    time.sleep(1)
    browser.find_element(by='css selector',value='div.lJ9FBc:nth-child(9) > center:nth-child(2) > input:nth-child(1)').click()
    time.sleep(1)
    #w = browser.find_element(by='css selector',value='.FPdoLc > center:nth-child(1) > input:nth-child(1)')
    #w.click()
    time.sleep(4)
    c = browser.find_element(by='xpath',value='/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3')
    c.click()
main()
while True:
    for i in range(1,20):
        x = random.randint(121,1778)
        y = random.randint(232,1009)
        time.sleep(5)
        pyautogui.click(x=x,y=y)
        pyautogui.press('down')
    k = 0
    with open('sayı.txt','+a',encoding='utf-8') as file:
        k+=1
        file.write('{}'.format(k))
    uyku = random.randint(180,300)
    time.sleep(uyku)
    main()
    if keyboard.is_pressed('esc'):
        break