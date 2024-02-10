import traceback
from loguru import logger

def exibir_produto(dados_produto: dict) -> None:
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
    try:
            
        logger.success(f'---- Dados do produto "{dados_produto["nome"]}" - {dados_produto["mercado"]} ----')
        logger.info(f'Titulo do produto: {dados_produto["titulo"]}')
        logger.info(f'Valor do produto: {dados_produto["valor"]}')
        logger.info(f'Link do produto: {dados_produto["link"]}\n')
    
    except KeyError as error:
        logger.error(f'Erro ao exibir produto | Chave {str(error)} não encontrada no dicionário | Dicionário: {dados_produto}')
    
    except Exception as error:
        logger.info(f'Erro ao exibir produto | {str(error)}')

if __name__=='__main__':
    exibir_produto(dados_produto={
        'a':12
    })