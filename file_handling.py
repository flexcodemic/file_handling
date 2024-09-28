# Create a new text file and write some lines to it
with open("my_file.txt", "w") as file:
    file.write("This is the first line of the file.\n")
    file.write("The number 12345 is written here.\n")
    file.write("Python file handling is fun!\n")

# Read the contents of the file and display them on the console
with open("my_file.txt", "r") as file:
    print("Contents of 'my_file.txt' after initial writing:")
    print(file.read())

# Open the file in append mode and add more lines
with open("my_file.txt", "a") as file:
    file.write("This is an appended line 1.\n")
    file.write("Appending more data with the number 67890.\n")
    file.write("File handling operations are quite useful.\n")

# Read the updated file contents and display them
with open("my_file.txt", "r") as file:
    print("Contents of 'my_file.txt' after appending:")
    print(file.read())
