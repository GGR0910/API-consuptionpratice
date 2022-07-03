from DAO import salvar_cliente
import requests
import string

print("Cadastrar cliente ")

Nome=input("Nome do cliente: ")

CPF= input("CPF do cliente: ")
CPF= CPF.translate(str.maketrans('', '', string.punctuation))
while len(CPF) != 11:
    CPF = input("CPF do cliente longo ou curto, preencha novamente: ")
    CPF = CPF.translate(str.maketrans('', '', string.punctuation))



CEP= input("Digite o CEP: ")
CEP= CEP.translate(str.maketrans('', '', string.punctuation))
while len(CEP) !=8:
    CEP= input("CEP inválido, digite novamente e verfique se há erro: ")
    CEP = CEP.translate(str.maketrans('', '', string.punctuation))


request = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')
requestjson= request.json()

print("A consultar CEP.")

if 'erro' not in requestjson:
    print(f"O CEP {CEP} foi encontrado, com os seguintes dados:")
    print(f"Rua: {requestjson['logradouro']}")
    print(f"Bairro: {requestjson['bairro']}")
    print(f"Cidade: {requestjson['localidade']}")
    if salvar_cliente(nomecliente=Nome, CPF=CPF, requestjson=requestjson, CEP=CEP):
        print("Cliente salvo!")


else:
    print("CEP inválido.")
