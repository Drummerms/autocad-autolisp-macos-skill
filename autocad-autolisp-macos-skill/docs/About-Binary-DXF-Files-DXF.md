# About Binary DXF Files (DXF)

The ASCII DXF file format is a complete representation of an AutoCAD drawing in ASCII text form, and is easily processed by
other programs. In addition, AutoCAD can produce or read a binary form of the full DXF file and accept limited input in another
binary file format.

The SAVE and SAVEAS commands provide a Binary option that writes binary DXF files. Such a file contains all the information
present in an ASCII DXF file but in a more compact form that takes about 25 percent less file space. It can be read and written
more quickly (typically, five times faster) by AutoCAD. Unlike ASCII DXF files, which entail a trade-off between size and
floating-point accuracy, binary DXF files preserve the accuracy in the drawing database. (AutoCAD Release 10 was the first
version to support this form of DXF file; it cannot be read by earlier releases.)

A binary DXF file begins with a 22-byte sentinel consisting of the following:

```
AutoCAD Binary DXF<CR><LF><SUB><NULL>
```

Following the sentinel are data pairs (group, value) which are the same as those in an ASCII DXF file except they are represented
in binary form. The group code is a 2-byte integer value (1 byte in DXF files prior to AutoCAD Release 13) with the least
significant byte first. Each group code is followed by its assigned value which can be one of the following:

* A bool represented as a 0 or 1 as a single byte
* A 2-byte integer with the least significant byte first and the most significant byte last
* A 4-byte integer with the least significant byte first and the most significant byte last
* An 8-byte integer with the least significant byte first and the most significant byte last
* An 8-byte IEEE double-precision floating-point number stored with the least significant byte first and the most significant
  byte last
* A binary chunk data represented as a single-byte unsigned integer length, followed by the specified number of bytes of chunk
  data
* An ASCII string terminated by a 0 (NULL) byte

The type of data following a group is determined from the group code by the same rules used in decoding ASCII DXF files. Translation
of angles to degrees and dates to fractional Julian date representation is performed for binary files as well as for ASCII
DXF files. The comment group, 999, is not used in binary DXF files.

In DXF files prior to AutoCAD Release 13, extended data group codes are represented in binary DXF as a single byte with the
value 255, followed by a 2-byte integer value (least significant byte first) containing the actual group code, followed by
the actual value. And, extended data values are represented in the same way as regular DXF data values.

So, for example, for an extended data long group in a DXF file prior to AutoCAD Release 13, the following values would appear,
occupying 1, 2, and 4 bytes respectively.

```
255

```
 Escape group code
```

1071

```
 True group code
```

999999

```
 Value for the 1071 group code
```
```

SAVEAS writes binary DXF files with the same file type
*(.dxf)* as for ASCII DXF files. The OPEN and INSERT commands automatically recognize a binary file by means of its sentinel string.
The file doesn't need to be identified as a binary file.

If the OPEN and INSERT commands encounter an error in a binary DXF file, the AutoCAD-based program reports the byte address
within the file where the error was detected.

#### Related References

* [About Drawing Interchange File Formats (DXF)](About-Drawing-Interchange-File-Formats-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*