# About Accessing and Requesting User Input (AutoLISP)

AutoLISP can collect raw input from an input device, in addition to offering a set of functions designed to request specific
types of input from the user.

The following are some of the functions that can be used to get input from the user:

* grread – Reads values from any of the AutoCAD input devices.
* initget – Establishes keywords and controls certain types of input for use by the next user-input function call.
* getstring – Pauses for the input of a string and returns that string.
* getpoint – Pauses for the input of a point and returns that point.
* getint – Pauses for the input of an integer and returns that integer.
* getdist – Pauses for the input of a distance and returns a real number.
* getangle – Pauses for the input of an angle and returns the angle expressed in radians.

## Getting Direct Keyboard and Mouse Input

The grread function returns raw user input, whether from the keyboard or from the pointing device (mouse or digitizer). If the call
to grread enables tracking, the function returns a digitized coordinate that can be used for things such as dragging. The value returned
by grread is a list and the first character defines the type of input that the user provided.

NOTE:There is no guarantee that applications calling grread will be upward compatible. Because it depends on the current hardware configuration, applications that call grread are not likely to work in the same way on all configurations.

The following example code uses grread and checks to see if the input provided was from the keyboard.

```
(defun c:GetCharacter ( / code)
  (prompt "\
Enter a single character: ")

  (setq code (grread))

  (if (= 2 (car code))
    (progn
      (prompt (strcat "\
Character entered was: " (chr (cadr code))))
      (prompt (strcat "\
ASCII code: " (itoa (cadr code))))
    )
    (prompt "\
Input was not from the keyboard.")
  )
 (princ)
)
```

Loading and running the example code results in the following prompt being displayed:

Enter a single character:

Pressing a key on the keyboard displays the character and ASCII code of the key at the AutoCAD Command prompt. For example,
the following is displayed if you press the F key when prompted for a single character and Caps Lock is not enabled or Shift
is not held down:

Character entered was: f

ASCII code: 102

## Requesting Input with the GetXXX Functions

AutoLISP provides several functions to get basic input from the user at the AutoCAD Command prompt. These functions allow
you to request get points, enter text or numbers, and even use keywords to make branching commands. Each user-input getXXX function pauses for data entry of the indicated type and returns the value entered. The application calling one of the functions
can specify an optional prompt to display before the function pauses for input. The initget function does not work with all getXXX functions.

The initget function can be used to control the next call to a getXXX function. This function accepts two arguments, bits and keywords, both of which are optional. The bits argument specifies
one or more control bits that enable or disable certain input values to the next user-input function call. The keywords argument
specifies one or more keywords that the next getXXX function call will recognize. The control bits and keywords established by initget apply only to the next getXXX function call and do not need to be discarded after that call.

The following code uses the getint function to prompt the user for an integer:

```
(defun c:AskForInteger ( / )
  (setq int (getint "\
Enter an integer: "))

  (if int
    (prompt (strcat "\
User entered: " (itoa int)))
    (prompt "\
User did not provide an integer.")
  )
 (princ)
)
```

Loading and running the example code results in the following prompt being displayed:

Enter an integer:

Providing a valid integer returns the value entered for the getint function and that value is displayed as part of the prompt “User entered:” at the AutoCAD Command prompt, but if an invalid
integer is provided the message “Requires an integer value.” is displayed and the user is requested to provide an integer
again. If Enter is pressed before a value is typed, the message “User did not provide an integer.” is displayed.

## Validating Input

You should protect your code from unintentional user errors. The AutoLISP user input getXXX functions do much of this for you. However, it is important to check for adherence to other program requirements that the
getXXX functions do not check for. If you neglect to check input validity, the program's integrity can be seriously affected.

#### Related Concepts

* [About Control Characters in Strings (AutoLISP)](About-Control-Characters-in-Strings-AutoLISP.md)
* [About Controlling User-Input Function Conditions (AutoLISP)](About-Controlling-User-Input-Function-Conditions-AutoLISP.md)
* [About Arbitrary Keyboard Input (AutoLISP)](About-Arbitrary-Keyboard-Input-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [About Angular Conversion (AutoLISP)](About-Angular-Conversion-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*