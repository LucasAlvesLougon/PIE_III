from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.tasks.task_extrabom import TaskExtrabom
from src.tasks.task_perim import TaskPerim

def main():

    # Optios do Driver 
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    # options.add_argument('--headless')


    # Instância do Driver
    driver = webdriver.Chrome(options=options)


    # Lista de produtos que serão iterados
    lista_produtos = [
        'Arroz',
        'Feijão',
        'Orégano',
        'Leite'
    ]


    # Task do mercado Extrabom
    task_extrabom = TaskExtrabom(
        driver=driver,
        lista_produtos=lista_produtos
    )
    task_extrabom.main()


    # Task do mercado Perim
    task_perim = TaskPerim(
        driver=driver,
        lista_produtos=lista_produtos
    )
    task_perim.main()


if __name__ == '__main__':
    main()
    