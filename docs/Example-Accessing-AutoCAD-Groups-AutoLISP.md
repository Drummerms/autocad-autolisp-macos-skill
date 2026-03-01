# Example: Accessing AutoCAD Groups (AutoLISP)

This example demonstrates one method for accessing the entities contained in a group.

This example assumes a group named G1 exists in the current drawing.

```
(setq objdict (namedobjdict))
(setq grpdict (dictsearch objdict "ACAD_GROUP"))
```

This sets the grpdict variable to the entity definition list of the ACAD\_GROUP dictionary and returns the following:

```
((-1 . <Entity name: 8dc10468>) (0 . "DICTIONARY") (5 . "D")
(102 . "{ACAD_REACTORS") (330 . <Entity name: 8dc10460>)
(102 . "}") (100 . "AcDbDictionary") (3 . "G1")
(350 . <Entity name: 8dc41240>))
```

The following code sets the variable group1 to the entity definition list of the G1 group:

```
(setq group1 (dictsearch (cdar grpdict) "G1"))

((-1 . <Entity name: 8dc10518>) (0 . "GROUP") (5 . "23")
(102 . "{ACAD_REACTORS") (330 . <Entity name: 8dc10468>)
(102 . "}") (100 . "AcDbGroup") (300 . "line and circle") (70 . 0) (71
. 1) (340 . <Entity name: 8dc10510>)(340 . <Entity name: 8dc10550>))
```

The 340 group codes are the entities that belong to the group.

#### Related Concepts

* [About Dictionary Objects and Entries (AutoLISP)](About-Dictionary-Objects-and-Entries-AutoLISP.md)
* [About Non-Graphical Object Handling (AutoLISP)](About-Non-Graphical-Object-Handling-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*