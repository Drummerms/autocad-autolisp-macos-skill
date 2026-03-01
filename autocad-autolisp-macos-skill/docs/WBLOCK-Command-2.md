# -WBLOCK (Command)

Saves selected objects or converts a block to a specified drawing file.

If FILEDIA is set to 1, entering
*-wblock*at the Command prompt displays a standard file selection dialog box in which to specify a name for the new drawing file. If
FILEDIA is set to 0, entering
*-wblock*at the Command prompt displays a prompt. The new drawing is saved in the file format that is specified in Save As on the General
tab in the Application Preferences dialog box.

After the file is created, the selected objects are deleted from the drawing. You can use OOPS to restore the objects.

In the new drawing, the world coordinate system (WCS) is set parallel to the user coordinate system (UCS).

The following prompts are displayed.

Name of output file
:   Specifies the path and name of the output file.

Existing Block
:   Saves the specified objects to an existing block file. You cannot enter the name of an external reference (xref) or one of
    its dependent blocks.

Define new drawing
:   Saves the objects to a new drawing file.

    * *=.*Specifies that the existing block and the output file have the same name.
    * *\*.*Writes the entire drawing to the new output file, except for unreferenced symbols. Model space objects are written to model
      space, and paper space objects are written to paper space.

    ![](../images/GUID-66B97DBD-4D8C-4790-82CA-F2B5F88633FD-low.png)

Insertion Base Point
:   Specifies an insertion base point for the block. The default value is 0,0,0.

Mode
:   Sets the effect of block creation on objects used to create a block.

    * *Convert to block.* Converts the selected object or objects to a block in the current drawing after saving them as a file.
    * *Retain.* Retains the selected objects in the current drawing after saving them as a file.
    * *Delete.* Deletes the selected objects from the current drawing after saving them as a file.

Select Objects
:   Selects one or more objects to save to the file.

#### Related References

* [WBLOCK (Command)](WBLOCK-Command.md)
* [Write Block Dialog Box](Write-Block-Dialog-Box.md)

#### Related Concepts

* [About Defining Blocks](About-Defining-Blocks.md)
* [About Modifying Block Definitions](About-Modifying-Block-Definitions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*