from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from loguru import logger


class SiteExtrabom():
    """
    ----
    Classe responsável iteragir no site do mercado ExtraBom

    ----
    Args:
        driver (webdriver.Chrome): Driver que será utilizado
    """

    def __init__(self, driver: webdriver.Chrome) -> None:

        logger.success("Iniciando iteração no site do mercado ExtraBom")

        self.driver : webdriver.Chrome = driver
        self.pagina_inicial = 'https://www.extrabom.com.br/'
        self.nome_mercado = 'ExtraBom'

    def abre_tela_inicial(self) -> None:
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
        try:
            self.driver.get(self.pagina_inicial)
            btn_fechar_anuncio = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'lightbox-load-content')]//a[contains(@class, 'button')]"))
            )
            btn_fechar_anuncio.click()
            logger.info('Anúncio fechado!')
        
        except TimeoutException:
            pass
        
        except Exception as error:
            raise Exception(f'Erro ao verificar anúncio | {str(error)}')
            

            
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
                'valor': 15.5
                'link': 'https://www.teste.com.br'
            }
        """
        try:
            
            campo_busca = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@class='search-input']"))
            )
            campo_busca.send_keys(produto)

            btn_pesquisa = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='header']//input[contains(@class, 'icon-search')]"))
            )
            btn_pesquisa.click()

            titulo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='name-produto']"))
            ).text

            valor = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//strong[@class='item-por__val']"))
            ).text

            link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@class='carousel__box__dados']"))
            ).get_attribute("href")

            dados_retorno = {
                'mercado': self.nome_mercado,
                'nome': produto,
                'titulo': titulo,
                'valor': valor,
                'link': link
            }

            return dados_retorno

        except Exception as error:
            raise Exception(f"Erro ao buscar produto | {str(error)}")
