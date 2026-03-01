# -LINETYPE (Command)

Loads, sets, and modifies linetypes.

## List of Prompts

The following prompts are displayed.

Enter an option [?/Create/Load/Set]:

?—List Linetypes
:   Displays the Select Linetype File dialog box (a
    [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)). After you select an LIN file, the linetypes available in the file are listed.

Create
:   Creates a new linetype and stores it in an LIN file.

    The Create or Append Linetype File dialog box (a
    [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)) is displayed. Specify the file to which you want the linetype added.

    You cannot create complex linetypes with LINETYPE. For more information, see "Linetypes and Linetype Definitions" in the
    *Customization Guide*.

Descriptive Text
:   Enter a linetype description up to 47 characters long. The description can be a comment or a series of underscores, dots,
    dashes, and spaces to show a simple representation of the linetype pattern.

Linetype Pattern
:   Enter a pattern definition as a series of numbers separated by commas. Enter positive values to specify lengths of dashes,
    and enter negative values to specify lengths of spaces. Use a zero to represent a dot.

    ![](../images/GUID-699DC6AF-43B6-4C7F-82D7-0E751EB716B1-low.png)

    The “A” in the pattern definition prompt specifies the pattern alignment used at the ends of individual lines, circles, and
    arcs. Only A-type alignment is supported. With A-type alignment, lines and arcs are guaranteed to start and end with a dash.
    The A is automatically included in the definition. If you use a text editor to create a linetype, you must enter
    *a* at the beginning of the definition.

    After creating a linetype, you must load it to make it accessible.

Load
:   Loads a linetype whose definition exists in a file. The
     *acad.lin*  file contains the standard linetypes.

    The Select Linetype File dialog box (a
    [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)) is displayed. Enter or select the file in which the linetype you want to load is stored.

Set
:   Sets the current linetype for objects that will be drawn subsequently. You can control the linetype of objects individually
    or by layer.

    The linetype you enter becomes the current linetype. All new objects are drawn with this linetype, regardless of the current
    layer. If the linetype you request is not loaded, the program searches for its definition in the
    acad.lin file. If the linetype is neither loaded nor in
    acad.lin, the program displays a message and returns you to the Command prompt.

    Enter
    *?* to list all loaded linetype names. If you enter
    *bylayer*, new objects inherit the linetype associated with the layer on which the object is drawn. If you enter
    *byblock*, new objects are drawn using the CONTINUOUS linetype until they are grouped into a block. Whenever you insert that block,
    the objects inherit the linetype of the block.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*