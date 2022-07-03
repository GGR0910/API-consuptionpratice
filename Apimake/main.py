from flask import Flask
from flask_restful import Api, Resource
import APIconsume.DAO


app = Flask(__name__)
api = Api(app)

#pega os dados do banco de dados de clientes
class helloworld(Resource):
    def get(self,name):
        dados=APIconsume.DAO.ler_cliente(name)
        return {"nome":dados[0][0],"rua":dados[0][3],"Cidade":dados[0][5]}

#atualiza o banco de dados com novos dados
    def post(self):
        return {"data": "posted"}

api.add_resource(helloworld, "/Ola_mundo/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
