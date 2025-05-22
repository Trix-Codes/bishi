import os
import argparse as arr

def readf():
    file = open(r"/bishicom/bishit.txt" , "r")
    probit = ""
    for i in file:
        probit += i
    probit = eval(probit)
    return probit

def openf(arg):
    filet = readf()
    file = open(r"/bishicom/bishit.txt" , "w")
    filet.append(str(arg))
    file.write(filet)
    file.close()

def tflag(arg):
    #fpath = os.path.expanduser(arg)
    filet = readf()
    fpath = str(filet[arg])
    command = "xdg-open " + str(fpath)
    os.system(command)

def flagger(arg):
    fpath = os.path.abspath(arg)
    filet = readf()
    filet.append(str(fpath))
    file = open("/bishicom/bishit.txt" , "w")
    file.write(str(filet))
    file.close()
    print(str(arg) + " is flagged!")
    print()

def default():
    filet = readf()
    command = "xdg-open " + str(filet[-1])
    os.system(command)

def listerall():
    filet = readf()
    for i in range(len(filet)):
        print(str(i) + "    :   " + str(filet[i]))

def listerlast():
    filet = readf()
    print(str(len(filet)-1) + "    :    " + filet[-1])

def unflagger(arg):
    filet = readf()
    newfilet = []
    file = open("/bishicom/bishit.txt" , "w")
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
    file.write(str(newfilet))
    file.close()

def pipeopen(arg):
    #bishi -open nvim#all/0,1,2,3
    filet = readf()
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

def test(arg):
    filet = readf()
    words = arg.split("#")
    editor = words[0]
    com = words[1]
    command = str(editor) + " '" + str(filet[int(com)]) + "'"
    print(command)


filet = readf()

parser = arr.ArgumentParser()
parser.add_argument("-target" , "-t" , type = int , help = "Opens the file corresponding to the index number mentioned.")
parser.add_argument("-list" , "-ls" , type = str , choices = ["all" , "last" , "a" , "l"] , help = "Shows all flagged files and their indexes")
parser.add_argument("-flag" , "-f" , type = str , help = "Flags a specified file so that it can be run later")
parser.add_argument("-unflag" , "-uf" , type = str , help = "Unflags the specified file or all files")
parser.add_argument("-open" , "-o" , type = str , help = "Opens the file with the selected app or editor")
parser.add_argument("-test" , type = str , help = "For my development purposes")
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
else:
    default()

