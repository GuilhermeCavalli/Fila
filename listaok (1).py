fila_idosos=[]
fila_gestante=[]
fila_normal=[]
def insere():
    nome=str(input('Instrira seu nome:'))
    fila=int(input('Escolha sua fila utilizando (1) para idosos (2) para gestantes e (3) para fila normal:'))
    if fila == 1:
        fila_idosos.append(nome)
    elif fila == 2:
        fila_gestante.append(nome)
    elif fila == 3:
        fila_normal.append(nome)
    else:
        print('A opcao escolhida nao existe')
        
def mostra():
    print('Fila dos idosos' , fila_idosos )
    print('Fila de gestantes' , fila_gestante)
    print('Fila normal' , fila_normal)

def deleta():
    if len(fila_idosos)!=0:
        delet=fila_idosos.pop(0)
        print(delet , 'foi atendido')
    elif len(fila_gestante)!=0:
        delet=fila_gestante.pop(0)
        print(delet , 'foi atendido')
    elif len(fila_normal)!=0:
        delet=fila_normal.pop(0)
        print(delet , 'foi atendido')
    else:
        print('o comando digitado nao existe')
rodando= True       
while rodando== True:
    menu=int(input('insira (1) para entrar na fila, (2) para tirar da fila, (3)para mostrar a fila e (4) para sair do programa:'))
    if menu==1:
        insere()
    elif menu==2:
        deleta()
    elif menu ==3:
        mostra()
    elif menu ==4:
        rodando = False
        print('Tenha um bom dia')
    else:
        print('O numero inserido nao eh uma opcao')
        
    


            
