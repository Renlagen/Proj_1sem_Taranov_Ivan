import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
# name, otdel, rashod, sum

class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#30d5c8', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить отчет', command=self.open_dialog, bg='#30d5c8', bd=0, fg='black',
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="img/edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#30d5c8',
                                    bd=0, fg='black', compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить отчет", command=self.delete_records, bg='#30d5c8',
                               bd=0, fg='black', compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск", command=self.open_search_dialog, bg='#30d5c8',
                               bd=0, fg='black', compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/update.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить список", command=self.view_records, bg='#30d5c8',
                                bd=0, fg='black', compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'number', 'name', 'otdel', 'rashod', 'sum'), height=15,
                                 show='headings')

        self.tree.column('number', width=20, anchor=tk.CENTER)
        self.tree.column('name', width=150, anchor=tk.CENTER)
        self.tree.column('otdel', width=200, anchor=tk.CENTER)
        self.tree.column('rashod', width=200, anchor=tk.CENTER)
        self.tree.column('sum', width=150, anchor=tk.CENTER)

        self.tree.heading('number', text='#')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('otdel', text='Отдел')
        self.tree.heading('rashod', text='Вид расхода')
        self.tree.heading('sum', text='Сумма')

        self.tree.pack()

    def records(self, number, name, otdel, rashod, sum):
        self.db.insert_data(number, name, otdel, rashod, sum)
        self.view_records()

    def update_record(self, number, name, otdel, rashod, sum):
        self.db.cur.execute(
            """UPDATE users SET number=?, name=?, otdel=?, rashod=?, sum=? WHERE number=?""",
            (number, name, otdel, rashod, sum, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE number=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, otdel):
        otdel = (otdel,)
        self.db.cur.execute("""SELECT * FROM users WHERE otdel=?""", otdel)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Отчет по канцелярии')
        self.geometry('400x250+400+300')
        self.resizable(False, False)

        label_number = tk.Label(self, text='Номер')
        label_number.place(x=50, y=15)
        self.entry_number = ttk.Entry(self, width=30)
        self.entry_number.place(x=170, y=15)

        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=40)
        self.entry_name = ttk.Entry(self, width=30)
        self.entry_name.place(x=170, y=40)

        label_otdel = tk.Label(self, text='Отдел')
        label_otdel.place(x=50, y=65)
        self.entry_otdel = ttk.Combobox(self, width=30,  values=[u'Отдел кадров', u'Секретариат', u'Вычислительный центр',
                                               u'Бухгалтерия', u'Финансовое подразделение'])
        self.entry_otdel.place(x=170, y=65)

        label_rashod = tk.Label(self, text='Вид расхода')
        label_rashod.place(x=50, y=90)
        self.entry_rashod = ttk.Entry(self, width=30)
        self.entry_rashod.place(x=170, y=90)

        label_sum = tk.Label(self, text='Сумма')
        label_sum.place(x=50, y=115)
        self.entry_sum = ttk.Entry(self, width=30)
        self.entry_sum.place(x=170, y=115)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_number.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_otdel.get(),
                                                                       self.entry_rashod.get(),
                                                                       self.entry_sum.get()))


        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать отчет")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_number.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_otdel.get(),
                                                                          self.entry_rashod.get(),
                                                                          self.entry_sum.get()))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        self.otdel_search = ttk.Combobox(self, values=[u'Отдел кадров', u'Секретариат', u'Вычислительный центр',
                                                       u'Бухгалтерия', u'Финансовое подразделение'])
        self.otdel_search.place(x=60, y=20, width=200)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=70, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.otdel_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('Office.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                number INTEGER,
                name TEXT,
                otdel TEXT, 
                rashod TEXT,
                sum INTEGER
                )""")

    def insert_data(self, number, name, otdel, rashod, sum):
        self.cur.execute(
            """INSERT INTO users(number, name, otdel, rashod, sum) VALUES (?, ?, ?, ?, ?)""",
            (number, name, otdel, rashod, sum))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Учет внутриофисных расходов")
    root.geometry("720x450+400+200")
    root.resizable(False, False)
    root.mainloop()