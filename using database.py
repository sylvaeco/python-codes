from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root= Tk()
root.title("Database")
root.geometry("500x500")

#create or connect to a database
con=sqlite3.connect("address_book.db")

#create cursor
c = con.cursor()

'''
#create table
c.execute("""
CREATE TABLE addresses(
first_name text NOT NULL,
last_name text NOT NULL,
address text NOT NULL,
city text NOT NULL, 
state text NOT NULL,
zipcode integer NOT NULL
)

""")
'''

    #   create edit function to update a record


def update():
    con=sqlite3.connect("address_book.db")

    #create cursor
    c = con.cursor()


    record_id=delete_box.get()
    c.execute("""
    UPDATE addresses SET 
    first_name = ?,
    last_name = ?,
    address = ?,
    city = ?, 
    state = ?,
    zipcode = ?
    WHERE oid = ?    
    """, 
    (
     f_name_editor.get(),
     l_name_editor.get(),
     address_editor.get(),
     city_editor.get(),
     state_editor.get(),
     zipcode_editor.get(),
     int(record_id)

    ))



    #commit to a database
    con.commit()

    #close the database
    con.close()

    editor.destroy()

def edit():
    global editor
    editor= Tk()
    editor.title("Update the Database")
    editor.geometry("400x250")
    con=sqlite3.connect("address_book.db")

    #create cursor
    c = con.cursor()

    record_id=delete_box.get()
    #Query the database
    c.execute("SELECT * FROM addresses WHERE oid= "+ record_id)
    records=c.fetchall()
    #print(records)    


    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #Create the textboxes    
    f_name_editor= Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))


    l_name_editor= Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)


    address_editor= Entry(editor, width=30)
    address_editor.grid(row=2, column=1)


    city_editor= Entry(editor, width=30)
    city_editor.grid(row=3, column=1)


    state_editor= Entry(editor, width=30)
    state_editor.grid(row=4, column=1)


    zipcode_editor= Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    #create textbox labels

    f_name_lab=Label(editor, text="First Name")
    f_name_lab.grid(row=0, column=0, pady=(10, 0))

    l_name_lab=Label(editor, text="Last Name")
    l_name_lab.grid(row=1, column=0)

    address_lab=Label(editor, text="Address")
    address_lab.grid(row=2, column=0)

    city_lab=Label(editor, text="City")
    city_lab.grid(row=3, column=0)

    state_lab=Label(editor, text="State")
    state_lab.grid(row=4, column=0)

    zipcode_lab=Label(editor, text="Zipcode")
    zipcode_lab.grid(row=5, column=0)

    
        #loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    
    #create a SAVE button
    save_btn= Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=146)


    #commit to a database
    con.commit()

    #close the database
    con.close()



def  delete():
    con=sqlite3.connect("address_book.db")

    #create cursor
    c = con.cursor()


    c.execute("DELETE from addresses where oid= "+ delete_box.get())

    #commit to a database
    con.commit()

    #close the database
    con.close()


#create submit function for database
def submit():
    con=sqlite3.connect("address_book.db")

    #create cursor
    c = con.cursor()

    #insert into table    
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                'f_name': f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city': city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
              })


    #commit to a database
    con.commit()

    #close the database
    con.close()
        
    
    #clear te text boxes 
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
#create a query function
def query():
    con=sqlite3.connect("address_book.db")

    #create cursor
    c = con.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    #print(records)    

    #loop through results
    print_records= ""
    for record in records:
        print_records+= str(record[0]) + " | "+ str(record[1])+" | "+  str(record[2])+" | "+  str(record[3])+" | "+  str(record[4])+ " |  "+  str(record[5])+" | " + "\t" +str(record[6])+ "\n"


    query_label=Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    #commit to a database
    con.commit()

    #close the database
    con.close()
    



#create text boxes
f_name= Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))


l_name= Entry(root, width=30)
l_name.grid(row=1, column=1)


address= Entry(root, width=30)
address.grid(row=2, column=1)


city= Entry(root, width=30)
city.grid(row=3, column=1)


state= Entry(root, width=30)
state.grid(row=4, column=1)


zipcode= Entry(root, width=30)
zipcode.grid(row=5, column=1)

#create delete box
delete_box=Entry(root, width=30)
delete_box.grid(row=9, column=1)


#create textbox labels

f_name_lab=Label(root, text="First Name")
f_name_lab.grid(row=0, column=0, pady=(10, 0))

l_name_lab=Label(root, text="Last Name")
l_name_lab.grid(row=1, column=0)

address_lab=Label(root, text="Address")
address_lab.grid(row=2, column=0)

city_lab=Label(root, text="City")
city_lab.grid(row=3, column=0)

state_lab=Label(root, text="State")
state_lab.grid(row=4, column=0)

zipcode_lab=Label(root, text="Zipcode")
zipcode_lab.grid(row=5, column=0)

delete_box_lab= Label(root, text="ID Number")
delete_box_lab.grid(row=9, column=0, pady=5)




#create submit button
submit_btn=Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0,columnspan=2, pady=10, padx=10, ipadx=100)

#create query button 
query_btn= Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#create delete button 
delete_btn= Button(root, text="DELETE Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

#create an update button
edit_btn= Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=146)



#commit to a database
con.commit()


#close the database
con.close()




root.mainloop()