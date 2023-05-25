import tkinter as tk
from tkinter import filedialog
import shutil
import os
from PIL import Image, ImageTk, ImageDraw
import json
import time





def carregar_informacoes(arquivo):
    # Abrir o arquivo no modo de leitura
    with open(arquivo, "r") as f:
        # Carregar o json do arquivo em um dicionário
        pedido = json.load(f)
        
    return pedido

def salvar_log(nome, itemid):
    itemid +=1
    # Criar um dicionário com as informações
    informacoes = {
        "nome": nome,
        "id": itemid
        
    }
    # Abrir o arquivo no modo de escrita
    with open('python\\trabalho ivo\\log', "w") as f:
        # Salvar o dicionário no arquivo como json
        json.dump(informacoes, f)



controlVar = carregar_informacoes('python\\trabalho ivo\\log')
itemid = controlVar['id']


def salvar_informacoes(nome, preco, descricao, arquivo):
    itemid = controlVar['id']
    salvar_log('ok',itemid)
    # Criar um dicionário com as informações
    informacoes = {
        "nome": nome,
        "preco": preco,
        "descricao": descricao,
        "id": itemid
        
    }
    # Abrir o arquivo no modo de escrita
    with open(arquivo, "w") as f:
        # Salvar o dicionário no arquivo como json
        json.dump(informacoes, f)





# Definição da cor do submenu
cor_submenu = '#d9d9d9'  # Cinza

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title("Interface com Submenu")
janela_principal.geometry('800x600')
janela_principal.configure(bg='white')

# Criar o Frame do submenu
frame_submenu = tk.Frame(janela_principal, bg=cor_submenu, width=200)
frame_submenu.pack(side='left', fill='y')

class EntradaTexto:
    def __init__(self, frame, tamanho_img, tamanho_caixa, pos, img_local):
        self.frame = frame
        self.tamanho_img = tamanho_img
        self.tamanho_caixa = tamanho_caixa
        self.pos = pos
        self.img_local = img_local

        # Carregar a imagem da caixa de entrada
        img = Image.open(self.img_local)
        img = img.resize((self.tamanho_img), Image.ANTIALIAS)
        self.img_tk = ImageTk.PhotoImage(img)

        # Criar a imagem de fundo
        self.bg = tk.Label(self.frame, image=self.img_tk, borderwidth=0)
        self.bg.image = self.img_tk
        self.bg.place(x=self.pos[0], y=self.pos[1])

        # Posicionamento da caixa de entrada no centro da imagem
        pos_x_caixa = self.pos[0] + (self.tamanho_img[0] - self.tamanho_caixa[0]) // 2
        pos_y_caixa = self.pos[1] + (self.tamanho_img[1] - self.tamanho_caixa[1]) // 2

        # Criar a caixa de entrada de texto sobre a imagem
        self.entrada = tk.Entry(self.frame, bg='white', fg='black', bd=-1, highlightthickness=0)
        self.entrada.place(x=pos_x_caixa, y=pos_y_caixa, width=self.tamanho_caixa[0], height=self.tamanho_caixa[1])

    # Método para obter a entrada de texto atual
    def get_text(self):
        return self.entrada.get()

Limgentry = 180
Aimgentry = 35
posVentry = 260
posHentry = 8
espaco = 60


# A seguir é como você poderia usar essa classe para adicionar uma caixa de entrada de texto ao frame_submenu
entradaNome = EntradaTexto(frame_submenu, (Limgentry,Aimgentry), (Limgentry-10, Aimgentry-10), (posHentry, posVentry), 'python\\trabalho ivo\\layout\\imgentrada.png')
entradaPreco = EntradaTexto(frame_submenu, (Limgentry,Aimgentry), (Limgentry-10, Aimgentry-10), (posHentry, posVentry + espaco), 'python\\trabalho ivo\\layout\\imgentrada.png')
entrada1 = EntradaTexto(frame_submenu, (Limgentry,Aimgentry), (Limgentry-10, Aimgentry-10), (posHentry, posVentry + (espaco*2)), 'python\\trabalho ivo\\layout\\imgentrada.png')



