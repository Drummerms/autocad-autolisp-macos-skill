# To Create a Simple Hatch Pattern

1. Open an existing PAT file or create a new file in a text editor that saves in ASCII format (for example, Notepad on Windows® or TextEdit on Mac OS®).

   NOTE:If you are creating a new PAT file, the PAT file and hatch pattern names must be identical.
2. Create a header line that begins with an asterisk and includes a pattern name that is no more than 31 characters in length.

   For example,
   \*ANSI31
3. Optionally, include a description for the hatch pattern by adding a comma and descriptive text after the pattern name.

   For example,
   \*ANSI31, ANSI Iron, Brick, Stone masonry
4. Create a descriptor line that includes
   * An angle at which the line is drawn
   * An
     *X,Y* origin point
   * A
     *delta-x*of 0
   * A
     *delta-y* of any value

   For example,
   45, 0,0, 0,.125
5. Add a blank line after the descriptor line.

   NOTE:If the blank line is missing, the hatch pattern won't be recognized by the program.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [FAQ: Why can't I use my custom hatch pattern (PAT) files?](FAQ-Why-can't-I-use-my-custom-hatch-pattern-PATfiles.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*