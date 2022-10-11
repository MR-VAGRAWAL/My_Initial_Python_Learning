# Use open function to read the content of a file. 
# f = open("40_sample.txt" , "r")
f = open("40_sample.txt") #By default mode ids "r"
# data = f.read()
data = f.read(7)   #Read first 7 characters from the text file.
print(data)
f.close() 