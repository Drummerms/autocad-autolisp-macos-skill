# To Create a Hatch Pattern with Dashed Lines

1. Open an existing PAT file or create a new file in a text editor that saves in ASCII format (for example, Notepad on Windows® or TextEdit on Mac OS®).
2. Create a header line that includes an asterisk and a pattern name. The name of the hatch pattern is limited to 31 characters.

   For example, \*ANSI33

   NOTE:If you are creating a new PAT file, the PAT file and pattern must have the same name.
3. (Optional) Include a description in the header line, follow the pattern name with a comma and description text.

   For example, \*ANSI33, ANSI Bronze, Brass, Copper
4. Create a descriptor line that includes
   * An angle at which the line is drawn
   * An *X,Y* origin point
   * A  *delta-x*  of any value if you want to offset alternating lines in the line family
   * A  *delta-y*  of any value
   * A value for a dash length
   * A value for a dot length
   * An optional second value for a different dash length
   * An optional second value for a different dot length

   For example,

   45, 0,0, 0,.25

   45, .176776695,0, 0,.25, .125,-.0625
5. Add a blank line after the last descriptor line.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Hatch Patterns with Dashed Lines](About-Hatch-Patterns-with-Dashed-Lines.md)
* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [FAQ: Why can't I use my custom hatch pattern (PAT) files?](FAQ-Why-can't-I-use-my-custom-hatch-pattern-PATfiles.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*