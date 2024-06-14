import os
import pandas as pd
from loguru import logger

class ManipulaPlanilhas:
    
    def __init__(self, arquivo_xlsx: str)-> None:
        """
        Inicializa a instância da classe ManipulaPlanilha.

        Args:
            arquivo_xlsx (str): O caminho do arquivo XLSX a ser manipulado.
        """
        self.arquivo_xlsx = arquivo_xlsx


    def preenche_planilha(self, planilha: str , dados: dict) -> None:
        """
        Adiciona dados a uma planilha e aplica estilos às células.

        Args:
            planilha (str): O nome da planilha onde os dados serão adicionados.
            dados (dict): Um dicionário contendo os dados a serem adicionados à planilha.
                Exemplo:
                {
                    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
                    'Idade': [25, 30, 22, 28],
                    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre'],
                    'Salário': [50000, 60000, 45000, 55000]
                }
        """

        df = pd.DataFrame([dados])

        # Nome do arquivo Excel de saída
        nome_arquivo = self.arquivo_xlsx

        # Escrever o DataFrame no arquivo Excel
        df.to_excel(nome_arquivo, index=False)

        print(f'Dados salvos em {nome_arquivo} com sucesso!')

    def obter_index_coluna(self, planilha: str, nome_coluna: str) -> int:
        """
        Obtém o índice da coluna pelo seu nome.

        Args:
            planilha (str): O nome da planilha onde a coluna está localizada.
            nome_coluna (str): O nome da coluna.

        Returns:
            int: O índice da coluna.
        """

        # Define a planilha
        ws = self.wb[planilha]

        # Itera sobre as colunas presentes na planilha
        for coluna in ws.iter_cols(min_col=1, max_col=ws.max_column, min_row=1, max_row=1):

            # Itera sobe a celula da coluna atual
            for celula in coluna:

                # Verifica se o valor da celula é igual ao nome da coluna busca
                if celula.value == nome_coluna:

                    # Retorna o indice da coluna
                    return celula.column
        return None


if __name__ == '__main__':

    # ---- CAMINHOS ----
    DIRETORIO_PLANILHA = r'C:\Projetos Pessoais\web-scraping-mercado\assets\planilhas'
    PLANILHA_1 = os.path.join(DIRETORIO_PLANILHA, 're.xlsx')

    # ---- DADOS DE ENTRADA ----
    dados = {'nome': 'Arroz', 'titulo': 'Arroz Arbório Granjeiro 1kg', 'valor': 'R$ 16,98 un.', 'mercado': 'Perim', 'link': 'https://www.perim.com.br/produtos/detalhe/8331/arroz-arborio-granjeiro-1kg'}

    manipula_planilhas = ManipulaPlanilhas(arquivo_xlsx=PLANILHA_1)

    manipula_planilhas.preenche_planilha(
        planilha='Principal',
        dados=dados
    )

    i = manipula_planilhas.obter_index_coluna(
        ws = 'Principal',
        nome_coluna='Nome'
    )

    logger.info(i)
 
    manipula_planilhas.preenche_coluna(
        planilha='Principal',
        coluna_referencia='Nome',
        coluna_destino='Retorno',
        dados={
            'João' : 'Sucesso',
            'Maria' : 'Erro',
            'Carlos': 'Erro',
            'Ana' : 'Sucesso' 
        }
    )
