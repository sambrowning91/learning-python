# learning-python

This is my Python cheatsheet to help me while I learn Python <br>


<b>Rules for If-Statements</b><br>
Every if-statement must have an else.<br>
If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error<br> message and dies, just like we did in the last exercise. This will find many errors.<br>
Never nest if-statements more than two deep and always try to do them one deep.<br>
Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.<br>
Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.<br><br>
<b>Rules for Loops</b><br>
Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.<br>
Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.

<b>Functions Checklist:</b><br>
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
<br>
<b> KEYWORDS </b>
<table>
  <tr>
    <td>KEYWORD</td>
    <td>DESCRIPTION</td>
    <td>EXAMPLE</td>
<tr><td>and</td>
  <td>Logical and.</td>
  <td>True and False == False</td>
  </tr>
<tr><td>as</td>
  <td>Part of the <cite>with-as</cite> statement.</td>
  <td>with X as Y: pass</td>
  </tr>
<tr><td>assert</td>
  <td>Assert (ensure) that something is true.</td>
  <td>assert False, "Error!"</td>
  </tr>
<tr><td>break</td>
  <td>Stop this loop right now.</td>
  <td>while True: break</td>
  </tr>
<tr><td>class</td>
  <td>Define a class.</td>
  <td>class Person(object)</td>
  </tr>
<tr><td>continue</td>
  <td>Don't process more of the loop, do it again.</td>
  <td>while True: continue</td>
  </tr>
<tr><td>def</td>
  <td>Define a function.</td>
  <td>def <span class="pre">X():</span> pass</td>
  </tr>
<tr><td>del</td>
  <td>Delete from dictionary.</td>
  <td>del X[Y]</td>
  </tr>
<tr><td>elif</td>
  <td>Else if condition.</td>
  <td>if: X; elif: Y; else: J</td>
  </tr>
<tr><td>else</td>
  <td>Else condition.</td>
  <td>if: X; elif: Y; else: J</td>
  </tr>
<tr><td>except</td>
  <td>If an exception happens, do this.</td>
  <td>except ValueError, e: print e</td>
  </tr>
<tr><td>exec</td>
  <td>Run a string as Python.</td>
  <td>exec 'print "hello"'</td>
  </tr>
<tr><td>finally</td>
  <td>Exceptions or not, finally do this no matter what.</td>
  <td>finally: pass</td>
  </tr>
<tr><td>for</td>
  <td>Loop over a collection of things.</td>
  <td>for X in Y: pass</td>
  </tr>
<tr><td>from</td>
  <td>Importing specific parts of a module.</td>
  <td>from x import Y</td>
  </tr>
<tr><td>global</td>
  <td>Declare that you want a global variable.</td>
  <td>global X</td>
  </tr>
<tr><td>if</td>
  <td>If condition.</td>
  <td>if: X; elif: Y; else: J</td>
  </tr>
<tr><td>import</td>
  <td>Import a module into this one to use.</td>
  <td>import os</td>
  </tr>
<tr><td>in</td>
  <td>Part of <span class="pre">for-loops</span>. Also a test of X in Y.</td>
  <td>for X in Y: pass also 1 in [1] == True</td>
  </tr>
<tr><td>is</td>
  <td>Like == to test equality.</td>
  <td>1 is 1 == True</td>
  </tr>
<tr><td>lambda</td>
  <td>Create a short anonymous function.</td>
  <td>s = lambda y: y ** y; s(3)</td>
  </tr>
<tr><td>not</td>
  <td>Logical not.</td>
  <td>not True == False</td>
  </tr>
<tr><td>or</td>
  <td>Logical or.</td>
  <td>True or False == True</td>
  </tr>
<tr><td>pass</td>
  <td>This block is empty.</td>
  <td>def <span class="pre">empty():</span> pass</td>
  </tr>
<tr><td>print</td>
  <td>Print this string.</td>
  <td>print 'this string'</td>
  </tr>
