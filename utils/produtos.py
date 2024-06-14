import traceback
import os
from loguru import logger
from utils.manipula_planilha import ManipulaPlanilhas

def registra_produtos(dados_produto: list) -> None:
    """
    ----
    Método responsável por exibir os dados do produto a partir de um dict.

    ----
    Args:
        dados_produto (dict): Um dict contendo o nome do produto, seu titulo, seu valor, seu 
        link e o nome do mercado correspondente. 
        Ex:
            dados_produto = {
                'nome': 'Nome do produto passado como parâmetro'
                'titulo': 'Titulo do produto exibido pelo site',
                'valor': 15.5,
                'link': 'https://www.teste.com.br',
                'mercado': 'Nome do mercado'
            }

    ----
    Returns:
        None
    """
    DIRETORIO_PLANILHA = r'C:\Projetos Pessoais\web-scraping-mercado\assets\planilhas'
    PLANILHA_1 = os.path.join(DIRETORIO_PLANILHA, '1.xlsx')


    for dados in dados_produto:
        try:
                
            logger.success(f'---- Dados do produto "{dados["nome"]}" - {dados["mercado"]} ----')
            logger.info(f'Titulo do produto: {dados["titulo"]}')
            logger.info(f'Valor do produto: {dados["valor"]}')
            logger.info(f'Link do produto: {dados["link"]}\n')

            manipula_planilhas = ManipulaPlanilhas(arquivo_xlsx=PLANILHA_1)

            manipula_planilhas.preenche_planilha(
                planilha='Principal',
                dados=dados
            )
        
        except KeyError as error:
            logger.error(f'Erro ao exibir produto | Chave {str(error)} não encontrada no dicionário | Dicionário: {dados}')
        
        except Exception as error:
            logger.info(f'Erro ao exibir produto | {str(error)}')

if __name__=='__main__':
    registra_produtos(dados_produto={
        'a':12
    })