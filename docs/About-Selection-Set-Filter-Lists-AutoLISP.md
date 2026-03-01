# About Selection Set Filter Lists (AutoLISP)

An entity filter list is an association list that uses DXF group codes in the same format as a list returned by entget.

The ssget function recognizes all group codes except entity names (group code -1), handles (group code 5), and xdata (group codes greater
than 1000). If an invalid group code is used in a filter-list, it is ignored by ssget. Use the group code -3 to search for objects with xdata. When a filter-list is provided as the last argument to ssget, the function scans the selected objects and creates a selection set containing the names of all main entities matching the
specified criteria. The *filter-list* specifies which property (or properties) of the entities are to be checked and which values constitute a match.

For example, you can obtain a selection set that includes all objects of a given type, on a given layer, or of a given color.

The following examples demonstrate different methods of using a *filter-list* with various object selection options.

| SSGET examples using filter lists | |
| Function call | Effect |
| (setq ss1  (ssget '((0 . "TEXT")))  ) | Prompts for general object selection but adds only text objects to the selection set. |
| (setq ss1  (ssget "P" '((0 . "LINE")))  ) | Creates a selection set containing all line objects from the last selection set created. |
| (setq ss1  (ssget "W" pt1 pt2 '((8 . "FLOOR9")))  ) | Creates a selection set of all objects inside the window that are also on layer FLOOR9. |
| (setq ss1  (ssget "X" '((0 . "CIRCLE")))  ) | Creates a selection set of all objects in the database that are Circle objects. |
| (setq ss1  (ssget "I" '((0 . "LINE") (62 . 5)))  ) | Creates a selection set of all blue Line objects that are part of the Implied selection set (those objects selected while the AutoCAD PICKFIRST system variable is in effect).  Note that this filter picks up lines that have been assigned color 5 (blue), but not blue lines that have had their color applied by the ByLayer or ByBlock properties. |

If both the group code and the desired value are known, the list may be quoted as shown previously. If either is specified
by a variable, the list must be constructed using the list and cons function. For example, the following code creates a selection set of all objects in the database that are on layer FLOOR3:

```
(setq lay_name "FLOOR3")
(setq ss1
  (ssget "X"
    (list (cons 8 lay_name))
  )
)
```

If the *filter-list* specifies more than one property, an entity is included in the selection set only if it matches all specified conditions,
as in the following example code:

```
(ssget "X" (list (cons 0 "CIRCLE")(cons 8 lay_name)(cons 62 3)))
```

This code selects only Circle objects on layer FLOOR3 that are colored green. This type of test performs a Boolean “AND” operation.

The ssget function filters a selection set by scanning the selected entities and comparing the fields of each main entity against the
specified filtering list. If an entity's properties match all specified fields in the filtering list, it is included in the
returned selection set. Otherwise, the entity is not included in the selection set. The ssget function returns nil if none of the selected entities match the specified filtering criteria.

NOTE:The meaning of certain group codes can differ from entity to entity, and not all group codes are present in all entities.
If a particular group code is specified in a filter, entities not containing that group code are excluded from the selection
set that ssget returns.

When ssget filters a selection set, the selected objects it retrieves might include entities from both paper space and model space.
However, when the selection set is passed to an AutoCAD command, only entities from the space that is currently in effect
are used. (The space to which an entity belongs is specified by the value of its 67 group code.)

#### Topics in this section

* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)

  Symbol names specified in filtering lists can include wild-card patterns.
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)

  You can select all entities containing extended data for a particular application using the filter-list argument of ssget.
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)

  Unless otherwise specified, an equivalency is implied for each item in the
  filter-list.
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)

  You can define test groups with nested Boolean expressions to filter objects from a selection set created with ssget.
* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)

  Once a selection set has been created, you can add entities to it or remove entities from it with ssadd and ssdel.

#### Related Concepts

* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)
* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*