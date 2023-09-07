from selenium import webdriver
from selenium.webdriver.support.ui import Select
# modul untuk running lebih lambat
import time  # Impor modul time




# Inisialisasi WebDriver (gunakan browser yang sesuai)
driver = webdriver.Chrome()

# Buka URL
url = "http://localhost:3000/add"
driver.get(url)

# Tambahkan penundaan selama 2 detik
time.sleep(3)
# Isi data form nama
name = driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[1]/div/input')
name.send_keys("Viona Lofreeey")

# Tambahkan penundaan selama 2 detik
time.sleep(3)
# isi email
email = driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[2]/div/input')
email.send_keys("vionalofrey@gmail.com")


# Tambahkan penundaan selama 2 detik
time.sleep(3)
# pilih jenis kelamin
# Field Identitas (Dropdown)
select_identitas = Select(driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[3]/div/div/select'))
select_identitas.select_by_value('Female')  



# Cari tombol "Save" dengan teks "Save" di dalamnya dan klik
save_button = driver.find_element("xpath", '//button[contains(text(), "Save")]')
save_button.click()

# Tunggu sebentar (Opsional: Tambahkan waktu tunggu jika perlu)
# driver.implicitly_wait(10)

# Tutup browser
driver.quit()


