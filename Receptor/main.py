from flask import Flask
from gpiozero import LED, Button
from threading import Thread
import requests

PASSWORD = 'grupocoracao'

botao = Button(27, pull_up=False)
led = LED(22)

app = Flask(__name__)

clientes_de_controle = [('172.17.8.42', 8800)]

def enviar_notificacao_de_desarme():
    led.off()

    for host, port in clientes_de_controle:
        requests.get(f'http://{host}:{port}/?password={PASSWORD}')

    return

botao_pressionado = False
alarme_acionado = False

@app.route('/')
def index():
    global alarme_acionado

    alarme_acionado = True
    led.on()

    return 'Ok'

def processo():
    global botao_pressionado

    while True:
        botao.wait_for_press()
        enviar_notificacao_de_desarme()
        botao.wait_for_release()

    return

def main():
    Thread(target=processo, daemon=True).start()
    app.run('0.0.0.0', 8800, debug=True)

    return

if __name__ == '__main__':
    main()
