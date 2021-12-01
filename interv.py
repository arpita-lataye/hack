a=[1,2,3,[4,5,6],7,8,[9]]
i=0
b=[]
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
# print(sum)

i=0
sum=0
while i<len(b):
    sum=sum+b[i]
    i=i+1
# print(sum)


# sum=0
# for i in range(len(a)):
#     n=a[i]
#     if type(n)==list:
#         for j in range(len(n)):
#             sum=sum+n[j]
#     else:
#         sum=sum+n
# print(sum)



a=[1,2,3,[4,5,6],7,8,[9]]
sum=0
for i in range(len( a)):
    if type(a[i])==list:
        for j in range(len(a[i])):
            sum=sum+a[i][j]
    else:
        sum=sum+a[i]
print(sum)