from tkinter import *
from currency_converter import CurrencyConverter
c = CurrencyConverter()

class Main(Frame):
    currencies = ["USD","RUB","EUR","BGN"]
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        x = 10
        y = 30

        self.first_label = Label(text="USD", font=("Times New Roman", 15))
        self.first_label.place(x=x,y=y,width=140,height=30)

        self.second_label = Label(text="RUB", font=("Times New Roman", 15))
        self.second_label.place(x=335,y=y,width=140,height=30)
        y+=40
        self.entry = Entry()
        self.entry.place(x=x,y=y,width=140,height=30)


        self.label = Label()
        self.label.place(x=335,y=y,width=140,height=30)
        y+=40

        self.button = Button(text="convert", bg="#FFF", font=("Times New Roman", 15),command=self.convert ).place(x=192, y=y, width=100,height=40)

        for button in self.currencies:
            command = lambda label=self.first_label, text=button: self.change_label_text(label, text)
            x=10
            Button(text=button, bg="#FFF", font=("Times New Roman", 15),command=command).place(x=x,y=y,width=60,height=30)
            command = lambda label=self.second_label, text=button: self.change_label_text(label, text)
            x=415
            Button(text=button, bg="#FFF", font=("Times New Roman", 15),command=command).place(x=x, y=y, width=60, height=30)
            y+=40

    def change_label_text(self, label, text):
        label.configure(text=text)

    def convert(self):
        first = self.first_label.cget("text")
        second = self.second_label.cget("text")
        value = int(self.entry.get())
        new_value = round(c.convert(value,first,second),2)
        self.label.configure(text=new_value)

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x300+200+200")
    root.title("Ковертер валют")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()