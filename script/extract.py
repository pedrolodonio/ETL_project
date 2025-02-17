# Bibliotecas
import requests
from bs4 import BeautifulSoup
import os

def extract_data(output_dir):
    
    # Fazendo requisição
    url = "https://en.wikipedia.org/wiki/COVID-19_pandemic"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

    # Extração dos dados
    tables = soup.find_all("table", {"class": "wikitable"})
    print(f"Numero de tabelas: {len(tables)}")

    # Salvar cada tabela para análise
    for i, table in enumerate(tables):
        file_path = os.path.join(output_dir, f"table{i}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(table))
            print(f"Tabela {i} salva em {file_path}")
