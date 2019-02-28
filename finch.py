from flask import Flask,render_template,request # Abrindo framework Flask

import csv, sys, itertools #Importando bibliotecas para  utilizar nos arquivos .csv

app = Flask (__name__)

@app.route('/') #Abrindo a pagina .html principal com o TextArea e o botão
def index():
    return render_template('index.html')
    
@app.route('/result', methods= ['GET'])
def result(): # Os dados do TextArea são passados pela URL e em seguida é feito uma busca com estes dados retornando e imprimindo na página .html "result"
    letra = request.args.get('tArea') 
    estilo = busca(letra) 

    return render_template('result.html', resultado=estilo)

# Função busca() abre os arquivos .csv e com uma sequencia de For procura simultaneamente o os dados do TextAre(variavel letra) nos arquivos
def busca(letra):

    letra = letra.replace ('%0D%0A', '%2C')
    print (letra)
    bn = open("bossa_nova.csv")
    funk = open("funk.csv")    
    gospel = open("gospel.csv")
    sertanejo = open("sertanejo.csv")

    # Lendo os arquivos .csv
    r_bn = csv.reader(bn)
    r_funk = csv.reader(funk)
    r_gospel = csv.reader(gospel)
    r_sertanejo = csv.reader(sertanejo)

    # 'For' onde os 4 arquivos .csv rodam simultaneamente procurando a variável 'letra' dentro dos arquivos 
    for row1, row2, row3, row4 in itertools.zip_longest(r_bn, r_funk,r_gospel,r_sertanejo):
        for field1, field2, field3, field4 in itertools.zip_longest(row1, row2, row3,row4) :   
            
            if letra in field1:
                resultado = 'Bossa nova'
                
                
            elif letra in field2:
                resultado = 'Funk'
                print(field2)
                
            elif letra in field3:
                resultado = 'Gospel'
                print(resultado)
                
            elif letra in field4:
                resultado = 'Sertanejo'
                print(resultado)
                

    return resultado           
#Palavras/Frases que o programa funciona :Eu sei que vou te amar - rabetão - quatro ou cinco - adorarei  
   
if __name__ == "__main__":

    app.run(debug=True)

