# Problema: é preciso cadastrar uma grande quantidade
# de produtos no site de uma empresa.
# Passo 1: entrar no site da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: fazer login no site
# Passo 3: importar a base de dados
# Passo 4: cadastrar um produto
# Passo 5: repetir o passo 4 até cadastrar todos os produtos'''
import pandas
import time
import pyautogui as pa
# essa biblioteca automatiza o mouse, teclado, etc
# pa.click - clicar
# pa.write - escrever
# pa.press - aperta 1 tecla
# pa.hotkey - combinação de teclas
# pa.scroll - scrollar a tela
pa.PAUSE = 0.5  # delay entre cada comando
# Passo 1
# Abrir navegador
pa.press("win")
pa.write("chrome")
pa.press("enter")
# Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login

pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(2)
# Passo 2
pa.press("tab")
pa.write("pythonimpressionador@gmail.com")
pa.press("tab")
pa.write("12345678")
pa.press("tab")
pa.press("enter")
time.sleep(2)

# Passo 3
table = pandas.read_csv("produtos.csv")

# Passo 4
for linha in table.index:
    # código
    pa.click(x=866, y=327)
    pa.press("enter")
    codigo = str(table.loc[linha, "codigo"])
    pa.write(codigo)
# marca
    pa.press("tab")
    marca = str(table.loc[linha, "marca"])
    pa.write(marca)

# tipo
    pa.press("tab")
    tipo = str(table.loc[linha, "tipo"])
    pa.write(tipo)
# categoria
    pa.press("tab")
    categoria = str(table.loc[linha, "categoria"])
    pa.write(categoria)
# preco_unitario
    pa.press("tab")
    preco_unitario = str(table.loc[linha, "preco_unitario"])
    pa.write(preco_unitario)
# custo
    pa.press("tab")
    custo = str(table.loc[linha, "custo"])
    pa.write(custo)
# obs
    pa.press("tab")
    obs = str(table.loc[linha, "obs"])
    if obs != "nan":
        pa.write(obs)
# enviar
    pa.press("tab")
    pa.press("enter")
    pa.scroll(5000)
