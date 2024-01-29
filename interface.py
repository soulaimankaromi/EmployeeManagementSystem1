from tkinter import *
from employee import Employee
from trainer import Trainer
from Agent import Agent
from tkinter import ttk
import json

main = Tk()
main.title("Employee Management System")

def Add():
    def Creation_COMPTE():
        employee_type = type_var.get()
        if employee_type == "Trainer":
            ACCOUNT = Trainer(nomentry.get(), datenentry.get(), dateeentry.get(), salaireentry.get(), heuresupentry.get(), tarifHsupentry.get())
            with open("dataem.json", "r") as file:
                date = json.load(file)
                date["Employee"].append({
                "Matricule": Employee.Getcounter() ,
                "Nom" : nomentry.get(),
                "Date de naissance": datenentry.get(),
                "Date d'embauche": dateeentry.get(),
                "Salaire de base": salaireentry.get(),
                "type de employe": type_var.get(),
                "heures supplementaires par mois": heuresupentry.get(),
                "La remuneration par heure supplementaire": tarifHsupentry.get(),
                "Prime de Responsabilite": ""
            })
                file.close()
        else:
            ACCOUNT = Agent(nomentry.get(), datenentry.get(), dateeentry.get(), salaireentry.get(), primeResponsabiliteentry.get())

            with open("dataem.json", "r") as file:
                date = json.load(file)
                date["Employee"].append({
                "Matricule": Employee.Getcounter() ,
                "Nom" : nomentry.get(),
                "Date de naissance": datenentry.get(),
                "Date d'embauche": dateeentry.get(),
                "Salaire de base": salaireentry.get(),
                "type de employe": type_var.get(),
                "heures supplementaires par mois": "",
                "La remuneration par heure supplementaire": "",
                "Prime de Responsabilite": primeResponsabiliteentry.get()
            })
        with open("dataem.json", "w") as file:
            json.dump(date, file, indent=2)

        nm.config(text = Employee.Getcounter() + 1)

        def insert_data(data_list):
            for employe in data_list:
                tree.insert("", "end", values=(
            employe["Matricule"],
            employe["Nom"],
            employe["Date de naissance"],
            employe["Date d'embauche"],
            employe["Salaire de base"],
            employe["type de employe"],
            employe["heures supplementaires par mois"],
            employe["La remuneration par heure supplementaire"],
            employe["Prime de Responsabilite"]
            ))

        # Create a Treeview widget
        tree = ttk.Treeview(main, columns=("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"), show="headings")

        # Define column headings
        tree.heading("Matricule", text="Matricule")
        tree.heading("Nom", text="Nom")
        tree.heading("Date de naissance", text="Date de naissance")
        tree.heading("Date d'embauche", text="Date d'embauche")
        tree.heading("Salaire de base", text="Salaire de base")
        tree.heading("type de employe", text="type de employe")
        tree.heading("heures supplementaires par mois", text="heures supplementaires par mois")
        tree.heading("La remuneration par heure supplementaire", text="La remuneration par heure supplementaire")
        tree.heading("Prime de Responsabilite", text="Prime de Responsabilite")

        # Specify column widths
        for column in ("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"):
            tree.column(column, width=100)

        # Insert data from the json fichier
        with open("dataem.json", "r") as file :
            data = json.load(file)
    

        insert_data(data["Employee"])

        # Add a vertical scrollbar
        vsb = ttk.Scrollbar(main, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Pack everything
        tree.grid(column=3, row=7, sticky=(W, E, N, S))
        vsb.grid(column=4, row=7, sticky=(N, S))

    def type_selected():
        employee_type = type_var.get()
        if employee_type == "Trainer":
            heuresupentry.config(state=NORMAL)
            tarifHsupentry.config(state=NORMAL)
            primeResponsabiliteentry.config(state=DISABLED)
        else:
            heuresupentry.config(state=DISABLED)
            tarifHsupentry.config(state=DISABLED)
            primeResponsabiliteentry.config(state=NORMAL)
    
    add_main = Tk()
    add_main.title("Add")

    numero = Label(add_main, text="Numero: ")
    numero.grid(row=0, column=0)

    nm = Label(add_main, text=Employee.Getcounter() + 1)
    nm.grid(row=0, column=1)

    nom = Label(add_main, text="Nom: ")
    nom.grid(row=1, column=0)

    nomentry = Entry(add_main)
    nomentry.grid(row=1, column=1)

    dateNaissance = Label(add_main, text="Date de naissance (YYYY-MM-DD): ")
    dateNaissance.grid(row=2, column=0)

    datenentry = Entry(add_main)
    datenentry.grid(row=2, column=1)

    dateEmbauche = Label(add_main, text="Date d'embauche (YYYY-MM-DD): ")
    dateEmbauche.grid(row=3, column=0)

    dateeentry = Entry(add_main)
    dateeentry.grid(row=3, column=1)

    salaire = Label(add_main, text="Salaire de base: ")
    salaire.grid(row=4, column=0)

    salaireentry = Entry(add_main)
    salaireentry.grid(row=4, column=1)

    salaire_unit = Label(add_main, text="DH")
    salaire_unit.grid(row=4, column=2)

    type_label = Label(add_main, text="Type: ")
    type_label.grid(row=5, column=0)

    type_var = StringVar()

    type_formateur = Radiobutton(add_main, text="Trainer", variable=type_var, value="Trainer", command=type_selected)
    type_formateur.grid(row=5, column=1)

    type_agent = Radiobutton(add_main, text="Agent", variable=type_var, value="Agent", command=type_selected)
    type_agent.grid(row=5, column=2)

    heuresup = Label(add_main, text="Le nombre des heures supplementaires par mois: ")
    heuresup.grid(row=6, column=0)

    heuresupentry = Entry(add_main)
    heuresupentry.grid(row=6, column=1)

    tarifHsup = Label(add_main, text="La remuneration par heure supplementaire: ")
    tarifHsup.grid(row=7, column=0)

    tarifHsupentry = Entry(add_main)
    tarifHsupentry.grid(row=7, column=1)

    primeResponsabilite = Label(add_main, text="Prime de Responsabilite: ")
    primeResponsabilite.grid(row=8, column=0)

    primeResponsabiliteentry = Entry(add_main)
    primeResponsabiliteentry.grid(row=8, column=1)

    button = Button(add_main, text="Creation Compte", command=Creation_COMPTE)  
    button.grid(row=9, column=1)

def Modify():
    def Modify_selected() :
        with open("dataem.json", "r") as file:
                date = json.load(file)
                date["Employee"][int(values[0])-1] = {
                "Matricule": Employee.Getcounter() ,
                "Nom" : nomentry.get(),
                "Date de naissance": datenentry.get(),
                "Date d'embauche": dateeentry.get(),
                "Salaire de base": salaireentry.get(),
                "type de employe": typeentry.get(),
                "heures supplementaires par mois": heuresupentry.get(),
                "La remuneration par heure supplementaire": tarifHsupentry.get(),
                "Prime de Responsabilite": primeResponsabiliteentry.get()
            }
        with open("dataem.json", "w") as file:
            json.dump(date, file, indent=2)
                
        def insert_data(data_list):
            for employe in data_list:
                tree.insert("", "end", values=(
            employe["Matricule"],
            employe["Nom"],
            employe["Date de naissance"],
            employe["Date d'embauche"],
            employe["Salaire de base"],
            employe["type de employe"],
            employe["heures supplementaires par mois"],
            employe["La remuneration par heure supplementaire"],
            employe["Prime de Responsabilite"]
            ))

        # Create a Treeview widget
        tree = ttk.Treeview(main, columns=("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"), show="headings")

        # Define column headings
        tree.heading("Matricule", text="Matricule")
        tree.heading("Nom", text="Nom")
        tree.heading("Date de naissance", text="Date de naissance")
        tree.heading("Date d'embauche", text="Date d'embauche")
        tree.heading("Salaire de base", text="Salaire de base")
        tree.heading("type de employe", text="type de employe")
        tree.heading("heures supplementaires par mois", text="heures supplementaires par mois")
        tree.heading("La remuneration par heure supplementaire", text="La remuneration par heure supplementaire")
        tree.heading("Prime de Responsabilite", text="Prime de Responsabilite")

        # Specify column widths
        for column in ("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"):
            tree.column(column, width=100)

        # Insert data from the json fichier
        with open("dataem.json", "r") as file :
            data = json.load(file)
    

        insert_data(data["Employee"])

        # Add a vertical scrollbar
        vsb = ttk.Scrollbar(main, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Pack everything
        tree.grid(column=3, row=7, sticky=(W, E, N, S))
        vsb.grid(column=4, row=7, sticky=(N, S))
    selected_item = tree.selection()
    if selected_item:
        mod_main = Tk()
        selected_item = selected_item[0]
        values = tree.item(selected_item, 'values')
        if values:
            numero = Label(mod_main, text="Numero: ")
            numero.grid(row=0, column=0)

            nm = Label(mod_main, text=values[0])
            nm.grid(row=0, column=1)

            nom = Label(mod_main, text="Nom: ")
            nom.grid(row=1, column=0)

            nomentry = Entry(mod_main)
            nomentry.grid(row=1, column=1)

            dateNaissance = Label(mod_main, text="Date de naissance (YYYY-MM-DD): ")
            dateNaissance.grid(row=2, column=0)

            datenentry = Entry(mod_main)
            datenentry.grid(row=2, column=1)

            dateEmbauche = Label(mod_main, text="Date d'embauche (YYYY-MM-DD): ")
            dateEmbauche.grid(row=3, column=0)

            dateeentry = Entry(mod_main)
            dateeentry.grid(row=3, column=1)

            salaire = Label(mod_main, text="Salaire de base: ")
            salaire.grid(row=4, column=0)

            salaireentry = Entry(mod_main)
            salaireentry.grid(row=4, column=1)

            salaire_unit = Label(mod_main, text="DH")
            salaire_unit.grid(row=4, column=2)

            type_label = Label(mod_main, text="Type: ")
            type_label.grid(row=5, column=0)

            typeentry = Entry(mod_main)
            typeentry.grid(row=6, column=1)

            heuresup = Label(mod_main, text="Le nombre des heures supplementaires par mois: ")
            heuresup.grid(row=6, column=0)

            heuresupentry = Entry(mod_main)
            heuresupentry.grid(row=6, column=1)

            tarifHsupentry = Entry(mod_main)
            tarifHsupentry.grid(row=7, column=1)

            tarifHsup = Label(mod_main, text="La remuneration par heure supplementaire: ")
            tarifHsup.grid(row=7, column=0)

            tarifHsupentry = Entry(mod_main)
            tarifHsupentry.grid(row=7, column=1)

            primeResponsabilite = Label(mod_main, text="Prime de Responsabilite: ")
            primeResponsabilite.grid(row=8, column=0)

            primeResponsabiliteentry = Entry(mod_main)
            primeResponsabiliteentry.grid(row=8, column=1)

            nomentry.insert(0, values[1])
            datenentry.insert(0, values[2])
            dateeentry.insert(0, values[3])
            salaireentry.insert(0, values[4])
            typeentry.insert(0, values[5])  
            heuresupentry.insert(0, values[6])
            tarifHsupentry.insert(0, values[7])
            primeResponsabiliteentry.insert(0, values[8])

            modifybutton = Button(mod_main, text="Modify", command=Modify_selected)
            modifybutton.grid(row=9, column=2)

def Delete():
    global tree
    selected_item = tree.selection()
    if selected_item:
        selected_item = selected_item[0]
        values = tree.item(selected_item, 'values')
        with open("dataem.json", "r") as file:
                date = json.load(file)
                del date["Employee"][int(values[0])-1] 
        
        with open("dataem.json", "w") as file:
            json.dump(date, file, indent=2)
                
        def insert_data(data_list):
            for employe in data_list:
                tree.insert("", "end", values=(
            employe["Matricule"],
            employe["Nom"],
            employe["Date de naissance"],
            employe["Date d'embauche"],
            employe["Salaire de base"],
            employe["type de employe"],
            employe["heures supplementaires par mois"],
            employe["La remuneration par heure supplementaire"],
            employe["Prime de Responsabilite"]
            ))

        # Create a Treeview widget
        tree = ttk.Treeview(main, columns=("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"), show="headings")

        # Define column headings
        tree.heading("Matricule", text="Matricule")
        tree.heading("Nom", text="Nom")
        tree.heading("Date de naissance", text="Date de naissance")
        tree.heading("Date d'embauche", text="Date d'embauche")
        tree.heading("Salaire de base", text="Salaire de base")
        tree.heading("type de employe", text="type de employe")
        tree.heading("heures supplementaires par mois", text="heures supplementaires par mois")
        tree.heading("La remuneration par heure supplementaire", text="La remuneration par heure supplementaire")
        tree.heading("Prime de Responsabilite", text="Prime de Responsabilite")

        # Specify column widths
        for column in ("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"):
            tree.column(column, width=100)

        # Insert data from the json fichier
        with open("dataem.json", "r") as file :
            data = json.load(file)
    

        insert_data(data["Employee"])

        # Add a vertical scrollbar
        vsb = ttk.Scrollbar(main, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        # Pack everything
        tree.grid(column=3, row=7, sticky=(W, E, N, S))
        vsb.grid(column=4, row=7, sticky=(N, S))
        

add = Button(main, text="Add", command=Add)
add.grid(row=0, column=0)

modify = Button(main, text="Modify", command=Modify)
modify.grid(row=0, column=1)

delete = Button(main, text="Delete", command=Delete)
delete.grid(row=0, column=2)

def insert_data(data_list):
    for employe in data_list:
        tree.insert("", "end", values=(
            employe["Matricule"],
            employe["Nom"],
            employe["Date de naissance"],
            employe["Date d'embauche"],
            employe["Salaire de base"],
            employe["type de employe"],
            employe["heures supplementaires par mois"],
            employe["La remuneration par heure supplementaire"],
            employe["Prime de Responsabilite"]
        ))

# Create a Treeview widget
tree = ttk.Treeview(main, columns=("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"), show="headings")

# Define column headings
tree.heading("Matricule", text="Matricule")
tree.heading("Nom", text="Nom")
tree.heading("Date de naissance", text="Date de naissance")
tree.heading("Date d'embauche", text="Date d'embauche")
tree.heading("Salaire de base", text="Salaire de base")
tree.heading("type de employe", text="type de employe")
tree.heading("heures supplementaires par mois", text="heures supplementaires par mois")
tree.heading("La remuneration par heure supplementaire", text="La remuneration par heure supplementaire")
tree.heading("Prime de Responsabilite", text="Prime de Responsabilite")

# Specify column widths
for column in ("Matricule", "Nom", "Date de naissance", "Date d'embauche", "Salaire de base", "type de employe", "heures supplementaires par mois", "La remuneration par heure supplementaire", "Prime de Responsabilite"):
    tree.column(column, width=100)

# Insert data from the json fichier
with open("dataem.json", "r") as file :
    data = json.load(file)
    

insert_data(data["Employee"])

# Add a vertical scrollbar
vsb = ttk.Scrollbar(main, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Pack everything
tree.grid(column=3, row=7, sticky=(W, E, N, S))
vsb.grid(column=4, row=7, sticky=(N, S))

main.mainloop()