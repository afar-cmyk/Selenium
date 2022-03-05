import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta de el webdriver del explorador Chrome
exe_file = Service('chromedriver.exe')
driver = webdriver.Chrome(service=exe_file)

# Pagina en donde se hará la prueba
driver.get('https://signup.lan.leagueoflegends.com/es/signup/index#/')

# Lista de datos
cuentas = [{'nombre':'WCFhtE145dc', 'contraseña' : '`]A9"?caG}'},
          {'nombre':'z4hRqAUidc0', 'contraseña' : '35,_BfTe.'},
          {'nombre':'XvlqrBe9z7e', 'contraseña' : 'rhW!df[5k'},
          {'nombre':'uXKeWfcm9Ur', 'contraseña' : "x!4{$Gab0"},
          {'nombre':'uXKeWfCC9Ur', 'contraseña' : "M5WTb,vVM"},
          {'nombre':'q60QR7OJLzo', 'contraseña' : ",GRW,h5M}"}]

# Envoltura para el botón siguiente
def boton_siguiente():
  return (WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.next-button'))).click())

# Envoltura para el tiempo de espera
def tiempo_espera(i):
  return (time.sleep(i))

# Espera un segundo antes de comenzar, para evitar estancarse por la carga del sitio
tiempo_espera(1)

# Envia el email
input_email = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(cuentas[5]["nombre"]+'@gmail.com')

# Aprieta el botón siguiente
boton_siguiente() 

# Selecciona los datos de nacimiento (Dia 6, Mes 6, Año 1966)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[2]/select/option[7]'))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[3]/select/option[7]'))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/form/div[1]/div[4]/select/option[58]'))).click()

# Aprieta el botón siguiente
boton_siguiente()

# Espera un segundo antes de continuar, para evitar estancarse por la carga del sitio
tiempo_espera(1)

# Ingresa los datos de la cuenta
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(cuentas[5]["nombre"])
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(cuentas[5]["contraseña"])
driver.find_element(By.CSS_SELECTOR, 'input[name="confirm_password"]').send_keys(cuentas[5]["contraseña"])

# Hace scroll vertical para ubicar los elementos inferiores
driver.execute_script("window.scrollTo(0, 450)") 

# Aprieta el checkbox de terminos y condiciones
checkbox1 = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/label[1]/div[1]").click()

# Acepta la creación de cuentas
boton_siguiente()
print('Debe confirmar el captcha de forma manual en menos de 1 minuto...')

# Conteo regresivo por consola para comprobar el estado de la cuenta registrada
contador = 40
while contador > 0 :
  print(f'Confirmando el captcha de forma manual: {contador}s restantes')
  contador = contador - 1
  tiempo_espera(1)
print('Confirmación de captcha terminado.')

# Manejo de errores y fin del programa
try:
  cuenta_creada = bool(driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/header/div/h1'))
  print('\n---> Cuenta creada con exito! <---')
except:
  cuenta_existente = bool(driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/header/h1'))
  print('\n---> ¡Error!, esta cuenta cuenta ya existe. <---')
finally:
  print('\nFin del programa, saliendo en 3 segundos.')
  tiempo_espera(3)
  driver.quit()
