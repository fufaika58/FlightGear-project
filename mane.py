from tkinter import *
from client import *
import time


def test():
    global rudder, heading, aileron, roll, throttle
    rudder = get_value('rudder')
    heading = get_value('heading')
    aileron = get_value('aileron')
    roll = get_value('roll')
    set_value('brake-parking', 0.0)
    throttle = 0.5
    test_rudder()
    test_throttle()


def test_throttle():
    global throttle, k
    for i in range(11):
        set_value('throttle', throttle)
        scake1.set(throttle)
        window.update()
        if 0.79 < throttle < 0.81:
            safe_button()
        throttle += 0.05
        time.sleep(0.8)


def safe_button():
    global rudder
    set_value('rudder', rudder - 0.45)
    rudder = rudder - 0.45
    scake2.set(rudder)


def test_rudder():
    global rudder, heading, throttle
    new_heading = get_value('heading')
    if abs(new_heading - heading) > 0.05:
        if new_heading - heading > 0.05:
            set_value('rudder', rudder - 0.05)
            rudder = rudder - 0.05
            scake2.set(rudder)
            window.update()
        elif new_heading - heading < -0.05:
            set_value('rudder', rudder + 0.05)
            rudder = rudder + 0.05
            scake2.set(rudder)
            window.update()
    heading = new_heading
    if throttle > 1.0:
        scake2.set(0.0)
        set_value('rudder', 0.0)
        window.after(10, test_aileron())
    else:
        window.after(200, test_rudder)


def test_aileron():
    global aileron, roll
    new_roll = get_value('roll')
    if roll > 0.05:
        set_value('aileron', -0.02)
        aileron = -0.02
        scake3.set(aileron)
    elif roll < -0.05:
        set_value('aileron', 0.0475)
        aileron = 0.0475
        scake3.set(aileron)
    roll = new_roll
    window.after(10, test_aileron)


window = Tk()
window.geometry('650x175')

btn1 = Button(window, text="Подключение", width=12, height=1, command=connect)
btn1.grid(column=0, row=0, stick='we')

btn3 = Button(window, text="Взлет", width=12, height=1, command=test)
btn3.grid(column=1, row=0, stick='we')


lab1 = Label(window, text='Throttle')
lab1.grid(column=0, row=1)

lab2 = Label(window, text='Rudder')
lab2.grid(column=0, row=2)

lab3 = Label(window, text='Aileron')
lab3.grid(column=0, row=3)


scake1 = DoubleVar(value=0)
sca1 = Scale(window, orient=HORIZONTAL, length=500, from_=0, to=1, resolution=0.01, variable=scake1)
sca1.grid(column=1, row=1)

scake2 = DoubleVar(value=0)
sca2 = Scale(window, orient=HORIZONTAL, length=500, from_=-1, to=1, resolution=0.01, variable=scake2)
sca2.grid(column=1, row=2)

scake3 = DoubleVar(value=0)
sca3 = Scale(window, orient=HORIZONTAL, length=500, from_=-0.05, to=0.05, resolution=0.0005, variable=scake3)
sca3.grid(column=1, row=3)

window.mainloop()
