from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeOptions'ı başlatma
chrome_options = webdriver.ChromeOptions()

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver_path = "C:/Users/Doğukan/OneDrive/Masaüstü/chromedriver_win32/chromedriver.exe"

chrome_options.binary_location = brave_path

# ChromeDriver'ı başlatma
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Web sayfasına gidin
driver.get("https://www.google.com")

# Sayfanın adını yazdırın
print(driver.title)

# Kullanıcıdan bir giriş alana kadar bekleyin
input("Press Enter to quit...")