class Botao:
    def __init__(self, frame, tamanho, img_local, pos, funcao):
        self.frame = frame
        self.tamanho = tamanho
        self.img_local = img_local
        self.pos = pos
        self.funcao = funcao

        # Carregar a imagem do botão
        img = Image.open(self.img_local)
        img = img.resize((self.tamanho), Image.ANTIALIAS)
        self.img_tk = ImageTk.PhotoImage(img)

        # Criar o botão
        self.botao = tk.Label(self.frame, image=self.img_tk, bd=0, highlightthickness=0)

        self.botao.image = self.img_tk  # referência para impedir GC
        self.botao.place(x=self.pos[0], y=self.pos[1])
        self.botao.bind("<Button-1>", self.funcao)

def selecionar_e_salvar_imagem(local_destino, nome_arquivo):
    # Cria uma nova janela e esconde a janela principal
    root = tk.Tk()
    root.withdraw()

    # Abre o seletor de arquivos
    caminho_imagem = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif')])

    # Verifica se um arquivo foi selecionado
    if caminho_imagem:
        # Abre a imagem selecionada
        img = Image.open(caminho_imagem)

        # Verifica se o diretório de destino existe, se não, cria
        if not os.path.exists(local_destino):
            os.makedirs(local_destino)

        # Salva a imagem no diretório de destino com o nome do arquivo fornecido
        img.save(os.path.join(local_destino, nome_arquivo))
        
        print(f"A imagem foi salva em: {os.path.join(local_destino, nome_arquivo)}")




def adicionar_display_imagem(frame, tamanho_display, tamanho_imagem, pos, caminho_img):
    # Carregar a imagem
    img = Image.open(caminho_img)

    # Redimensionar a imagem para o tamanho especificado
    img = img.resize(tamanho_imagem, Image.ANTIALIAS)

    # Criar uma nova imagem com bordas arredondadas
    img_arredondada = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img_arredondada)
    d.rounded_rectangle([(0, 0), img.size], radius=20, fill=(255, 255, 255, 255))
    img_arredondada = Image.alpha_composite(img_arredondada, img)

    # Converter a imagem para um formato que o tkinter pode usar
    img_tk = ImageTk.PhotoImage(img_arredondada)

    # Criar um widget de label para exibir a imagem
    if frame != frame_submenu:
        cor_submenu = 'white'
    else:
        cor_submenu = '#d9d9d9'
    label_imagem = tk.Label(frame, image=img_tk, bd=0, bg=cor_submenu)
    label_imagem.image = img_tk  # guardar uma referência para evitar o garbage collector
    label_imagem.place(x=pos[0], y=pos[1], width=tamanho_display[0], height=tamanho_display[1])

def adicionar_texto(frame, pos, fonte, cor, cor_submenu, texto):
    # Criar um widget de label para exibir o texto
    label_texto = tk.Label(frame, text=texto, font=fonte, fg=cor, bg=cor_submenu)

    # Posicionar o label
    label_texto.place(x=pos[0], y=pos[1])

