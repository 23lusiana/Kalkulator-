from tkinter import*
window=Tk()

def click(item):
    global expression
    expression+=str(item)
    input_teks.set(expression)

def tmbl_clear(): 
    global expression 
    expression = "" 
    input_teks.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_teks.set(result)
    expression=""

expression=""
input_teks=StringVar()

frame1=Frame(window, bg="pink", width=500, height=300)
frame1.pack()

frame2=Frame(window, bg="red", width=500, height=300)
frame2.pack()

label1=Label(frame1, text="KALKULATOR ", font=("Arial", 9))
label1.pack(pady=20, padx=20)

label3=Label(frame1, text="Lusiana PPLG 1 ",anchor="w",width=50,font=("Arial", 9))
label3.pack(pady=20, padx=20)

label2=Label(frame1, text="", font=("Arial", 9),anchor="e",width=50,textvariable=input_teks)
label2.pack(pady=20, padx=20)

button1=Button(frame2, text="C", width=17, bg="black", fg="white", command =lambda:tmbl_clear())
button1.grid(row=0, column=1, columnspan=2 )

button3=Button(frame2, width=6, text="/", bg="grey", fg="black",command=lambda:click("/") )
button3.grid(row=0, column=3, pady=5, padx=5)

button4=Button(frame2, width=6, text="*", bg="grey", fg="black",command=lambda:click("*") )
button4.grid(row=0, column=4, pady=5, padx=5)

button5=Button(frame2, width=6, text="7", command=lambda:click("7"))
button5.grid(row=1, column=1, pady=5, padx=5)

button6=Button(frame2, width=6, text="8", command=lambda:click("8"))
button6.grid(row=1, column=2, pady=5, padx=5)

button7=Button(frame2, width=6, text="9", command=lambda:click("9"))
button7.grid(row=1, column=3, pady=5, padx=5)

button8=Button(frame2, width=6, text="+", bg="grey", fg="black", command=lambda:click("+"))
button8.grid(row=1, column=4, pady=5, padx=5)

button9=Button(frame2, width=6, text="4",command=lambda:click("4"))
button9.grid(row=2, column=1, pady=5, padx=5)

button10=Button(frame2, width=6, text="5",command=lambda:click("5") )
button10.grid(row=2, column=2, pady=5, padx=5)

button11=Button(frame2, width=6, text="6", command=lambda:click("6"))
button11.grid(row=2, column=3, pady=5, padx=5)

button12=Button(frame2, width=6, text="-",bg="grey", fg="black",command=lambda:click("-") )
button12.grid(row=2, column=4, pady=5, padx=5)

button13=Button(frame2, width=6, text="1", command=lambda:click("1"))
button13.grid(row=3, column=1, pady=5, padx=5)

button14=Button(frame2, width=6, text="2",command=lambda:click("2"))
button14.grid(row=3, column=2, pady=5, padx=5)

button15=Button(frame2, width=6, text="3",command=lambda:click("3") )
button15.grid(row=3, column=3, pady=5, padx=5)

button16=Button(frame2, width=6, text="=", height=3,bg="grey", fg="black", command = lambda:btn_equal())
button16.grid(row=3, rowspan=2, column=4, pady=5, padx=5)

button17=Button(frame2, text="0", width=6, command=lambda:click("0"))
button17.grid(row=4, column=2)

button19=Button(frame2, text="00", width=6, command=lambda:click("00"))
button19.grid(row=4, column=1,  pady=5, padx=5)

button18=Button(frame2, width=6, text=".",bg="grey", fg="black",command=lambda:click(".") )
button18.grid(row=4, column=3, pady=5, padx=5)


window.mainloop()