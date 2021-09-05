import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile #как открыть, сохранить файл
from tkinter.messagebox import showerror #показ ошибок
from tkinter import messagebox #уведомления


from settings import * #Настройки

class Text_edit():
    def __init__(self):
        self.file_name="Придумай название,молодой"

    def new_file(self):
        self.file_name="Придумай названиe,молодой"
        text.delete('1.0',tkinter.END)

    def open_file(self):
        inp=asksaveasfile(mode="r")
        if inp is None:
            return
        data=inp.read()
        text.delete('1.0',tkinter.END)
        text.insert('1.0',data)


    def save_file(self):
        data=text.get('1.0', tkinter.END)
        output=open(self.file_name,'w',encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output=asksaveasfile(mode="w",defaultextension="txt")
        data=text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка!",message="Ошибка при сохранении файла")

    def get_info(self):
        messagebox.showinfo('Справка',"Информация о нашем приложении! Спасибо, что используете его")

app = tkinter.Tk() #создаю окно приложения
app.title(APP_NAME) #Название приложения
app.minsize(width=WIDTH,height=HEIGHT)
app.maxsize(width=WIDTH,height=HEIGHT)

text=tkinter.Text(app,width=WIDTH,height=HEIGHT,wrap='word') #создали поле с текстом
scroll=Scrollbar(app,orient=VERTICAL,command=text.yview) #создали scroll
scroll.pack(side="right",fill="y") #разместили scroll
text.configure(yscrollcommand=scroll.set) #связь теста со scroll-ом
text.pack() #размещение поле с текстом

menuBar=tkinter.Menu(app) #Создаю меню

editor=Text_edit()

app_menu=tkinter.Menu(menuBar) #Выпадающее меню у "Файл"
app_menu.add_command(label="Новый файл",command=editor.new_file)
app_menu.add_command(label="Открыть",command=editor.open_file)
app_menu.add_command(label="Сохранить",command=editor.save_file)
app_menu.add_command(label="Сохранить как",command=editor.save_as_file)

app.configure(menu=menuBar) #публикую меню

menuBar.add_cascade(label="Файл",menu=app_menu)
menuBar.add_cascade(label="Справка",command=editor.get_info)
menuBar.add_cascade(label="Правка")
menuBar.add_cascade(label="Выход",command=app.quit)


app.mainloop() #бесконечный цикл моего приложения

