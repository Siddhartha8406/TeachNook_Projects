from tkinter import  Tk, Button, Label, LEFT

class Timer:
    def __init__(self, timer_time):
        self.main_status = True
        self.timer_status = True
        self.current_time = 0
        self.target_time = timer_time

    def Create_UI(self):
        self.root = Tk()
        self.root.config(bg="#24F0E3")
        self.root.title('Counter Timer')

        self.label = Label(self.root, text='Timer', font=('Arial', 90),borderwidth=1)
        self.label.pack()

        self.startbtn = Button(self.root, text='Start', font=('Arial', 25),command=self.start,borderwidth=1)
        self.startbtn.pack(side=LEFT)

        self.stopbtn = Button(self.root, text='Stop', font=('Arial', 25),borderwidth=1, command=self.stop, state='disabled')
        self.stopbtn.pack(side=LEFT)

        self.resume = Button(self.root, text='Resume', font=('Arial', 25),borderwidth=1, command=self.resume, state='disabled')
        self.resume.pack(side=LEFT)

        self.reset = Button(self.root, text='Restart', font=('Arial', 25),borderwidth=1, command=self.restart, state='disabled')
        self.reset.pack(side=LEFT)

        self.quit = Button(self.root, text='Quit', font=('Arial', 25),borderwidth=1, command=self.root.destroy)
        self.quit.pack()

        self.root.mainloop()

    def start(self):
        self.startbtn['state'] = 'disabled'
        if not self.timer_status:
            self.timer_status = True
            self.main_status = True
            self.resume['state'] = 'disabled'
            self.stopbtn['state'] = 'normal'
        else:
            self.reset['state'] = 'normal'
            self.stopbtn['state'] = 'normal'
            self.update()

    def update(self):
        if self.main_status:
            if self.timer_status:
                if self.current_time <= self.target_time:
                    time_left = self.target_time - self.current_time
                    self.label.config(text=time_left)
                    self.current_time += 1
                elif self.current_time > self.target_time:
                    self.label.config(text='Time Up!')
                    self.main_status=False
                    self.timer_status=False
            self.label.after(1000, self.update)

    def stop(self):
        self.timer_status = False
        self.resume['state'] = 'normal'
        self.stopbtn['state'] = 'disabled'

    def resume(self):
        self.timer_status = True
        self.resume['state'] = 'disabled'
        self.stopbtn['state'] = 'normal'

    def restart(self):
        self.timer_status = False
        self.main_status = False
        self.current_time = 0
        self.start()

if __name__ == "__main__":
    time = int(input("Enter the Time(in sec): "))
    test = Timer(time)
    test.Create_UI()