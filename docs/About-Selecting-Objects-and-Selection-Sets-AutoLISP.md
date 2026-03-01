# About Selecting Objects and Selection Sets (AutoLISP)

Selection sets are groups of one or more selected objects (entities).

You can interactively add objects to, remove objects from, or list objects in a selection set. The following example code
uses the
ssget function to return a selection set containing all the objects in a drawing.

```
(ssget "X")
<Selection set: 1>
```

AutoLISP provides a number of functions for handling selection sets. The following lists some of the functions available for
working with selection sets:

* ssget - Prompts the user to select objects (entities), and returns a selection set.
* ssadd - Adds an object (entity) to a selection set, or creates a new selection set.
* ssdel - Removes an object (entity) from a selection set.
* ssname - Returns the object (entity) name of the indexed element of a selection set.
* sslength - Returns an integer containing the number of objects (entities) in a selection set.

The
ssget function provides the most general means of creating a selection set. It can create a selection set in one of the following
ways:

* Explicitly specifying the objects to select, using the Last, Previous, Window, Implied, Window Polygon, Crossing, Crossing
  Polygon, or Fence options
* Specifying a single point
* Selecting all objects in the database
* Prompting the user to select objects

With any option, you can use filtering to specify a list of properties and conditions that the selected objects must match.

NOTE:Selection set and entity names do not remain the same between drawing sessions.

The first argument to
ssget is a string that describes which selection option to use. The next two arguments,
*pt1* and
*pt2*, specify point values for the relevant options (they should be left out if they do not apply). A point list,
*pt-list*, must be provided as an argument to the selection methods that allow selection by polygons (that is, Fence, Crossing Polygon,
and Window Polygon). The last argument,
*filter-list*, is optional. If
*filter-list* is supplied, it specifies the list of entity field values used in filtering. For example, you can obtain a selection set
that includes all objects of a given type, on a given layer, or of a given color.

The following table shows examples of calls to
ssget:

| SSGET Examples | |
| Function call | Effect |
| ``` (setq  pt1 '(0.0 0.0 0.0)        pt2 '(5.0 5.0 0.0)        pt3 '(4.0 1.0 0.0)        pt4 '(2.0 6.0 0.0) ) ``` | Sets pt1, pt2, pt3, and pt4 to point values |
| ``` (setq ss1 (ssget)) ``` | Prompts the user for a general object selection and places those items in a selection set |
| ``` (setq ss1 (ssget "P")) ``` | Creates a selection set from the most recently created selection set |
| ``` (setq ss1 (ssget "L")) ``` | Creates a selection set of the last object added to the database that is visible on the screen |
| ``` (setq ss1 (ssget pt2)) ``` | Creates a selection set of an object passing through point (5,5) |
| ``` (setq ss1 (ssget "W" pt1 pt2)) ``` | Creates a selection set of the objects inside the window from (0,0) to (5,5) |
| ``` (setq ss1 (ssget "F" (list pt2 pt3 pt4))) ``` | Creates a selection set of the objects crossing the fence and defined by the points (5,5), (4,1), and (2,6) |
| ``` (setq ss1 (ssget "WP" (list pt1 pt2 pt3))) ``` | Creates a selection set of the objects inside the polygon defined by the points (0,0), (5,5), and (4,1) |
| ``` (setq ss1 (ssget "X")) ``` | Creates a selection set of all objects in the database |

When an application has finished using a selection set, it is important to release it from memory. This can be done by setting
it to
nil:

```
(setq ss1 nil)
```

RELATED:You can also release the memory used by the values stored in a variable by defining it as a local variable in a function.

Attempting to manage a large number of selection sets simultaneously is not recommended. An AutoLISP application cannot have
more than 128 selection sets open at once. (The limit may be lower on your system.) When the limit is reached, AutoCAD will
not create more selection sets. Keep a minimum number of sets open at a time, and set unneeded selection sets to
nil as soon as possible. If the maximum number of selection sets is reached, you must call the
gc function to free unused memory before another
ssget will work.

#### Topics in this section

* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)

  An entity filter list is an association list that uses DXF group codes in the same format as a list returned by entget.
* [About Passing Selection Sets Between AutoLISP and ObjectARX Applications (AutoLISP)](About-Passing-Selection-Sets-Between-AutoLISP-and-ObjectARX-Applications-AutoLISP.md)

#### Related Concepts

* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)
* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*