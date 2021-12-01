a=['python',2.5,20,True]
i=0
while i<len(a):
    if a[i]==20:
        print(a[i])
    i=i+1                # this is universal code. univerasl code means we change code many time in one code. for different output.




# this is non universal code 
i=0
while i<len(a):
    print(a[i])
    break
    i=i+1

i=-1
while i<len(a):
    i=i-1
    print(a[i])
    break