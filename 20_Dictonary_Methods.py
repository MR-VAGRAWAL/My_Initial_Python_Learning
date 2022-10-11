myDict = {
    "Fast" : "In a quick manner",
    "Vaibhav" : "A becoming multi-billionaire",
    "Marks" : [100,100,100],
    "dict" : {"Vaibhav" : "Multi-Billionaire"},
    1:2
}
# Dictionary Methods 
print(myDict.keys())           #--> Prints the keys of the dictionary.
print(list(myDict.keys()))     #--> Prints the keys of the dictionary.
print(type(myDict.keys()))     #--> Print the type of dictioniory.
print(myDict.items())          #--> Prints the (key , values) for all content of the dictionary. 
print(myDict)
# To add new (keys , values) pairs in our dictioniory. 
updatedmyDict = {
    "Pragyat" : "Brother",
    "Mr Pawan Agrawal" : "GOD Father",
    "Mrs Pooja Agrawal" : "Loving Mom"
}
myDict.update(updatedmyDict)
print(myDict)
myDict.update({"Muskan" : "Sister"})     #--> To add (keys , values) in the dictionary.
print(myDict)
print(myDict.get("Vaibhav"))   #--> Prints value assosciated with key "Vaibhav"
print(myDict["Vaibhav"])       #--> Prints value assosciated with key "Vaibhav"

# Difference between .et and [] syntax in Dictionory. 

# print(myDict.get("Vaibhav1")) ---> Returns none as Vaibhav1 is not present 
# print(myDict["Vaibhav"1])    ---> Throws error as Vaibhav1 is not present in the dictionary. 