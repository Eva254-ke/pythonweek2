
def file_read_write():
    try:
        
        input_filename = input("Enter the name of the file to read: ")
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper() + "\n\n[Modified by Python Script]"
        
    
        output_filename = f"modified_{input_filename}"
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


