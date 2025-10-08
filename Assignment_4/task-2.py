# User input text write in file
user = input("Enter text to write to the file: ")

with open('Output.txt', 'w') as file:
    file.write(user + "\n")
print("Data successfully written to Output.txt")

# Additional text to append

append_input = input("Enter additional text to append:")

with open('Output.txt', 'a') as file:
    file.write(append_input + "\n")
print("Data successfully appended")

# Final Output

print("\nFinal content of output.txt")

with open('Output.txt', 'r') as file:
    print(file.read())
