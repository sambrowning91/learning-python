# learning-python

This is my Python cheatsheet to help me while i learn Python <br>


<b>Rules for If-Statements</b><br><br>
Every if-statement must have an else.<br>
If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error<br> message and dies, just like we did in the last exercise. This will find many errors.<br>
Never nest if-statements more than two deep and always try to do them one deep.<br>
Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.<br>
Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.<br><br>

Functions Checklist:<br>
Did you start your function definition with def?<br>
Does your function name have only characters and _ (underscore) characters?<br>
Did you put an open parenthesis ( right after the function name?<br>
Did you put your arguments after the parenthesis ( separated by commas?<br>
Did you make each argument unique (meaning no duplicated names)?<br>
Did you put a close parenthesis and a colon ): after the arguments?<br>
Did you indent all lines of code you want in the function four spaces? No more, no less.<br>
Did you "end" your function by going back to writing with no indent (dedenting we call it)?<br>
<br>
N.B. Difference between a function and a method >> A function is a piece of code that is called by name. It can be passed data to operate on (i.e., the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.A method is a piece of code that is called by name that is associated with an object. In most respects it is identical to a function except for two key differences.<br>
<br>
It is implicitly passed for the object for which it was called.<br>
It is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).<br>
<br>
<b> FUNCTIONS </b><br>
print - prints the string, variable, etc.<br>
raw_input() - takes input from a user, note that raw_input should be used over 'input' as the latter has security issues<br>

<br>
<b> METHODS </b><br>
.truncate() - erases all of the data within the file defined by the variable 'text' (i.e. requires text = open(filename))<br>
<br>
<b> MODULES </b><br>
(sys) argv - lets you define a number of command-line arguments to be passed to the script<br>
