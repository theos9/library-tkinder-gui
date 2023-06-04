from tkinter import *
import back_end
window = Tk()
window.title("library")
# ======================== labels ========================
l1 = Label(window, text="Title : ")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author : ")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year : ")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN : ")
l4.grid(row=1, column=2)
# ======================== entries ========================
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)
# ======================== listbox ========================

list1 = Listbox(window, width=28, height=15)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)
scrol1 = Scrollbar(window)
scrol1.grid(row=2, column=2, rowspan=2)
list1.configure(yscrollcommand=scrol1.set)
scrol1.configure(command=list1.yview)


def get_selected_row(event):
    global selected_book
    if len(list1.curselection())>0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        e4.delete(0, END)
        e4.insert(END, selected_book[4])


list1.bind("<<ListboxSelect>>", get_selected_row)
# ======================== func ========================


def clear_list():
    list1.delete(0, END)


def insert_in_list(books):
    for book in books:
        list1.insert(END, book)


def view():
    clear_list()
    books = back_end.view()
    insert_in_list(books)


def search():
    clear_list()
    books = back_end.search(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    insert_in_list(books)


def add():
    clear_list()
    back_end.insert(title_text.get(), author_text.get(),
                    year_text.get(), isbn_text.get())
    view()


def update():
    back_end.update(selected_book[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())
    view()


def delete():
    back_end.delete(selected_book[0])
    view()


# ======================== button ========================
but1 = Button(window, text="view all", width=12, command=lambda: view())
but1.grid(row=2, column=3)
but2 = Button(window, text="search", width=12, command=lambda: search())
but2.grid(row=3, column=3)
but3 = Button(window, text="add", width=12, command=lambda: add())
but3.grid(row=4, column=3)
but4 = Button(window, text="update", width=12, command=lambda: update())
but4.grid(row=5, column=3)
but5 = Button(window, text="delete", width=12, command=lambda: delete())
but5.grid(row=6, column=3)
but6 = Button(window, text="clear ", width=12, command=lambda: clear_list())
but6.grid(row=7, column=3)
but7 = Button(window, text="close ", width=12, command=window.destroy)
but7.grid(row=8, column=3)


window.mainloop()
