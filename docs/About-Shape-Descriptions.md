# About Shape Descriptions

Font and shape files (SHX) are compiled from shape definition files (SHP). You can create or modify shape definition files
with a text editor or word processor that saves files in ASCII format.

The syntax of the shape description for each shape or character is the same regardless of the final use (shape or font) for
that shape description. If a shape definition file is to be used as a font file, the first entry in the file describes the
font itself rather than a shape within the file. If this initial entry describes a shape, the file is used as a shape file.

Each line in a shape definition file can contain up to 128 characters. Longer lines cannot be compiled. Because the program
ignores blank lines and text to the right of a semicolon, you can embed comments in shape definition files.

Each shape description has a header line of the following form and is followed by one or more lines containing specification
bytes, separated by commas and terminated by a 0.

```
*shapenumber,defbytes,shapenamespecbyte1,specbyte2,specbyte3,...,0
```

The following list describes the fields of a shape description:

shapenumber
:   A number, unique to the file, between 1 and 258 (and up to 32768 for Unicode fonts), and preceded by an asterisk (\*). Non-Unicode
    font files use the shape numbers 256, 257, and 258 for the symbolic identifiers Degree\_Sign, Plus\_Or\_Minus\_Sign, and Diameter\_Symbol.
    For Unicode fonts these glyphs appear at the U+00B0, U+00B1, and U+2205 shape numbers and are part of the “Latin Extended-A”
    subset.

    Text fonts (files containing shape definitions for each character) require specific numbers corresponding to the value of
    each character in the ASCII code; other shapes can be assigned any numbers.

defbytes
:   The number of data bytes ( *specbytes* ) required to describe the shape, including the terminating 0. The limit is 2,000 bytes per shape.

shapename
:   The shape name. Shape names must be uppercase to be recognized. Names with lowercase characters are ignored and are usually
    used to label font shape definitions.

specbyte
:   A shape specification byte. Each specification byte is a code that defines either a vector length and direction or one of
    a number of special codes. A specification byte can be expressed in the shape definition file as either a decimal or hexadecimal
    value. If the first character of a specification byte is a 0 (zero), the two characters that follow are interpreted as hexadecimal
    values.

#### Topics in this section

* [About Vector Length and Direction Codes](About-Vector-Length-and-Direction-Codes.md)

  A simple shape specification byte contains vector length and direction encoded into one specification byte.
* [Special Codes Reference](Special-Codes-Reference.md)

  Special codes can be used to create additional geometric forms and specify certain actions.
* [About Text Font Descriptions](About-Text-Font-Descriptions.md)

  Text fonts are files of shape definitions with shape numbers corresponding to an ASCII code for each character.
* [About Unicode Font Descriptions](About-Unicode-Font-Descriptions.md)

  A single Unicode font, due to its large character set, is capable of supporting all languages and platforms. Unicode shape
  definition files are virtually identical in format and syntax to regular shape definition files.
* [About Big Font Descriptions](About-Big-Font-Descriptions.md)

  Some languages, such as Japanese, use text fonts with thousands of non-ASCII characters. In order for drawings to contain
  such text, the product supports a special form of shape definition file called a Big Font file.
* [About Superscripts and Subscripts in SHX Files](About-Superscripts-and-Subscripts-in-SHX-Files.md)

  You can modify shape definition files to improve their ability to display superscripts and subscripts.

#### Related References

* [Special Codes Reference](Special-Codes-Reference.md)
* [Sample: Extended Simplex Roman Font Characters](Sample-Extended-Simplex-Roman-Font-Characters.md)
* [Sample: Extended Standard Font for UNICODE Characters](Sample-Extended-Standard-Font-for-UNICODE-Characters.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Superscripts and Subscripts in SHX Files](About-Superscripts-and-Subscripts-in-SHX-Files.md)
* [About Text Font Descriptions](About-Text-Font-Descriptions.md)
* [About Unicode Font Descriptions](About-Unicode-Font-Descriptions.md)
* [About Defining a Big Font](About-Defining-a-Big-Font.md)
* [About Compiling Shape and Font Files](About-Compiling-Shape-and-Font-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*