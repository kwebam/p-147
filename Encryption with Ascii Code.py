from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")
root.geometry("500x500")

enter_name = Entry(root)
enter_name.place(relx=0.5, rely=0.2, anchor=CENTER)

show_ascii_name = Label(root, text="Name in Ascii:")
show_ascii_name.place(relx=0.5, rely=0.5, anchor=CENTER)

show_encrypted_name = Label(root, text="Encrypted Name:")
show_encrypted_name.place(relx=0.5, rely=0.7, anchor=CENTER)

def ascii_password_converter():
    name = str(enter_name.get())
    for letter in name:
        ascii_name = ord(name)
        show_ascii_name['text'] = ascii_name + " "
        ascii_name_less_1 = int(ascii_name)
        ascii_name_less_1-1
        str(chr(ascii_name_less_1))
        show_encrypted_name['text'] = ascii_name_less_1

btn = Button(root, text="Display the Ascii code & the Encrypted value", command=ascii_password_converter)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()