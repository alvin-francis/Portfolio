import tkinter as tk

class MethodOne:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="How to use this Calculator", command=self.instructions)
        self.helpmenu.add_command(label="How to manually compute", command=self.manual)

        self.aboutmenu=tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=self.aboutmenu)
        self.aboutmenu.add_command(label='Thank you!', command=self.thankyou)


        self.root.config(menu=self.menubar)


        self.root.title("Method 1")

        self.root.geometry('300x300')
        self.root.resizable(False, False)

        self.label1 = tk.Label(self.root, text = 'Method 1', font = ('Arial Black', 20))
        self.label1.pack(padx = 10, pady= 10)

        self.label2 = tk.Label(self.root, text = 'Simple cooling capacity estimation using area only', font = ("Arial", 8))
        self.label2.pack(padx=10,pady=5)

        self.description = tk.Label(self.root, text='Enter Area (square meters)', font = ('Arial', 7))
        self.description.pack()

        #self.m1_frame = tk.Frame(self.root)
        #di pa tapos tooooooooooooooooooooooo!!!!!!!!!!!!!!!!!

        self.area = tk.Entry(self.root)
        self.area.pack(padx=10, pady=10)

        self.btn = tk.Button(self.root, text = 'Calculate', command = self.calculate)
        self.btn.pack()

        self.output = tk.Label(self.root, text = 'Click calculate for the result!', font = ('Arial', 8), wraplength=150, justify="left")
        self.output.pack()

        self.root.mainloop()

    def instructions(self):
        try:
            self.inst_frame.destroy()
        except:
            pass
        try:
            self.manual_frame.destroy()
        except:
            pass
        try:
            self.thankyou_frame.destroy()
        except:
            pass
        manualtext='1.)Enter the floor area in the text box.\n2.)Choose your units (square meters or square foot).\n3.)Click the Calculate button'
        self.inst_frame=tk.Frame(self.root)
        self.inst_frame.rowconfigure(0, weight=4)
        manual_label = tk.Label(self.inst_frame, text=manualtext, font=('Times', 10))
        manual_label.grid(row=0, sticky='news', pady=10, padx=10)
        manual_button = tk.Button(self.inst_frame, text='OK', command=self.tomain, width=10)
        manual_button.grid(row=1, sticky='ns')
        self.inst_frame.place(x=0, y=0, anchor='nw', height=250)
        self.inst_frame.focus_set()

    def manual(self):
        try:
            self.inst_frame.destroy()
        except:
            pass
        try:
            self.manual_frame.destroy()
        except:
            pass
        try:
            self.thankyou_frame.destroy()
        except:
            pass
        manualtext='Get the floor area of a room, make sure it is in square foot. Multiply it by 80. (80 is the value of a constant know as "heat factor"). You will get BTU/hr. Divide this number by 9500 to get the cooling capacity in HP!'
        self.manual_frame=tk.Frame(self.root)
        self.manual_frame.rowconfigure(0, weight=4)
        manual_label = tk.Label(self.manual_frame, text=manualtext, wraplength=300, justify ='center', font = ('Times', 10))
        manual_label.grid(row=0,sticky='news',pady=10)
        manual_button = tk.Button(self.manual_frame,text='OK', command = self.tomain, width = 10)
        manual_button.grid(row=1,sticky='ns')
        self.manual_frame.place(x=0, y=0, anchor='nw',height=250)
        self.manual_frame.focus_set()

    def thankyou(self):
        try:
            self.inst_frame.destroy()
        except:
            pass
        try:
            self.manual_frame.destroy()
        except:
            pass
        try:
            self.thankyou_frame.destroy()
        except:
            pass
        manualtext = "Thank you for using my calculator! If you'd like to support me, here's my GCASH:\n0917 505 7946"
        self.thankyou_frame = tk.Frame(self.root)
        self.thankyou_frame.rowconfigure(0, weight=4)
        manual_label = tk.Label(self.thankyou_frame, text=manualtext, wraplength=300, justify='center', font=('Times', 10))
        manual_label.grid(row=0, sticky='news', pady=10, padx=12)
        manual_button = tk.Button(self.thankyou_frame, text='OK', command=self.tomain, width=10)
        manual_button.grid(row=1, sticky='ns')
        self.thankyou_frame.place(x=0, y=0, anchor='nw', height=250)
        self.thankyou_frame.focus_set()



    def tomain(self):
        try:
            self.inst_frame.destroy()
        except:
            pass
        try:
            self.manual_frame.destroy()
        except:
            pass
        try:
            self.thankyou_frame.destroy()
        except:
            pass

    def calculate(self):
        try:
            area=float(self.area.get())
            cap_btu = 80 * area * 10.764
            computed_hp = cap_btu / 9500

            units = 1
            if computed_hp > 4:
                while computed_hp > 4:
                    computed_hp = computed_hp / 2
                    units += 1
            else:
                pass
            # Make a list of standard ac unit hp ratings in HP and check the computed ratings against it.
            stdhplist = [0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]

            # Below code will make sure that the returned value is the nearest value in the list.
            hp = min(stdhplist, key=lambda x: abs(x - computed_hp))
            # If the nearest value of the list is lower than the computed, we must make sure that the returned value is higher
            if hp < computed_hp:
                z = stdhplist.index(hp)
                adjust = z + 1
                cap_hp = stdhplist[adjust]
            else:
                cap_hp = hp
            # divide the btu capacity requirement by amount of units
            cap_btu = round(cap_btu / units, 0)

            if units > 1:
                start_statement = ' units of aircon with capacity of '
                end_statement = ' each.'
            else:
                start_statement = ' unit of aircon with a capacity of '
                end_statement = '.'

            self.output.config(text='We recommend ' + str(units) + start_statement + str(cap_btu) + ' BTU/Hr or ' + str(
                cap_hp) + ' HP' + end_statement)
        except:
            self.output.config(text='Please enter numbers only!')

MethodOne()