#Bibliotecas
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from script.extract import extract_data
from script.transform import transform_table_0,transform_table_1
from script.load import load_ifrs,load_variants

def main ():
    #diretórios entrada e saída
    # Obtém o diretório raiz do projeto subindo dois níveis a partir do script
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    print(f"Diretório raiz do projeto: {project_root}")

    # Caminhos baseados no diretório do projeto
    raw_data_dir = os.path.join(project_root, "data", "raw")
    processed_data_dir = os.path.join(project_root, "data", "processed")

    # Cria os diretórios se não existirem (garante que 'data/raw' e 'data/processed' estejam no nível correto)
    os.makedirs(raw_data_dir, exist_ok=True)
    os.makedirs(processed_data_dir, exist_ok=True)

    if not os.path.exists(raw_data_dir) or not os.path.exists(processed_data_dir):
        print("❌ ERRO: As pastas 'data/raw' e 'data/processed' não existem. Execute o script de extração antes.")
        sys.exit(1)  # Interrompe a execução
    
    #Extração
    print("Iniciando extração de dados...")
    extract_data(raw_data_dir)
    print("Extração Concluída\n")

    #Transformação
    print("Iniciando transformação...")
    transform_table_0(
        input_path=os.path.join(raw_data_dir, "table0.html"),
        output_path=os.path.join(processed_data_dir, "ifrs.csv"),
    )

    transform_table_1(
        input_path=os.path.join(raw_data_dir, "table1.html"),
        output_path=os.path.join(processed_data_dir, "variants.csv"),
    )
    print("Transformação concluída\n")

    #Carregamento
    print("Iniciando Carregamento...")
    load_ifrs(csv_path=os.path.join(processed_data_dir, "ifrs.csv"))
    load_variants(csv_path=os.path.join(processed_data_dir, "variants.csv"))
    print("Carregamento concluido")

    print("Pipeline ETL concluído com sucesso !!")

if __name__ == '__main__':
    main()


    