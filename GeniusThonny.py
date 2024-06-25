from machine import Pin, PWM
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

buzzer = PWM(Pin(25, Pin.OUT))
buzzer.deinit()

listaAleatoria = []
listaJogador = []
erro = False

def play_tone(freq, duration_ms):
    buzzer.freq(freq)  # Define a frequência em Hz
    buzzer.duty(50)    # Define o ciclo de trabalho (50% para som contínuo)
    time.sleep_ms(duration_ms)
    buzzer.duty(0)     # Para o som

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
            play_tone(400, 500)
            time.sleep(0.3)
            apagarLed(ledAmarelo)
        elif listaAleatoria[i] == 2:
            time.sleep(0.3)
            acenderLed(ledVermelho)
            play_tone(300, 500)
            time.sleep(0.3)
            apagarLed(ledVermelho)
        elif listaAleatoria[i] == 3:
            time.sleep(0.3)
            acenderLed(ledAzul)
            play_tone(250, 500)
            time.sleep(0.3)
            apagarLed(ledAzul)
        elif listaAleatoria[i] == 4:
            time.sleep(0.3)
            acenderLed(ledVerde)
            play_tone(150, 500)
            time.sleep(0.3)
            apagarLed(ledVerde)
        time.sleep(0.2)
        
    corLed = random.randint(1, 4)
    
    if corLed == 1:
        time.sleep(0.3)
        acenderLed(ledAmarelo)
        play_tone(400, 500)
        listaAleatoria.append(1)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 2:
        time.sleep(0.3)
        acenderLed(ledVermelho)
        play_tone(300, 500)
        listaAleatoria.append(2)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 3:
        time.sleep(0.3)
        acenderLed(ledAzul)
        play_tone(250, 500)
        listaAleatoria.append(3)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
    elif corLed == 4:
        time.sleep(0.3)
        acenderLed(ledVerde)
        play_tone(150, 500)
        listaAleatoria.append(4)
        time.sleep(0.3)
        apagarLed(ledAmarelo)
        
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
            play_tone(400, 500)
            listaJogador.append(1)
            conferirSequencia(i)
            i+=1
            
        elif buttonVermelhoValue == 1:
            acenderLed(ledVermelho)
            play_tone(300, 500)
            listaJogador.append(2)
            conferirSequencia(i)
            i+=1
            
        elif buttonAzulValue == 1:
            acenderLed(ledAzul)
            play_tone(250, 500)
            listaJogador.append(3)
            conferirSequencia(i)
            i+=1
            
        elif buttonVerdeValue == 1:
            acenderLed(ledVerde)
            play_tone(150, 500)
            listaJogador.append(4)
            conferirSequencia(i)
            i+=1
            
        time.sleep(0.2)
        

def musicaComeco():
    play_tone(392, 300)  # G4
    play_tone(440, 300)  # A4
    play_tone(392, 300)  # G4
    play_tone(523, 500)  # C5
    
    time.sleep(0.3)  # Pausa curta
    
    play_tone(494, 300)  # B4
    play_tone(392, 300)  # G4
    play_tone(440, 300)  # A4
    play_tone(523, 500)  # C5
    
def musicaFinal():
    play_tone(450, 500)
    play_tone(400, 100)
    play_tone(380, 100)
    play_tone(360, 100)
    play_tone(340, 100)
    play_tone(320, 100)
    play_tone(300, 100)
    play_tone(280, 100)
    play_tone(260, 100)
    play_tone(240, 100)
    play_tone(220, 100)
    play_tone(200, 100)
    play_tone(180, 100)
    play_tone(160, 100)
    play_tone(140, 100)
    play_tone(120, 100)
    play_tone(140, 100)
    play_tone(160, 100)
    play_tone(120, 100)
    play_tone(140, 100)
    play_tone(100, 100)

    
def jogoPrincipal():
    global erro
    erro = False
    i = 0
    
    buzzer.init()
    musicaComeco()
    while not erro:
        print(f"Jogada {i}:")
        coresJogo()
        time.sleep(0.5)
        jogadaJogador(i)
        time.sleep(0.2)
        apagarLed(ledAmarelo); apagarLed(ledVermelho); apagarLed(ledAzul); apagarLed(ledVerde)
        if erro:
            print("Erro!")
            
            play_tone(100, 500)
            time.sleep(0.2)
            musicaFinal()
            time.sleep(0.3)
            buzzer.deinit()
            break
        else:
            i+=1


jogoPrincipal()


