# coding: utf-8
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extension import proxies
from colorama import Fore, init
from random import choice
import os
import time

def open_browser():
    chrome_options = webdriver.ChromeOptions()
    proxies_extension = proxies("voltz1020", "voltz1020_country-br", "geo.iproyal.com", "12321")
    chrome_options.add_extension(proxies_extension)
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://api.my-ip.io/v2/ip.json")
    input("")
    
if __name__ == "__main__":
    driver = open_browser()