<tr><td>raise</td>
  <td>Raise an exception when things go wrong.</td>
  <td>raise <span class="pre">ValueError("No")</span></td>
  </tr>
<tr><td>return</td>
  <td>Exit the function with a return value.</td>
  <td>def <span class="pre">X():</span> return Y</td>
  </tr>
<tr><td>try</td>
  <td>Try this block, and if exception, go to except.</td>
  <td>try: pass</td>
  </tr>
<tr><td>while</td>
  <td>While loop.</td>
  <td>while X: pass</td>
  </tr>
<tr><td>with</td>
  <td>With an expression as a variable do.</td>
  <td>with X as Y: pass</td>
  </tr>
<tr><td>yield</td>
  <td>Pause here and return to caller.</td>
  <td>def <span class="pre">X():</span> yield Y; <span class="pre">X().next()</span></td>
  </tr>
</table>
<br>
<b> DATA TYPES </b>

<table>
  <tr>
    <td>TYPE</td>
    <td>DESCRIPTION</td>
    <td>EXAMPLE</td>
<tbody valign="top">
<tr><td><tt class="docutils literal">True</tt></td>
<td>True boolean value.</td>
<td><tt class="docutils literal">True or False == True</tt></td>
</tr>
<tr><td><tt class="docutils literal">False</tt></td>
<td>False boolean value.</td>
<td><tt class="docutils literal">False and True == False</tt></td>
</tr>
<tr><td><tt class="docutils literal">None</tt></td>
<td>Represents "nothing" or "no value".</td>
<td><tt class="docutils literal">x = None</tt></td>
</tr>
<tr><td><tt class="docutils literal">strings</tt></td>
<td>Stores textual information.</td>
<td><tt class="docutils literal">x = "hello"</tt></td>
</tr>
<tr><td><tt class="docutils literal">numbers</tt></td>
<td>Stores integers.</td>
<td><tt class="docutils literal">i = 100</tt></td>
</tr>
<tr><td><tt class="docutils literal">floats</tt></td>
<td>Stores decimals.</td>
<td><tt class="docutils literal">i = 10.389</tt></td>
</tr>
<tr><td><tt class="docutils literal">lists</tt></td>
<td>Stores a list of things.</td>
<td><tt class="docutils literal">j = [1,2,3,4]</tt></td>
</tr>
<tr><td><tt class="docutils literal">dicts</tt></td>
<td>Stores a key=value mapping of things.</td>
<td><tt class="docutils literal">e = {'x': 1, 'y': 2}</tt></td>
</tr>
</table>

<br>

