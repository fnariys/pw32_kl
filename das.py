import urllib.request
import subprocess
import shutil
import os

url_arquivo_inicializacao = "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe"

def baixar_arquivo(url, nome_arquivo):
    urllib.request.urlretrieve(url, nome_arquivo)

baixar_arquivo(url_arquivo_inicializacao, "arquivo_inicializacao.exe")

diretorio_inicializacao = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
shutil.copy("arquivo_inicializacao.exe", diretorio_inicializacao)

subprocess.run(["arquivo_inicializacao.exe"])
