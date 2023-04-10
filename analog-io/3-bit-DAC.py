import board
import digitalio
import time

step_delay = .1

ASB = digitalio.DigitalInOut(board.GP20)
ASB.direction = digitalio.Direction.OUTPUT

BSB = digitalio.DigitalInOut(board.GP19)
BSB.direction = digitalio.Direction.OUTPUT

CSB = digitalio.DigitalInOut(board.GP18)
CSB.direction = digitalio.Direction.OUTPUT

while True:
    ASB.value = 0
    BSB.value = 0
    CSB.value = 0
    print("binary 0")
    time.sleep(step_delay)
    
    ASB.value = 0
    BSB.value = 0
    CSB.value = 1
    print("binary 1")
    time.sleep(step_delay)
    
    ASB.value = 0
    BSB.value = 1
    CSB.value = 0
    print("binary 2")
    time.sleep(step_delay)
    
    ASB.value = 0
    BSB.value = 1
    CSB.value = 1
    print("binary 3")
    time.sleep(step_delay)
    
    ASB.value = 1
    BSB.value = 0
    CSB.value = 0
    print("binary 4")
    time.sleep(step_delay)
    
    ASB.value = 1
    BSB.value = 0
    CSB.value = 1
    print("binary 5")
    time.sleep(step_delay)
    
    ASB.value = 1
    BSB.value = 1
    CSB.value = 0
    print("binary 6")
    time.sleep(step_delay)
    
    ASB.value = 1
    BSB.value = 1
    CSB.value = 1
    print("binary 7")
    time.sleep(step_delay)
