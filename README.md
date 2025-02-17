# Projeto de Sistema ETL
Este projeto foi desenvolvido como parte do curso de Python da CodeMaster Academy, disponível na plataforma Udemy. O objetivo do projeto é a criação de um sistema ETL (Extração, Transformação e Carga), o qual automatiza a coleta de dados, realiza o processamento necessário e os armazena de forma estruturada para análise.

## Pré-requisitos

Para executar o projeto, você precisa ter os seguintes pré-requisitos:

- Python 3.13
- PostgreSQL

## Para Executar:

1.Clone este repositório

2.Crie um Ambiente virtual:

```
python -m venv venv
venv\Scripts\activate

```

3.Instale as dependências do projeto usando o comando:
```
pip install -r requirements.txt
```
4.Configure o PostgreSQL

-Crie um banco de dados no PostgreSQL.

-No arquivo config/db_config.py, você precisa fornecer as credenciais do banco de dados:
```
DB_CONFIG = {
    "host":"localhost",
    "port":5432,
    "database": "seu_db",
    "user": "seu_user",
    "password": "sua_senha"
}
```
5.Execute o main.py no terminal:
```
python script/main.py
```



