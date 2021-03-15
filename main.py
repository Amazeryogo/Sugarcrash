import argparse
import sys 
#print("Enter the data") 
#data = sys.stdin.read()  

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
file = args.filename

print("Sugarcrash/Surf-Exel v1.0-beta")
print("This is Free and Open Software with no Warranty Whatsoever")
print('Made by Suvid Datta\n')

while True:
    x = input(">>")
    if x == "help":
        print('''
        Here are the commands you can use:

    r for reading the file \n
    w for writing \n
    ov to overwrite and destroy the contents of a file \n
    i to insert text at the end of the file
    q to quit
        
        
        ''')
    elif x == 'r':
        with open(file,'r') as bruh:
            c = bruh.read()
            print(c)
            bruh.close()
    elif x == 'w':
        data = sys.stdin.read()
        with open(file,'w+') as f:
            f.write(data)
            f.close()
            print("done!")
    elif x == 'i':
        data = sys.stdin.read()
        with open(file,'a') as f:
            f.write(data)
            f.close()
            print("done!")
    elif x == 'q':
        quit()
