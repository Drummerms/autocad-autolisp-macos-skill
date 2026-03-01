# About Compiling Shape and Font Files

You can define, create, and compile shape and font files to use custom symbols and text fonts in your drawings.

*Shapes* are objects that you use like blocks. Blocks are more versatile and easier to use and insert than shapes. However, shapes
are more efficient for the program to store and draw. User-defined shapes are helpful when you must insert a simple part many
times and when speed is important.

Use the LOAD command to load a compiled shape (SHX) file containing the shape definition. Then you use the SHAPE command
to insert shapes from the file into your drawing. You can specify the scale and rotation to use for each shape as you insert
it. SHP fonts are a special type of shape file, and are defined in the same way as shape files.

## Compile Shape/Font Files

You enter the description of shapes in a specially formatted text file with a file extension of .*shp*. You use a text editor or word processor that enables you to save in ASCII format to create the shape definition (SHP) file,
and then you compile the file with the COMPILE command. Compiling a shape definition file generates a compiled shape file
(SHX) with the same name as the shape definition file.

If the shape definition file defines a font, you use the STYLE command to define a text style. Then, you add text to a drawing
to use the characters defined in the compiled shape file. If the shape definition file defines shapes, you use the LOAD command
to load the shape file into the drawing. Use the SHAPE command to insert the specified shapes into the drawing.

## Compile PostScript Fonts

A Type 1 PostScript font must first compile it into a shape file before it can be used in the program. The COMPILE command accepts both SHP and
PFB files as input and generates an SHX file.

The program cannot compile and load every Type 1 font. The PostScript font facilities in AutoCAD-based programs are intended
to process a subset of Adobe fonts. If you receive an error while compiling a PostScript font, the resulting SHX file (if
one is generated) may not load into the program.

For more information on the Adobe Type 1 font format, refer to *Adobe Type1 Font Format Version 1.1*. When you have purchased and installed these fonts, you can begin using them with the program.

NOTE:Make sure you understand any copyright that accompanies the PostScript fonts you use. The same copyright restrictions generally
apply to the SHX form of fonts you have compiled.

#### Topics in this section

* [To Compile a Shape or Font File](To-Compile-a-Shape-or-Font-File.md)

#### Related Tasks

* [To Compile a Shape or Font File](To-Compile-a-Shape-or-Font-File.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Shape Descriptions](About-Shape-Descriptions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*