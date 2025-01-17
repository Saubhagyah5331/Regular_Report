# Using with Statement
# with statement is used for resource management. It ensures that file is properly closed after its suite finishes, even if an exception is raised. with open() as method automatically handles closing the file once the block of code is exited, even if an error occurs. This reduces the risk of file corruption and resource leakage.

with open('File Handling/wth_statement/with.txt', 'r') as file:
    content = file.read()
    print(content)