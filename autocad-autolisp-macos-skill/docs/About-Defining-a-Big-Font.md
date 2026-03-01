# About Defining a Big Font

Special codes in the first line of a Big Font file specify how to read two-byte hexadecimal codes.

A font with hundreds or thousands of characters must be handled differently from a font containing the ASCII set of up to
256 characters. In addition to using more complicated techniques for searching the file, the program needs a way to represent
characters with two-byte codes as well as one-byte codes. Both situations are addressed by the use of special codes at the
beginning of a Big Font file.

The first line of a Big Font shape definition file must be as follows:

```
*BIGFONT nchars,nranges,b1,e1,b2,e2,...
```

*nchars*  represents the approximate number of character definitions in the set; if it is off by more than about 10 percent, either
speed or file size suffers. You can use the rest of the line to name special character codes (escape codes) that signify the
start of a two-byte code. For example, on Japanese computers, Kanji characters start with hexadecimal codes in the range 90-AF
or E0-FF. When the operating system sees one of these codes, it reads the next byte and combines the two bytes into a code
for one Kanji character. In the \*BIGFONT line,  *nranges*  tells how many contiguous ranges of numbers are used as escape codes;  *b1* ,  *e1* ,  *b2* ,  *e2* , and so on, define the beginning and ending codes in each range. Therefore, the header for a Japanese Big Font file might
look like this:

```
*BIGFONT 4000,2,090,0AF,0E0,0FF
```

After the \*BIGFONT line, the font definition is just like a regular text font, except that character codes (shape numbers) can have values up
to 65535.

#### Topics in this section

* [To Enable Big Fonts](To-Enable-Big-Fonts.md)

#### Related Tasks

* [To Enable Big Fonts](To-Enable-Big-Fonts.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Defining an Extended Big Font File](About-Defining-an-Extended-Big-Font-File.md)
* [About Using Big Font Text in a Drawing](About-Using-Big-Font-Text-in-a-Drawing.md)
* [About Using a Big Font to Extend a Font](About-Using-a-Big-Font-to-Extend-a-Font.md)
* [About Shape Descriptions](About-Shape-Descriptions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*