from selenium import webdriver   
from selenium.webdriver.chrome.service import Service    # Gerencia o serviço do Chrome no Windows
from webdriver_manager.chrome import ChromeDriverManager # O "gerente de infraestrutura"
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

print("Navegador aberto. Aguardando 3 segundos...")
time.sleep(3)

print("Acessando o site...")

navegador.get("https://g1.globo.com/")
time.sleep(5)
navegador.quit()

print("Teste finalizado com sucesso! 🏁")                                              # Controle de tempo (pausas)