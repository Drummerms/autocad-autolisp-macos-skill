# To Create a Hatch Pattern with Multiple Lines

1. Open an existing PAT file or create a new file in a text editor that saves in ASCII format (for example, Notepad on Windows® or TextEdit on Mac OS®).

   NOTE:If you are creating a new PAT file, the PAT file and pattern must have the same name.
2. Create a header line that begins with an asterisk and includes a pattern name that is no more than 31 characters in length.

   For example,
   \*ANGLE
3. Optionally, include a description for the hatch pattern by adding a comma and descriptive text after the pattern name.

   For example,
   \*ANGLE, Angle steel
4. Create a descriptor line that includes
   * An angle at which the line is drawn
   * An
     *X,Y* origin point
   * A
     *delta-x* of any value if you want to offset alternating lines in the line family
   * A
     *delta-y* of any value
   * A value for a dash length
   * A value for a dot length
   * An optional second value for a different dash length
   * An optional second value for a different dot length

   For example,
   0, 0,0, 0,.275, .2,-.075
5. Create a second line including all the parameters in the previous step.

   For example,
   90, 0,0, 0,.275, .2,-.075
6. Optionally, create additional lines to complete the multiple-line hatch pattern.
7. Add a blank line after the last descriptor line.

   NOTE:If the blank line is missing, the hatch pattern won't be recognized by the program.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Hatch Patterns With Multiple Lines](About-Hatch-Patterns-With-Multiple-Lines.md)
* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [FAQ: Why can't I use my custom hatch pattern (PAT) files?](FAQ-Why-can't-I-use-my-custom-hatch-pattern-PATfiles.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*