!!! ATTENTION !!!
YOU NEED TO DOWNLOAD THIS FILE TO READ IT, GITHUB REMOVES SOME ELEMENTS



Functions are defined with < FUNCTION >
The main functions are: <prt> <stm> <inp> <var> <con> <cmt>
Everything else will be ignored
To run the interpreter, open the command prompt, type "interpret.exe -h"
That will give you the help menu for the interpreter

Here is the help for the commands:
. <prt> prints the content below
. <stm> statement, for a string you must type "". You can also consider <stm> as raw data
Example is <stm> "Some Text"
. <inp> input
. <var> declares a variable
Example is <var> aVariableNice
The next line is its value
. <con> gets the content of a variable, combined with <prt> prints the variables value
Example is <con> aVariableNice
. <cmt> comment, but in the build version
Details, this gets ignored in the build, but <cmt> doesnt

This will be an example of all the commands currently:

!!!ATTENTION!!!
NO <cmt> FUNCTION CAN BE DEFINED AFTER <prt> and <var>

<cmt> First we create a variable named "a" and we assign the variable value to the user input
<var> a
<inp>
<cmt> Now we will define a print funcion and we give it a statement
<prt>
<stm> "You typed:"
<cmt> Define another print function and print the variable value
<prt>
<con> a

To run this code
Open the command prompt
Type: .\dist\interpreter.exe -f README.DEMO.MD

Now, if you want to see the diffrence between normal text like this and <cmt>
Open README.DEMO.MD.CPLD
