from tkinter import Tk, Button, Entry, Label, Text, END
from main import main, getInfo

class Application:

    def __init__(self):
        # 主窗口
        self.window = Tk()
        self.window.title('无咎词典')
        self.window.geometry("280x350+500+200")

        # 输入框
        self.entry = Entry(self.window)
        # pack grid place
        self.entry.place(x=10, y=10, width=200, height=25)

        # 查询按钮
        self.submit_btn = Button(self.window, text='查询', command=self.submit)
        self.submit_btn.place(x=220, y=10, width=50, height=25)

        # 翻译标签
        self.label = Label(self.window, text='翻译结果：')
        self.label.place(x=10, y=40)

        # 显示框
        self.text = Text(self.window, background='#ccc')
        self.text.place(x=10, y=65, width=260, height=275)

    def run(self):
        self.window.mainloop()

    def submit(self):
        content = self.entry.get() # 读取输入框中的数据
        rs = main(content)
        self.text.delete(1.0, END) # 清除输出框
        self.text.insert(END, rs)  # 在输出框中显示数据

if __name__ == '__main__':
    app = Application()
    app.run()