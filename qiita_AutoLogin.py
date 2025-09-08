# seleniumの基本的な更新
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Chromeドライバマネジャーの更新
service = Service(ChromeDriverManager().install)
driver = webdriver.Chrome(service=service)

#新たにChromeのWEBサイトにアクセスする
driver =webdriver.Chrome()
driver.get("https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2F&realm=qiita")

#ユーザー名とパスワードの欄を探す
identity = driver.find_element(By.ID, "identity")
password = driver.find_element(By.ID, "password")

#ユーザー名、パスワードを入力
identity.send_keys("ramunedayo")
password.send_keys("Seruka373")

#ログインする 
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()

