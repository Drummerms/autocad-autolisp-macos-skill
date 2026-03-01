# About Using a Big Font to Extend a Font

To include special symbols in text strings, you can use a Big Font instead of extending a standard text font.

In some drafting disciplines, many special symbols can appear in text strings. The standard text fonts can be extended to
include special symbols. However, extending standard text fonts has several limitations:

* The number of shapes is 255 per font file.
* Standard character set uses almost half the available shape numbers. Only codes 1 through 9, 11 through 31, and 130 through
  255 are available.
* Multiple text fonts require duplication of the symbol definitions in each font.
* Special symbols require that you enter  **%%nnn** , where *nnn* is the symbol's shape number.

The Big Font mechanism avoids these problems. You can select one or more seldom-used characters, such as the tilde (˜) or
the vertical bar (|), as an escape code, and use the next character to select the appropriate special symbol. For instance,
you can use the following Big Font file to draw Greek letters by entering a vertical bar (|, ASCII code 124) followed by the
equivalent Roman letter. Because the first byte of each character is 124, the character codes are biased by 124 x 256, or
31744.

```
*BIGFONT 60,1,124,124
*0,4,Greek
above, below, modes, 0
*31809,n,uca
. . .   uppercase Alpha definition, invoked by "|A"
*31810,n,ucb
. . .   uppercase Beta definition, invoked by "|B"
*31841,n,lca
. . .   lowercase Alpha definition, invoked by "|a"
*31842,n,lcb
. . .   lowercase Beta definition, invoked by "|b"
*31868,n,vbar
. . .   vertical bar definition, invoked by "||"
. . .
```

#### Related Tasks

* [To Enable Big Fonts](To-Enable-Big-Fonts.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Using Big Font Text in a Drawing](About-Using-Big-Font-Text-in-a-Drawing.md)
* [About Defining an Extended Big Font File](About-Defining-an-Extended-Big-Font-File.md)
* [About Defining a Big Font](About-Defining-a-Big-Font.md)
* [About Shape Descriptions](About-Shape-Descriptions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*