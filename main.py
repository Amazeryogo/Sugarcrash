import argparse
import sys 
#print("Enter the data") 
#data = sys.stdin.read()  

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
file = args.filename

print("Sugarcrash/Surf-Exel v1.0")
print("This is Free and Open Software with no Warranty Whatsoever")
print('Made by Suvid Datta\n')

while True:
    x = input(">>")
    if x == "help":
        print('''
        Here are the commands you can use:

            help to open up all the commands\n
            r to read the file \n
            w to write the file \n
            ov to overwrite and destroy the contents of a file \n
            i to insert text at the end of the file \n
            q to quit \n

            PS- I bet you love sugar :)      
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
    elif x == 'ov':
        with open(file,'w+') as f:
            f.truncate()
            f.close()
            print("done!")
    else:
        print("command not found, try running help to find commands")
