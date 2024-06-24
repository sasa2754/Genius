from machine import Pin
import random
import time
import urequests
import ujson
import network

ledAmarelo = Pin(13, Pin.OUT)
ledVermelho = Pin(12, Pin.OUT)
ledAzul = Pin(14, Pin.OUT)
ledVerde = Pin(27, Pin.OUT)

buttonAmarelo = Pin(33, Pin.IN)
buttonVermelho = Pin(32, Pin.IN)
buttonAzul = Pin(35, Pin.IN)
buttonVerde = Pin(34, Pin.IN)

buzzer = Pin(25, Pin.OUT)

listaAleatoria = []
listaJogador = []
erro = False

#Credenciais do WIFI
nome = "" #Coloque o nome da rede
senha = "" #Coloque a senha da rede

# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    url = FIREBASE_URL + "Sabrina.json"  

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()


conectarWifi()

def acenderLed(ledCor):
    ledCor.value(1)

def apagarLed(ledCor):
    ledCor.value(0)

def conferirSequencia(i):
    global erro
    if listaJogador[i] != listaAleatoria[i]:
        erro = True

def coresJogo():
    global listaAleatoria
    for i in range(len(listaAleatoria)):
        apagarLed(ledAmarelo); apagarLed(ledVermelho); apagarLed(ledAzul); apagarLed(ledVerde)
        if listaAleatoria[i] == 1:
            time.sleep(0.3)
            acenderLed(ledAmarelo)
            time.sleep(0.3)
            apagarLed(ledAmarelo)
        elif listaAleatoria[i] == 2:
            time.sleep(0.3)
            acenderLed(ledVermelho)
            time.sleep(0.3)
            apagarLed(ledVermelho)
        elif listaAleatoria[i] == 3:
            time.sleep(0.3)
            acenderLed(ledAzul)
            time.sleep(0.3)
            apagarLed(ledAzul)
        elif listaAleatoria[i] == 4:
            time.sleep(0.3)
            acenderLed(ledVerde)
            time.sleep(0.3)
            apagarLed(ledVerde)
        time.sleep(0.2)
        
    corLed = random.randint(1, 4)
    
    if corLed == 1:
        time.sleep(0.3)
        acenderLed(ledAmarelo)
        listaAleatoria.append(1)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 2:
        time.sleep(0.3)
        acenderLed(ledVermelho)
        listaAleatoria.append(2)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 3:
        time.sleep(0.3)
        acenderLed(ledAzul)
        listaAleatoria.append(3)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 4:
        time.sleep(0.3)
        acenderLed(ledVerde)
        listaAleatoria.append(4)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
    time.sleep(0.5)
        
def jogadaJogador(qtd):
    global listaJogador
    i = 0
    listaJogador = []
    while (i<=qtd):
        apagarLed(ledAmarelo); apagarLed(ledVermelho); apagarLed(ledAzul); apagarLed(ledVerde)
        time.sleep(0.1)
        
        buttonAmareloValue = buttonAmarelo.value()
        buttonVermelhoValue = buttonVermelho.value()
        buttonAzulValue = buttonAzul.value()
        buttonVerdeValue = buttonVerde.value()
        
        if buttonAmareloValue == 1:
            acenderLed(ledAmarelo)
            listaJogador.append(1)
            conferirSequencia(i)
            i+=1
            
        elif buttonVermelhoValue == 1:
            acenderLed(ledVermelho)
            listaJogador.append(2)
            conferirSequencia(i)
            i+=1
            
        elif buttonAzulValue == 1:
            acenderLed(ledAzul)
            listaJogador.append(3)
            conferirSequencia(i)
            i+=1
            
        elif buttonVerdeValue == 1:
            acenderLed(ledVerde)
            listaJogador.append(4)
            conferirSequencia(i)
            i+=1
            
        time.sleep(0.3)
        

        
def jogoPrincipal():
    global erro
    buzzer.value(0)
    erro = False
    i = 0
    
    while not erro:
        print(f"Jogada {i}:")
        coresJogo()
        time.sleep(0.5)
        jogadaJogador(i)
        time.sleep(0.2)
        time.sleep(1)
        apagarLed(ledAmarelo); apagarLed(ledVermelho); apagarLed(ledAzul); apagarLed(ledVerde)
        if erro:
            print("Erro!")
            for j in range(3):
                buzzer.value(1)
                time.sleep(0.2)
                buzzer.value(0)
                time.sleep(0.2)
            break
        else:
            i+=1
            
        informacao = {
            "Pontuação": i,
        }

        enviarFire(informacao)


jogoPrincipal()

