from tkinter import *

langas = Tk()
atkurimui = StringVar()

def spausdinti():
    ivesta = laukas1.get()
    rezultatas["text"] = f'Sveiki, {ivesta}'
    bottom_field['text'] = "Sukurta"


def atkurti():
    ivesta = laukas1.get()
    rezultatas["text"] = f'Sveiki, {ivesta}'
    bottom_field['text'] = "Atkurti"


def erase_output_in_main_page():
    laukas1.delete(0, 'end')
    rezultatas["text"] = ''
    bottom_field['text'] = "Išvalyta"


def quit_program():
    langas.destroy()


# Turėtų laukelį "Įveskite vardą", kur galima įvesti vardą, mygtukas kurį nuspaudus atspausdintų "Labas, {vardas}!"
uzrasas1 = Label(langas, text="Įveskitę vardą")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Įvesti", command=spausdinti)
rezultatas = Label(langas, text="")
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas

bottom_field = Label(langas, text="")


# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"
langas.bind("<Return>", lambda event: spausdinti())
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą"
langas.bind("<Escape>", lambda event: quit_program())

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)
bottom_field.grid(row=4, column=1)

# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
#
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje atspausdintų paskutinį atspausdintą tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=erase_output_in_main_page)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=quit_program)

# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas

bottom_field = Label(langas, text="")
bottom_field.grid(row=4, column=1)


langas.mainloop()
