q1='''is python case sensitive when dealing with indentifiers?
a.yes
b.no
c.machine dependent
d.none'''
q2='''which of the following is not a keyword?
a.eval
b.assert
c.local
d.pass'''
q3='''which one is the floor division?
a./
b.//
c.%
d.none'''
q4='''what is the output of this 3*1**3?
a.27
b.9
c.3
d.1'''
q5='''"a"+"bc"=?
a.a
b.bc
c.bca
d.abc'''

questions={q1:'a',q2:'a',q3:'b',q4:'c',q5:'d'}

name=input('enter your name:')
print('hello',name,'welcome to the quize world')

score=0
for i in questions:
    print()
    print(i)
    flag1=input('do you want ot skip this question (yes/no):')
    if flag1=='yes':
        continue
    ans=input('enter the answer (a/b/c/d):')
    if ans==questions[i]:
        print('correct answer, you got 1 point')
        score=score+1
        print('current score is:',score)
    else:
        print('wrong answer ,you lost 1 point')
        score=score-1
        print('current score is:',score)
    flag2=input('do you want to quite (yes/no):') 
    if flag2=='yes':
        break
print('final score is:',score)