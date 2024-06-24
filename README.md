# Como montar o circuíto
1° Passo: Conectando na ESP32:
- Entrada do led Amarelo -- GPIO 13
- Entrada do led Vermelho -- GPIO 12
- Entrada do led Azul -- GPIO 14
- Entrada do led Verde -- GPIO 27
- Saída do botão Amarelo -- GPIO 33
- Saída do botão Vermelho -- GPIO 32
- Saída do botão Azul -- GPIO 35
- Saída do botão Verde -- GPIO 34
- Buzzer -- GPIO 25

2° Passo: O que vai no GND?
- GND do buzzer
- Saída de todos os leds, conectado com um resistor de 220
- Saída de todos os botões, conectado com um resistor de 220 (Na mesma linha que está conectado na esp)

3° Passo: O que vai no VIN?
- VCC do buzzer
- Entrada de todos os botões

# Exemplo de circuíto:
<img src= "https://i.ibb.co/nL1KQ9K/IMG-20240621-WA0002.jpg"/>
