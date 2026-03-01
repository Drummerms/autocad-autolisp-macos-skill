# About Calculating the Scale of Annotation Objects in Model Space

If you print from model space, annotation objects must be scaled according to the scale of the intended output.

When calculating the scale for annotation objects for printing from model space, follow these guidelines:

* *Dimensions.* Set the dimension scale factor to the inverse of the drawing scale. For example, if the intended scale is 1" = 4' (1:48 scale),
  set the dimension scale factor, DIMSCALE, to 48. Then, when the drawing is printed at 1:48 scale, the dimensions will be printed
  at the correct scale.
* *Text.* Text height must be multiplied by the inverse of the intended scale. For 1/4" text at a 1:48 scale, create the text with
  a height of 12". The calculation is 1/4 x 48 = 12.
* *Linetypes.* The linetype scale factor also needs to be changed based on the linetype definition and intended scale of the drawing. For
  example, if the intended scale is 1" = 4' (1:48 scale) and you want to use a dashed linetype that prints dashes that are 1/8"
  in length, set the linetype scale factor, LTSCALE, to 12.
* *Hatches.* Set the hatch scale based on the pattern used. Hatch patterns that start with AR commonly use the drawing scale factor as
  the appropriate value for the hatch scale.
* *Attributes and Tables*. Use the same scaling as text objects.
* *Block Definitions.* Blocks are usually created at a 1:1 scale. However, if they contain text or attributes they might need to be scaled using
  the same method as text.

#### Related Tasks

* [To Calculate the Fixed Height for Text Objects in Model Space](To-Calculate-the-Fixed-Height-for-Text-Objects-in-Model-Space.md)

#### Related Concepts

* [About Annotation Scale](About-Annotation-Scale.md)
* [About Annotative Objects and Styles](About-Annotative-Objects-and-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*