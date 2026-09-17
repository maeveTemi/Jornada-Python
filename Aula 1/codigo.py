# Import Libraries

import pyautogui
import time
import pandas
pyautogui.PAUSE = 0.5

# First Step: Access company's website

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Open Browser

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#Bigger pause to let page to load

time.sleep(3)

# Second Step: Login

# Click on the email field

pyautogui.click(x=846, y=366)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha muito dificil")
pyautogui.press("tab")
pyautogui.press("enter")

# Third Step: Open Database

time.sleep(3)
table = pandas.read_csv("produtos.csv")

# Fifth Step: Repeat step 4 until all products are registered

for row in table.index:

    # Fourth Step: Register first product

    pyautogui.click(x=710, y=252)

    # codigo
    codigo = str(table.loc[row, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = str(table.loc[row, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = str(table.loc[row, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = str(table.loc[row, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = str(table.loc[row, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # custo
    custo = str(table.loc[row, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # obs
    obs = str(table.loc[row, "obs"])    
    pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    # Scroll back to the top

    pyautogui.scroll(5000)