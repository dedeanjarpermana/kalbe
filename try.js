const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

// Setel opsi Chrome WebDriver
const options = new chrome.Options();
options.addArguments("--disable-notifications"); // Opsional: Untuk menonaktifkan notifikasi browser

// Inisialisasi WebDriver
const driver = new Builder()
  .forBrowser('chrome')
  .setChromeOptions(options)
  .build();

// Buka URL login
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');

// Isi kolom username dan password
driver.findElement(By.id('txtUsername')).sendKeys('Admin');
driver.findElement(By.id('txtPassword')).sendKeys('admin123');

// Klik tombol Login
driver.findElement(By.id('btnLogin')).click();

// Tunggu hingga halaman berhasil dimuat
driver.wait(until.urlContains('dashboard'), 5000).then(() => {
  console.log('Login berhasil!');
}).catch((error) => {
  console.error('Login gagal: ' + error);
});

// Tutup browser setelah selesai
driver.quit();
