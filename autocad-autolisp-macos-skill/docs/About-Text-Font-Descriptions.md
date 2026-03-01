# About Text Font Descriptions

Text fonts are files of shape definitions with shape numbers corresponding to an ASCII code for each character.

Text fonts must include a special shape number 0 that conveys information about the font itself. Codes 1 through 31 are for
control characters, only one of which is used in a text font:

10 (LF)
:   The line feed (LF) must drop down one line without drawing. This is used for repeated TEXT commands, to place succeeding lines
    below the first one.

    \*10,5,lf

    2,8,(0,-10),0

    You can modify the spacing of lines by adjusting the downward movement specified by the LF shape definition.

Text fonts must include a special shape number 0 that conveys information about the font itself. The format has the following
syntax:

```
*0,4,font-nameabove,below,modes,0
```

The  *above*  value specifies the number of vector lengths above the baseline that the uppercase letters extend, and  *below*  indicates how far the lowercase letters descend below the baseline. The baseline is similar in concept to the lines on writing
paper. These values define the basic character size and are used as scale factors for the height specified for the text object.

The  *modes*  byte should be 0 for a horizontally oriented font and 2 for a dual-orientation (horizontal or vertical) font. The special
00E (14) command code is honored only when  *modes*  is set to 2.

The standard fonts supplied with the program include a few additional characters required for dimensioning.

*%%d* Degree symbol (°)

*%%p* Plus/minus tolerance symbol (±)

*%%c* Circle diameter dimensioning symbol

You can use these and other %%*nnn* control sequences to specify a character.

NOTE:The program draws text characters by their ASCII codes (shape numbers) and not by name. To save memory, specify the shape
name portion of each text shape definition in lowercase as shown in the following example. (Lowercase names are not saved
in memory.)

```
*65,11,uca
024,043,04d,02c,2,047,1,040,2,02e,0
```

Because the shape name  *uca*  contains lowercase letters, the program does not save the name in memory. However, you can use the name for reference when
editing the font definition file. In this example,  *uca*  stands for uppercase A.

#### Related References

* [Sample: Extended Simplex Roman Font Characters](Sample-Extended-Simplex-Roman-Font-Characters.md)
* [Sample: Extended Standard Font for UNICODE Characters](Sample-Extended-Standard-Font-for-UNICODE-Characters.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Shape Descriptions](About-Shape-Descriptions.md)
* [About Unicode Font Descriptions](About-Unicode-Font-Descriptions.md)
* [About Defining a Big Font](About-Defining-a-Big-Font.md)
* [About Using Big Font Text in a Drawing](About-Using-Big-Font-Text-in-a-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*