#ZIPUNLOCKER
#Made by SH
import zipfile
#TITULO
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"Reset": "\u001b[0m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

f  = open("title","r")
ascii = "".join(f.readlines())
print(colorText(ascii))

dic = input("Please enter the path of the password dictionary: ")
print("Do you want to continue with the dictionary: " + (dic) + " ?")
option1 = input("Enter y/n: ")
if option1 == "y":
    print("Processing...")
    global contras
    contras = []
    with open((dic),'r') as stop_words: 
        lineas = [linea.strip() for linea in stop_words]
    for linea in lineas:
        contras.append(linea)
    for i in contras:
        print(i)
    print(contras)
    zf = input("Please enter the path of the zip file: ")
    go = input("Please enter the path to unzip files: ")
    i = 1
    e = 0
    archivo=(zf)
    # check if file exists
    if zipfile.is_zipfile(archivo):
        # read files
        zf=zipfile.ZipFile(archivo,"r")
        for zfile in zf.filelist:
            print(zfile.filename, " size:", zfile.file_size, "B"," compresed:", zfile.compress_size, "B")
        # extract files
        while(i != len(contras)):
            pswd = contras[e]
            password=((pswd.encode()))
            rutaExtract=(go)
            print((contras[e]))
            e = e + 1
            print("Unzipping...")
            zf.extractall(path=rutaExtract,pwd=password)
            print("FINISHED")
            print("Error")
            i = i + 1
elif option1 == "n":
    print("PLEASE RESET")
else:
    print("ERROR: PLEASE RESET")
