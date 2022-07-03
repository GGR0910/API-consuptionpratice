import MySQLdb

conn= MySQLdb.connect(host='127.0.0.1', user='root', password='Gogoll90@', port=3306)
cursor= conn.cursor()

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
