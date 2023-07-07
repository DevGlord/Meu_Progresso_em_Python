import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'cadastro',
)

cursor = conexao.cursor()

#CRUD
nome = input('Digite o seu nome:')
rg = input('Digite o seu rg:')
cpf = int(input('CPF:'))
limite = int(input('Limite:'))
comando = f'INSERT INTO pessoas (nome,rg,cpf,limite) VALUES ("{nome}","{rg}",{cpf},{limite})'
cursor.execute(comando)
conexao.commit()

#resultado = cursor.fetchall()
#print(resultado)

cursor.close()
conexao.close()
