from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time  # Impor modul time

# driver untuk menambahkan waktu tunggu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Buka URL
url = "http://103.16.199.79:5000/login"
driver.get(url)
time.sleep(3)

# wait = WebDriverWait(driver, 3)  # Tunggu hingga 20 detik
# elemen = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/form/div/div/div[4]/input")))
# Isi kolom Username dan Password
username = driver.find_element("id", 'email')
password = driver.find_element("id", 'password')

# username = driver.find_element("name", 'username')
# password = driver.find_element("name", 'password')

#cara gini ga bisa
# username = driver.find_element_by_class_name('oxd-input oxd-input--focus')
# password = driver.find_element_by_class_name('oxd-input oxd-input--active') 

# cara ini berhasil, tinggal nambah wait 20 detik
# username= driver.find_element("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# password= driver.find_element("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# username = driver.find_element("xpath", '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# password = driver.find_element("xpath", '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
time.sleep(3)
username.send_keys("admin@mail.com")

time.sleep(3)
password.send_keys("12345")

# Submit formulir login
time.sleep(3)
password.send_keys(Keys.RETURN)

# Tunggu beberapa saat untuk memastikan halaman terbuka
driver.implicitly_wait(15)

dashboard = driver.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div/ul/li[2]/a/span')
time.sleep(2)
dashboard.click()
# Verifikasi apakah login berhasil
# if "a_Dashboard" in driver.current_url:
#     print("Login berhasil!")
# else:
#     print("Login gagal!")

# Tutup browser
driver.quit()
