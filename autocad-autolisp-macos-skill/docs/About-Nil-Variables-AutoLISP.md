# About Nil Variables (AutoLISP)

A variable that has not been assigned a value has a default value of nil.

This is different from blank, which is considered a character string, and different from 0, which is a number. So, in addition
to checking a variable for its current value, you can test to determine if the variable has been assigned a value.

Each variable consumes a small amount of memory, so it is good programming practice to reuse variable names or set variables
to nil when their values are no longer needed. Setting a variable to nil releases the memory used to store that variable's value. If you no longer need the val variable, you can release its value from memory with the following expression:

```
(setq val nil)
nil
```

Another efficient programming practice is to use local variables whenever possible.

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Predefined Variables (AutoLISP)](About-Predefined-Variables-AutoLISP.md)
* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*