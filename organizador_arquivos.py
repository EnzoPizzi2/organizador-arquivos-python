import os
import shutil

# pasta que será organizada
pasta_origem = "arquivos"

# regras de organização
pastas_destino = {
    "pdf": "PDFs",
    "jpg": "Imagens",
    "png": "Imagens",
    "docx": "Documentos",
    "txt": "Textos"
}

# cria as pastas caso não existam
for pasta in set(pastas_destino.values()):
    caminho = os.path.join(pasta_origem, pasta)
    os.makedirs(caminho, exist_ok=True)

# percorre os arquivos
for arquivo in os.listdir(pasta_origem):

    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):

        extensao = arquivo.split(".")[-1].lower()

        if extensao in pastas_destino:

            pasta_destino = pastas_destino[extensao]

            destino = os.path.join(pasta_origem, pasta_destino, arquivo)

            shutil.move(caminho_arquivo, destino)

            print(f"{arquivo} movido para {pasta_destino}")