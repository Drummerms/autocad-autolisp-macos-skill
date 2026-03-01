# About Arbitrary Keyboard Input (AutoLISP)

Arbitrary input allows you to provide a string to most of the getXXX functions as if it is a keyword; control bits and keywords are honored first.

An application using this facility can be written to permit the user to call an AutoLISP function at a getXXX function prompt. You enable arbitrary keyboard input by using the 128 control bit with the initget function.

The following example code defines a command named ARBENTRY and a function named REF. The REF function is used in response to the getpoint function in the ARBENTRY command which is set to allow arbitrary keyboard input.

```
(defun C:ARBENTRY ( / pt1)
  (initget 128)                     ; Sets arbitrary entry bit
  (setq pt1 (getpoint "\
Point: ")) ; Gets value from user.
  (if (= 'STR (type pt1))           ; If it's a string, convert it
    (setq pt1 (eval (read pt1)))    ; to a symbol, try evaluating
                                    ; it as a function; otherwise,
    pt1                             ; just return the value.
  )
)

(defun REF ( )
  (setvar "LASTPOINT" (getpoint "\
Reference point: "))
  (getpoint "\
Next point: " (getvar "LASTPOINT"))
)
```

The following command sequence demonstrates how you can use ARBENTRY and REF together:

Command: *arbentry*

Point: *(ref)*

Reference point: *Select a point*

Next point: *@1,1,0*

#### Related Concepts

* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Controlling User-Input Function Conditions (AutoLISP)](About-Controlling-User-Input-Function-Conditions-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*