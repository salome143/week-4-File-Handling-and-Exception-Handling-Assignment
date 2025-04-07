def read_and_modify_file(input_filename, output_filename):
    try:
        # Attempt to open the input file and read its contents
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, converting all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Content from {input_filename} has been read, modified, and written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write to '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for the filename
    input_filename = input("Please enter the input filename (with extension): ")
    output_filename = input("Please enter the output filename (with extension): ")

    # Call the function to read, modify and write the content
    read_and_modify_file(input_filename, output_filename)


# Run the main function
if __name__ == "__main__":
    main()
