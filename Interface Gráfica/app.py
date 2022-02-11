# Importa todos os módulos do CcProfile e do tkinter OBS.: o tkinter escrito em caixa baixa é para a versão 3 do Python. Tkinter com T maiúsculo é para a versão
# 2.7 do Python

from cProfile import label
from tkinter import * 

# Widget raiz, chamando Tk(). Ele cria automaticamente uma janela gráfica com a barra de título, botões minimizar, maximizar e fechar.
app = Tk()
# nomeia a janela principal como Hello World.
app.title('Hello World')
# Cria um widget Label filho da janela raiz. O pai de nosso widget de rótulo que definimos como “Hello, World!”
a = Label(app, text='Se inscreva no canal! :D ')
# O pack() chama uma widget que dimensiona todo o texto dentro da janela que será criada.
a.pack()
# O Loop Principal pega todos os modulos que criamos e exibe na tela. Fica em execução até que seja fechado pelo usuário. 
app.mainloop()
