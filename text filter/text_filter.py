fileName=input("Insert file name: ")
finalFile=input("File to write to: ")

file=open(fileName, "rb")
log=open(finalFile,"w")

char=''
cnt=0
charCnt=1

for letter in file.readline():
    if char=='':
        char=letter
    if letter==char:
        cnt+=1
    else:
        log.write(f'The character {charCnt}: {"{:02x} ".format(char)} appears {cnt} times\n')
        cnt=1
        char=letter
        charCnt+=1