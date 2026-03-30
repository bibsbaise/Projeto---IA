import pandas as pd

def create_sample():
    file_path = "dataset/raw/2012-2013-data-with-predictions-4-final.csv"

    print("Carregando dataset...")

    chunks = pd.read_csv(file_path, chunksize=100000) #lê em pedaços para não estourar RAM

    sample_list = []

    for chunk in chunks:
        sample = chunk.sample(frac=0.01) #pega 1% de cada pedaço
        sample_list.append(sample)

    df_sample = pd.concat(sample_list)

    print("Criando amostra...")

    df_sample.to_csv("dataset/sample.csv", index=False)

    print("Amostra criada em dataset/sample.csv")

if __name__ == "__main__":
    create_sample()