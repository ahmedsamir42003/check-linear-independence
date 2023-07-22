def postition(A):
   for i in range(x):
        if A[i][i] != 0 and A[i][i] == 1:
            pass
        else:
            for j in range(i+1,len(A)):
                if A[j][i] == 1:
                    li=A[j]
                    A[j]=A[i]
                    A[i]=li
                    break
            else:
                for j in range(i+1,len(A)):
                    if A[j][i] != 0:
                       li=A[j]
                       A[j]=A[i]
                       A[i]=li
   return(A)

n=int(input('Please enter the number of vectors you would like to check for linear dependence among them'))

A=[]
for i in range(n):
    row=[]
    row=list(map(int,input(f'enter the {i+1} vector').split()))
    A.append(row)


mx=-1
for i in range(len(A)):
    if len(A[i]) > mx:
        mx=len(A[i])

for i in range(len(A)):
    if len(A[i])!=mx:
        z = mx - len(A[i])
        for j in range(z):
            A[i].append(0)

x=min(len(A[i]),len(A))



for i in range(x):
    A=postition(A)
    for j in range(i+1,len(A)):
        if A[j][i]==0:
            continue
        update=-(A[j][i]/A[i][i])
        li=[update * x for x in A[i]]
        A[j]=[x+y for x,y  in zip(li,A[j])]

q=0
for i in range(len(A)):
    if sum(A[i]) != 0:
        q+=1

if q<len(A) :
    print('linearly dependent')
else:
    print('linearly independent')