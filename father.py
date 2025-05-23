import os
import argparse as arr
import json

def readf():
    file = open(r"/bishicom/bishit.txt" , "r")
    probit = ""
    for i in file:
        probit += i
    probit = eval(probit)
    return probit

def readj():
    file = open(r"/bishicom/bishit.json" , "r")
    newl = json.load(file)
    filet = newl["flagged_files"]
    return filet

def writej(data):
    file = open(r"/bishicom/bishit.json" , "r+")
    filet = json.load(file)
    filet["flagged_files"].append(data)
    file.seek(0)
    json.dump(filet , file , indent = 1)

def writejuf(data):
    file = open(r"/bishicom/bishit.json" , "r")
    filet = json.load(file)
    file.close()
    filet["flagged_files"] = data
    file = open(r"/bishicom/bishit.json" , "w")
    file.seek(0)
    json.dump(filet , file , indent = 1)
    file.close()

def openf(arg):
    filet = readj()
    filet.append(str(arg))
    writej(filet)

def tflag(arg):
    #fpath = os.path.expanduser(arg)
    filet = readj()
    fpath = str(filet[arg])
    command = str(op) + str(fpath)
    os.system(command)

def flagger(arg):
    fpath = os.path.abspath(arg)
    filet = readj()
    filet.append(str(fpath))
    writej(str(fpath))
    print(str(arg) + " is flagged!")
    print()

def default():
    filet = readj()
    command = str(op) + str(filet[-1])
    os.system(command)

def listerall():
    filet = readj()
    for i in range(len(filet)):
        print(str(i) + "    :   " + str(filet[i]))

def listerlast():
    filet = readj()
    print(str(len(filet)-1) + "    :    " + filet[-1])

def unflagger(arg):
    filet = readj()
    newfilet = []
    if arg.isdigit() == True:
        index = int(arg)
        for i in range(len(filet)):
            if i == index:
                continue
            else:
                newfilet.append(filet[i])
        print(str(filet[index]) + " is unflagged!")
    elif arg == "all":
        newfilet = []
        print("All files are unflagged")
    else:
        fpath = os.path.abspath(arg)
        fpath = str(fpath)
        for i in filet:
            if i == fpath:
                continue
            else:
                newfilet.append(i)
        print(str(fpath) + " is unflagged!")
    writejuf(newfilet)

def pipeopen(arg):
    #bishi -open nvim#all/0,1,2,3
    filet = readj()
    words = arg.split("#")
    editor = words[0]
    com = words[1]
    if com == "all":
        for i in filet:
          command = str(editor) + " '" + str(i) + "'"
          os.system(command)
    else:
        command = str(editor) + " '" + str(filet[int(com)]) + "'"
        os.system(command)

def defaultopen():
    file = open(r"/bishicom/bishit.json" , "r")
    filet = json.load(file)
    com = str(filet["opener"]).strip() + " "
    return com

def customdefault(arg):
    file = open(r"/bishicom/bishit.json" , "r")
    filet = json.load(file)
    file.close()
    file = open(r"/bishicom/bishit.json" , "w")
    com = str(arg).strip() + " "
    filet["opener"] = com
    json.dump(filet , file , indent = 1)
    file.close()
    print("Default opener changed to:" , com)

def restore():
    file = open(r"/bishicom/bishit.json" , "r")
    filet = json.load(file)
    file.close()
    file = open(r"/bishicom/bishit.json" , "w")
    filet["opener"] = "xdg-open "
    json.dump(filet , file , indent = 1)
    file.close()
    print("Default settings restored!")


def test(arg):
    filet = readj()
    newfilet = []
    if arg.isdigit() == True:
        index = int(arg)
        for i in range(len(filet)):
            if i == index:
                continue
            else:
                newfilet.append(filet[i])
        print(str(filet[index]) + " is unflagged!")
    elif arg == "all":
        newfilet = []
        print("All files are unflagged")
    else:
        fpath = os.path.abspath(arg)
        fpath = str(fpath)
        for i in filet:
            if i == fpath:
                continue
            else:
                newfilet.append(i)
        print(str(fpath) + " is unflagged!")
    print(newfilet)


filet = readj()
op = defaultopen()

parser = arr.ArgumentParser()
parser.add_argument("-target" , "-t" , type = int , help = "Opens the file corresponding to the index number mentioned.")
parser.add_argument("-list" , "-ls" , type = str , choices = ["all" , "last" , "a" , "l"] , help = "Shows all flagged files and their indexes")
parser.add_argument("-flag" , "-f" , type = str , help = "Flags a specified file so that it can be run later")
parser.add_argument("-unflag" , "-uf" , type = str , help = "Unflags the specified file or all files")
parser.add_argument("-open" , "-o" , type = str , help = "Opens the file with the selected app or editor")
parser.add_argument("-test" , type = str , help = "For my development purposes")
parser.add_argument("-default" , "-do" , type = str , help = "Sets the default app, program or command to open directories.")
parser.add_argument('-restore' , type = str , choices = ["True" , "False"] , help = "Restores default settings")

args = parser.parse_args()

if args.target is not None:
    tflag(args.target)
elif args.list in ["all" , "a"]:
    listerall()
elif args.list in ["last" , "l"]:
    listerlast()
elif args.flag is not None:
    flagger(args.flag)
elif args.unflag is not None:
    unflagger(args.unflag)
elif args.open is not None:
    pipeopen(args.open)
elif args.test is not None:
    test(args.test)
elif args.default is not None:
    customdefault(args.default)
elif args.restore is not None:
    if args.restore == "True":
        restore()
    elif args.restore == "False":
        print("Why did you bother typing this command then?")
else:
    default()
