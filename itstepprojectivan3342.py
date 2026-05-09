import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# ---------------- БАЗА ДАНИХ ----------------

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
)
""")

conn.commit()

# ---------------- ФУНКЦІЇ ----------------

def add_book():
    title = title_entry.get()
    author = author_entry.get()

    if title and author:
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )

        conn.commit()

        messagebox.showinfo("Успіх", "Книгу додано!")

        title_entry.delete(0, "end")
        author_entry.delete(0, "end")

        load_books()

def load_books():
    books_box.delete("0.0", "end")

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    for book in books:
        books_box.insert(
            "end",
            f"{book[0]}. {book[1]} — {book[2]}\n"
        )

# ---------------- ВІКНО ----------------

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x500")
app.title("Бібліотека книг")

title_label = ctk.CTkLabel(app, text="Назва книги")
title_label.pack(pady=5)

title_entry = ctk.CTkEntry(app, width=300)
title_entry.pack()

author_label = ctk.CTkLabel(app, text="Автор")
author_label.pack(pady=5)

author_entry = ctk.CTkEntry(app, width=300)
author_entry.pack()

add_button = ctk.CTkButton(
    app,
    text="Додати книгу",
    command=add_book
)

add_button.pack(pady=10)

books_box = ctk.CTkTextbox(app, width=400, height=250)
books_box.pack(pady=10)

load_books()

app.mainloop()