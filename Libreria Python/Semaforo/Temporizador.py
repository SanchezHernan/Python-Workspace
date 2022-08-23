from time import sleep

def temporizar(tiempo):
    while tiempo > -1:
        tiempo-=1
        sleep(1)
