# About Extended Data - Xdata (AutoLISP)

Several AutoLISP functions are provided to handle extended data (xdata), which is created by routines written with AutoLISP,
ObjectARX, or Managed .NET.

If an entity contains xdata, it follows the entity's regular definition data. You can retrieve an entity's extended data
by calling entget. The entget function retrieves an entity's regular definition data and the xdata for those applications specified in the entget call.

When xdata is retrieved with entget, the beginning of extended data is indicated by a -3 dxf group code. The -3 dxf group code is in a list that precedes the
first 1001 dxf group code. The 1001 dxf group code contains the application name of the first application retrieved, as shown
in the table and as described in the topics in this section.

| Group codes for regular and extended data | | |
| Group code | Field | Type of data |
| (-1, -2  (0-239        ) | Entity name)  Regular definition data fields)  .  .  . | Normal entity definition data |
| (-3  (1001  (1000,  1002-1071        (1001  (1000,  1002-1071        (1001 | Extended data sentinel  Registered application name 1)    XDATA fields)  .  .  .  Registered application name 2)    XDATA fields)  .  .  .  Registered application name 3)  .  . | Extended data |

#### Topics in this section

* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)

  Extended data consists of one or more 1001 group codes, each of which begin with a unique application name.
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)

  An application must register its name or names to be recognized by AutoCAD.
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)

  An application can obtain the extended data (xdata) that it has attached to an entity with entget.
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)

  You can use extended data (xdata) to store any type of information you want on an entity.
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)

  Extended data is limited to 16K per entity.
* [About Handles in Extended Data (AutoLISP)](About-Handles-in-Extended-Data-AutoLISP.md)

  Extended data can contain handles (dxf group code 1005) to save relational structures within a drawing.

#### Related Concepts

* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [About Handles in Extended Data (AutoLISP)](About-Handles-in-Extended-Data-AutoLISP.md)
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*