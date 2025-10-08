try:
    with open('Sample.txt', 'r') as file:
        print("Reading file content")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file Sample.txt not found")
except Exception as e:
    print(f"An unexpected error occurred:{e}")
