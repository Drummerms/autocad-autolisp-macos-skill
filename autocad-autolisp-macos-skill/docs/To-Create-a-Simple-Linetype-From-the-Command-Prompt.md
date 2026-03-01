# To Create a Simple Linetype From the Command Prompt

1. At the Command prompt, enter *-linetype*.
2. Enter *c* and press Enter.
3. Enter a name for the linetype and press Enter.

   The linetype name can include up to 255 characters. Linetype names can contain letters, digits, and the special characters
   dollar sign ($), hyphen (-), and underscore (\_). Linetype names cannot include blank spaces.
4. In the Create or Append Linetype File dialog box, select an existing LIN linetype file or enter a new file name in the File
   Name box. Click Save.

   If you select an existing file, the new linetype name is added to the file.
5. (Optional) Enter text that describes the new linetype and press Enter.
6. At the Enter Linetype Pattern prompt, specify the pattern for the tinetype and press Enter. Follow these guidelines:
   * All linetypes must begin with a dash.
   * Enter zeros for dots.
   * Enter negative real numbers for spaces. The value defines the length of the space in drawing units.
   * Enter positive real numbers for dashes. The value defines the length of the dash in drawing units.
   * Separate each dot, dash, or space value from the next with a comma.
   * Use a space between a dot and a dash.
7. Press Enter to end the command.

NOTE:When you create a linetype, it is not loaded into your drawing automatically. Use the Load option of the -LINETYPE or the
Load button in the Linetype Manager (LINETYPE command).

#### Related Tasks

* [To Add a Simple Linetype to an LIN File](To-Add-a-Simple-Linetype-to-an-LIN-File.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*