# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# def get_driver():
#     service = Service(ChromeDriverManager().install())
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--start-maximized")
#     options.add_extension('extension/adblocker.crx')
#     driver = webdriver.Chrome(service=service, options=options)

#     return driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

os.system("Xvfb :99 -screen 0 1920x1080x16 &")

def get_driver(adblock = False, vpn = False):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    
    if adblock == True:
        options.add_extension("extension/Adblock_Plus-free_ad_blocker-Chrome_Web_Store_4.15.0.0.crx")
    
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver
