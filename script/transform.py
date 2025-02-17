# Importação de bibliotecas
import pandas as pd
from bs4 import BeautifulSoup
import os
import sys

# Tratamento de Tabelas

def transform_table_0(input_path, output_path):
    # Essa função transformará a tabela do IFR (fatalidade por faixa etária)
    with open(input_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        table = soup.find("table")
        dataframe = pd.read_html(str(table))[0]
    
    dataframe.columns = ["Age group", "IFR"]
    dataframe.to_csv(output_path, index=False)

    print(f"Tabela IFR transformada e salva em {output_path}")

def transform_table_1(input_path, output_path):
    # Essa função transformará a tabela variants of concern
    with open(input_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        table = soup.find("table")
        dataframe = pd.read_html(str(table))[0]
    
    dataframe.columns = ["Name", "Lineage", "Detected", "Countries", "Priority"]
    dataframe.to_csv(output_path, index=False)

    print(f"Tabela Variants of Concern transformada e salva em {output_path}")