<b> STRING ESCAPE SEQUENCES </b>
<table>
<tbody valign="top">
<tr><td><tt class="docutils literal">\\</tt></td>
<td>Backslash</td>
</tr>
<tr><td><tt class="docutils literal">\'</tt></td>
<td>Single-quote</td>
</tr>
<tr><td><tt class="docutils literal">\"</tt></td>
<td>Double-quote</td>
</tr>
<tr><td><tt class="docutils literal">\a</tt></td>
<td>Bell</td>
</tr>
<tr><td><tt class="docutils literal">\b</tt></td>
<td>Backspace</td>
</tr>
<tr><td><tt class="docutils literal">\f</tt></td>
<td>Formfeed</td>
</tr>
<tr><td><tt class="docutils literal">\n</tt></td>
<td>Newline</td>
</tr>
<tr><td><tt class="docutils literal">\r</tt></td>
<td>Carriage</td>
</tr>
<tr><td><tt class="docutils literal">\t</tt></td>
<td>Tab</td>
</tr>
<tr><td><tt class="docutils literal">\v</tt></td>
<td>Vertical tab</td>
</tr>
</table>
<br>
<b> STRING FORMATS </b>
<table>
<tbody valign="top">
<tr><td><tt class="docutils literal">%d</tt></td>
<td>Decimal integers (not floating point).</td>
<td><tt class="docutils literal">"%d" % 45 == '45'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%i</tt></td>
<td>Same as %d.</td>
<td><tt class="docutils literal">"%i" % 45 == '45'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%o</tt></td>
<td>Octal number.</td>
<td><tt class="docutils literal">"%o" % 1000 == '1750'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%u</tt></td>
<td>Unsigned decimal.</td>
<td><tt class="docutils literal">"%u" % <span class="pre">-1000</span> == <span class="pre">'-1000'</span></tt></td>
</tr>
<tr><td><tt class="docutils literal">%x</tt></td>
<td>Hexadecimal lowercase.</td>
<td><tt class="docutils literal">"%x" % 1000 == '3e8'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%X</tt></td>
<td>Hexadecimal uppercase.</td>
<td><tt class="docutils literal">"%X" % 1000 == '3E8'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%e</tt></td>
<td>Exponential notation, lowercase 'e'.</td>
<td><tt class="docutils literal">"%e" % 1000 == '1.000000e+03'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%E</tt></td>
<td>Exponential notation, uppercase 'E'.</td>
<td><tt class="docutils literal">"%E" % 1000 == '1.000000E+03'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%f</tt></td>
<td>Floating point real number.</td>
<td><tt class="docutils literal">"%f" % 10.34 == '10.340000'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%F</tt></td>
<td>Same as %f.</td>
<td><tt class="docutils literal">"%F" % 10.34 == '10.340000'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%g</tt></td>
<td>Either %f or %e, whichever is shorter.</td>
<td><tt class="docutils literal">"%g" % 10.34 == '10.34'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%G</tt></td>
<td>Same as %g but uppercase.</td>
<td><tt class="docutils literal">"%G" % 10.34 == '10.34'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%c</tt></td>
<td>Character format.</td>
<td><tt class="docutils literal">"%c" % 34 == '"'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%r</tt></td>
<td>Repr format (debugging format).</td>
<td><tt class="docutils literal">"%r" % int == "&lt;type <span class="pre">'int'&gt;"</span></tt></td>
</tr>
<tr><td><tt class="docutils literal">%s</tt></td>
<td>String format.</td>
<td><tt class="docutils literal">"%s there" % 'hi' == 'hi there'</tt></td>
</tr>
<tr><td><tt class="docutils literal">%%</tt></td>
<td>A percent sign.</td>
<td><tt class="docutils literal"><span class="pre">"%g%%"</span> % 10.34 == '10.34%'</tt></td>
</tr>
</table>
<br>
<b> OPERATORS </b>
<table>
<tbody valign="top">
<tr><td><tt class="docutils literal">+</tt></td>
<td>Addition</td>
<td><tt class="docutils literal">2 + 4 == 6</tt></td>
</tr>
<tr><td><tt class="docutils literal">-</tt></td>
<td>Subtraction</td>
<td><tt class="docutils literal">2 - 4 == <span class="pre">-2</span></tt></td>
</tr>
<tr><td><tt class="docutils literal">*</tt></td>
<td>Multiplication</td>
<td><tt class="docutils literal">2 * 4 == 8</tt></td>
</tr>
<tr><td><tt class="docutils literal">**</tt></td>
<td>Power of</td>
<td><tt class="docutils literal">2 ** 4 == 16</tt></td>
</tr>
<tr><td><tt class="docutils literal">/</tt></td>
<td>Division</td>
<td><tt class="docutils literal">2 / 4.0 == 0.5</tt></td>
</tr>
<tr><td><tt class="docutils literal">//</tt></td>
<td>Floor division</td>
<td><tt class="docutils literal">2 // 4.0 == 0.0</tt></td>
</tr>
<tr><td><tt class="docutils literal">%</tt></td>
<td>String interpolate or modulus</td>
<td><tt class="docutils literal">2 % 4 == 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">&lt;</tt></td>
<td>Less than</td>
<td><tt class="docutils literal">4 &lt; 4 == False</tt></td>
</tr>
<tr><td><tt class="docutils literal">&gt;</tt></td>
<td>Greater than</td>
<td><tt class="docutils literal">4 &gt; 4 == False</tt></td>
</tr>
<tr><td><tt class="docutils literal">&lt;=</tt></td>
<td>Less than equal</td>
<td><tt class="docutils literal">4 &lt;= 4 == True</tt></td>
</tr>
<tr><td><tt class="docutils literal">&gt;=</tt></td>
<td>Greater than equal</td>
<td><tt class="docutils literal">4 &gt;= 4 == True</tt></td>
</tr>
<tr><td><tt class="docutils literal">==</tt></td>
<td>Equal</td>
<td><tt class="docutils literal">4 == 5 == False</tt></td>
</tr>
<tr><td><tt class="docutils literal">!=</tt></td>
<td>Not equal</td>
<td><tt class="docutils literal">4 != 5 == True</tt></td>
</tr>
<tr><td><tt class="docutils literal">&lt;&gt;</tt></td>
<td>Not equal</td>
<td><tt class="docutils literal">4 &lt;&gt; 5 == True</tt></td>
</tr>
<tr><td><tt class="docutils literal">( )</tt></td>
<td>Parenthesis</td>
<td><tt class="docutils literal"><span class="pre">len('hi')</span> == 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">[ ]</tt></td>
<td>List brackets</td>
<td><tt class="docutils literal">[1,3,4]</tt></td>
</tr>
<tr><td><tt class="docutils literal">{ }</tt></td>
<td>Dict curly braces</td>
<td><tt class="docutils literal">{'x': 5, 'y': 10}</tt></td>
</tr>
<tr><td><tt class="docutils literal">@</tt></td>
<td>At (decorators)</td>
<td><tt class="docutils literal">@classmethod</tt></td>
</tr>
<tr><td><tt class="docutils literal">,</tt></td>
<td>Comma</td>
<td><tt class="docutils literal">range(0, 10)</tt></td>
</tr>
<tr><td><tt class="docutils literal">:</tt></td>
<td>Colon</td>
<td><tt class="docutils literal">def <span class="pre">X():</span></tt></td>
</tr>
<tr><td><tt class="docutils literal">.</tt></td>
<td>Dot</td>
<td><tt class="docutils literal">self.x = 10</tt></td>
</tr>
<tr><td><tt class="docutils literal">=</tt></td>
<td>Assign equal</td>
<td><tt class="docutils literal">x = 10</tt></td>
</tr>
<tr><td><tt class="docutils literal">;</tt></td>
<td>semi-colon</td>
<td><tt class="docutils literal">print "hi"; print "there"</tt></td>
</tr>
<tr><td><tt class="docutils literal">+=</tt></td>
<td>Add and assign</td>
<td><tt class="docutils literal">x = 1; x += 2</tt></td>
</tr>
<tr><td><tt class="docutils literal"><span class="pre">-=</span></tt></td>
<td>Subtract and assign</td>
<td><tt class="docutils literal">x = 1; x <span class="pre">-=</span> 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">*=</tt></td>
<td>Multiply and assign</td>
<td><tt class="docutils literal">x = 1; x *= 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">/=</tt></td>
<td>Divide and assign</td>
<td><tt class="docutils literal">x = 1; x /= 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">//=</tt></td>
<td>Floor divide and assign</td>
<td><tt class="docutils literal">x = 1; x //= 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">%=</tt></td>
<td>Modulus assign</td>
<td><tt class="docutils literal">x = 1; x %= 2</tt></td>
</tr>
<tr><td><tt class="docutils literal">**=</tt></td>
<td>Power assign</td>
<td><tt class="docutils literal">x = 1; x **= 2</tt></td>
</tr>
</table>
