# About the General DXF File Structure (DXF)

Essentially, a DXF file is composed of pairs of codes and associated values. The codes, known as
*group codes*, indicate the type of value that follows. Using these group code and value pairs, a DXF file is organized into sections composed
of records, which are composed of a group code and a data item. Each group code and value are on their own line in the DXF
file.

Each section starts with a group code 0 followed by the string SECTION. This is followed by a group code 2 and a string indicating
the name of the section (for example, HEADER). Each section is composed of group codes and values that define its elements.
A section ends with a 0 followed by the string ENDSEC.

It may be helpful to produce a DXF file from a small drawing, print it, and refer to it while reading the information presented
in this section.

The overall organization of a DXF file is as follows:

* *HEADER section.* Contains general information about the drawing. It consists of a database version number and a number of system variables.
  Each parameter contains a variable name and its associated value.
* *CLASSES section.* Holds the information for application-defined classes, whose instances appear in the BLOCKS, ENTITIES, and OBJECTS sections
  of the database. A class definition is permanently fixed in class hierarchy.
* *TABLES section.*Contains definitions for the following symbol tables:

  APPID (application identification table)

  BLOCK\_RECORD (block reference table)

  DIMSTYLE (dimension style table)

  LAYER (layer table)

  LTYPE (linetype table)

  STYLE (text style table)

  UCS (user coordinate system table)

  VIEW (view table)

  VPORT (viewport configuration table)
* *BLOCKS section.* Contains block definition and drawing entities that make up each block reference in the drawing.
* *ENTITIES section.* Contains the graphical objects (entities) in the drawing, including block references (insert entities).
* *OBJECTS section.* Contains the nongraphical objects in the drawing. All objects that are not entities or symbol table records or symbol tables
  are stored in this section. Examples of entries in the OBJECTS section are dictionaries that contain mline styles and groups.
* *THUMBNAILIMAGE section.* Contains the preview image data for the drawing. This section is optional.

If you use the Select Objects option of the SAVE or SAVEAS command, the ENTITIES section of the resulting DXF file contains
only the entities you select.

#### Related References

* [About ASCII DXF Files](About-ASCII-DXF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*