from time import sleep
from itertools import cycle

# other parts unchanged, though it could still be cleaned up, too.

#identical in behavior to the while(True) loop
for x in cycle(range(8)):
   digits = [int(y) for y in (3-len(bin(x)[2:]) * '0' + bin(x)[2:]]
   ASB.value, BSB.value, CSB.value = digits[-3:]
   print("binary {}".format(x))
   sleep(SLEEP_DELAY)
