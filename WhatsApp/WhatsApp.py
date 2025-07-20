# Importing all Dependencies

import pathlib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://web.whatsapp.com/"
path = ChromeDriverManager().install()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.114 Safari/537.36"
user_data_dir = pathlib.Path().absolute()

services = Service(path)
chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument(f"user-data-dir={user_data_dir}\\chromeData")

driver = webdriver.Chrome(service=services, options=chrome_options)
driver.minimize_window()
driver.get(url=url)