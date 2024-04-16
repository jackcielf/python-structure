# Ao executar este arquivo é criado automaticamente o banco de dados e suas tabelas
# A partir dos dados fornecidos nos arquivos deste diretório (db.sql e db_config.txt)

import mysql.connector
from mysql.connector import errorcode

with open('db_config.txt', 'r') as f:
  lines = f.readlines()
  config = dict(line.strip().split('=') for line in lines)

# Connect with MySQL
try:
  cnx = mysql.connector.connect(
    user=config['user'],
    password=config['password'],
    host=config['host'],
  )

  # Create DB and tables
  cursor = cnx.cursor()

  with open('sql.sql', 'r') as f:
    sql_script = f.read()
    commands = sql_script.split(';')

  for command in commands:
    try:
      cursor.execute(command)

    except mysql.connector.Error as err:
      print(f"Failed to execute command: {err}")

  cnx.commit()
  cursor.close()
  cnx.close() # Close connection

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("ERROR: Is there any incorrect connection data")

  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("ERROR: Database does not exist")

  else:
    print(err)