# To declare local variables (AutoLISP)

Local variables are only accessible within the user-defined function that they are defined in.

1. In the arguments and variables list of the defun function, add a forward slash ( */* ) delimiter to the list.
2. After the forward slash, list each local variable.

   Be certain there is at least one space between the slash and each local variable.

## Example

The LOCAL function in the following example defines two local variables: aaa and bbb.

1. At the AutoCAD Command prompt, enter the following code:

   ```
   (defun LOCAL ( / aaa bbb)
     (setq aaa "A" bbb "B")
     (princ (strcat "\
   aaa has the value " aaa ))
     (princ (strcat "\
   bbb has the value " bbb))
     (princ)
   )
   LOCAL
   ```

   NOTE:You can also add the example code to an existing or create a new LSP file. Then load the LSP file with the APPLOAD command.
2. Enter the following code to define two global variables before using the LOCAL function:

   ```
   (setq aaa 1 bbb 2)
   2
   ```
3. Enter the following code to check the value of the two global variables:

   ```
   !aaa
   1

   !bbb
   2
   ```
4. Enter the following code to check the value of the two local variables:

   ```
   (local)
   aaa has the value A
   bbb has the value B
   ```

   You will notice the function used the values for aaa and bbb that are local within the function. The current values for aaa and bbb are still set to their global values and can be verified with the following statements:

   ```
   !aaa
   1

   !bbb
   2
   ```

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Symbols and Variables (AutoLISP)](About-Symbols-and-Variables-AutoLISP.md)
* [About Predefined Variables (AutoLISP)](About-Predefined-Variables-AutoLISP.md)
* [About Nil Variables (AutoLISP)](About-Nil-Variables-AutoLISP.md)
* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*