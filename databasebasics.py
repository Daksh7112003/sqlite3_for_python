import sqlite3

# Connect to database...
conn = sqlite3.connect('hello.db')

c = conn.cursor()








#Query the database amd return all the records...
#for the app ...


def show_all():



    conn = sqlite3.connect('hello.db')

    c = conn.cursor()
    c.execute("SELECT rowid, * FROM hello")
                     # ","  MANDATORY SYNTAX....
    items = c.fetchall()
    for item in items:
        print(item)

        
    #commit your command ... 


    conn.commit()



    #close your connection....


    conn.close() 



#adding the records  in the app....



def add_one(first,last,email):
    conn= sqlite3.connect('hello.db')

    c=conn.cursor()




    c.execute("INSERT INTO hello VALUES(?,?,?)",(first,last,email))




    #deleting the database ...
def delete_one(id):


    conn=sqlite3.connect("hello.db")


    c=conn.cursor()

    c.execute("DELETE FROM hello WHERE rowid = (?)",id ) 


    
    conn.commit()

    conn.close()














# Create a table ...



# c.execute("""CREATE TABLE hello(
#           first_name text,
#           last_name text,
#           email text
# )""")





# Inserting one record into table.....

# c.execute("INSERT INTO hello VALUES('Mary','Brown','mary@codemt.com')")



# c.execute("SELECT* FROM hello")


# print(c.fetchall())

print("Command successfully executed ...")



#Another way of printing the dta ....




# items= c.fetchall()
# for item in items:
#     print(item)





# Another way of printing the data .....



# items = c.fetchall()


# for item in items:
#     print(item[0]+" "+item[1]+"\t\t\t"+item[2])


#     print(item[0]+" "+item[1]+"\t"+item[2])

#     print(item[0]+" "+item[1]+"\t\t"+item[2])


#more the t's..... more the space ...

# less the t's ... less the space










#primary key .........

# c.execute("SELECT rowid, * FROM hello")
#                      # ","  MANDATORY SYNTAX....
# items = c.fetchall()
# for item in items:
#     print(item)

    #This will give the row id to each items ....


    



# Query the database ....


# c.execute("SELECT * FROM hello WHERE rowid=1")

# items= c.fetchall()
# print(items)


#this will print the needed value of the code .....








#update the records....


 
#1 EXAMPLE



# c.execute("""UPDATE hello SET first_name='abca'
#         WHERE last_name='henry'
          
          
#           """)


#2 EXAMPLE 

# c.execute(""" UPDATE hello SET first_name='daksh'
#            WHERE rowid=2
#           """)














#DELETING THE RECORDS...


# c.execute(""" DELETE from hello WHERE rowid=3 """)

#rowid =3 === deleted ...





#ORDER  BY QUERY.....




#for descending order .....#ORDER  BY QUERY.....


# c.execute("SELECT rowid ,* FROM hello ORDER BY rowid DESC ")

# items= c.fetchall()

# for item in items:

#     print(item)







#for ascending order ....#ORDER  BY QUERY.....







# c.execute("SELECT rowid ,* FROM hello ORDER BY rowid ASC ")
# items= c.fetchall()

# for item in items:

#     print(item)












# Query the database ....


# c.execute("SELECT  * FROM hello ")

# items= c.fetchall()

# for item in items:

#     print(item)




#commit your command ... 


conn.commit()



#close your connection....


conn.close() 


