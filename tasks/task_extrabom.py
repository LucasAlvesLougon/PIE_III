from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from loguru import logger


class TaskExtrabom():
    '''
    Classe responsável por realiar a task no mercado ExtraBom
    '''

    def __init__(self, driver: webdriver, lista_produtos: list[str]):

        # Log
        logger.success("Iniciando task no mercado Extrabom\n")

        # Driver
        self.driver = driver

        # Lista de produtos que serão iterados
        self.lista_produtos = lista_produtos

        # URL da página principal do mercado
        self.url = 'https://www.extrabom.com.br/'

        # XPATH
        self.xpath_campo_busca = "//input[@class='search-input']"
        self.xpath_btn_busca = "//input[contains(@class, 'input-submit-search')]"
        self.xpath_titulo_produto = "//div[@class='name-produto']"
        self.xpath_valor_produto = "//strong[@class='item-por__val']"
        self.url_produto = "//a[@class='carousel__box__dados']"


    def main(self):

        # Abre a página principal
        self.driver.get(self.url)

        for produto in self.lista_produtos:

            # Campo de busca
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_campo_busca))
            )[0].send_keys(produto)

            # Clica no elemento de indice 0 (primeiro elemento)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_btn_busca))
            )[0].click()

            # Titulo do produto
            titulo_produto = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_titulo_produto))
            )[0]
            titulo_produto = titulo_produto.text

            # Valor do produto
            valor_produto = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_valor_produto))
            )[0]
            valor_produto = valor_produto.text

            # Link do produto
            url_produto = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.url_produto))
            )[0]
            url_produto = url_produto.get_attribute("href")

            # Log
            logger.info(f"---- Dados do produto {produto} ----")
            logger.info(f'Titulo do produto: {titulo_produto}')
            logger.info(f'Valor do produto: {valor_produto}')
            logger.info(f'URL do produto: {url_produto}\n')
