
status ="maravilhoso"

def comportamento():
    global status
    status = "cansativo"
    print(f"Python é {status}")
    
comportamento()

print(f"Python é {status}")