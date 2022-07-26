import sys
import os

argv = sys.argv
programName = "null"
run = True
delete = False
exitFunction = False
read = False
tabIndex = 0

try:
    if argv[1] == "-h":
        print('''
    HELP MENU

    arguments:

    ARGUMENT    EXAMPLE         OPTIONAL    DESCRIPTION

    -h          -h                 O        Displays this help menu

    -f          -f file            N        The file to run

    -a          -a c/cr/crd/r/rd   Y        The arguments for the compiler (DEFAULT: cr)
                                            c: just compile
                                            cr: compile then run
                                            crd: compile, run and finally delete the compiled file
                                            r: run the specified compiled file
                                            rd: run the specified compiled file, then delete it

    OPTIONAL EXPLANATION

    O: The only argument
    N: Required
    Y: Optional
        ''')
        input("<<<END>>>")

        exitFunction = True
except IndexError:
    pass

def operatorConverter(operator):
    if operator.upper() == "<EQL>":
        return "=="
    elif operator.upper() == "<GRT>":
        return ">"
    elif operator.upper() == "<LST>":
        return "<"
    elif operator.upper() == "<GTE>":
        return "<="
    elif operator.upper() == "<LTE>":
        return ">="
    elif operator.upper() == "<NEQ>":
        return "!="
    elif operator.upper() == "<ADD>":
        return "+"
    elif operator.upper() == "<SUB>":
        return "-"
    elif operator.upper() == "<DIV>":
        return "/"
    elif operator.upper() == "<MUL>":
        return "*"

    elif operator.upper() == "<STM>":
        return "none"
    elif operator.upper() == "<CON>":
        return "none"
    else:
        return False

if not exitFunction:
    for arg in argv[1:len(argv)]:
        if arg == "-f":
            programName = argv[argv.index(arg) + 1]

        if arg == "-a":
            argument = argv[argv.index(arg) + 1]

            if argument == "c":
                run = False
            elif argument == "crd":
                delete = True
            elif argument == "r":
                read = True
            elif argument == "rd":
                read = True
                delete = True

    if programName == "null":
        print("No file specifien. Try '-h' for help")
        input("<<<END>>>")
        exitFunction = True

    if not exitFunction:
        newLine = True
        printLine = False
        varLine = True

        if read:
            with open(programName, "r") as program:
                code = ""
                for line in program.readlines():
                    code += line
                    
                exec(code)

            if delete:
                os.remove(programName)
        else:
            with open(programName, "r") as program:
                program = program.readlines()

                with open(programName + ".cpld", "w") as newProgram:
                    newProgram.write("")

                with open(programName + ".cpld", "a") as newProgram:
                    for line in program:
                        line = line.replace("\n", "").split(" ")

                        if line[0].upper() == "<PRT>":
                            newProgram.write("print(")
                            newLine = False
                            printLine = True

                        if line[0].upper() == "<STM>":
                            newProgram.write(" ".join(line[1:len(line)]))
                            newLine = True


                            if printLine:
                                newProgram.write(")")
                                printLine = False

                        if line[0].upper() == "<CMT>":
                            newProgram.write("# " + " ".join(line[1:len(line)]))

                        if line[0].upper() == "<INP>":
                            newProgram.write("input()")

                            if varLine:
                                newLine = True
                                varLine = False

                        if line[0].upper() == "<VAR>":
                            newProgram.write(line[1] + " = ")
                            varLine = True
                            newLine = False

                        if line[0].upper() == "<CON>":
                            newProgram.write(line[1] + ")")
                            newLine = True
                            varLine = False

                        if line[0].upper() == "<CND>":
                            newProgram.write("if ")

                            for element in line[1:len(line)]:
                                if operatorConverter(element) != False:
                                    if operatorConverter(element) != "none":
                                        newProgram.write(operatorConverter(element))
                                else:
                                    newProgram.write(element)

                                newProgram.write(" ")
                            
                            newProgram.write(":")
                            tabIndex += 1

                        if line[0].upper() == "<END>":
                            tabIndex -= 1

                        if newLine:
                            newProgram.write("\n")
                            newProgram.write("  " * tabIndex)

                if run:
                    with open(programName + ".cpld", "r") as newProgram:
                        code = ""
                        for line in newProgram.readlines():
                            code += line

                        exec(code)

                if delete:
                    os.remove(programName + ".cpld")

        input("<<<END>>>")