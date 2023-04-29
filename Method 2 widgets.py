import tkinter as tk
import math

class MethodTwo():

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('300x300')
        self.root.resizable(False,False)

        self.header=tk.Label(self.root, text = "METHOD 2", font = ('Arial Black', 20))
        self.header.pack()

        self.description=tk.Label(self.root, text ='Simple cooling capacity estimation using area and height', font = ('Arial', 8), justify ='center')
        self.description.pack(pady=10)

        self.parameter_frame = tk.Frame(self.root)
        self.parameter_frame.columnconfigure(0, weight = 1)
        self.parameter_frame.columnconfigure(1, weight=1)
        self.parameter_frame.columnconfigure(2, weight=1)

        self.area_desc=tk.Label(self.parameter_frame, text = "Enter Floor Area (sq.m)", font=('Arial',8), justify='left')
        self.area_desc.grid(row=0,column=0,sticky='w',pady=5)

        self.area_entry = tk.Entry(self.parameter_frame)
        self.area_entry.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10,pady=5)

        self.height_desc = tk.Label(self.parameter_frame, text="Enter Floor Height (m)", font=('Arial', 8), justify='left')
        self.height_desc.grid(row=1, column=0,sticky='w',pady=5)

        self.height_entry = tk.Entry(self.parameter_frame)
        self.height_entry.grid(row=1, column=1, sticky=tk.E+tk.W, padx=10,pady=5)

        self.people_desc = tk.Label(self.parameter_frame, text="How many people reside in this room?", font=('Arial', 8),justify='left', wraplength=150)
        self.people_desc.grid(row=2, column=0,sticky='w',pady=5)

        self.people_entry = tk.Entry(self.parameter_frame)
        self.people_entry.grid(row=2, column=1, sticky='w', padx=10,pady=5)

        self.check_state=tk.IntVar()

        self.checker=tk.Checkbutton(self.parameter_frame, text='The room being designed is in the ground floor.', wraplength=150, font =('Arial', 8), justify='left', variable=self.check_state)
        self.checker.grid(row = 3, column = 0, pady=10, sticky = 'w')

        self.btn=tk.Button(self.parameter_frame, text = 'Calculate', command=self.calculate)
        self.btn.grid(row=4, column = 0, sticky = tk.W+tk.E,padx=10)

        self.output=tk.Label(self.parameter_frame,text = 'Click calculate for the results!', font = ('Arial', 8), wraplength=120, justify = 'left')
        self.output.grid(row = 3, column = 1, rowspan=2)

        self.parameter_frame.pack(fill='x')


        self.root.mainloop()

    def calculate(self):
        try:
            area=float(self.area_entry.get())
            height=float(self.height_entry.get())
            people=int(self.people_entry.get())
            if self.check_state.get() == 1:
                heat_factor = 40
            else:
                heat_factor = 50

            height_ft = height * 3.28
            if height_ft < 8:
                height_factor = 0
            else:
                height_factor = 1000 * math.ceil(height_ft / 8)

            people_factor = people * 600

            cap_btu = (area * 10.764 * heat_factor) + height_factor + people_factor
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