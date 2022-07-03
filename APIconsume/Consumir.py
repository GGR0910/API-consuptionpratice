import DAO
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

requestjson=DAO.ler_api(CEP=CEP)
print("A consultar CEP.")


if DAO.salvar_cliente(nomecliente=Nome, CPF=CPF, requestjson=requestjson, CEP=CEP):
    print("Cliente salvo!")


else:
    print("CEP inválido.")
