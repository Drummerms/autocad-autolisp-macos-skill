# OLE2FRAME (DXF)

The following group codes apply to ole2frame entities. This information is read-only. During OPEN, the values are ignored
because they are part of the OLE binary object, and are obtained by access functions.

| Ole2frame group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbOle2Frame) |
| 70 | OLE version number |
| 3 | Length of binary data |
| 10 | Upper-left corner (WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of upper-left corner (in WCS) |
| 11 | Lower-right corner (WCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of lower-right corner (in WCS) |
| 71 | OLE object type, 1 = Link; 2 = Embedded; 3 = Static |
| 72 | Tile mode descriptor:  0 = Object resides in model space  1 = Object resides in paper space |
| 90 | Length of binary data |
| 310 | Binary data (multiple lines) |
| 1 | End of OLE data (the string “OLE”) |

Sample DXF output:

```
    OLE2FRAME
      5
    2D
    100
    AcDbEntity
     67
         1
      8
    0
    100
    AcDbOle2Frame
     70
         2
      3
    Paintbrush Picture
     10
    4.43116
     20
    5.665992
     30
    0.0
     11
    6.4188
     21
    4.244939
     31
    0.0
     71
         2
     72
         1
     90
        23680
    310   0155764BD60082B91140114B08C8F9A916400000000000000000506DC0D0D9AC
    310
    1940114B08C8F9A916400000000000000000506DC0D0D9AC194002303E5CD1FA
    310
    10400000000000000000764BD60082B9114002303E5CD1FA1040000000000000
    ...
    ...
```

AutoLISP  *entnext*  function sample output:

```
Command: (setq e (entget e3))
    ((-1 . <Entity name: 7d50428>) (0 . "OLE2FRAME") (5 . "2D")
    (100 . "AcDbEntity") (67 . 1) (8 . "0") (100 . "AcDbOle2Frame")
    (70 . 2) (3 "Paintbrush Picture") (10 4.43116 5.66599 0.0)
    (11 6.4188 4.24494 0.0) (71 . 2) (72 . 1))
```

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*