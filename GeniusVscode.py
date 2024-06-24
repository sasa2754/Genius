import requests
import json
import time
import pyodbc

proxies = {'https': "http://disrct:etsps2024401@10.224.200.26:8080"}

FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"


url = FIREBASE_URL + "Sabrina.json"
data = requests.get(url, proxies=proxies).content
dados = json.loads(data)
pontos = dados.get("Recorde")
print(f"Dados do firebase pegos com sucesso! Última pontuação: {pontos}")

server = 'CA-C-0064H\SQLEXPRESS'
database = 'Genius_SQL'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
cursor = cnxn.cursor()

def InserirBD(sinal):
    cursor.execute("INSERT INTO Recordes (Recorde) VALUES (?)", (pontos,))
    cursor.commit()
    print("Inserido com sucesso!")

# def apresentar(sinal):
#     print(f"Pontuação: {sinal['Recorde']}")

def maiorPontuacao(cursor):
    maior = 0
    idJogador = None
    SQL_QUERY = "SELECT * FROM Recordes ORDER BY Recorde DESC"
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    for r in records:
        print(f"ID: {r.id}\nPontuação: {r.Recorde}\n")
        if r.Recorde is not None and r.Recorde > maior:
            maior = r.Recorde
            idJogador = r.id
        
    if idJogador is not None:
        print(f"==========Maior pontuação==========\nID: {idJogador}\nRecorde: {maior}\n\n")
    else:
        print("Nenhum registro encontrado.")

url = FIREBASE_URL + "Sabrina.json"
data = requests.get(url, proxies=proxies).content
dados = json.loads(data)
pontos = dados.get("Recorde")
# apresentar(pontos)
InserirBD(pontos)
maiorPontuacao(cursor)
