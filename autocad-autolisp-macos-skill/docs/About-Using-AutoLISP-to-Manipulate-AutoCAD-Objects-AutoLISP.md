# About Using AutoLISP to Manipulate AutoCAD Objects (AutoLISP)

You can select and handle objects, and use their extended data.

Most AutoLISP ®  functions that handle selection sets and objects identify a set or an object by the entity name. For selection sets, which
are valid only in the current session, the volatility of names poses no problem, but it does for objects because they are
saved in the drawing database. An application that must refer to the same objects in the same drawing (or drawings) at different
times can use the objects' handles.

AutoLISP uses symbol tables to maintain lists of graphic and non-graphic data related to a drawing, such as the layers, linetypes,
and block definitions. Each symbol table entry has a related entity name and handle and can be manipulated in a manner similar
to the way other AutoCAD ®  entities are manipulated.

#### Topics in this section

* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)

  Selection sets are groups of one or more selected objects (entities).
* [About Object Handling (AutoLISP)](About-Object-Handling-AutoLISP.md)
* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)

  Several AutoLISP functions are provided to handle extended data (xdata), which is created by routines written with AutoLISP,
  ObjectARX, or Managed .NET.
* [About Xrecord Objects (AutoLISP)](About-Xrecord-Objects-AutoLISP.md)

  Xrecord objects are used to store and manage arbitrary data.
* [About Symbol Table and Dictionary Access (AutoLISP)](About-Symbol-Table-and-Dictionary-Access-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*