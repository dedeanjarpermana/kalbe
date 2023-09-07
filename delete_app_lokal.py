from selenium import webdriver
from selenium.webdriver.support.ui import Select
# modul untuk running lebih lambat
import time  # Impor modul time

# Inisialisasi WebDriver (gunakan browser yang sesuai)
driver = webdriver.Chrome()

# Buka URL
url = "http://localhost:3000"
driver.get(url)

time.sleep(3)
# Temukan elemen input pencarian dengan XPath yang telah Anda berikan
search_input = driver.find_element("xpath", '//*[@id="root"]/div/div/div/input')

time.sleep(2)
# Isi field pencarian dengan teks yang ingin Anda cari
search_input.send_keys('a')


time.sleep(3)
# Klik tombol hapus dengan XPath yang telah Anda berikan

# Temukan elemen yang ingin dihapus dengan XPath
delete_button = driver.find_element("xpath", '//button[contains(text(), "Delete")]')
                                    
# Klik tombol hapus
delete_button.click()

# delete_button = driver.find_element("xpath", '//*[@id="root"]/div/div/table/tbody/tr[23]/td[5]/button')
# delete_button.click()


# Tutup browser
driver.quit()


