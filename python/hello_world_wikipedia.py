# Instalar Selenium con pip (pip install selenium) e importar webdriver desde selenium
from selenium import webdriver

# Importar esta libreria para utilizar las teclas especiales (enter, shift, ctrl)
from selenium.webdriver.common.keys import Keys

# Ruta del webdriver del explorador deseado (en este caso Edge esta en la misma carpeta)
driver = webdriver.Chrome(r'chromedriver.exe')

# Enlace a la pagina que voy a utilizar
driver.get('https://www.google.com')

# Crea una variable y le asigna el elemento con el cual va a interactuar
searchbar = driver.find_element_by_class_name('gLFyf.gsfi')

# Envia texto al elemento que esta interactuando
searchbar.send_keys('hola mundo Selenium')

# Aprieta la tecla enter
searchbar.send_keys(Keys.ENTER)

# Busca otro elemento por su XPath
next_page = driver.find_element_by_xpath('//*[@id="pnnext"]')

# Hace click en el elemento que se definio por el XPath
next_page.click()

# Hace click en el emeneto cuyo enlace tiene un texto como el ingresado
driver.find_element_by_partial_link_text('Robot Framework - Wikipedia, la enciclopedia libre').click()
