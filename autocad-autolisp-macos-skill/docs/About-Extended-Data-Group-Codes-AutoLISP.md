# About Extended Data Group Codes (AutoLISP)

Extended data consists of one or more 1001 group codes, each of which begin with a unique application name.

The xdata groups returned by entget follow the definition data in the order in which they are saved in the database. Within each application's group, the contents,
meaning, and organization of the data are defined by the application. AutoCAD maintains the information but does not use it.
The table also shows that the group codes for xdata are in the range 1000-1071. Many of these group codes are for familiar
data types, as follows:

String
:   1000. Strings in extended data can be up to 255 bytes long (with the 256th byte reserved for the null character).

Application Name
:   1001 (also a string value). Application names can be up to 31 bytes long (the 32nd byte is reserved for the null character)
    and must adhere to the rules for symbol table names (such as layer names). An application name can contain letters, digits,
    and the special characters  *$*  (dollar sign),  *-*  (hyphen), and  *\_*  (underscore). It cannot contain spaces.

Layer Name
:   1003. Name of a layer associated with the xdata.

Database -Handle
:   1005. Handle of an entity in the drawing database.

3D Point
:   1010. Three real values, contained in a point.

Real
:   1040. A real value.

Integer
:   1070. A 16-bit integer (signed or unsigned).

Long
:   1071. A 32-bit signed (long) integer. If the value that appears in a 1071 group code is a short integer or real value, it
    is converted to a long integer; if it is invalid (for example, a string), it is converted to a long zero (0L).

    NOTE:AutoLISP manages 1071 group codes as real values. If you use entget to retrieve an entity's definition list that contains a 1071 group code, the value is returned as a real, as shown in the
    following example:

    ```
    (1071 . 12.0)
    ```

    If you want to create a 1071 group code in an entity with entmake or entmod, you can use either a real or an integer value, as shown in the following example:

    ```
    (entmake '((..... (1071 . 12) .... )))
    (entmake '((..... (1071 . 12.0) .... )))
    (entmake '((..... (1071 . 65537.0) .... )))
    (entmake '((..... (1071 . 65537) .... )))
    ```

    But AutoLISP still returns the group code value as a real:

    ```
    (entmake '((..... (1071 . 65537) .... )))
    ```

    The preceding statement returns the following:

    ```
    (1071 . 65537.0)
    ```

    ObjectARX and Managed .NET always manages 1071 group codes as long integers.

Several other extended data group codes have special meanings in this context (if the application chooses to use them):

Control String
:   1002. An xdata control string can be either "{" or "}". These braces enable the application to organize its data by subdividing it into lists. The left brace begins a list, and
    the right brace terminates the most recent list. Lists can be nested.

    NOTE:If a 1001 group code appears within a list, it is treated as a string and does not begin a new application group code.

Binary Data
:   1004. Binary data that is organized into variable-length chunks, which can be handled in ObjectARX and Managed .NET with the
    ads\_binary structure. The maximum length of each chunk is 127 bytes.

    NOTE:AutoLISP cannot directly handle binary chunks, so the same precautions that apply to long (1071) group codes apply to binary
    group codes as well.

World Space Position
:   1011. Unlike a simple 3D point, the WCS coordinates are moved, scaled, rotated, and mirrored along with the parent entity
    to which the extended data belongs. The WCS position is also stretched when the AutoCAD STRETCH command is applied to the
    parent entity and when this point lies within the select window.

World Space -Displacement
:   1012. A 3D point that is scaled, rotated, or mirrored along with the parent, but not stretched or moved.

World -Direction
:   1013. A 3D point that is rotated or mirrored along with the parent, but not scaled, stretched, or moved. The WCS direction
    is a normalized displacement that always has a unit length.

Distance
:   1041. A real value that is scaled along with the parent entity.

Scale Factor
:   1042. Also a real value that is scaled along with the parent.

#### Related Concepts

* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*