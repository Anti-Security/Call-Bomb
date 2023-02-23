import os
from time import sleep
from selenium import webdriver
from colorama import Fore, init
from selenium.webdriver.common.keys import Keys

init(autoreset="true")

def data():
    global browser

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome('chromedriver/chromedriver', options=options)
    browser.get("https://id.vk.com/auth?app_id=7913379&v=1.58.5&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin&uuid=OU9h-RgQm6peljHtJiPht&scheme=bright_light&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl91cCJ9fQ%3D%3D")
    sleep(3)
    os.system("cls")

def call():
    phone_number = input(Fore.YELLOW + "Telefon numarasını giriniz: ")
    
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div/form/div[1]/section/div[1]/div/div/input').send_keys(Keys.CONTROL + "a")
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div/form/div[1]/section/div[1]/div/div/input').send_keys(Keys.DELETE)
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div/form/div[1]/section/div[1]/div/div/input').send_keys(phone_number)
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div/form/div[2]/div[1]/button').click()
    sleep(1)

    try:
        value = browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div/div/div/div/form/div[1]/h1/div/span')
        print(Fore.GREEN + "[*] Bot Gönderildi")
        sleep(3)
    
    except:
        print(Fore.RED + "[*] Bot Gönderilemedi")
        sleep(3)

data()
call()