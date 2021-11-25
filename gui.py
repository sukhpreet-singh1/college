from tkinter import Radiobutton, Tk, Canvas, Entry, Text, Button, PhotoImage
import string
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfile


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def popupmsg(msg):
    NORM_FONT = ("Helvetica", 10)
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


main_width = 1000
main_height = 600


window = Tk()

window.geometry(f'{main_width}x{main_height}')
window.configure(bg="#1C1D1F")
q = []
w = []
e = []
r = []
t = []
data_fromcsv = None
t1 = None
t2 = None
t3 = None
t4 = None
t5 = None
a1 = None
a2 = None
a3 = None
a4 = None
a5 = None
am1 = None
am2 = None
am3 = None
am4 = None
am5 = None


def page1(window):
    canvas = Canvas(
        window,
        bg="#1C1D1F",
        height=main_height,
        width=main_width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        main_width//5,
        main_height,
        fill="#282828",
        outline="")

    canvas.create_text(90, 40, text="", fill="#FFF", font=("Calibri", 18))
    title1 = canvas.create_text(
        main_width/2+100, 40, text="Assets Account", fill="#FFF", font=("Calibri", 45))
    serial_number = canvas.create_text(
        main_width/2-180, 180, text="S.No", fill="#FFF", font=("Calibri", 18))
    temp = canvas.create_text(main_width/2-40, 180,
                              text="Assets", fill="#FFF", font=("Calibri", 18))
    amount = canvas.create_text(
        main_width/2+330, 180, text="Amount", fill="#FFF", font=("Calibri", 18))

    def cal_var_amount():
        if len(am5.get()) != 0:
            canvas.itemconfig(
                toal_amount_all, text=f'Total Amount {np.sum(list(map(int,[ am1.get(),am2.get(),am3.get(),am4.get(),am5.get()])))}')

    toal_amount_all = canvas.create_text(
        main_width/2+330, 480, text=f'Total Amount ', fill="#FFF", font=("Calibri", 18))
    button_total_amount = Button(window, text="Calculate Total Amount", foreground="#FFF", command=cal_var_amount,
                                 width=25, height=2, activebackground="#33B5E5", background="#0A84FF")
    button_window = canvas.create_window(
        main_width/2+330, 550, window=button_total_amount)
    var = tk.IntVar(name="s")
    var.set(1)

    def sel():
        global q, w, e, r, t
        if var.get() == 3:
            q = []
            w = []
            e = []
            r = []
            canvas.itemconfig(temp, text="Principal")
            canvas.itemconfigure(title1, text="Profilt and Loss Account")
        if var.get() == 1:
            q = []
            w = []
            e = []
            r = []
            canvas.itemconfig(temp, text="Assets")
            canvas.itemconfigure(title1, text="Assets Account")
        if var.get() == 2:
            q = []
            w = []
            e = []
            r = []
            canvas.itemconfig(temp, text="Liability")
            canvas.itemconfigure(title1, text="Liability Account")

    canvas.create_text(100, 70, text="1.Enter Your Data\n2.Click on Generate\n3.Click on load data",
                       fill="#FFF", font=("Calibri", 10))
    r1 = Radiobutton(window, bg="#282828", text='Assets Account', border=1, activebackground="#282828",
                     variable=var, value=1, command=sel)
    r2 = Radiobutton(window, bg="#282828", text='Liability Account',
                     variable=var, value=2, command=sel, border=1, activebackground="#282828")
    r3 = Radiobutton(window, bg="#282828", text='Profit and Loss Account',
                     variable=var, value=3, command=sel, border=1, activebackground="#282828")
    canvas.create_window(57, 160, window=r1)
    canvas.create_window(60, 180, window=r2)
    canvas.create_window(80, 200, window=r3)

    ##############
    ######SN0###########################################################################
    global t1, t2, t3, t4, t5, a1, a2, a3, a4, a5, am1, am2, am3, am4, am5
    t1 = Entry()
    t2 = Entry()
    t3 = Entry()
    t4 = Entry()
    t5 = Entry()
    canvas.create_window(main_width/2-150, 220, window=t1)
    canvas.create_window(main_width/2-150, 240, window=t2)
    canvas.create_window(main_width/2-150, 260, window=t3)
    canvas.create_window(main_width/2-150, 280, window=t4)
    canvas.create_window(main_width/2-150, 300, window=t5)
    a1 = Entry(width=60)
    a2 = Entry(width=60)
    a3 = Entry(width=60)
    a4 = Entry(width=60)
    a5 = Entry(width=60)
    canvas.create_window(main_width/2+95, 220, window=a1)
    canvas.create_window(main_width/2+95, 240, window=a2)
    canvas.create_window(main_width/2+95, 260, window=a3)
    canvas.create_window(main_width/2+95, 280, window=a4)
    canvas.create_window(main_width/2+95, 300, window=a5)

    am1 = Entry()
    am2 = Entry()
    am3 = Entry()
    am4 = Entry()
    am5 = Entry()

    canvas.create_window(main_width/2+340, 220, window=am1)
    canvas.create_window(main_width/2+340, 240, window=am2)
    canvas.create_window(main_width/2+340, 260, window=am3)
    canvas.create_window(main_width/2+340, 280, window=am4)
    canvas.create_window(main_width/2+340, 300, window=am5)
    ##############
    button_load = Button(window, text="Load Data", foreground="#FFF", command=openfile,
                         width=20, height=2, activebackground="#33B5E5", background="#0A84FF")
    button_window = canvas.create_window(100, 510, window=button_load)
    button = Button(window, text="Generate", foreground="#FFF", command=changepage,
                    width=20, height=2, activebackground="#33B5E5", background="#0A84FF")
    button_window = canvas.create_window(100, 570, window=button)


