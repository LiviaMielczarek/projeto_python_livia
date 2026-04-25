from selenium import webdriver   
from selenium.webdriver.chrome.service import Service    # Gerencia o serviço do Chrome no Windows
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

print("Navegador aberto. Aguardando 3 segundos...")
time.sleep(3)
navegador.implicitly_wait(5)
print("Acessando o site...")
navegador.get("https://g1.globo.com/")
time.sleep(10)

print("Buscando Reportagem no G1.com")

# Reportagem = navegador.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div[2]/div[1]/h1")
endereco = "/html/body/div[2]/main/div[3]/div[2]/div[1]/h1"
reportagem = navegador.find_element(By.XPATH,endereco)
texto_reportagem = reportagem.text

print(f"Reportagem: {texto_reportagem}")