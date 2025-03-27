import tkinter as tk
from tkinter import messagebox

def show_order():
    order = "Ваш заказ:\n"
    if var_pizza.get():
        order += "Пицца\n"
    if var_burger.get():
        order += "Бургер\n"
    if var_salad.get():
        order += "Салат\n"
    if var_pasta.get():
        order += "Паста\n"
    if order == "Ваш заказ:\n":
        order = "Вы ничего не выбрали."
    messagebox.showinfo("Заказ", order)

# Создаем главное окно
root = tk.Tk()
root.title("Меню ресторана")

# Создаем переменные для флажков
var_pizza = tk.BooleanVar()
var_burger = tk.BooleanVar()
var_salad = tk.BooleanVar()
var_pasta = tk.BooleanVar()

# Создаем флажки
tk.Checkbutton(root, text="Пицца", variable=var_pizza).pack(anchor='w')
tk.Checkbutton(root, text="Бургер", variable=var_burger).pack(anchor='w')
tk.Checkbutton(root, text="Салат", variable=var_salad).pack(anchor='w')
tk.Checkbutton(root, text="Паста", variable=var_pasta).pack(anchor='w')

# Создаем кнопку для оформления заказа
order_button = tk.Button(root, text="Оформить заказ", command=show_order)
order_button.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
