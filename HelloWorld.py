# text that is written to file
text = "Hello World :D"

# creates new file and opens it for writing 
file = open("HelloWorld.txt", "w")

# writes the text to the new file 
file.write(text)

# closes the file
file.close()
