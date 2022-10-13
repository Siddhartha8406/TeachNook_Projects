from tkinter import  Tk, Button, Label, LEFT
from tracemalloc import start

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

        self.label = Label(self.root, text='Counter Timer', font=('Arial', 50),borderwidth=1)
        self.label.pack()

        self.startfun = Button(self.root, text='Start', font=('Arial', 25),command=self.start,borderwidth=1)
        self.startfun.pack(side=LEFT)

        self.stopbtn = Button(self.root, text='Stop', font=('Arial', 25),borderwidth=1, command=self.stop, state='disabled')
        self.stopbtn.pack(side=LEFT)

        self.resume = Button(self.root, text='Resume', font=('Arial', 25),borderwidth=1, command=self.resume, state='disabled')
        self.resume.pack(side=LEFT)

        self.quit = Button(self.root, text='Quit', font=('Arial', 25),borderwidth=1, command=self.root.quit)
        self.quit.pack(side=LEFT)

        self.reset = Button(self.root, text='Reset', font=('Arial', 25),borderwidth=1, command=self.restart, state='disabled')
        self.reset.pack()

        self.root.mainloop()

    def start(self):
        if not self.timer_status:
            self.timer_status = True
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
                print('Here')
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
        self.current_time = 0
        self.start()

if __name__ == "__main__":
    test = Timer(20)
    test.Create_UI()