# Gabriel Frederico Takahashi Vargas 

import random
import urllib.request

right  = False
certas = ''
erradas = '' 
sortiando = ''
lenofpalavra = [] 
contadordeerros = 0
letters = ''
text = ''
forca = ['''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
            |   |               |X|
            |___|               |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
            |   |\              |X|
            |___|\\             |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
  _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\             |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\             |X|
               ||               |X|
               ||               |X|
               ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡x _ʖ ͡x)            |X|
           /|   |\              |X|
          //|___|\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\
''','''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡x _ʖ ͡x)            |X|
           /|   |\              |X|
          //|___|\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\

''']

            
def escolhe():

    global lenofpalavra
    global letters
    global text
    global sortiando 

    lenofpalavra = [] 
    sortiando = ''    
    letters = ''
    text = ''
    

    site = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br') 
    text = site.read().decode('iso8859')
    texto_trabalhando = text.lower()
    texto_trabalhando2 = texto_trabalhando.split() 
    sortiando = random.choice(texto_trabalhando2) 

    if len(sortiando) > 5: 
        print( "A palavra atende os requisitos. ")
    else:
        while len(sortiando) <= 5:
            sortiando = random.choice.split(text)

    for k in range(0,len(sortiando)):
        lenofpalavra.append('-') 

    chute(letters) 

    
def desenha():

    if contadordeerros == 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros == 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print ('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros == 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
            |   |               |X|
            |___|               |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros == 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
            |   |\              |X|
            |___|\\\             |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros == 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\\             |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros == 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\\             |X|
               ||               |X|
               ||               |X|
               ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros == 6 and contadordeerros != 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡° ͜ʖ ͡°)            |X|
           /|   |\              |X|
          //|___|\\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if  contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros == 7 and contadordeerros != 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡x _ʖ ͡x)            |X|
           /|   |\              |X|
          //|___|\\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\
''')
    if  contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and contadordeerros != 7 and contadordeerros == 8:
       print('''
 _________________________________
 |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|+|
            | :: |              |X|
            | :: |              |X|
         \|||||||||/            |X|
         ( ͡x _ʖ ͡x)            |X|
           /|   |\              |X|
          //|___|\\\             |X|
            || ||               |X|
            || ||               |X|
            || ||               |X|
                                |X|
                                |X|
                                |X|
                                |X|
===============================/|X|\\

''')


def chute(letters):
 
    global erradas
    global contadordeerros
    right = False

    contadordeerros = 0
    erradas = ''
    certas = ''
    caracteresinvalidos = ["0"]
    caracteresinvalidos.append("1")
    caracteresinvalidos.append("2")
    caracteresinvalidos.append("3")
    caracteresinvalidos.append("4")
    caracteresinvalidos.append("5")
    caracteresinvalidos.append("6")
    caracteresinvalidos.append("7")
    caracteresinvalidos.append("8")
    caracteresinvalidos.append("9")
    caracteresinvalidos2 = ["!"]
    caracteresinvalidos2.append("@")
    caracteresinvalidos2.append("#")
    caracteresinvalidos2.append("$")
    caracteresinvalidos2.append("%")
    caracteresinvalidos2.append("&")
    caracteresinvalidos2.append("*")
    caracteresinvalidos2.append("(")
    caracteresinvalidos2.append(")")
    caracteresinvalidos2.append("-")
    caracteresinvalidos2.append("_")
    caracteresinvalidos2.append("+")
    caracteresinvalidos2.append("=")
    caracteresinvalidos2.append("}")
    caracteresinvalidos2.append("{")
    caracteresinvalidos2.append("[")
    caracteresinvalidos2.append("]")
    caracteresinvalidos2.append("^")
    caracteresinvalidos2.append("~")
    caracteresinvalidos2.append(".")
    caracteresinvalidos2.append(",")
    caracteresinvalidos2.append("/")
    caracteresinvalidos2.append("?")
    caracteresinvalidos2.append("|")
    caracteresinvalidos2.append("¨")
    caracteresinvalidos2.append("¬")
    caracteresinvalidos2.append(" ")
    caracteresinvalidos2.append("  ") 
    caracteresinvalidos2.append("¢")
    caracteresinvalidos2.append("£")
    caracteresinvalidos2.append("¹")
    caracteresinvalidos2.append("²")
    caracteresinvalidos2.append("³")
    caracteresinvalidos2.append("°")
    caracteresinvalidos2.append(";")

    lista_validas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','é','ê','ú','û','á','ã','â','í','î','ó','ô','õ',]   

    chute = ''

    while right ==  False: 
        print (lenofpalavra)
        desenha()
        chute = input("Digite  a letra desejada: ") 
        
        g = False
        
        while g == False: 
           if chute in caracteresinvalidos or chute in caracteresinvalidos2 or chute not in lista_validas:
              print("Números ou caracteres especiais são invalidos.")
              chute = input ("Digite um caracter válido: ") 
           
           elif chute in letters or chute not in lista_validas:
               print ("A letra selecionada já foi utilizada")
               chute = input ("Digite um caracter diferente: ")

           elif len(chute) > 1 or chute not in lista_validas:
            print ("Não é aceito mais de um caracter.")
            chute = input("Digite apenas uma palavra: ")

           else:
              g = True   

        print ("Tentativas erradas: ",erradas)

        print ("Tentativas corretas: ",certas)
        

        for j in range(0,len(sortiando)):
            if chute == sortiando[j]:
                lenofpalavra[j] = chute

        right = True

        for x in range(0,len(sortiando)):
            if lenofpalavra[x] == "-":
                right = False
                    
        if chute not in sortiando:
            erradas = erradas + chute + ' '
            contadordeerros += 1
            
        else:
            certas = certas + chute + ' '
         
        ganhou() 
          
def ganhou():
    global right
    global contadordeerros
    

    if contadordeerros != 0 and contadordeerros != 1 and contadordeerros != 2 and contadordeerros != 3 and contadordeerros != 4 and contadordeerros != 5 and contadordeerros != 6 and     contadordeerros != 7 and contadordeerros == 8: #Verificando se o usuario ultrapassou o limite de erros
       print("Você perdeu :c")
       jogar_novamente() 
    return False

    if contadordeerros == 0 or contadordeerros == 1 or contadordeerros == 2 or contadordeerros == 3 or contadordeerros == 4 or contadordeerros == 5 or contadordeerros == 6 or   contadordeerros == 7 and contadordeerros != 8:
       print ("Você ganhou, parabéns !! :)")
       jogar_novamente()
       return True

def jogar_novamente(): 
    lista_sim = ['sim','s','S','SIM','ss', 'SS']
    lista_nao = ['n', 'N', 'nao', 'NAO', 'não', 'NÃO','NN','nn']

    g = False
    joga_dnv = input('Você gostaria de jogar novamente? (S/N): ')

    while g == False:   

        if joga_dnv in lista_sim or joga_dnv in lista_nao:
            if joga_dnv in lista_sim:
                g = True
                escolhe()
            elif joga_dnv in lista_nao:
                g = True
                quit()
        else:
            print("Opção invalida, porfavor digite um caracter correto ")
            joga_dnv = input("Gostaria de jogar novamente? (S/N):")
            
escolhe()

