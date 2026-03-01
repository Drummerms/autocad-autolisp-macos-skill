# About Xrecord Objects (AutoLISP)

Xrecord objects are used to store and manage arbitrary data.

They are composed of DXF group codes with normal object group codes (that is, non-xdata group codes), ranging from 1 through
369 for supported ranges. These objects are similar in concept to xdata but are not limited by size or order.

The following code examples create and list xrecord data in a custom dictionary named XRECLIST.

```
(defun C:MAKEXRECORD( / xrec xname )
  ; create the xrecord's data list.
  (setq xrec '((0 . "XRECORD")(100 . "AcDbXrecord")
    (1 . "This is a test xrecord list")
    (10 1.0 2.0 0.0) (40 . 3.14159) (50 . 3.14159)
    (62 . 1) (70 . 180))
  )

  ; use entmakex to create the xrecord with no owner.
  (setq xname (entmakex xrec))

  ; add the new xrecord to the named object dictionary.
  (dictadd (namedobjdict) "XRECLIST" xname)
 (princ)
)

(defun C:LISTXRECORD ( / xlist )
  ; find the xrecord in the named object dictionary.
  (setq xlist (dictsearch (namedobjdict) "XRECLIST"))

  ; print out the xrecord's data list.
  (princ xlist)
 (princ)
)
```

The results of the LISTXRECORD command will look similar to the following:

```
((-1 . <Entity name: 7ffffb05ee0>) (0 . XRECORD) (5 . 1E6) (102 . {ACAD_REACTORS) (330 . <Entity name: 7ffffb038c0>) (102 . }) (330 . <Entity name: 7ffffb038c0>) (100 . AcDbXrecord) (280 . 1) (1 . This is a test xrecord list) (10 1.0 2.0 0.0) (40 . 3.14159) (50 . 3.14159) (62 . 1) (70 . 180))
```

#### Related Concepts

* [About Non-Graphical Object Handling (AutoLISP)](About-Non-Graphical-Object-Handling-AutoLISP.md)
* [About Dictionary Objects and Entries (AutoLISP)](About-Dictionary-Objects-and-Entries-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Symbol Tables (AutoLISP)](About-Symbol-Tables-AutoLISP.md)
* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*