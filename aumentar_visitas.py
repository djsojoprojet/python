# Crear un bot para aumentar las visitas de YouTube con Python

#librerías (se requiere instalar selenium / descargar webdriver)
import time;
from selenium import webdriver;

#Tiempo para refrescas la página
Timer = 5

#Enlace (Blog, YouTube)
enlace = https://www.youtube.com/watch?v=AKPVznR4kmU

#Número visitas
views = 100.000

#driver
driver = webdriver.Chrome("C:/gisbook/chromedriver.exe")
driver.get(enlace)

for i in range(views):4000
    time.sleep(Timer)5 min
    driver.refresh()5 min
    print(i)
