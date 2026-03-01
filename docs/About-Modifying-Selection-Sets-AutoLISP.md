# About Modifying Selection Sets (AutoLISP)

Once a selection set has been created, you can add entities to it or remove entities from it with ssadd and ssdel.

You can use the ssadd function to create a new selection set or add entities to an existing selection set. The following example code creates a
selection set that includes the first and last entities in the current drawing (entnext and entlast):

```
(setq fname (entnext))                 ; Gets first entity in the drawing.
(setq lname (entlast))                 ; Gets last entity in the drawing.
(if (not fname)
  (princ "\
No entities in drawing. ")
  (progn
    (setq ourset (ssadd fname))        ; Creates a selection set
                                       ; of the first entity.
    (ssadd lname ourset)               ; Adds the last entity to
                                       ; the selection set.
  )
)
```

The example runs correctly even if only one entity is in the database (in which case both entnext and entlast set their arguments to the same entity name). If ssadd is passed the name of an entity already in the selection set, it ignores the request and does not report an error.

The following example code removes the first entity from the selection set created in the previous example:

```
(ssdel fname ourset)
```

If there is more than one entity in the drawing (that is, if fname and lname are not equal), then the selection set ourset contains only lname, the last entity in the drawing.

The function sslength returns the number of entities in a selection set, and ssmemb tests whether a particular entity is a member of a selection set. Finally, the function ssname returns the name of a particular entity in a selection set, using an index to the set (entities in a selection set are numbered
from 0).

The following example code shows calls to ssname:

```
(setq sset (ssget))                     ; Prompts the user to create
                                        ; a selection set.
(setq ent1 (ssname sset 0))             ; Gets the name of the first
                                        ; entity in sset.
(setq ent4 (ssname sset 3))             ; Gets the name of the fourth
                                        ; entity in sset.
(if (not ent4)
  (princ "\
Need to select at least four entities. ")
)
(setq ilast (sslength sset))            ; Finds index of the last
                                        ; entity in sset.
                                        ; Gets the name of the last
                                        ; entity in sset.
(setq lastent (ssname sset (1- ilast)))
```

Regardless of how entities are added to a selection set, the set never contains duplicate entities. If the same entity is
added more than once, the later additions are ignored. Therefore, sslength accurately returns the number of distinct entities in the specified selection set.

#### Related Concepts

* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)
* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*