# About Foreign Language or International Support (AutoLISP)

AutoLISP programs can be used in an AutoCAD release that supports a language other than the original language the program
was developed for.

The standard AutoCAD commands and keywords used in an AutoLISP program can be automatically translated if you precede each
command or keyword with an underscore (\_).

```
(command "_line" pt1 pt2 pt3 "_c")
```

If you are using the dot prefix (to avoid using redefined commands), you can place the dot and underscore in either order.
Both ".\_line" and "\_.line" are valid.

NOTE:It is recommended to always add an underscore (\_) in front of a command name or keyword when using the command or command-s functions; this will help your program to work as expected when executed in a language other than it was originally targeted
for.

#### Related Concepts

* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*