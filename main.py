def EliminarPrograma():
    global Programa
    Programa = []


def on_received_number(receivedNumber):
    if esAvanzar(receivedNumber) or esGirarDerecha(receivedNumber):
        Programa.append(receivedNumber)
    elif receivedNumber == BORRAR:
        EliminarPrograma()
    else:
        Ejecutar()
radio.on_received_number(on_received_number)


def esAvanzar(instruccion: number):
    return instruccion == AVANZAR
def esGirarDerecha(instruccion2: number):
    return instruccion2 == GIRAR_DERECHA
def GirarDerecha():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 80)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 80)
    basic.pause(320)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.motor_stop(maqueen.Motors.ALL)
def Ejecutar():
    for instruccion3 in Programa:
        if esAvanzar(instruccion3):
            Avanzar()
        else:
            GirarDerecha()
def Avanzar():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
Programa: List[number] = []
BORRAR = 0
GIRAR_DERECHA = 0
AVANZAR = 0
AVANZAR = 0
GIRAR_DERECHA = 1
BORRAR = 2
EJECUTAR = 3
Programa = []
radio.set_group(1)




