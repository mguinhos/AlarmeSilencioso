from gpiozero import LED, MotionSensor
import requests
from flask import Flask, request
from time import sleep
from threading import Thread
from time import sleep

PASSWORD = 'grupocoracao'

pir = MotionSensor(17)

led_vermelho = LED(27)
led_verde = LED(22)

acionado = False

servidores_de_controle = [('172.17.8.8', 8800)]

def enviar_notificacao_acionamento():
    for ip, port in servidores_de_controle:
        try:
            requests.get(f'http://{ip}:{port}')
        except:
            pass

    return

def acionar_alarme():
    global acionado

    if acionado:
        return

    acionado = True
    led_verde.off()
    led_vermelho.on()

    Thread(target=enviar_notificacao_acionamento, daemon=True).start()

    return

def desarme_negado():
    led_verde.off()

    for _ in range(4):
        led_vermelho.off()
        sleep(0.125)
        led_vermelho.on()
        sleep(0.25)

    acionar_alarme()

    return

pir.when_motion = acionar_alarme

app = Flask(__name__)

@app.route('/')
def index():
    global acionado

    password = request.args.get('password')

    if password != PASSWORD:
        Thread(target=desarme_negado, daemon=True).start()

        return 'Denied'

    acionado = False

    led_vermelho.off()
    led_verde.on()

    return 'Ok'

def main():
    led_vermelho.off()
    led_verde.on()

    app.run('0.0.0.0', 8800, debug=True)

    return

if __name__ == '__main__':
    main()
