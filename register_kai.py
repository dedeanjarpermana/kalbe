# Impor Modul Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka url 
url = "https://booking.kai.id/register"
driver.get(url)

# isi data pendaftaran 
# Field Jenis Kelamin (Dropdown)
# Field Jenis Kelamin (Dropdown)
select_jenis_kelamin = Select(driver.find_element("id", 'member_title'))
select_jenis_kelamin.select_by_value('1')  # Laki-lak

# Field Nama Lengkap
nama_lengkap = driver.find_element("xpath", '//*[@id="member_nama"]')
nama_lengkap.send_keys("Dede Anjar")

# Field Identitas (Dropdown)
select_identitas = Select(driver.find_element("id", 'member_tandapengenal'))
select_identitas.select_by_value('ktp')  # NIK

# Field Nomor Identitas
nomor_identitas = driver.find_element("xpath", '//*[@id="member_notandapengenal"]')
nomor_identitas.send_keys("3217041703860003")

# Field Tanggal Lahir
tanggal_lahir = driver.find_element("xpath", '//*[@id="member_tanggallahir"]')
tanggal_lahir.send_keys("17-Maret-1986")

# Field No. HP
no_hp = driver.find_element("xpath", '//*[@id="member_nohp"]')
no_hp.send_keys("085860495780")

# Field Email
email = driver.find_element("xpath", '//*[@id="member_email"]')
email.send_keys("dedeanjarpermana@gmail.com")

# Field Password
password = driver.find_element("xpath", '//*[@id="member_pass1"]')
password.send_keys("dedeanjar1980")

# Field Konfirmasi Password
konfirmasi_password = driver.find_element("xpath", '//*[@id="member_pass2"]')
konfirmasi_password.send_keys("dedeanjar1980")

# Submit formulir pendaftaran
driver.find_element_by_id('btn_submit').click()

# tutup browser
driver.quit()
