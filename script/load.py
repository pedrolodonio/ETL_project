# Bibliotecas
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.db_config import DB_CONFIG
import pandas as pd
import psycopg2

# Carregar ifrs.csv
def load_ifrs(csv_path):
    # Estabelecer conexão com o postgres
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    
    # Criação da tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ifrs
    (
    age_group TEXT,
    IFR TEXT
    );
    """
    # Executa função para criar tabela
    cursor.execute(create_table_query)
    connection.commit()

    # Leitura do CSV
    dataframe = pd.read_csv(csv_path)

    # Inserção dos dados
    for _, row in dataframe.iterrows():
        cursor.execute("INSERT INTO ifrs (age_group, IFR) VALUES (%s, %s)", (row["Age group"], row["IFR"]))
    
    # Encerrando conexão com o db
    connection.commit()
    cursor.close()
    connection.close()

    print("Dados IFR carregados com sucesso!")

# Carregar variants.csv
def load_variants(csv_path):
    # Estabelecer conexão com o postgres
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    
    # Criação da tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS variants
    (
    Name TEXT,
    Lineage TEXT,
    Detected TEXT,
    Countries INT,
    Priority TEXT
    );
    """
    # Executa função para criar tabela
    cursor.execute(create_table_query)
    connection.commit()

    # Leitura do CSV
    dataframe = pd.read_csv(csv_path)

    # Inserção dos dados
    for _, row in dataframe.iterrows():
        cursor.execute(
            "INSERT INTO variants (Name, Lineage, Detected, Countries, Priority) VALUES (%s, %s, %s, %s, %s)",
            (row["Name"], row["Lineage"], row["Detected"], int(row["Countries"]), row["Priority"])
        )
    
    # Encerrando conexão com o db
    connection.commit()
    cursor.close()
    connection.close()

    print("Dados Variants carregados com sucesso!")