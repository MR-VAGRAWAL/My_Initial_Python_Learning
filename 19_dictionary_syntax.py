# We can create dictionary by {} 
myDict = {
    "Fast" : "In a quick manner",
    "Vaibhav" : "A becoming multi-billionaire",
    "Marks" : [100,100,100],
    "dict" : {"Vaibhav" : "Multi-Billionaire"}
}
print(myDict["Fast"])
print(myDict["Vaibhav"])
print(myDict["Marks"])
print(myDict["dict"]["Vaibhav"])    #--> To print the value within the nested list.
myDict["Marks"] = [100,100]         #--> It is mutable.