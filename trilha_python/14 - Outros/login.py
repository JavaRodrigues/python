from tkinter import *
 
class Principal: #cria a classe principal 
    def __init__(self, master=None):  #cria o método inicial e que será filho da classe Principal
        self.fontePadrao = ("Arial", "10") 
        self.Container1 = Frame(master) #definimos o container pai com um frame
        self.Container1["pady"] = 10 #posiciona o container na tela a partir do top e bottom
        self.Container1["bg"] = "light green" # define uma cor de fundo
        self.Container1.pack() #para exibir os widgets do container
 
        self.Container2 = Frame(master) #cria um container para label e text field nome
        self.Container2["padx"] = 20 #posiciona o container na tela a partir de left e right
        self.Container2["bg"] = "light green"
        self.Container2.pack()
 
        self.Container3 = Frame(master) #cria um container para label e text field senha
        self.Container3["padx"] = 20
        self.Container3["bg"] = "light green"
        self.Container3.pack()
 
        self.Container4 = Frame(master) #cria um container para o botão AUTENTICAR e a label MENSAGEM
        self.Container4["pady"] = 20
        self.Container4["bg"] = "light green"
        self.Container4.pack()
 
        self.titulo = Label(self.Container1, text="Dados do usuário:")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["bg"] = "light green"
        self.titulo.pack()
 
        self.nomeLabel = Label(self.Container2,text=" Nome:", font=self.fontePadrao)
        self.nomeLabel["bg"] = "light green"
        self.nomeLabel.pack(side=LEFT) #define o lado da exbição
 
        self.nome = Entry(self.Container2) #utiliza o método Entry (input) para receber dados via teclado
        self.nome.focus() #determina a posição do cursor na caixa de texto
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
 
        self.senhaLabel = Label(self.Container3, text="Senha:", font=self.fontePadrao)
        self.senhaLabel["bg"] = "light green"
        self.senhaLabel.pack(side=LEFT)
 
        self.senha = Entry(self.Container3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
 
        self.autenticar = Button(self.Container4)
        self.autenticar["text"] = "AUTENTICAR"
        self.autenticar["font"] = ("Calibri", "10","bold")
        self.autenticar["width"] = 12
        self.autenticar["bg"] = "white"
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
 
        self.sair = Button()
        self.sair["text"] = "SAIR"
        self.sair["font"] = ("Calibri", "10","bold")
        self.sair["width"] = 5
        self.sair["command"] = quit
        self.sair.pack(side=TOP)
 
        self.mensagem = Label(self.Container4, text="", font=self.fontePadrao)
        self.mensagem["bg"] = "light green"
        self.mensagem.pack()
 
    #Método para verificar senha
    def verificaSenha(self):
        usuario = self.nome.get() #apanha os dados digitados pelo usuário no text field 'nome'
        senha = self.senha.get()
        
        if usuario == "Denilson" and senha == "123":
            self.mensagem["text"] = "Autenticado!"
            self.nome["fg"] = "gray"
            self.senha["fg"] = "gray"
            self.sair.focus_force()
        else:
            self.mensagem["text"] = "Usuário e/ou senha incorretos!"
            self.senha.delete(0,END)
            self.nome.delete(0,END)
            self.nome.focus()
 
tela = Tk() #instancia a classe 'Tk()' através da variável 'tela'
tela.title("TELA DE LOGIN")
tela["bg"] = "light green"
tela.geometry("400x250") #define o tamanho da tela em width (largura) x height (altura)
Principal(tela) #instância da classe Principal, passamos a variável tela como parâmetro
tela.mainloop() #método obrigatório para carregar a tela e para que os eventos ocorram