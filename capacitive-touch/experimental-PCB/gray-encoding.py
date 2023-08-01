# Still WIP - JSCook 7/31/2023

import board
import touchio
import time

# Gray Encoder --> pins 13, 12, 11, 10

graybit1 = touchio.TouchIn(board.GP13)
graybit2 = touchio.TouchIn(board.GP12)
graybit3 = touchio.TouchIn(board.GP11)
graybit4 = touchio.TouchIn(board.GP10)

graybit1.threshold = 1800
graybit2.threshold = 1500
graybit3.threshold = 1500
graybit4.threshold = 1500

grayIndex = {0b0000:0, 0b0001:1, 0b0011:2, 0b0010:3, 0b0110:4, \
0b0111:5, 0b0101:6, 0b0100:7, 0b1100:8, 0b1101:9, 0b1111:10, \
0b1110:11, 0b1010:12, 0b1011:13, 0b1001:14, 0b1000:15}

while True:

    index1 = (
    graybit1.value << 0
    | graybit2.value << 1
    | graybit3.value << 2
    | graybit4.value << 3
    )
    print("bit1 raw ", graybit1.raw_value, "bit2 raw ", graybit2.raw_value, \
    "bit3 raw ", graybit3.raw_value, "bit4 raw ", graybit4.raw_value)
    print("index1 ", bin(index1), "Gray number ", grayIndex[index1])
    time.sleep(.1)
    # print("Gray number ", grayIndex[index1])
    # time.sleep(.1)
