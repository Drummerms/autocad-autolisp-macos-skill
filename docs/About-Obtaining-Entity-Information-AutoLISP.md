# About Obtaining Entity Information (AutoLISP)

The entget function returns the definition data of a specified entity as a list.

Each item in the list is specified by a DXF group code. The first item in the list contains the entity's current name.

In this example, the following (default) conditions apply to the current drawing:

* Layer is 0
* Linetype is CONTINUOUS
* Elevation is 0

The user has drawn a line with the following sequence of commands:

Command:  *line*

From point:  *1,2*

To point:  *6,6*

To point:  *Press Enter*

An AutoLISP application can retrieve and output the definition data for the line by using the following example code:

```
(defun C:PRINTDXF ( )
  (setq ent (entlast))               ; Set ent to last entity.
  (setq entl (entget ent))           ; Set entl to association list of last entity.
  (setq ct 0)                        ; Set ct (a counter) to 0.
  (textpage)                         ; Switch to the text screen.
  (princ "\
entget of last entity:")
  (repeat (length entl)              ; Repeat for number of members in list:
    (print (nth ct entl))            ; Output a newline, then each list member.
    (setq ct (1+ ct))                ; Increments the counter by one.
  )
 (princ)                             ; Exit quietly.
)
```

This would output the following:

```
entget of last entity:
(-1 . <Entity name: 1bbd1c8>)
(0 . "LINE")
(330 . <Entity name: 1bbd0c8>)
(5 . "69")
(100 . "AcDbEntity")
(67 . 0)
(410 . "Model")
(8 . "0")
(100 . "AcDbLine")
(10 1.0 2.0 0.0)
(11 6.0 6.0 0.0)
(210 0.0 0.0 1.0)
```

The -1 item at the start of the list contains the name of the entity. The entmod function, which is described in this section, uses the name to identify the entity to be modified. The individual dotted
pairs that represent the values can be extracted by using assoc with the cdr function.

Sublists for points are not represented as dotted pairs like the rest of the values returned. The convention is that the cdr of the sublist is the group code's value. Because a point is a list of two or three reals, the entire group is a three- (or
four-) element list. The cdr of the group code value is the list representing the point, so the convention that cdr always returns the value is preserved.

The group codes for the components of the entity are those used by DXF. As with DXF, the entity header items (color, linetype,
thickness, the attributes-follow flag, and the entity handle) are returned only if they have values other than the default.
Unlike DXF, optional entity definition fields are returned whether or not they equal their defaults and whether or not associated
*X*, *Y*, and *Z* coordinates are returned as a single point variable, rather than as separate *X* (10), *Y* (20), and *Z* (30) group codes.

All points associated with an object are expressed in terms of that object's Object Coordinate System (OCS). For point, line,
3D line, 3D face, 3D polyline, 3D mesh, and dimension objects, the OCS is equivalent to the WCS (the object points are World
points). For all other objects, the OCS can be derived from the WCS and the object's extrusion direction (its 210 group code).
When working with objects that are drawn using coordinate systems other than the WCS, you may need to convert the points to
the WCS or to the current UCS by using the trans function.

When writing functions to process entity lists, make sure the function logic is independent of the order of the sublists;
use assoc to guarantee this. The assoc function searches a list for a group code of a specified type. The following code returns the object type "LINE" (0) from
the list entl.

```
(cdr (assoc 0 entl))
```

If the group code specified is not present in the list (or if it is not a valid group code), assoc returns nil.

IMPORTANT:Before performing an entget on vertex entities, you should read or write the polyline entity's header. If the most recently processed polyline entity
is different from the one to which the vertex belongs, width information (the 40 and 41 group codes) can be lost.

#### Related Concepts

* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Deleting an Entity (AutoLISP)](About-Deleting-an-Entity-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*