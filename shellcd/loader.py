import sys 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python loader.py shellcode.bin/or shellcode file")
    else:
        shl_f = sys.argv[1]
        with open(shl_f, 'rb') as f_in:
              bx = f_in.read()
            
        with open('shelcode.py', 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if 'b_x = b"' in line:
                bx = bx.hex()

                bx = "\\x" + "\\x".join(bx[i:i + 2] for i in range(0, len(bx), 2))


                lines[i] = '    b_x = b"'  +  bx + '"\n'  

        with open('shelcode.py', 'w') as file:
            file.writelines(lines)