# To Calculate the Fixed Height for Text Objects in Model Space

1. Determine the plot scale if outputting from model space or the scale of a viewport on a layout.

   NOTE:A drawing scale consists of two values separated by an = or : character. The number on the left is the *paper units* and the number to the right is the *drawing units*. An example of a drawing scale would be 1/4"=1’ 0” or 4:1.
2. Divide the drawing units by the paper units to obtain the drawing scale factor.

   For example, 12 / 0.25 = 48. 48 is the drawing scale factor of the drawing scale 1/4” = 1’-0”.
3. Multiply the drawing scale factor by the desired text output height to determine the height of the text objects in the drawing.

   Using the drawing scale factor of 48 and a desired text height of 3/16” for the output, you would take 48 x 0.1875 to get
   a final text height of 9.

#### Related Concepts

* [About Annotation Objects](About-Annotation-Objects.md)
* [About Annotation Scale](About-Annotation-Scale.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*