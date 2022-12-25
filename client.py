import socket

comands = {'aileron': '/controls/flight/aileron', 'elevator': '/controls/flight/elevator',
           'rudder': '/controls/flight/rudder', 'throttle': '/controls/engines/engine/throttle',
           'roll': '/orientation/roll-deg', 'pitch': '/orientation/pitch-deg',
           'heading': '/orientation/heading-deg', 'brake-parking': '/controls/gear/brake-parking',}
message_end = bytes([13, 10])


def get_value(comand):
    message = comands[comand]
    message = 'get {}'.format(message)
    message = bytes(message, encoding='utf-8') + message_end
    sock.send(message)
    result = sock.recv(1024)
    result.decode()
    result = str(result)
    result1 = result.split("'")
    return float(result1[1])


def set_value(comand, value):
    message = comands[comand]
    message = 'set {} {}'.format(message, value)
    message = bytes(message, encoding='utf8') + message_end
    sock.send(message)
    result = sock.recv(1024)


def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5051))


def disconnect():
    global sock
    sock.close()
