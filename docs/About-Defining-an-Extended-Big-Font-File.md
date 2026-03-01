# About Defining an Extended Big Font File

To reduce the size of composite Kanji characters, you can define an extended Big Font file. Extended big fonts use the subshape
code, followed immediately by a 0.

The first line of an extended Big Font file is the same as the regular Big Font file. This is the format for the remaining
lines of the file:

```
*0,5,font-name character-height, 0, modes, character-width,0
            .
            .
            .
*shape-number,defbytes,shape-name
            .
code,0,primitive#,basepoint-x,basepoint-y,width,height,
            .
            .
code,0,primitive#,basepoint-x,basepoint-y,width,height,
            .
terminator
```

The following list describes the fields of a Big Font definition file:

character height
:   Used along with character width to indicate the number of units that define the font characters.

character width
:   Used along with character height to indicate the number of units that define the font characters. The character-height and character-width values are used to scale the primitives of the font. In this context, primitives are the points, lines, polygons, or character
    strings of the font geometrically oriented in 2D space. A Kanji character consists of several primitives used repeatedly in
    different scales and combinations.

modes
:   The  *modes*  byte should be 0 for a horizontally oriented font and 2 for a dual-orientation (horizontal or vertical) font. The special
    00E (14) command code is honored only when  *modes*  is set to 2.

shape-number
:   Character code.

defbytes
:   Byte size. It is always 2 bytes, consisting of a hexadecimal or a combination of decimal and hexadecimal codes.

shape-name
:   Character name.

code
:   Shape description special code. It is always 7 so that it can use the subshape feature.

primitive#
:   Reference to the subshape number. It is always 2 bytes.

basepoint-x
:   *X* origin of the primitive.

basepoint-y
:   *Y* origin of the primitive.

width
:   Scale of the width of the primitive.

height
:   Scale of the height of the primitive.

terminator
:   End-of-file indicator for the shape definition. It is always 0.

To arrive at the scale factor, the program scales down the primitive to a square unit and then multiplies it by the height
and width to get the shape of the character. Character codes (shape numbers) in the Big Font shape definition file can have
values up to 65535. The following table describes the fields of the extended Big Font file.

| Fields of the extended Big Font file | | | |
| Variable | Value | Byte size | Description |
| *shape-number* | xxxx | 2 bytes | Character code |
| *code* | 7,0 | 2 bytes | Extended font definition |
| *primitive#* | xxxx | 2 bytes | Refer to subshape number |
| *basepoint-x* |  | 1 byte | Primitive *X* origin |
| *basepoint-y* |  | 1 byte | Primitive *Y* origin |
| *width* |  | 1 byte | Scale of primitive width |
| *height* |  | 1 byte | Scale of primitive height |
| *terminator* | 0 | 1 byte | End of shape definition |

The following figure is an example of a 16 x 16 dot matrix that you could use to design an extended Big Font, such as a Kanji
character. In the example, the distance between each dot is one unit. The callout points to a square unit.

![](../images/GUID-E290DDD5-6C09-47CC-BCEE-CBD7C73623CC-low.png)

A square matrix for a Kanji character

The following figure shows examples of Kanji characters. Each character occupies an M×N matrix (matrices don't have to be
square), similar to the one shown in the previous figure. The numbers above each figure are the associated shape numbers.

![](../images/GUID-932F82B1-5650-436B-BF14-2F834090DE8B-low.png)

Examples of Kanji characters

The following figure shows Kanji primitives.

![](../images/GUID-E9FDDA1F-219B-49A2-8C77-097D3FA5321F-low.png)

Examples of Kanji primitives

NOTE:Not all fonts are defined in a square matrix; some are defined in rectangular matrices.

## Example: Shape Definition File for an Extended Big Font

```
*BIGFONT 50,1,080,09e
*0,5,Extended Font
15,0,2,15,0
*08D91,31,unspecified
2,0e,8,-7,-15,
7,0,08cfb,0,0,16,16,7,0,08bca,2,3,12,9,
2,8,18,0,2,0e,8,-11,-3,0
*08CD8,31,unspecified
2,0e,8,-7,-15,
7,0,08be0,0,0,8,16,7,0,08cc3,8,0,8,16,
2,8,18,0,2,0e,8,-11,-3,0
*08ADF,31,unspecified
2,0e,8,-7,-15,
7,0,089a4,0,0,8,16,7,0,08cb3,8,0,8,16,
2,8,18,0,2,0e,8,-11,-3,0
*08CE8,39,unspecified
2,0e,8,-7,-15,
7,0,089a4,0,1,5,14,7,0,08cc3,5,2,5,14,7,0,08c8e,9,0,7,
16,2,8,18,0,2,0e,8,-11,-3,0
*089A4,39,primitive
2,0e,8,-7,-15,2,8,1,14,1,0c0,
2,8,-11,-6,1,0a0,2,8,-12,-7,1,
0e0,2,8,-7,13,1,0dc,2,8,11,-1,
2,0e,8,-11,-3,0
*08BCA,41,primitive
2,0e,8,-7,-15,2,8,1,14,1,0c0,
2,8,-11,-6,1,0a0,2,8,-12,-8,1,
0e0,2,0e5,1,0ec,2,063,1,8,
2,-3,2,06f,2,0e,8,-11,-3,0
*08BE0,81,primitive
2,0e,8,-7,-15,2,8,3,9,1,080,
2,8,-10,-4,1,0c0,2,8,-13,-5,1,
0e0,2,8,-7,9,1,09c,2,8,-1,14,
1,8,-6,-5,2,8,8,5,1,8,6,-5,
2,8,-11,-6,1,8,1,-3,2,8,7,3,
1,8,-1,-3,2,8,-3,15,1,01a,2,
012,1,01e,2,8,10,-14,2,0e,8,
-11,-3,0
*08C8E,44,primitive
2,0e,8,-7,-15,2,8,3,15,1,090,0fc,038,
2,8,-6,11,1,090,2,8,-9,-5,1,
090,2,096,1,0ac,8,-1,-3,01a,01a,2,8,
18,0,2,0e,8,-11,-3,0
*08CB3,61,primitive
2,0e,8,-7,-15,2,042,1,02b,02a,018,2,
0d0,1,012,034,2,069,1,01e,040,2,8,
-8,6,1,02b,2,8,4,5,1,08c,2,8,
-3,8,1,03c,2,8,-5,3,1,0e0,2,8,
-12,5,1,0a0,2,8,6,-14,2,0e,8,
-11,-3,0
*08CC3,34,primitive
2,0e,8,-7,-15,2,0c1,1,06c,0a8,064,0a0,2,8,
-5,9,1,09c,2,8,-7,5,1,0e0,2,8,
4,-11,2,0e,8,-11,-3,0
*08CFB,22,primitive
2,0e,8,-7,-15,2,0d2,1,0cc,0c8,0c4,0c0,2,8,
5,-13,2,0e,8,-11,-3,0
```

#### Related Tasks

* [To Enable Big Fonts](To-Enable-Big-Fonts.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Defining a Big Font](About-Defining-a-Big-Font.md)
* [About Using Big Font Text in a Drawing](About-Using-Big-Font-Text-in-a-Drawing.md)
* [About Using a Big Font to Extend a Font](About-Using-a-Big-Font-to-Extend-a-Font.md)
* [About Shape Descriptions](About-Shape-Descriptions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*