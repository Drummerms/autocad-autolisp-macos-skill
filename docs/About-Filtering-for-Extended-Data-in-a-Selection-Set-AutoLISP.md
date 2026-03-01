# About Filtering for Extended Data in a Selection Set (AutoLISP)

You can select all entities containing extended data for a particular application using the *filter-list* argument of ssget.

The *filter-list* argument must be a list that contains -3 as its first element. The following example code selects all the objects in a drawing
that include extended data for the "APPNAME" application:

```
(ssget "X" '((-3 ("APPNAME"))))
```

You can also expand the scope of the filter to filter specific types of objects. The following example code selects all the
circles in a drawing that include extended data for the "APPNAME" application:

```
(ssget "X" '((0 . "CIRCLE") (-3 ("APPNAME"))))
```

If more than one application name is included in the -3 group's list, an AND operation is implied and the entity must contain extended data for all of the specified applications. So, the following statement
would select all the objects with extended data for both the "APP1" and "APP2" applications:

```
(ssget "X" '((-3 ("APP1")("APP2"))))
```

Wild-card matching is also permitted, so either of the following statements will select all the objects with extended data
for either or both of these applications.

```
(ssget "X" '((-3 ("APP[12]"))))
(ssget "X" '((-3 ("APP1,APP2"))))
```

#### Related Concepts

* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*