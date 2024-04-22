import os


def main():
    documentos_path = "C:\\Users\\" + os.getlogin() + "\\Documents\\"
    a = open(documentos_path + "Para Ti.txt", "w")
    a.write("Soy un hacker")
    a.close()

    
if __name__ == "__main__":
    main()