import traceback
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.site_extrabom import SiteExtrabom
from src.site_perim import SitePerim
from utils.produtos import registra_produtos
from loguru import logger

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def __exibir_dados_produto(dados_produto: dict) -> None:
        """
        ----
        Método privato responsável por exibir os dados do produto.

        ----
        Args:
            dict: {
                'titulo': 'Titulo do produto exibido pelo site',
                'valor': 15.5
                'link': 'https://www.teste.com.br'
            }

        ----
        Returns:
            None
        """
        logger.success(f'---- Dados do produto {dados_produto["titulo"]} ----')
        logger.info(f'Titulo do produto: {dados_produto["titulo"]}')
        logger.info(f'Valor do produto: {dados_produto["valor"]}')
        logger.info(f'Link do produto: {dados_produto["link"]}\n')

def exibe_produtos_perim(driver: webdriver.Chrome, lista_produtos: list) -> list:

    site_perim = SitePerim(
        driver=driver
    )

    site_perim.abre_tela_inicial()

    produtos_encontrados = []
    for produto in lista_produtos:

        try:
            produto_perim = site_perim.buscar_produto(
                produto=produto
            )
            produtos_encontrados.append(produto_perim)

        except Exception as error:
            logger.error(traceback.format_exc())

    return produtos_encontrados

def exibe_produtos_extrabom(driver: webdriver.Chrome, lista_produtos: list) -> list:

    site_extrabom = SiteExtrabom(
        driver=driver
    )

    site_extrabom.abre_tela_inicial()

    produtos_encontrados = []
    for produto in lista_produtos:

        try:
            produto_extrabom = site_extrabom.buscar_produto(
                produto=produto
            )
            produtos_encontrados.append(produto_extrabom)
        
        except Exception as error:
            logger.error(traceback.format_exc())

    return produtos_encontrados

def main():

    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(width=1920,height=1080)

    produtos_encontrados = []
    lista_produtos = [
        'Arroz',
        'Feijão',
        'Orégano',
        'Leite'
    ]

    produtos_perim = exibe_produtos_perim(
        driver=driver,
        lista_produtos=lista_produtos
    )
    produtos_encontrados.append(produtos_perim)

    produtos_extrabom = exibe_produtos_extrabom(
        driver=driver,
        lista_produtos=lista_produtos
    )
    produtos_encontrados.append(produtos_extrabom)

    for produto in produtos_encontrados:
        registra_produtos(
            dados_produto=produto
        )


if __name__ == '__main__':
    main()
    