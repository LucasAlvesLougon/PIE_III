from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from loguru import logger


class SitePerim():
    """
    ----
    Classe responsável iteragir no site do mercado Perim

    ----
    Args:
        driver (webdriver.Chrome): Driver que será utilizado
    """

    def __init__(self, driver: webdriver.Chrome):
        
        logger.success("Iniciando iteração no site do mercado Perim")

        self.driver : webdriver.Chrome = driver
        self.pagina_inicial = 'https://www.perim.com.br/'
        self.nome_mercado = 'Perim'

    def abre_tela_inicial(self):
        """
        ----
        Método público responsável por abrir a tela inicial do site do mercado.

        ----
        Args:
            None

        ----
        Returns:
            None
        """
        self.driver.get(self.pagina_inicial)

    def buscar_produto(self, produto: str) -> dict:
        """
        ----
        Método privato responsável por pesquisar pelo produto no site e retornar nome um dicionário
        contendo o nome do mercado, o nome do produto passado como parâmetro, o titulo do produto exibido, valor do 
        produto e o link do produto.

        ----
        Args:
            produto (str): Nome do produto desejado

        ----
        Returns:
            dict: {
                'nome': 'Nome do produto passado como parâmetro'
                'titulo': 'Titulo do produto exibido pelo site',
                'valor': 15.5,
                'link': 'https://www.teste.com.br',
                'mercado': 'Nome do mercado'
            }
        """

        try:

            campo_busca = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='inputBuscaRapida']"))
            )
            campo_busca.clear()
            campo_busca.send_keys(produto)

            btn_pesquisa = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-search']"))
            )
            btn_pesquisa.click()

            titulo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-success description')]"))
            ).text

            valor = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'info-price ng-star-inserted')]"))
            ).text

            link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='ghost-link clearfix']"))
            ).get_attribute("href")

            dados_retorno = {
                'nome': produto,
                'titulo': titulo,
                'valor': valor,
                'mercado': self.nome_mercado,
                'link': link
            }

            return dados_retorno

        except Exception as error:
            raise Exception(f"Erro ao buscar produto | {str(error)}")
