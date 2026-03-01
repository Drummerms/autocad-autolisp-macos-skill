# To Add a Simple Linetype to an LIN File

1. Open an LIN file in a text editor that saves in ASCII format (for example, Notepad on Windows® or TextEdit on Mac OS®).
2. Create a header line that includes an asterisk and a linetype pattern name. The name of the linetype pattern is limited to
   31 characters.

   For example,

   ```
   *BORDER,Border
   ```
3. (Optional) Include a description on the header line, follow the linetype pattern name with a comma and description text.

   For example,

   ```
   *BORDER,Border __ __ . __ __ . __ __ . __ __ . __ __ .
   ```
4. Create a descriptor line that follows these rules:
   * All linetypes must begin with a dash.
   * Enter zeros for dots.
   * Enter negative real numbers for spaces. The value defines the length of the space in drawing units.
   * Enter positive real numbers for dashes. The value defines the length of the dash in drawing units.
   * Separate each dot, dash, or space value from the next with a comma.
   * Use a space between a dot and a dash.

   For example,

   ```
   A,.5,-.25,.5,-.25,0,-.25
   ```

#### Related Tasks

* [To Create a Simple Linetype From the Command Prompt](To-Create-a-Simple-Linetype-From-the-Command-Prompt.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*