# About Attaching Extended Data to an Entity (AutoLISP)

You can use extended data (xdata) to store any type of information you want on an entity.

The xdata attached to an entity might be a record in an external database, a date and time stamp when an entity was added
or modified, or contain information that represents an item in the real-world such as a telephone or workstation. Since xdata
is hidden from the user, it makes it harder to modify without using a custom application.

NOTE:Xdata attached to an entity is maintained when an object is copied in the current drawing or between drawings.

The following example code demonstrates the basics of attaching xdata to the last entity added to a drawing. Before executing
the following example code, draw an entity (such as a line or a circle):

```
; Gets the association list of definition data
; for the last entity.
(setq lastent (entget (entlast)))

; Registers the application name.
(regapp "NEWDATA")

(setq exdata                        ; Sets the variable
  '((-3 ("NEWDATA"                  ; exdata equal to the
    (1000 . "This is a new thing!") ; new extended data—
  )))                               ; in this case, a text
)                                   ; string.

; Appends new data list to entity's list.
(setq newent
  (append lastent exdata))

; Modifies the entity with the new definition data.
(entmod newent)
```

The following example code can be used to verify that your new xdata has been attached to the entity:

```
(entget (car (entsel)) '("NEWDATA"))
```

#### Related Concepts

* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)
* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [About Handles in Extended Data (AutoLISP)](About-Handles-in-Extended-Data-AutoLISP.md)
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*