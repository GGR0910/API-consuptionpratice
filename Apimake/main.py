from flask import Flask,request
from flask_restful import Api, Resource
import APIconsume.DAO

app = Flask(__name__)
api = Api(app)



# pega os dados do banco de dados de clientes
class clientes(Resource):
    def get(self):
        CPF=request.form['CPF']
        dados = APIconsume.DAO.ler_cliente(CPF)
        return {"nome": dados[0][0], "rua": dados[0][3], "Cidade": dados[0][5]}

    # atualiza o banco de dados com novos dados
    def put(self):
        CEP=request.form['CEP']
        CPF=request.form['CPF']
        print(CPF)
        respostaAPI= APIconsume.DAO.ler_api(CEP=CEP)
        APIconsume.DAO.salvar_cliente(requestjson=respostaAPI,CEP=CEP,nomecliente=request.form['nomecliente']
                                      ,CPF=request.form['CPF'])
        Valor=self.get()
        return Valor


api.add_resource(clientes, "/Ola_mundo")

if __name__ == '__main__':
    app.run(debug=True)