# A seguir é como você poderia usar essa classe para adicionar um botão ao frame_submenu
def botselimg(event):
    selecionar_e_salvar_imagem('C:\\Users\\crist\\Code\\python\\trabalho ivo\\cache', 'imagemdisplay.png')
    adicionar_display_imagem(frame_submenu, (200, 200), (150, 120), (6, 10), 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\cache\\imagemdisplay.png')

def mostraritensadicionados():
    posHinicial = 250
    posVinicial = 30
    espacoHmenu = 200
    espacoVmenu = 250
    arquivos = os.listdir('C:\\Users\\crist\\Code\\python\\trabalho ivo\\img')
    cont = 0
    for i in arquivos:
        if cont<=3:
         adicionar_display_imagem(janela_principal, (150, 120), (150, 120), (posHinicial, posVinicial), f'C:\\Users\\crist\\Code\\python\\trabalho ivo\\img\\{i}')
         adicionar_texto(janela_principal, (posHinicial+10, posVinicial+130), (fonte, tamanhofonte), corfont, 'white', f'{i[:-11]}')
         posHinicial += espacoHmenu
         if posHinicial > (espacoHmenu*4):
            posVinicial =+ espacoVmenu
            posHinicial = 250

            cont +=1
        if posHinicial>(espacoHmenu*4) and posVinicial>(espacoVmenu*2):
            posVinicial = espacoVmenu*3


        
        

        
    
def botadd(event):
    controlVar = carregar_informacoes('C:\\Users\\crist\\Code\\log')
    itemid = controlVar['id']
    salvar_log('ok',itemid)
    salvar_informacoes(entradaNome.get_text(), entradaPreco.get_text(), entrada1.get_text(), f'{entradaNome.get_text()} desc[{itemid}]')
    shutil.copy2('C:\\Users\\crist\\Code\\python\\trabalho ivo\\cache\\imagemdisplay.png', 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\img')
    time.sleep(0.5)
    os.rename('C:\\Users\\crist\\Code\\python\\trabalho ivo\\img\\imagemdisplay.png', f'C:\\Users\\crist\\Code\\python\\trabalho ivo\\img\\{entradaNome.get_text()} img[{itemid}].png')
    mostraritensadicionados()
    print("adicionardo")


def botsalvar(event):
    print("salvando")
    for widget in frame_submenu.winfo_children():
        widget.destroy()
    for widget in janela_principal.winfo_children():
        if widget != frame_submenu:
            widget.destroy()
    

##iniciando o objeto   |frame do local||tamanho||local da imagem do botão||||||||||||||||||||||||||||||||||||||||||||||||||||posicao|||funcao que ira ser chamada
botaoseletor = Botao(frame_submenu, (180, 35), 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\layout\\botselimg.png', (10, 200), botselimg)
botaoadicionar = Botao(frame_submenu, (180, 50), 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\layout\\botaoadicionar.png', (10, 440), botadd)
botaosalvar = Botao(frame_submenu, (180, 50), 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\layout\\botaosalvar.png', (10, 500), botsalvar)

#'C:\\Users\\crist\\Code\\python\\trabalho ivo\\layout\\botao1.png'



def botadd(event):
    salvar_informacoes(entradaNome.get_text(), entradaPreco.get_text(), entrada1.get_text(), f'{entradaNome.get_text} desc[{itemid}]')
    shutil.copy2('C:\\Users\\crist\\Code\\python\\trabalho ivo\\cache\\imagemdisplay.png', 'C:\\Users\\crist\\Code\\python\\trabalho ivo\\img')
    os.rename('C:\\Users\\crist\\Code\\python\\trabalho ivo\\img\\imagemdisplay', f'{entradaNome.get_text()} img[{itemid}]')
    adicionar_display_imagem(janela_principal, (200, 200), (150, 120), (50, 10), f'C:\\Users\\crist\\Code\\python\\trabalho ivo\\cache\\{entradaNome.get_text()} img[{itemid}].png')
    print("adicionardo")
textVPos = 235
textHPos = 45
espacotext = 60
fonte = 'Modern Sans Serif 7'
tamanhofonte = 12
corfont = 'gray'

adicionar_texto(frame_submenu, (textHPos, textVPos), (fonte, tamanhofonte), corfont, cor_submenu, 'Nome do Item')
adicionar_texto(frame_submenu, (textHPos, textVPos+espacotext), (fonte, tamanhofonte), corfont, cor_submenu, '    Preço')
adicionar_texto(frame_submenu, (textHPos, textVPos+(espacotext*2)), (fonte, tamanhofonte), corfont, cor_submenu, '  Descrição')




janela_principal.mainloop()
