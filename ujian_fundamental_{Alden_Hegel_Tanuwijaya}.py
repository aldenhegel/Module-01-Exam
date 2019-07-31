# soal1
def calculate_years(principal, interest, tax, desired):
    z=0
    summoney=principal
    while(summoney<desired):
        interestmoney=summoney*interest 
        taxmoney=interestmoney*tax
        summoney=summoney*(1+interest)-taxmoney
        z+=1
    print(z)

# soal2
def expandedform(num):
    k=''
    y=str(num)
    for i,index in zip(range(len(str(num))-1,0,-1),range(len(str(num))-1)):
        if y[index]!='0':
            x=10**i
            a=x*int(y[index])
            k+=str(a)+'+'
    k+=y[-1]
    print(k)

# soal3
def tower_builder(n_floors, block_size):
    w,h=block_size
    b=w+(w*(n_floors-1)*2)
    for i in range(n_floors-1,-1,-1):
        for j in range(h):
            z=''
            for k in range(1,b+1):
                if k>i*w and k<=b-(i*w):
                    z+='*'
                else:
                    z+=' '
            print(z)