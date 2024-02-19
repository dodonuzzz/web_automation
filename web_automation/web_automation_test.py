from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# UYARI !!! WEBDRİVER PROJENİN HAZIRLANDIĞI TARİH 20.02.2024 İTİBARİYLE PYTHON 3.12 SÜRÜMÜNÜ DESTEKLEMEMEKTEDİR. ŞAYET PROGRAM ÇALIŞMAZSA PYTHON'IN ALT SÜRÜMLERİNİ KULLANINIZ.

# ChromeOptions'ı başlatma
chrome_options = webdriver.ChromeOptions()

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver_path = "C:/Users/Doğukan/OneDrive/Masaüstü/chromedriver_win32/chromedriver.exe"

chrome_options.binary_location = brave_path

# ChromeDriver'ı başlatma
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Web sayfasına gidin
driver.get("https://www.google.com")

try:
    # Formdaki Öğelerin Yüklenmesini Bekleyin
    input_field_xpath = "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input"  # Giriş alanının XPath'i
    submit_button_xpath = "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]"  # Gönderme düğmesinin XPath'i

    input_field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, input_field_xpath)))
    submit_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))

    input_field.send_keys("Formu Dolduruyorum.")

    # Formu Gönderin
    submit_button.click()

    print("Form Başarıyla Gönderildi.")
except Exception as e:
    print("Form Yüklenemedi.")
    print("Hata: ", e)
finally:
    driver.quit()


