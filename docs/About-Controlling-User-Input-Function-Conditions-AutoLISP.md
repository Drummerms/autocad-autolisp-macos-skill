# About Controlling User-Input Function Conditions (AutoLISP)

The
initget function provides a level of control over the next user-input function call.

The
initget function establishes various options for use by the next
entsel,
nentsel,
nentselp, or
getXXX function (except
getstring,
getvar, and
getenv). This function accepts two arguments, bits and string, both of which are optional. The
*bits* argument specifies one or more control bits that enable or disable certain input values to the next user-input function call.
The
*string* argument can specify keywords that the next user-input function call will recognize.

The control bits and keywords established by
initget apply only to the next user-input function call. They are discarded after that call. The application does not have to call
initget a second time to clear special conditions.

## Setting Input Options

The value of the bits argument of
initget restricts the types of user input to the next user-input function call. This reduces error-checking.

The following are some of the available bit values:

* 1 - disallows null input
* 2 - disallows input of 0 (zero)
* 4 - disallows negative input

More than one condition can be set at a time by adding the values together (in any combination) to create a bits value between
0 and 255. If bits is not included or is set to 0, none of the control conditions applies to the next user-input function
call. (For a complete listing of
initget bit settings.)

As an example, if these values are set before a call to the
getint function, the user is forced to enter an integer value greater than 0.

```
(initget (+ 1 2 4))
(getint "\
How old are you? ")
```

This sequence requests the user's age. AutoCAD displays an error message and repeats the prompt if the user attempts to enter
a negative or zero value, or if the user only presses Enter, or enters a string (the
getint function rejects attempts to enter a value that is not an integer).

## Setting Keyword Options

The optional string argument of
initget specifies a list of keywords recognized by the next user-input function call. The user-input function returns one of the
predefined keywords if the input from the user matches the spelling of a keyword (not case sensitive), or if the user enters
the abbreviation of a keyword.

NOTE:A keyword can't contain the underscore character as it has a special meaning in a keywords list. The underscore character
is the separator between the global and localized keyword lists.

The following example code demonstrates how to define two keywords with
initget before a call to
getreal. The program checks for these keywords and sets the input value accordingly.

```
(defun C:GETNUM (/ num)
  (initget 1 "Pi Two-pi")
  (setq num (getreal "Pi/Two-pi/<number>: "))
  (cond
    ((eq num "Pi") pi)
    ((eq num "Two-pi") (* 2.0 pi))
    (T num)
  )
)
```

The bits argument of
initget is passed a value of 1 which inhibits null input, and the string argument is passed a string value that represents two keywords,
"Pi" and "Two-pi". The
getreal function is used to obtain a real number, issuing the following prompt:

Pi/Two-pi/<number>:

The result is placed in the local variable symbol
num. If the user enters a number, that number is returned by
C:GETNUM. However, if the user enters the keyword Pi (or simply P),
getreal returns the keyword Pi. The cond function detects this and returns the value of
PI in this case. The Two-pi keyword is handled similarly.

NOTE:You can also use
initget to enable
entsel,
nentsel, and
nentselp to accept keyword input.

#### Topics in this section

* [About Arbitrary Keyboard Input (AutoLISP)](About-Arbitrary-Keyboard-Input-AutoLISP.md)

  Arbitrary input allows you to provide a string to most of the getXXX functions as if it is a keyword; control bits and keywords
  are honored first.

#### Related Concepts

* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Arbitrary Keyboard Input (AutoLISP)](About-Arbitrary-Keyboard-Input-AutoLISP.md)
* [About Control Characters in Strings (AutoLISP)](About-Control-Characters-in-Strings-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*