import sys

argv = sys.argv
programName = "null"
run = True
delete = False
exitFunction = False

try:
    if argv[1] == "-h":
        print('''
    HELP MENU

    arguments:

    ARGUMENT    EXAMPLE       OPTIONAL    DESCRIPTION

    -h          -h               O        Displays this help menu

    -f          -f file          N        The file to run

    -a          -a c/cr/crd      Y        The arguments for the compiler (DEFAULT: cr)
                                        c: just compile
                                        cr: compile then run
                                        crd: compile, run and finally delete the compiled file

    OPTIONAL EXPLANATION

    O: The only argument
    N: Not optional (REQUIRED)
    Y: Optional
        ''')
        input("<<<END>>>")

        exitFunction = True
except IndexError:
    pass

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

    if programName == "null":
        print("No file specifien. Try '-h' for help")
        input("<<<END>>>")
        exitFunction = True

    if not exitFunction:
        newLine = True
        printLine = False
        varLine = True

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


                    if newLine:
                        newProgram.write("\n")

            if run:
                with open(programName + ".cpld", "r") as newProgram:
                    code = ""
                    for line in newProgram.readlines():
                        code += line

                    exec(code)

            if delete:
                import os
                os.remove(programName + ".cpld")

        input("<<<END>>>")