from flask import Flask
from flask_restful import Api
from resources.cliente import cliente,clientes

app = Flask(__name__)
api = Api(app)


api.add_resource(clientes,'/clientes')
api.add_resource(cliente,'/cliente/<int:CPF>')

if __name__ == "__main__":
    app.run(debug=True)