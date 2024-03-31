from tkinter import *

class EasyCimputer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("easy computer")

        self.current = 0
        self.term = 0
        self.option = 1

        btn_count = 0
        for c in range(3):
            for r in range(3):
                btn_count += 1

                Button(
                    self.master,
                    text=str(btn_count),
                    command=lambda x=btn_count: self.key(x),
                    width=2
                ).grid(row=3-c, column=r)

        option_s = [ "+", "-", "*", "/" ]
        for i in range(len(option_s)):
            btn_count += 1

            Button(
                self.master,
                text=option_s[i],
                command=lambda x=btn_count: self.key(x),
                width=2
            ).grid(row=i+1, column=3)

        Button(
            self.master,
            text="0",
            command=lambda: self.key(0),
            width=2
        ).grid(row=4, column=0)

        Button(
            self.master,
            text="=",
            command=lambda: self.key(14),
            width=2
        ).grid(row=3, column=4)

        Button(
            self.master,
            text="C",
            command=lambda: self.key(15),
            width=2,
            bg="red"
        ).grid(row=1, column=4)

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=0, columnspan=5)

    def key(self, num):
        if num > 9:
            if num < 14:
                self.option = num - 9
                self.term = self.current
                self.current = 0
            elif num == 14 and self.term:
                if self.option == 1:
                    self.current = self.term + self.current
                elif self.option == 2:
                    self.current = self.term - self.current
                elif self.option == 3:
                    self.current = self.term * self.current
                elif self.option == 4:
                    self.current = (self.term + 0.0) / (self.current + 0.0)
            elif num == 15:
                self.current = self.term = 0
        else:
            self.current = self.current * 10 + num

        self.entry.delete(0, END)
        self.entry.insert(0, str(self.current))



root = Tk()
frame = EasyCimputer(root)
frame.grid()

root.mainloop()

