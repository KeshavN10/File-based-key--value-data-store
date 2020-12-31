import code as x 
#importing the main file("code" is the name of the file I have used) as a library 

x.create("sastra",25)

x.create("src",70,3600) 

x.read("sastra")

x.read("src")

x.create("sastra",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("sastra",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("sastra")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn

