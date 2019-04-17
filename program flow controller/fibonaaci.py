first=-1
second=1
for j in range(0,9):
        j=first+second
        first=second
        second=j
        print(j,end='\t')