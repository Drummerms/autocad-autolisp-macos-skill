# About Symbols and Variables (AutoLISP)

AutoLISP uses symbols to refer to functions and data holders.

Symbol names are not case sensitive and may consist of any sequence of alphanumeric and notation characters, except the following:

| Characters restricted from symbol names | |
| *(* | (Open Parenthesis) |
| *)* | (Close Parenthesis) |
| *.* | (Period) |
| *'* | (Apostrophe) |
| *"* | (Quote Symbol) |
| *;* | (Semicolon) |

A symbol name cannot consist only of numeric characters.

Technically, AutoLISP applications consist of either symbols or constant values, such as strings, reals, and integers. For
the sake of clarity, this documentation uses the term symbol to refer to a symbol name that stores static data, such as built-in
and user-defined functions. Examples of symbols are, the predefined variable T and the defun function.

The term variable is used to refer to a symbol name that stores program data. The following example uses the setq function to assign the string value "this is a string" to the str1 variable:

```
(setq str1 "this is a string")
"this is a string"
```

NOTE:When declaring variables or defining a function, choose meaningful names to make it easy to identify the type of data a variable
holds or the purpose of a function.

#### Topics in this section

* [About Protected Symbols (Visual LISP IDE)](About-Protected-Symbols-Visual-LISP-IDE.md)

  When Visual LISP is loaded, you may be warned if you attempt to change the value of some symbols used by the AutoLISP language.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Formatting and Spaces in Code (AutoLISP)](About-Formatting-and-Spaces-in-Code-AutoLISP.md)
* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*