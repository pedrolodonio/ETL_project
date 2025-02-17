# Projeto de Sistema ETL
Este projeto foi desenvolvido como parte do curso de Python da CodeMaster Academy, disponível na plataforma Udemy. O objetivo do projeto é a criação de um sistema ETL (Extração, Transformação e Carga), o qual automatiza a coleta de dados, realiza o processamento necessário e os armazena de forma estruturada para análise.

## Tabela de Conteúdos

- [Pré-requisitos](#pré-requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Executar](#Para-Executar)

## Pré-requisitos

Para executar o projeto, você precisa ter os seguintes pré-requisitos:

- Python 3.13
- PostgreSQL

#Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

webscraping_etl_project/
│
├── data/
│   ├── raw/                # Dados brutos coletados via scraping
│   ├── processed/          # Dados processados antes de serem carregados no banco de dados
│
├── script/                 
│   ├── extract.py          # Script responsável pelo scraping dos dados
│   ├── transform.py        # Script responsável pela transformação dos dados
│   ├── load.py             # Script responsável por carregar os dados no PostgreSQL
│   ├── main.py             # Script principal que orquestra o processo ETL
│
├── config/
│   ├── db_config.py        # Configurações do banco de dados (credenciais)
│
├── requirements.txt        # Arquivo com todas as dependências do projeto
├── README.md               # Este arquivo

#Para Executar:

1.Clone este repositório
2.Instale as dependências do projeto usando o comando:
```
pip install -r requirements.txt
```
3.Configure o PostgreSQL
-Crie um banco de dados no PostgreSQL.
-No arquivo config/db_config.py, você precisa fornecer as credenciais do banco de dados:
´´´
DB_CONFIG = {
    "host":"localhost",
    "port":5432,
    "database": "seu_db",
    "user": "seu_user",
    "password": "sua_senha"
}
´´´
4.Execute o main.py no terminal:
´´´
python script/main.py
´´´



