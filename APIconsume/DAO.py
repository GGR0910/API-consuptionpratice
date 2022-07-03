import MySQLdb
import requests

conn= MySQLdb.connect(host='127.0.0.1', user='root', password='Gogoll90@', port=3306)
cursor= conn.cursor()


#read the API
def ler_api(CEP):
    request = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')
    requestjson = request.json()
    if 'erro' not in requestjson:
        print(f"O CEP {CEP} foi encontrado, com os seguintes dados:")
        print(f"Rua: {requestjson['logradouro']}")
        print(f"Bairro: {requestjson['bairro']}")
        print(f"Cidade: {requestjson['localidade']}")
        return(requestjson)

#Save information at db
def salvar_cliente(requestjson,CPF,nomecliente,CEP):
    CPF=int(CPF)
    rua= requestjson['logradouro']
    bairro= requestjson['bairro']
    cidade= requestjson['localidade']
    estado= requestjson['uf']
    ddd= int(requestjson['ddd'])
    cursor.execute(f'Insert into API.APICEP(nomecliente,CPF,CEP,rua,bairro,cidade,estado,ddd)'
                   f'values("{nomecliente}",{CPF},{CEP},"{rua}","{bairro}","{cidade}","{estado}",'
                   f'{ddd})')
    conn.commit()
    return True

#Read db info
def ler_cliente(nome):
    cursor.execute(f'Select * from API.APICEP where nomecliente = "{nome}"')
    dados=cursor.fetchall()
    return dados