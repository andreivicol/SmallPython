image=input("Photo name: ")
file=input("File name: ")

f=open(image, "rb")
final=open(file, "w")

cnt=0

for line in f.read():
    final.write("{:02x}".format(line))
    cnt+=1
    if cnt==32:
        final.write("\r\n")
        cnt=0