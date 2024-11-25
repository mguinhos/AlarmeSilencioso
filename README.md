# Alarme Silencioso de Presença (E controlador em Rede)

Alunos: Arthur Angelo Barbosa Salviano, Marcel Guinhos de Menezes Feitosa; Natani Monte Brito;
Disciplina: Hardware

## Nosso Projeto
Nosso projeto é um alarme silencioso, que pode ser desarmado por um controlador na mesma rede wifi.

### Componentes
* 1x Sensor de presença infravermelho (PIR)
* 2x Raspberry Pi
* 2x Protoboards
* 2x Leds Vermelhos
* 1x Led Verde


## Requisitos
### Pacotes
* python-is-python3
* python3
* pip3

### Bibliotecas
* flask
* gpiozero
* requests

## Executando
* Clone o repositorio em ambas as duas raspberry pi

## Instalando os requisitos
```
$ pip install -r requirements.txt
```

### Para rodar o serviço do Receptor
Logue na raspberry pi que será o receptor.

```
$ python Receptor/main.py
```

### Para rodar o serviço do Alarme
Logue na raspberry pi que sera o alarme.
```
$ python Alarme/main.py
```
