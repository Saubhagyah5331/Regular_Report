file = open('File Handling/write/write.txt', 'r+')
file.write("Hello world")
content = file.readline()
print(content)