# Group Code Value Types Reference (DXF)

Group codes define the type of the associated value as an integer, a floating-point number, or a string, according to the
following table of group code ranges.

| Group code value types | |
| Code range | Group value type |
| 0-9 | String (with the introduction of extended symbol names in AutoCAD 2000, the 255-character limit has been increased to 2049 single-byte characters not including the newline at the end of the line); see the "Storage of String Values" section for more information |
| 10-17 | Double precision 3D point value |
| 20-27 | Double precision 3D point value |
| 30-37 | Double precision 3D point value |
| 38-59 | Double-precision floating-point value |
| 60-79 | 16-bit integer value |
| 90-99 | 32-bit integer value |
| 100-102 | String (255-character maximum, less for Unicode strings); see the "Storage of String Values" section for more information |
| 105 | String representing hexadecimal (hex) handle value |
| 110-119 | Double precision floating-point value |
| 120-129 | Double precision floating-point value |
| 130-139 | Double precision floating-point value |
| 140-149 | Double precision scalar floating-point value |
| 160-169 | 64-bit integer value |
| 170-179 | 16-bit integer value |
| 210-239 | Double-precision floating-point value |
| 270-279 | 16-bit integer value |
| 280-289 | 16-bit integer value |
| 290-299 | Boolean flag value |
| 300-309 | Arbitrary text string; see the "Storage of String Values" section for more information |
| 310-319 | String representing hex value of binary chunk |
| 320-329 | String representing hex handle value |
| 330-369 | String representing hex object IDs |
| 370-379 | 16-bit integer value |
| 380-389 | 16-bit integer value |
| 390-399 | String representing hex handle value |
| 400-409 | 16-bit integer value |
| 410-419 | String; see the "Storage of String Values" section for more information |
| 420-429 | 32-bit integer value |
| 430-439 | String; see the "Storage of String Values" section for more information |
| 440-449 | 32-bit integer value |
| 450-459 | Long |
| 460-469 | Double-precision floating-point value |
| 470-479 | String; see the "Storage of String Values" section for more information |
| 480-481 | String representing a hex handle value |
| 999 | Comment (string); see the "Storage of String Values" section for more information |
| 1000-1003 | String (same limits as indicated with 0-9 code range); see the "Storage of String Values" section for more information |
| 1004 | String representing a hex value of binary chunk |
| 1005 | String (same limits as indicated with 0-9 code range); see the "Storage of String Values" section for more information |
| 1010-1013 | Double-precision floating-point value |
| 1020-1023 | Double-precision floating-point value |
| 1030-1033 | Double-precision floating-point value |
| 1040-1042 | Double-precision floating-point value |
| 1070 | 16-bit integer value |
| 1071 | 32-bit integer value |

## Storage of String Values

String values stored in a DXF file can be expressed in plain ASCII, UTF-8, CIF (Common Interchange Format), and MIF (Maker
Interchange Format) formats. The UTF-8 format is only supported in the
AutoCAD 2007 DXF and later file formats. When the
AutoCAD program writes a DXF file, the format in which string values are written is determined by the DXF file format chosen. String
values are written out in these formats:

* *AutoCAD 2007 DXF and later format* - UTF-8

* *AutoCAD 2004 DXF and earlier format* - Plain ASCII and CIF
  
  String values containing Unicode characters are represented with control character sequences.
  
  For example,
   "TEST\U+7F3A\U+4E4F\U+89E3\U+91CA\U+6B63THIS\U+56FE"

String values can be stored with these dxf group codes:

* 0 - 9
* 100 - 101
* 300 - 309
* 410 - 419
* 430 - 439
* 470 - 479
* 999 - 1003

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)
* [About the DXF Format (DXF)](About-the-DXF-Format-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*