## X64MAYHEM

raw=[]

with open("data","r") as file:
    s=file.readlines()
    raw=s

data=""
for i in raw:
    str=i
    str=str.strip('\n')
    # print(str)
    str=str.split(' ')
    str.pop()
    for i in str:
        r=i[0:2]
        l=i[2:]
        print(r+'-'+l)
        if(r == '00'):
            data+='A'
        elif(r == '10'):
            data+='C'
        elif(r == '01'):
            data+='G'
        elif(r == '11'):
            data+='T'
        if(l == '00'):
            data+='A'
        elif(l == '10'):
            data+='C'
        elif(l == '01'):
            data+='G'
        elif(l == '11'):
            data+='T'

data+='T'

print(data)

with open("dna","w")as file:
    file.write(data)

