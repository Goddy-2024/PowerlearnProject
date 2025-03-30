#1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

    try:
        with open(input_filename, 'r') as file:
            content = file.readlines()

        # Modify content (e.g., convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write to new file
        with open(output_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content saved to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Unable to read or write the file.")



#2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
    filename = input("Enter your filename: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read.")


