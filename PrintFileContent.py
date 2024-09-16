file_path = "SimpleTextfile.txt"
file_object = open(file_path)

print(file_object)

file_contect = file_object.read()
print(file_contect)
file_object.close()

# another way to iterate thorugh the file and print the content
file_object = open(file_path)
for line in file_object:
    print(line)
file_object.close()
