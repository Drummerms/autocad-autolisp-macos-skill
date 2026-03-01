# To Add Superscript and Subscript Definitions to a Font

This example procedure is based on the AutoCAD Romans font file, although a similar method applies to any font. This procedure
adds four new shape definitions to a font: super\_on, super\_off, sub\_on, and sub\_off, which control the position and size of
the characters that follow. For simplicity, this example replaces the brackets characters (*[* and *]*) and the braces characters (*{* and *}*) with the new characters. You may choose to replace other characters or use a shape number in the extended range (ASCII codes
128 through 256). If you use an extended shape number, you need to use the %%*nnn* method for placing the new characters (where *nnn* is the ASCII value of the character).

1. Edit your SHP file with an ASCII text editor (for example, Notepad on Windows or TextEdit on Mac OS).
2. Search for the shape definitions of the characters you are replacing. To comment out those definitions so the new definitions
   can take their place, insert a semicolon in front of each line of the shape definition. The shape definition may continue
   for a number of lines.

   The left- and right-bracket characters have ASCII values of 91 and 93 (05B and 05D hex values, if the font is Unicode). The
   left and right curly brace characters have ASCII values of 123 and 125 (07B and 07D hex).
3. Add the first and second values on the second line of the definition, and divide the total by 2 as shown in the following
   example:

   ```
   *UNIFONT,6,Extended Simplex Roman for UNICODE
   21,7,2,0 21 + 7 = 28, then 28 / 2 = 14. This number is used later.
   ```
4. Add the following lines to the end of the SHP file:

   ```
   *91,8,super_on
   2,8,(0,14),003,2,1,0
   *93,8,super_off
   2,004,2,8,(0,-14),1,0
   *123,8,sub_on
   2,8,(0,-14),003,2,1,0
   *125,8,sub_off
   2,004,2,8,(0,14),1,0
   ```

   Notice the 14 and -14 values in the preceding lines. They are *Y* axis offsets for the imaginary pen. The value 14 is half the maximum height of a character in this font, which is the correct
   approximation for superscripts and subscripts. This value needs to be calculated for each font file, but you can modify it
   any way you want.
5. Save the file.
6. Use the COMPILE command to compile the SHP file.

   Once the shape is compiled and an appropriate style is defined, you can access the new pen-up and pen-down commands by entering
   the brackets (*[* and *]*) and braces (*{* and *}*) characters. The [ (left bracket) character initiates superscript and the ] (right bracket) character returns from superscript
   to normal. The { (left brace) character initiates subscript and the } (right brace) character returns from subscript to normal.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Superscripts and Subscripts in SHX Files](About-Superscripts-and-Subscripts-in-SHX-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*