# About Non-Graphical Object Handling (AutoLISP)

A drawing database contains two types of non-graphical objects: dictionary and symbol table objects.

Although there are similarities between these object types, they are handled differently. All object types are supported by
the entget, entmod, entdel, and entmake functions, although object types individually dictate their participation in these functions and may refuse any or all processing.
With respect to AutoCAD built-in objects, the rules apply for symbol tables and for dictionary objects.

All rules and restrictions that apply to graphical objects apply to non-graphical objects as well. Non-graphical objects cannot
be passed to the entupd function. When using entmake, the object type determines where the object will reside. For example, if a layer object is passed to entmake, it automatically goes to the layer symbol table. If a graphical object is passed to entmake, it will reside in the current space (model or paper).

#### Related Concepts

* [About Dictionary Objects and Entries (AutoLISP)](About-Dictionary-Objects-and-Entries-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [Example: Accessing AutoCAD Groups (AutoLISP)](Example-Accessing-AutoCAD-Groups-AutoLISP.md)
* [FAQ: What Symbol Table Entries Cannot Be Renamed or Modified? (AutoLISP)](FAQ-What-Symbol-Table-Entries-Cannot-Be-Renamed-or-Modified-AutoLISP.md)
* [About Symbol Tables (AutoLISP)](About-Symbol-Tables-AutoLISP.md)
* [About Xrecord Objects (AutoLISP)](About-Xrecord-Objects-AutoLISP.md)
* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*