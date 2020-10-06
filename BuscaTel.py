import timeit # Marcar tempo 
import os # Import para usar Path
import threading # Import para multithread	
from tkinter import *
  
class Application:
    def __init__(self, master):
   
        self.frame=Frame(master,width=500,height=100) #Titulo Programa
        master.title("Controle de Vendas")
        self.frame.pack
        
        self.fonte = ("Arial", "10") #Conteiner 1
        self.pb = Frame(master)
        self.pb["pady"] = 10
        self.pb.pack()
        
        self.p1 = Frame(master) #Conteiner 2
        self.p1["padx"] = 20
        self.p1.pack()
        
        self.fonte = ("Arial", "10")  #Conteiner 3
        self.pb1 = Frame(master)
        self.pb1["pady"] = 10
        self.pb1.pack()
        
        self.p2 = Frame(master) #Conteiner 4
        self.p2["padx"] = 20
        self.p2.pack()
        
        self.pc = Frame(master) #Conteiner 4
        self.pc["pady"] = 10
        self.pc.pack()
  
        self.sc = Frame(master) #Conteiner 5
        self.sc["padx"] = 20
        self.sc.pack()
        
        self.tc = Frame(master) #Conteiner 6
        self.tc["padx"] = 20
        self.tc.pack()
  
        self.qc = Frame(master) #Conteiner 7
        self.qc["padx"] = 20
        self.qc.pack()
        
        self.titulopb = Label(self.pb, text="Digite a Pasta Busca") #Titulo 1
        self.titulopb["font"] = ("Arial", "10", "bold")
        self.titulopb.pack()
        
        self.pastaB = Entry(self.p1) #Entrada da Pasta 1
        self.pastaB["width"] = 30
        self.pastaB["font"] = self.fonte
        self.pastaB.pack(side=LEFT)
        
        self.titulopb1 = Label(self.pb1, text="Digite a Pasta Destino") #Titulo 2
        self.titulopb1["font"] = ("Arial", "10", "bold")
        self.titulopb1.pack()
        
        self.pastaD = Entry(self.p2) #Entrada da Pasta 2
        self.pastaD["width"] = 30
        self.pastaD["font"] = self.fonte
        self.pastaD.pack(side=LEFT)
  
        self.titulo = Label(self.pc, text="Digite o Telefone ou CPF") #Titulo 3
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.telLabel = Label(self.sc,text="Telefone", font=self.fonte) #SubTitulo 3
        self.telLabel.pack(side=LEFT)
  
        self.tel = Entry(self.sc)  #Entrada Telefone
        self.tel["width"] = 30
        self.tel["font"] = self.fonte
        self.tel.pack(side=LEFT)
        
        self.cpfLabel = Label(self.tc,text="CPF", font=self.fonte) #SubTitulo 4
        self.cpfLabel.pack(side=LEFT)
  
        self.cpf = Entry(self.tc) #Entrada CPF
        self.cpf["width"] = 34
        self.cpf["font"] = self.fonte
        self.cpf.pack(side=LEFT)
  
        self.exe = Button(self.qc)  #Comando Executar
        self.exe["text"] = "Executar"
        self.exe["font"] = ("Calibri", "8")
        self.exe["width"] = 12
        self.exe["command"] = self.BuscaNumero
        self.exe.pack()

    def BuscaNumero(self):
        inicio = timeit.default_timer()   #Inicia Tempo     
        x = self.tel.get()  #Entrada telefone
        y = self.cpf.get()  #Entrada cpf
        path = self.pastaB.get() #Caminho dos números
        path2 = self.pastaD.get() #Caminho do novo .TXT
        dirs = os.listdir(path) #Cria uma lista de todos números
        for pasta in dirs: #Foreach para ler todos arquivos e comparar
            print(pasta) #Mostra as pastas que já foram lidas
            variavel = ''' \ ''' #Variavel de Mudança
            variavel2 = "\\"     #Variavel de Mudança
            arq = open(path.replace(variavel,variavel2)+"\\"+pasta,'r') #Abre arquivo para ler
            arquivo = open(path2.replace( variavel , variavel2 )+"\\" + 'busca_tel_'+x+y+'.txt','a+') #Cria novo .TXT \ a+ = append
            try: #Para mostrar mensagem de erro em alguns arquivos
                arquivo.writelines("")
                for linha in arq: 
                    valores = linha.split(',')
                    if valores[3] == x: #Compara se o '3 - telefone' é igual ao número informado
                        arquivo.writelines(linha)  #Escreve no arquivo
                    elif valores[0] == y:
                        arquivo.writelines(linha)
            except:
                print('Erro')
        fim = timeit.default_timer()
        print('Duração: %f' %(fim-inicio))
        arquivo.close()
        return print('Busca concluída')

    

root = Tk()
Application(root)
root.mainloop()