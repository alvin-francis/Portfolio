import tkinter as tk
import math

class MethodTwo():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Method 2")

        self.menubar = tk.Menu(self.root)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="How to use this Calculator", command=self.instructions)
        self.helpmenu.add_command(label="How to manually compute", command=self.manual)

        self.aboutmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=self.aboutmenu)
        self.aboutmenu.add_command(label='Thank you!', command=self.thankyou)

        self.root.config(menu=self.menubar)

        self.root.geometry('350x350')
        self.root.resizable(False,False)

        self.header=tk.Label(self.root, text = "METHOD 2", font = ('Arial Black', 20))
        self.header.pack()

        self.description=tk.Label(self.root, text ='Simple cooling capacity estimation using area and height', font = ('Arial', 8), justify ='center')
        self.description.pack(pady=10)

        self.parameter_frame = tk.Frame(self.root)
        self.parameter_frame.columnconfigure(0, weight = 1)
        self.parameter_frame.columnconfigure(1, weight=1)
        self.parameter_frame.columnconfigure(2, weight=1)

        self.area_desc=tk.Label(self.parameter_frame, text = "Floor Area", font=('Arial',8),wraplength=100, justify='left')
        self.area_desc.grid(row=0,column=0,sticky='w',pady=5)

        self.area_entry = tk.Entry(self.parameter_frame)
        self.area_entry.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10,pady=5)

        self.option1 = ['Square Meters', 'Square Feet']
        self.option2 = ['Meters', 'Feet']
        self.choice1 = tk.StringVar()
        self.choice2 = tk.StringVar()
        self.choice1.set("Square Meters")
        self.choice2.set("Meters")

        self.dropdown1 = tk.OptionMenu(self.parameter_frame, self.choice1, *self.option1)
        self.dropdown1.grid(row=0, column=2, sticky=tk.E + tk.W)

        self.height_desc = tk.Label(self.parameter_frame, text="Floor Height", font=('Arial', 8), wraplength=50,justify='left')
        self.height_desc.grid(row=1, column=0,sticky='w',pady=5)

        self.height_entry = tk.Entry(self.parameter_frame)
        self.height_entry.grid(row=1, column=1, sticky=tk.E+tk.W, padx=10,pady=5)

        self.dropdown2 = tk.OptionMenu(self.parameter_frame, self.choice2, *self.option2)
        self.dropdown2.grid(row=1, column=2, sticky=tk.E + tk.W)

        self.people_desc = tk.Label(self.parameter_frame, text="How many people reside in this room?", font=('Arial', 8), wraplength=100,justify='left')
        self.people_desc.grid(row=2, column=0,sticky='w',pady=5)

        self.people_entry = tk.Entry(self.parameter_frame)
        self.people_entry.grid(row=2, column=1, sticky='w', padx=10,pady=5)

        self.check_state=tk.IntVar()

        self.checker=tk.Checkbutton(self.parameter_frame, text='The room is in the ground floor.', wraplength=100, font =('Arial', 8), justify='left', variable=self.check_state)
        self.checker.grid(row = 3, column = 0, pady=10, sticky = 'w')

        self.btn=tk.Button(self.parameter_frame, text = 'Calculate', command=self.calculate)
        self.btn.grid(row=4, column = 0, sticky = tk.W+tk.E,padx=10)

        self.output=tk.Label(self.parameter_frame,text = 'Click calculate for the results!', font = ('Arial', 8), wraplength=120, justify = 'left')
        self.output.grid(row = 3, column = 1, rowspan=2, columnspan=2)

        self.parameter_frame.pack(fill='x')


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
        manualtext='1.)Enter the floor area and floor height in the text box.\n\n2.)Choose your units (square meters or square foot).\n\n3.) Input how many people reside in this building.\n\n4.) Identify if the building is on the main (ground) floor or not.\n\n5.)Click the Calculate button'
        self.inst_frame=tk.Frame(self.root)
        self.inst_frame.rowconfigure(0, weight=4)
        manual_label = tk.Label(self.inst_frame, text=manualtext, font=('Times', 10), wraplength = 350, justify='left')
        manual_label.grid(row=0, sticky='news', pady=10)
        manual_button = tk.Button(self.inst_frame, text='OK', command=self.tomain, width=10)
        manual_button.grid(row=1, sticky='ns')
        self.inst_frame.place(x=0, y=0, anchor='nw', height=320,width=350)
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
        manualtext='1.)Get the floor area of a room, make sure it is in square foot.\n2.) Get the heat factor which depends on the room location - If the room is on the main floor, the factor is 40. Otherwise, the factor is 50.\n3.) Get the height factor - For each foot above 8 ft of ceiling, add 1000 BTU/hr. \n4.) Identify how many people normally reside in the room. Each person contributes 600 BTU/Hr.'
        manualtext2='Use the formula:\n\n(Area x Heat Factor) + Height Factor + People Factor'
        self.manual_frame=tk.Frame(self.root)
        self.manual_frame.rowconfigure(0, weight=1)
        self.manual_frame.rowconfigure(1, weight=1)
        manual_label1 = tk.Label(self.manual_frame, text=manualtext, wraplength=350, justify ='left', font = ('Times', 10))
        manual_label1.grid(row=0,sticky='news',pady=10)
        manual_label2 = tk.Label(self.manual_frame, text=manualtext2, wraplength=350, justify ='center', font=('Times', 10))
        manual_label2.grid(row=1, sticky='news',pady=10)
        manual_button = tk.Button(self.manual_frame,text='OK', command = self.tomain, width = 10)
        manual_button.grid(row=2,sticky='ns')
        self.manual_frame.place(x=0, y=0, anchor='nw',height=320,width=350)
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
        manual_label = tk.Label(self.thankyou_frame, text=manualtext, wraplength=350, justify='center', font=('Times', 10))
        manual_label.grid(row=0, sticky='news', pady=10, padx=12)
        manual_button = tk.Button(self.thankyou_frame, text='OK', command=self.tomain, width=10)
        manual_button.grid(row=1, sticky='ns')
        self.thankyou_frame.place(x=0, y=0, anchor='nw', height=320,width=350)
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
            area=float(self.area_entry.get())
            height=float(self.height_entry.get())
            people=int(self.people_entry.get())

            if self.check_state.get() == 1:
                heat_factor = 40
            else:
                heat_factor = 50

            if self.choice1.get() =="Square Meters":
                area_ft = area*10.764
            else:
                area_ft = area

            if self.choice2.get()=="Meters":
                height_ft = height * 3.28
            else:
                height_ft = height
            if height_ft < 8:
                height_factor = 0
            else:
                height_factor = 1000 * math.ceil(height_ft / 8)

            people_factor = people * 600

            cap_btu = (area_ft * heat_factor) + height_factor + people_factor
            computed_hp = cap_btu / 9500
            # Since standard ac units (for residential and commercial) is up to 4 hp only, we deduct extra hp and add in additional units
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
                start_statement = ' unit of aircon with capacity of '
                end_statement = '.'
            self.output.config(text='We recommend ' + str(units) + start_statement + str(cap_btu) + ' BTU/Hr or ' + str(cap_hp) + ' HP' + end_statement)
        except:
            self.output.config(text ='Please check the parameters! Numbers only on area and height, and whole numbers only on people!')



MethodTwo()
