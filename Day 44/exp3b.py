import glob, os

print("Enter Full Path of a Folder: ", end="")

path = input()

os.chdir(path)

print("\n1. List all Files ?")

print("2. List all Files with Particular Extension ?")

print("Enter Your Choice (1 or 2): ", end="")

try:

    ch = int(input())

    if ch == 1:

        print("\nList of All Files:")

        for file in glob.glob("*.*"):
            print(file)

    elif ch == 2:

        print("\nEnter the Extension (eg, .txt, .html, .css etc): ", end="")

        e = input()

        fileslist = []

        for file in glob.glob("*" + e):
            fileslist.append(file)

        if len(fileslist) > 0:

            print("\nList of All Files with \"" + e + "\" Extension:")

            for f in fileslist:
                print(f)

        else:

            print("\nNot found with \"" + e + "\" extension!")

    else:

        print("\nInvalid Choice!")

except ValueError:

    print("\nInvalid Input!")