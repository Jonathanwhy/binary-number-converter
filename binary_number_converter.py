binarynum = [0,0,0,0]

def DecimalToBinary(num):
    if num>=8:
        binarynum[0]=1
        num=num-8
        #return num
    elif num<8:
        binarynum[0]=0
    if num>=4:
        binarynum[1]=1
        num=num-4
        #return num
    elif num<4:
        binarynum[1]=0
    if num>=2:
        binarynum[2]=1
        num=num-2
    elif num<2:
        binarynum[2]=0
    if num>=1:
        binarynum[3]=1
        num=num-1
    elif num<1:
        binarynum[3]=0
 
    return binarynum
    
print(DecimalToBinary(14))