def openfile():
    global data_fromcsv, t1, t2, t3, t4, t5, a1, a2, a3, a4, a5, am1, am2, am3, am4, am5
    filename = askopenfile(mode='r', filetypes=[
                           ('Comma-separated values', '*.csv')])
    data_fromcsv = pd.read_csv(filename)
    t1.delete(0, 'end')
    t2.delete(0, 'end')
    t3.delete(0, 'end')
    t4.delete(0, 'end')
    t5.delete(0, 'end')
    t1.insert(0, data_fromcsv["S.No"][0])
    t2.insert(0, data_fromcsv["S.No"][1])
    t3.insert(0, data_fromcsv["S.No"][2])
    t4.insert(0, data_fromcsv["S.No"][3])
    t5.insert(0, data_fromcsv["S.No"][4])
    a1.delete(0, 'end')
    a2.delete(0, 'end')
    a3.delete(0, 'end')
    a4.delete(0, 'end')
    a5.delete(0, 'end')
    a1.insert(0, data_fromcsv["Assets"][0])
    a2.insert(0, data_fromcsv["Assets"][1])
    a3.insert(0, data_fromcsv["Assets"][2])
    a4.insert(0, data_fromcsv["Assets"][3])
    a5.insert(0, data_fromcsv["Assets"][4])
    am1.delete(0, 'end')
    am2.delete(0, 'end')
    am3.delete(0, 'end')
    am4.delete(0, 'end')
    am5.delete(0, 'end')
    am1.insert(0, data_fromcsv["Amount"][0])
    am2.insert(0, data_fromcsv["Amount"][1])
    am3.insert(0, data_fromcsv["Amount"][2])
    am4.insert(0, data_fromcsv["Amount"][3])
    am5.insert(0, data_fromcsv["Amount"][4])


def page2(window):
    global dataLoad
    canvas = Canvas(
        window,
        bg="#1C1D1F",
        height=main_height,
        width=main_width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    ##############
    sample = {"S.No": q[::-1],
              'Assets': w[::-1],
              'Amount': e[::-1],
              }

    df = pd.DataFrame(sample)
    cols = list(df.columns)
    print(df['Amount'].values)
    total_amount = np.sum(list(map(int, df['Amount'].values)))

    def save_to_csv():
        global q, w, e, r
        q = []
        w = []
        e = []
        r = []

        df['total_amount'] = [0, 0, 0, 0, total_amount]
        df.to_csv(f'ALA-{id_generator()}.csv', index=False)
        popupmsg("File saved")

    style = ttk.Style(window)
    style.theme_use("default")
    style.configure("Treeview", background="#1C1D1F",
                    fieldbackground="#1C1D1F", foreground="white")
    tree = ttk.Treeview(window, height=5)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')

    for index, row in df.iterrows():
        tree.insert("", 0, text=index, values=list(row))

    canvas.create_window(500, 210, window=tree)
    canvas.create_text(
        700, 370, text=f'Total Amount {total_amount}', fill="#FFF", font=("Calibri", 28))

    button = Button(window, text="Back", foreground="#FFF", command=changepage,
                    width=15, height=2, activebackground="#33B5E5", background="red")
    button_window = canvas.create_window(900, 570, window=button)
    button_tocsv = Button(window, text="Save to csv", foreground="#FFF", command=save_to_csv,
                          width=15, height=2, activebackground="#33B5E5", background="#0A84FF")
    button_window = canvas.create_window(100, 570, window=button_tocsv)


def changepage():
    global pagenum, window, q, w, e, r, t1, t2, t3, t4, t5, a1, a2, a3, a4, a5, am1, am2, am3, am4, am5
    # for widget in window.winfo_children():
    #     widget.destroy()
    if pagenum == 1:
        ############addData##########
        q.extend([t1.get(), t2.get(), t3.get(), t4.get(), t5.get()])
        w.extend([a1.get(), a2.get(), a3.get(), a4.get(), a5.get()])
        e.extend([am1.get(), am2.get(), am3.get(), am4.get(), am5.get()])
        if len(am5.get()) != 0:
            page2(window)
            pagenum = 2
        else:
            popupmsg("Enter Values")
    else:
        page1(window)
        q = []
        w = []
        e = []
        r = []
        t = []
        pagenum = 1


pagenum = 1
page1(window)
window.resizable(False, False)
window.mainloop()
