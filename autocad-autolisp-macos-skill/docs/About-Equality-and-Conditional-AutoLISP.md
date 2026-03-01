# About Equality and Conditional (AutoLISP)

AutoLISP includes functions that provide equality verification as well as conditional branching and looping. The equality
and conditional functions are listed in AutoLISP Function Synopsis (AutoLISP), under the heading Equality and Conditional
Functions (AutoLISP).

When writing code that checks string and symbol table names, keep in mind that AutoLISP automatically converts symbol table
names to upper case in some instances. When testing symbol names for equality, you need to make the comparison insensitive
to the case of the names. Use the strcase function to convert strings to the same case before testing them for equality.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*