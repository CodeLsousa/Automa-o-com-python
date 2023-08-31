import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# URL do site com os dados a serem copiados
source_url = "https://www.bling.com.br/produtos.php#edit/16115514770"
css_selector = "codigoVariacao"

# URLs dos outros dois sites onde os dados serão colados
target_url1 = "https://www.mercadolivre.com.br/anuncios/MLB3907138550/modificar/1289489126-update-20876c97c954/detail"
target_url2 = "https://sso.geiwohuo.com/#/spmp/commoditiesInfo/edit/z23081814874"

# Inicializar o driver do Selenium (certifique-se de ter o ChromeDriver instalado)
service = Service("C:\Program Files\Google\Chrome\Application")
driver = webdriver.Chrome(service=service)

try:
    # Fazer a solicitação HTTP para o site de origem
    response = requests.get(source_url)
    response.raise_for_status()

    # Analisar o HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    data_to_copy = soup.select_one(css_selector).text

    # Abrir os sites de destino usando o Selenium
    driver.get(target_url1)
    element1 = driver.find_element_by_css_selector ("SELLER_SKU")
    element1.send_keys(data_to_copy)

    driver.get(target_url2)
    element2 = driver.find_element_by_css_selector("id38")
    element2.send_keys(data_to_copy)

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Fechar o driver do Selenium
    driver.quit()