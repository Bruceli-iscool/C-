def generate_x64_assembly(expression):
    assembly = ".intel_syntax noprefix\n"
    assembly += ".global main\n"
    assembly += "main:\n"
    
    # Load the value into the eax register
    assembly += f"mov eax, {expression}\n"
    
    # Return statement
    assembly += "ret\n"
    
    return assembly

def main():
    expression = input("Enter the arithmetic expression: ")
    assembly_code = generate_x64_assembly(expression)
    print("\nGenerated x64 Assembly Code:\n")
    print(assembly_code)

if __name__ == "__main__":
    main()
