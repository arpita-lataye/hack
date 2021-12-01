import tkinter
from tkinter import *
import random

questions_list=[
    'Which country has 11 official languages?',
    'How many bytes are equal to 1 MB (megabyte)?',
    'Nairobi is the capital of which country?',
    'Disease scurvy is caused due to lack of ____',
    'Traffic signal of which colour ask us to stop ?',
    'Which of these is River ?',
    'Which state has the "Longest Coastline" in india ?',
    'Which of these month have 31 days',
    'Who was the leader of the "Indian Natinal Army"?',
    'What is used to take "Temperature of Body"?',]

answers_list=[
    ['(A)India','(B)Canada','(C)USA','(D)South Africa'],
    ['(A)1024 KB','(B)1024 GB','(C)1004 KB','(D)1024 TB'],
    ['(A)Zimbabwe','(B)Kenya','(C)Ugenda','(D)SRi Lanka'],
    ['(A)Vitamin A','(B)vitamin C','(C)Vitamin D','(D)Vitamin B12'],
    ['(A)Green','(B)Red','(C)Yellow','(D)Blue'],
    ['(A)Yamuna','(B)Bhramaputra','(C)Ganga','(D)All of these'],
    ['(A)Maharashtra','(B)Tamil Nadu','(C)Karnataka','(D)Gujarat'],
    ['(A)October','(B)June','(C)February','(D)April'],
    ['(A)Mahatma Gandhi','(B)Subhash Chandra Bose','(C) Sardar Vallabhai Patel','(D)Bhagat Singh'],
    ['(A)Thermos','(B)Scale','(C)Speedometer','(D)Thermometer'],
]

# answers=['D','A','B','B','B','D','D','A','B','D']
answers=[3,0,1,1,1,3,3,0,1,3]


user_ans=[]

indexes=[]
def gen():
    global indexes
    while (len(indexes)<5):
        x= random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background='#ffffff',
        border=0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext= Label(
        root,
        font=('freeserif,italic',20),
        background='#ffffff'
    )
    labelresulttext.pack()
    if score>=20:
        img=PhotoImage(file='/home/oem/Downloads/great1.png')
        labelimage.configure(image=img)
        labelimage.image= img
        labelresulttext.configure(text='You Are Excellent !!')
    elif score>=10 and score <20:
        img=PhotoImage(file='/home/oem/Downloads/ok.png')
        labelimage.configure(image=img)
        labelimage.image= img
        labelresulttext.configure(text='You Can Be Better !!')
    else:
        img=PhotoImage(file='/home/oem/Downloads/bad.png')
        labelimage.configure(image=img)
        labelimage.image= img
        labelresulttext.configure(text='You Should Work Hard !!')


def calc():
    global indexes,user_ans,answers
    x=0
    score=0
    for i in indexes:
        if user_ans[x]==answers[i]:
            score=score+5
        x=x+1
    print(score)
    showresult(score)

ques=1
def selected():
    global radiovar, user_ans
    global lblquestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    if ques<5:
        lblquestion.config(text=questions_list[indexes[ques]])
        r1['text']=answers_list[indexes[ques]][0]
        r2['text']=answers_list[indexes[ques]][1]
        r3['text']=answers_list[indexes[ques]][2]
        r4['text']=answers_list[indexes[ques]][3]
        ques+=1 
    else:
        print(indexes)
        print(user_ans)
        calc()


def startquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion=Label(
        root,
        text=questions_list[indexes[0]],
        font=('norasi,obique',16),
        width=500,
        justify='center',
        wraplength= 400,
        background='#ffffff'
    )
    lblquestion.pack(pady=(100,30))
    
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    
    r1=Radiobutton(
        root,
        text=answers_list[indexes[0]][0],
        font=('norasic italic',12),
        value=0,
        variable=radiovar,
        command = selected,
        background='#ffffff'
    )
    r1.pack(pady=5)

    r2=Radiobutton(
        root,text=answers_list[indexes[0]][1],
        font=('norasic italic',12),
        value=1,
        variable=radiovar,
        command = selected,
        background='#ffffff'
    )
    r2.pack(pady=5)

    r3=Radiobutton(
        root,text=answers_list[indexes[0]][2],
        font=('norasic italic',12),
        value=2,
        variable=radiovar,
        command = selected,
        background='#ffffff'
    )
    r3.pack(pady=5)

    r4=Radiobutton(
        root,text=answers_list[indexes[0]][3],
        font=('norasic italic',12),
        value=3,
        variable=radiovar,
        command = selected,
        background='#ffffff'
    )
    r4.pack(pady=5)


def startispressed():
    labelimage.destroy()
    labletext.destroy()
    lblInstruction.destroy()
    lblrules.destroy()
    btnstart.destroy()
    gen()
    startquiz()

root=Tk()
root.title('kaun banega carorepati')
# label=Label(root,text='kbc',bg='red',fg='black',font='aakar,midium,40')
root.geometry('700x800')
root.config(background='#ffffff')
root.resizable(0,0)

img1 = PhotoImage(file="/home/oem/Downloads/images.png")


labelimage=Label(
    root,image=img1,
    background='#ffffff'
)
labelimage.pack(pady=(40,0))

labletext = Label(
    root,
    text='Welcome In KBC Quize',
    font=('anjalioldlipi',24,'bold'),
    background='#ffffff'
)
labletext.pack(pady=(0,40))

img2=PhotoImage(file='/home/oem/Downloads/download.png')

btnstart=Button(
    root,image = img2,
    relief=GROOVE,
    border=4,
    background='#ffffff',
    command=startispressed,
)
btnstart.pack()

lblInstruction = Label(
    root,text = 'read the rules and\nclick start once you are ready',
    background='#ffffff',
    font=('freemono',14,'bold'),
    justify='center',
)
lblInstruction.pack(pady=(10,70))

lblrules=Label(
    root,text="this quize contains 10 questions\nyou will get 20 seconds to solve a question\nonce you select a correct answer button that will be a final choice\n hence think before you select.",
    width=60,
    font=('numbus mono ps',14),
    background='black',
    foreground='yellow'
)
lblrules.pack(pady=(10,0))


root.mainloop()

