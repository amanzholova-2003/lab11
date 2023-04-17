import tkinter as tk

# Создание окна
root = tk.Tk()
root.title("Мой логотип")

# Создание холста
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Нарисовать буквы имени на холсте
canvas.create_text(200, 200, text="Assel", font=("Arial", 60), fill="blue")

# Запустить главный цикл окна
root.mainloop()
