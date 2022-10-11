greeting = "Good Morning "
name = "Vaibhav"
# Contacenating Two String
print(greeting + name)
# To get type of function 
print(type(name))
# To get Number of Characters in a variable 
print(len(name))
# To get character at a particular imdex.
print(name[3])
# name[3] = "d"--> Does not work 
print(name[0:3])    #-->It goes to (length-1)th index.  
print(name[:3])     #-->Same as name[0:3]
print(name[1:])     #-->Same as name[1:6]
print(name[-1])     #-->Last word od the senteance.
print(name[-5:-1])  #--> same as print(name[2:6])
name = "Vaibhav"
print(name[0:7:3])  #-->skiping 3 values 