# Old Slide Header (DXF)

The slide format described in the previous section is produced by AutoCAD Release 9 and later, and is portable among all
computers running AutoCAD Release 9 or later. Earlier versions of AutoCAD (as well as AutoShade ®  1.0 and AutoSketch ®  1.02) produce slides with a somewhat different header, as shown in the following table.

| Old slide file header | | |
| Field | Bytes | Description |
| ID string | 17 | “AutoCAD Slide” CR LF ^Z NUL |
| Type indicator | 1 | 56 (decimal) |
| Level indicator | 1 | 1 (old format) |
| High X dot | 2 | Width of the drawing area: 1, in pixels |
| High Y dot | 2 | Height of the drawing area: 1, in pixels |
| Aspect ratio | 8 | Drawing area aspect ratio (horizontal size/vertical size in inches), written as a floating-point number |
| Hardware fill | 2 | Either 0 or 2 (value is unimportant) |
| Filler byte | 1 | Unused |

Note that the old-format header does not contain a test number field. The floating-point aspect ratio value and all 2-byte
integers are written in the native format of the CPU that was used to create the file (for 8086-family CPUs, IEEE double-precision,
and low-order byte first). Old-format slide files are not portable across machine types, but they can be read by any release
of the AutoCAD program running on the same CPU type as the CPU with which the slide was created.

#### Related References

* [Slide Files (DXF)](Slide-Files-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*