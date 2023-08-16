# Importações
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Inicialização do webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Resto do seu código para interagir com o navegador
fle = r'C:\Users\migue\OneDrive\Documents\seleniumpyformulario.html'
print(fle)
driver.get(fle)

# Alert box
driver.find_element(By.XPATH, '/html/body/form/input[1]').click()
driver.switch_to.alert.accept()

# Check-box
driver.find_element(By.XPATH, '/html/body/form/input[3]').click()
driver.find_element(By.XPATH, '/html/body/form/input[2]').click()

# Verificação
ischeck1 = driver.find_element(By.XPATH, '/html/body/form/input[3]').is_selected()
ischeck2 = driver.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
print(ischeck1, ischeck2)

# Text box
driver.find_element(By.XPATH, '/html/body/form/input[16]').send_keys("Vasco")
vl = driver.find_element(By.XPATH, '/html/body/form/input[16]').get_attribute("value")
print(vl)

# Color
driver.find_element(By.XPATH, '/html/body/form/input[4]').send_keys("#E92121")
hex1 = driver.find_element(By.XPATH, '/html/body/form/input[4]').get_attribute("value")

driver.find_element(By.XPATH, '/html/body/form/input[5]').send_keys("#2143E8")
hex2 = driver.find_element(By.XPATH, '/html/body/form/input[5]').get_attribute("value")
print(hex1, hex2)

# Dates
driver.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('20/06/2004')
driver.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('20/06/2004', Keys.TAB, '04:05')
driver.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('Agosto', Keys.TAB, '2023')

# Send Files
value = driver.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(r'C:\Users\migue\Downloads\image.png')
value = driver.find_element(By.XPATH, '/html/body/form/input[8]').get_attribute("value")
print(value)

# Numeral
driver.find_element(By.XPATH, '/html/body/form/input[10]').send_keys('123456')

# Password
driver.find_element(By.XPATH, '/html/body/form/input[11]').send_keys('123456')

# Radio button
driver.find_element(By.XPATH, '/html/body/form/input[12]').click()
iselect1 = driver.find_element(By.XPATH, '/html/body/form/input[13]').is_selected()
iselect12 = driver.find_element(By.XPATH, '/html/body/form/input[14]').is_selected()
print(iselect1, iselect1)

# Hour
driver.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('15:15')

# week
driver.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('17', '2004')

# typing
driver.find_element(By.XPATH, '//*[@id="story"]').send_keys('A', Keys.ENTER,
 'B', Keys.ENTER, 'C', Keys.ENTER, 'D', Keys.ENTER, 'E'
)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="story"]').clear()

# Select
driver.find_element(By.TAG_NAME, 'select').send_keys('C')
time.sleep(1)
elmnt = driver.find_element(By.TAG_NAME, 'select')
element_select = Select(elmnt)
element_select.select_by_index(1)

# Slider
elemento = driver.find_element(By.XPATH, '/html/body/form/input[15]')
elemento.clear()
for i in range(70 - 50):
  elemento.send_keys(Keys.ARROW_RIGHT)

# Driver quit
input("Pressione ' para fechar o navegador...")
driver.quit()
