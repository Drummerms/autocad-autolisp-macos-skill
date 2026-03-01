# About Unicode Font Descriptions

A single Unicode font, due to its large character set, is capable of supporting all languages and platforms. Unicode shape
definition files are virtually identical in format and syntax to regular shape definition files.

The main difference is in the syntax of the font header as shown in the following code:

```
*UNIFONT,6,font-name above,below,modes,encoding,type,0
```

The  *font-name* ,  *above* ,  *below* , and  *modes*  parameters are the same as in regular fonts. The remaining two parameters are defined as follows:

encoding
:   Font encoding. Uses one of the following integer values.

    *0* Unicode

    *1* Packed multibyte 1

    *2* Shape file

type
:   Font embedding information. Specifies whether the font is licensed. Licensed fonts must not be modified or exchanged. Bitcoded
    values can be added.

    *0* Font can be embedded

    *1* Font cannot be embedded

    *2* Embedding is read-only

Another important difference is the handling of the code 7 subshape reference. If a shape description includes a code 7 subshape
reference, the data following the code 7 is interpreted as a two-byte value. This affects the total number of data bytes ( *defbytes* ) in the shape description header. For example, the following shape description is found in the *romans.shp* file:

```
*00080,4,keuroRef
7,020AC,0
```

The second field in the header represents the total number of bytes in the shape description. If you are not used to working
with Unicode font descriptions, you may be inclined to use three bytes rather than four, but this would cause an error during
the compiling of the SHP file. This is true even if the shape number you are referencing is not in the two-byte range (below
255); the compiler always uses two bytes for this value, so you must account for that in the header.

The only other difference between Unifont shape definitions and regular shape definitions is the shape numbers. The Unifont
shape definitions that the program provides use hexadecimal shape numbers as opposed to decimal values. Although hexadecimal
numbers are not required, their use makes it easier to cross-reference the shape numbers with the \U+ control character values.

#### Related References

* [Sample: Extended Simplex Roman Font Characters](Sample-Extended-Simplex-Roman-Font-Characters.md)
* [Sample: Extended Standard Font for UNICODE Characters](Sample-Extended-Standard-Font-for-UNICODE-Characters.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Shape Descriptions](About-Shape-Descriptions.md)
* [About Text Font Descriptions](About-Text-Font-Descriptions.md)
* [About Defining a Big Font](About-Defining-a-Big-Font.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*