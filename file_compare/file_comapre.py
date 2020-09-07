# file1=input("f1: ")
# file2=input("f2: ")

correct=open("jpg1.txt", 'r').readlines()
wrong=open("jpg2.txt",'r').readlines()

line=0
cnt=0
coord={}
mem=0
seq=''
end=False


for pair in zip(correct, wrong):
    for char in pair[0]:
        try:
            if char==pair[1][cnt-1]:
                cnt+=1
                end=False
                if mem!=0 and end==False:
                    coord[str(line)]=mem
                    mem=0
            else:
                cnt+=1
                if mem==0:
                    end=True
                    coord[str(line)]=mem
                seq+=str(char)
        except:
            IndexError
        if cnt==64:
            cnt=0
            line+=1


# print(coord)
#print(seq)
