from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configurare driver Chrome
# TODO Adaugare path-ul catre propriul chrome driver
chrome_driver_path = '/Users/raresrosu/Downloads/chromedriver_mac64 (1)'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigăm către site-ul Emag
driver.get('https://www.emag.ro/')

# Găsim elementul care declanșează bara de căutare
trigger_element = driver.find_element(By.CSS_SELECTOR, 'div.searchbox-overlay-trigger.searchbox-trigger.visible-xs')

# Folosim JavaScript pentru a declanșa evenimentul de clic pe element
driver.execute_script("arguments[0].click();", trigger_element)

# Așteptăm ca input-ul de căutare să fie vizibil
time.sleep(2)

# Găsim elementul de căutare după ID
search_input = driver.find_element(By.ID, 'searchboxAutocomplete')

# Introducem cautarea
search_input.send_keys('casti wireless')

# Găsim elementul butonului de căutare
search_button = driver.find_element(By.CLASS_NAME, 'searchbox-submit-button')

# Click pe butonul de cautare
driver.execute_script("arguments[0].click();", search_button)

time.sleep(2)

# Cautare buton "Adauga in Cos"
add_to_cart_button = driver.find_element(By.CLASS_NAME, 'yeahIWantThisProduct')

# Click "Adauga in Cos"
driver.execute_script("arguments[0].click();", add_to_cart_button)

time.sleep(2)

# Găsim butonul "X"
close_button = driver.find_element(By.CLASS_NAME, 'close')

# Click butonul "X"
driver.execute_script("arguments[0].click();", close_button)

time.sleep(2)

# Cautare link-ul de autentificare după ID
login_link = driver.find_element(By.ID, 'my_account')

# Click 'autentificare'
driver.execute_script("arguments[0].click();", login_link)

time.sleep(2)

driver.quit()
