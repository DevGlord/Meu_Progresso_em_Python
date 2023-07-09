


"""
import mysql.connector


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'minha_empresa'
)

cursor = conexao.cursor()

# CREATE

nome_disciplina = str(input('\033[1;32mDisciplina:\033[m'))
participacao_aula = str(input('\033[1;32mParticipação:\033[m'))
nota_media = float(input('\033[1;32mNota:\033[m'))

comando = f'INSERT INTO disciplinas (nome_disciplina,participacao_aula,nota_media) VALUES ("{nome_disciplina}","{participacao_aula}",{nota_media})'

cursor.execute(comando)
conexao.commit()
"""



# UPDATE
#cursor.execute('UPDATE disciplinas SET nota_media = 15.0 where nota_media = 15')
#conexao.commit()

# DELETE
cursor.execute('DELETE FROM disciplinas where nome_disciplina = "Ing"')
conexao.commit()

# READ
cursor.execute('SELECT * FROM disciplinas;')
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()


