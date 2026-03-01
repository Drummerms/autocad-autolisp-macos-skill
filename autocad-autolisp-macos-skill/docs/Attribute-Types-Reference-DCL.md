# Attribute Types Reference (DCL)

Attributes are used to control the behavior and appearance of DCL tiles in a dialog definition.

The value of an attribute must be one of the following data types:

Integer
:   Numeric values (both integers and real numbers) that represent distances, such as the width or height of a tile, are expressed
    in character-width or character-height units.

Real Number
:   A fractional real number must have a leading digit: for example,
    0.1, not .1.

Quoted String
:   A quoted string consists of text enclosed in quotation marks (""). Attribute values are case-sensitive:
    B1 is not the same as
    b1. If the string must contain a quotation mark, precede the quotation mark character with a backslash (\"). Quoted strings can contain other control characters as well. The characters recognized by DCL are shown in the following
    table:

    | Control characters allowed in DCL strings | |
    | Control character | Meaning |
    | \" | quote (embedded) |
    | \\ | backslash |
    | \ | newline |
    | \t | horizontal tab |

Reserved Word
:   A reserved word is an identifier made up of alphanumeric characters, beginning with a letter. For example, many attributes
    require a value of either
    true or
    false. Reserved words are also case-sensitive:
    True does not equal
    true.

Like reserved words and strings, attribute names are case-sensitive; for example, you cannot assign a width by calling it
Width.

Application programs always retrieve attributes as strings. If your application uses numeric values, it must convert them
to and from string values.

Some attributes, such as
width and
height, are common to all tiles. Attribute specifications are optional. Many attributes have default values that are used if the
attribute is not specified. Other attributes are specifically meant for certain kinds of tiles—for example, the background
color of an image. If you attempt to assign this attribute to a different kind of tile, AutoCAD ®  may report an error. Usually, it ignores the attribute.

#### Related Concepts

* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [About User-Defined Attributes (DCL)](About-User-Defined-Attributes-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*