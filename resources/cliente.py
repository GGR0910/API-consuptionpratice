from flask_restful import Resource, reqparse
from APIconsume.DAO import ler_cliente, ler_api, salvar_cliente


class clientes(Resource):
    def get(self):
        return {"Name": "Mara"}


class cliente(Resource):
    def get(self, CPF):
        cliente = ler_cliente(CPF=CPF)
        clientejson = {'clientid': cliente[0][0], 'clientname': cliente[0][1], "CPF": cliente[0][2],
                       "CEP": cliente[0][3], "Cidade": cliente[0][6]}
        print(clientejson)
        return clientejson

    def post(self, CPF):
        args = reqparse.RequestParser()

        print(args)
        print("nha")
        args.add_argument('nome', type=str, help='Nome não fornecido')
        args.add_argument('CPF', type=str, help='CPF não fornecido')
        args.add_argument('CEP', type=int, help='CEP não fornecido')

        dadoscliente = args.parse_args()
        novo_client = {
            "nome": dadoscliente['nome']
            , "CPF": dadoscliente['CPF']
            , "CEP": dadoscliente['CEP']

        }
        return novo_client

    def delete(self, CPF):
        pass

    def put(self, CPF):
        pass
