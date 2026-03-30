import kagglehub
import os
import shutil

def download_dataset():
    print("Baixando dataset do Kaggle...")

    path = kagglehub.dataset_download(
        "nicolaswattiez/skillbuilder-data-2009-2010"
    )

    print("Dataset baixado em:", path)

    # cria pasta raw se não existir
    os.makedirs("dataset/raw", exist_ok=True)

    # move arquivos para dataset/raw
    for file in os.listdir(path):
        origem = os.path.join(path, file)
        destino = os.path.join("dataset/raw", file)

        if not os.path.exists(destino):
            shutil.move(origem, destino)

    print("Arquivos movidos para dataset/raw")

if __name__ == "__main__":
    download_dataset()