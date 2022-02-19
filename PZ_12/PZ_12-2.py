# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Программа взята из ПЗ_7-1
# Дана строка, изображающая целое положительное число. Вывести сумму цифр этого числа.
import tkinter as tk


def func():
    try:
        x = 0
        n = int(n1.get())
        while n > 0:
            d = n % 10
            n = n // 10
            x += d
        res.config(text="Сумма цифр этого числа равна: {}".format(x))
    except ValueError:
        res.config(text="Ошибка, введите цифры")


root = tk.Tk()
root.geometry('200x80')
root.title('PZ_12-2')
n1 = tk.Entry(root)
n1.pack()
res = tk.Label(root, text="Результат:")
res.pack()
button = tk.Button(root, text='Получить числа', command=func)
button.pack()
root.mainloop()

