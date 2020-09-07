import os
import math

f=open("photo.jpg", "rb")

firstPacket=''
secondPacket=''
memPacket=''
cnt=0

size=os.stat("C:/Users/Andrei/Desktop/PythonProjects/file_compare/photo.jpg")
fileSize= math.ceil(size.st_size / 1460)

for i in range(0, fileSize-1):
    buff=f.read(1460)
    secondPacket=''
    for j in buff:
        secondPacket+="{:02x}".format(j)
    if(secondPacket==firstPacket):
        print(f'Packet {i+1} identical with {i}')
        print(secondPacket)
    firstPacket=secondPacket