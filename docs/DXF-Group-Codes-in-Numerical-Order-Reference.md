# DXF Group Codes in Numerical Order Reference

The following table gives the group code or group code range accompanied by an explanation of the group code value. In the
table, “fixed” indicates that the group code always has the same purpose. If a group code isn't fixed, its purpose depends
on the context.

| Group codes by number | |
| Group code | Description |
| -5 | APP: persistent reactor chain |
| -4 | APP: conditional operator (used *only* with  *ssget* ) |
| -3 | APP: extended data (XDATA) sentinel (fixed) |
| -2 | APP: entity name reference (fixed) |
| -1 | APP: entity name. The name changes each time a drawing is opened. It is never saved (fixed) |
| 0 | Text string indicating the entity type (fixed) |
| 1 | Primary text value for an entity |
| 2 | Name (attribute tag, block name, and so on) |
| 3-4 | Other text or name values |
| 5 | Entity handle; text string of up to 16 hexadecimal digits (fixed) |
| 6 | Linetype name (fixed) |
| 7 | Text style name (fixed) |
| 8 | Layer name (fixed) |
| 9 | DXF: variable name identifier (used only in HEADER section of the DXF file) |
| 10 | Primary point; this is the start point of a line or text entity, center of a circle, and so on  DXF: *X* value of the primary point (followed by *Y* and *Z* value codes 20 and 30)  APP: 3D point (list of three reals) |
| 11-18 | Other points  DXF: *X* value of other points (followed by *Y* value codes 21-28 and *Z* value codes 31-38)  APP: 3D point (list of three reals) |
| 20, 30 | DXF: Y and *Z*values of the primary point |
| 21-28, 31-37 | DXF: *Y* and *Z*values of other points |
| 38 | DXF: entity's elevation if nonzero |
| 39 | Entity's thickness if nonzero (fixed) |
| 40-48 | Double-precision floating-point values (text height, scale factors, and so on) |
| 48 | Linetype scale; double precision floating point scalar value; default value is defined for all entity types |
| 49 | Repeated double-precision floating-point value. Multiple 49 groups may appear in one entity for variable-length tables (such as the dash lengths in the LTYPE table). A 7*x* group always appears *before* the first 49 group to specify the table length |
| 50-58 | Angles (output in degrees to DXF files and radians through AutoLISP and ObjectARX applications) |
| 60 | Entity visibility; integer value; absence or 0 indicates visibility; 1 indicates invisibility |
| 62 | Color number (fixed) |
| 66 | “Entities follow” flag (fixed) |
| 67 | Space—that is, model or paper space (fixed) |
| 68 | APP: identifies whether viewport is on but fully off screen; is not active or is off |
| 69 | APP: viewport identification number |
| 70-78 | Integer values, such as repeat counts, flag bits, or modes |
| 90-99 | 32-bit integer values |
| 100 | Subclass data marker (with derived class name as a string). Required for all objects and entity classes that are derived from another concrete class. The subclass data marker segregates data defined by different classes in the inheritance chain for the same object.  This is in addition to the requirement for DXF names for each distinct concrete class derived from ObjectARX (see Subclass Markers) |
| 102 | Control string, followed by “{<arbitrary name>” or “}”. Similar to the xdata 1002 group code, except that when the string begins with “{“, it can be followed by an arbitrary string whose interpretation is up to the application. The only other control string allowed is “}” as a group terminator. AutoCAD does not interpret these strings except during drawing audit operations. They are for application use |
| 105 | Object handle for DIMVAR symbol table entry |
| 110 | UCS origin (appears only if code 72 is set to 1)  DXF: *X* value; APP: 3D point |
| 111 | UCS *X*-axis (appears only if code 72 is set to 1)  DXF: *X* value; APP: 3D vector |
| 112 | UCS *Y*-axis (appears only if code 72 is set to 1)  DXF: *X* value; APP: 3D vector |
| 120-122 | DXF: *Y* value of UCS origin, UCS *X*-axis, and UCS *Y*-axis |
| 130-132 | DXF: Z value of UCS origin, UCS *X*-axis, and UCS *Y*-axis |
| 140-149 | Double-precision floating-point values (points, elevation, and DIMSTYLE settings, for example) |
| 170-179 | 16-bit integer values, such as flag bits representing DIMSTYLE settings |
| 210 | Extrusion direction (fixed)  DXF: *X* value of extrusion direction  APP: 3D extrusion direction vector |
| 220, 230 | DXF: *Y* and *Z*values of the extrusion direction |
| 270-279 | 16-bit integer values |
| 280-289 | 16-bit integer value |
| 290-299 | Boolean flag value |
| 300-309 | Arbitrary text strings |
| 310-319 | Arbitrary binary chunks with same representation and limits as 1004 group codes: hexadecimal strings of up to 254 characters represent data chunks of up to 127 bytes |
| 320-329 | Arbitrary object handles; handle values that are taken “as is”. They are not translated during INSERT and XREF operations |
| 330-339 | Soft-pointer handle; arbitrary soft pointers to other objects within same DXF file or drawing. Translated during INSERT and XREF operations |
| 340-349 | Hard-pointer handle; arbitrary hard pointers to other objects within same DXF file or drawing. Translated during INSERT and XREF operations |
| 350-359 | Soft-owner handle; arbitrary soft ownership links to other objects within same DXF file or drawing. Translated during INSERT and XREF operations |
| 360-369 | Hard-owner handle; arbitrary hard ownership links to other objects within same DXF file or drawing. Translated during INSERT and XREF operations |
| 370-379 | Lineweight enum value (AcDb::LineWeight). Stored and moved around as a 16-bit integer. Custom non-entity objects may use the full range, but entity classes only use 371-379 DXF group codes in their representation, because AutoCAD and AutoLISP both always assume a 370 group code is the entity's lineweight. This allows 370 to behave like other "common" entity fields |
| 380-389 | PlotStyleName type enum (AcDb::PlotStyleNameType). Stored and moved around as a 16-bit integer. Custom non-entity objects may use the full range, but entity classes only use 381-389 DXF group codes in their representation, for the same reason as the Lineweight range above |
| 390-399 | String representing handle value of the PlotStyleName object, basically a hard pointer, but has a different range to make backward compatibility easier to deal with. Stored and moved around as an object ID (a handle in DXF files) and a special type in AutoLISP. Custom non-entity objects may use the full range, but entity classes only use 391-399 DXF group codes in their representation, for the same reason as the lineweight range above |
| 400-409 | 16-bit integers |
| 410-419 | String |
| 420-427 | 32-bit integer value. When used with True Color; a 32-bit integer representing a 24-bit color value. The high-order byte (8 bits) is 0, the low-order byte an unsigned char holding the Blue value (0-255), then the Green value, and the next-to-high order byte is the Red Value. Converting this integer value to hexadecimal yields the following bit mask: 0x00RRGGBB. For example, a true color with Red==200, Green==100 and Blue==50 is 0x00C86432, and in DXF, in decimal, 13132850 |
| 430-437 | String; when used for True Color, a string representing the name of the color |
| 440-447 | 32-bit integer value. When used for True Color, the transparency value |
| 450-459 | Long |
| 460-469 | Double-precision floating-point value |
| 470-479 | String |
| 480-481 | Hard-pointer handle; arbitrary hard pointers to other objects within same DXF file or drawing. Translated during INSERT and XREF operations |
| 999 | DXF: The 999 group code indicates that the line following it is a comment string. SAVEAS does not include such groups in a DXF output file, but OPEN honors them and ignores the comments. You can use the 999 group to include comments in a DXF file that you have edited |
| 1000 | ASCII string (up to 255 bytes long) in extended data |
| 1001 | Registered application name (ASCII string up to 31 bytes long) for extended data |
| 1002 | Extended data control string (“{” or “}”) |
| 1003 | Extended data layer name |
| 1004 | Chunk of bytes (up to 127 bytes long) in extended data |
| 1005 | Entity handle in extended data; text string of up to 16 hexadecimal digits |
| 1010 | A point in extended data  DXF: *X*value (followed by 1020 and 1030 groups)  APP: 3D point |
| 1020, 1030 | DXF: *Y* and *Z* values of a point |
| 1011 | A 3D world space position in extended data  DXF: *X* value (followed by 1021 and 1031 groups)  APP: 3D point |
| 1021, 1031 | DXF: *Y* and *Z* values of a world space position |
| 1012 | A 3D world space displacement in extended data  DXF: *X* value (followed by 1022 and 1032 groups)  APP: 3D vector |
| 1022, 1032 | DXF: *Y* and *Z* values of a world space displacement |
| 1013 | A 3D world space direction in extended data  DXF: *X* value (followed by 1022 and 1032 groups)  APP: 3D vector |
| 1023, 1033 | DXF: *Y* and *Z* values of a world space direction |
| 1040 | Extended data double-precision floating-point value |
| 1041 | Extended data distance value |
| 1042 | Extended data scale factor |
| 1070 | Extended data 16-bit signed integer |
| 1071 | Extended data 32-bit signed long |

#### Related References

* [Subclass Markers (DXF)](Subclass-Markers-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)
* [About the DXF Format (DXF)](About-the-DXF-Format-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*