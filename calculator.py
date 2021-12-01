import tkinter
from tkinter import*


root=tkinter.Tk()
root.geometry('250x400+300+300')
root.resizable(0,0)
root.title('calculator')

lbl=Label(
    root,
    text= 'Label',
    anchor = SE,
    font=('aakar medium',20)
)
lbl.pack(expand= True,fill ='both')


btnrow1=Frame(root,bg='#000000')
btnrow1.pack(expand=True,fill='both',)

btnrow2 = Frame(root)
btnrow2.pack(expand=True,fill='both')

btnrow3 = Frame(root)
btnrow3.pack(expand=True,fill='both')

btnrow4 = Frame(root)
btnrow4.pack(expand=True,fill='both')

btn1= Button(
    btnrow1,
    text= '7',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn1.pack(side=LEFT, expand= True, fill='both',)

btn2= Button(
    btnrow1,
    text= '8',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn2.pack(side=LEFT, expand= True, fill='both',)

btn3= Button(
    btnrow1,
    text= '9',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn3.pack(side=LEFT, expand= True, fill='both',)

btn4= Button(
    btnrow1,
    text= '/',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn4.pack(side=LEFT, expand= True, fill='both',)



btn1= Button(
    btnrow2,
    text= '4',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn1.pack(side=LEFT, expand= True, fill='both',)

btn2= Button(
    btnrow2,
    text= '5',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn2.pack(side=LEFT, expand= True, fill='both',)

btn3= Button(
    btnrow2,
    text= '6',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn3.pack(side=LEFT, expand= True, fill='both',)

btn4= Button(
    btnrow2,
    text= 'X',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn4.pack(side=LEFT, expand= True, fill='both',)



btn1= Button(
    btnrow3,
    text= '1',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn1.pack(side=LEFT, expand= True, fill='both',)

btn2= Button(
    btnrow3,
    text= '2',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn2.pack(side=LEFT, expand= True, fill='both',)

btn3= Button(
    btnrow3,
    text= '3',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn3.pack(side=LEFT, expand= True, fill='both',)

btn4= Button(
    btnrow3,
    text= '-',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn4.pack(side=LEFT, expand= True, fill='both',)



btn1= Button(
    btnrow4,
    text= 'C',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn1.pack(side=LEFT, expand= True, fill='both',)


btn2= Button(
    btnrow4,
    text= '0',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn2.pack(side=LEFT, expand= True, fill='both',)

btn3= Button(
    btnrow4,
    text= '=',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn3.pack(side=LEFT, expand= True, fill='both',)

btn4= Button(
    btnrow4,
    text= '+',
    font= ('C059 Bold',22),
    relief=GROOVE,
    border=0,
)
btn4.pack(side=LEFT, expand= True, fill='both',)


root.mainloop()