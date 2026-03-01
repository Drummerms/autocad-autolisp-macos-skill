# -BLOCK (Command)

If you enter
*-block*at the Command prompt, the following prompts are displayed.

## Block Name

Names the block. The name can have up to 255 characters and can include letters, numbers, blank spaces, and any special character
not used by the operating system and the program for other purposes if the system variable EXTNAMES is set to 1.

Redefine Block Reference
:   By redefining a block, you automatically update all references to that block. Attributes attached to existing block references
    remain unchanged in the drawing. However, new insertions of the block do not prompt for attributes unless the attribute definitions
    are included in the new block definition.

    Use the ATTREDEF command to update the attributes of an existing block insert. (Not available in AutoCAD LT.)

## Insertion Base Point

The point specified as the base point is used for subsequent insertions of the block. Typically, a base point is the center
of the block or its lower-left corner. The base point is also the point about which you can rotate the block during insertion.
A block with 0 rotation is oriented according to the UCS in effect when it was created. Entering a 3D point inserts the block
at a specific elevation. Omitting the
*Z* coordinate uses the current elevation.

![](../images/GUID-87FC52E1-34DA-4E5F-86E9-D901C50A7B38-low.png)

Annotative
:   Creates an annotative block.

    Orient Relative to Sheet in Paper Space Viewports
    :   If you enter
        *yes*, the block’s orientation in paper space viewports will match the orientation of the layout.

Mode
:   Specifies the mode for object conversion.

    * *Convert to block.* Converts the selected objects to a block instance in the drawing after you create the block.
    * *Retain.* Retains the selected objects as distinct objects in the drawing after you create the block.
    * *Delete.* Deletes the selected objects from the drawing after you create the block.

## Select Objects

Selects the objects for the block.

![](../images/GUID-18E7E333-B2B1-4C20-960A-B5BCBE444720-low.png)

## ?—List Previously Defined Blocks

Lists the block names in the text window.

Enter Blocks to List
:   In the list, external references (xrefs) are indicated with the notation
    *Xref: resolved*.

    In addition, externally dependent blocks (blocks in an xref) are indicated with the notation
    *xdep: XREFNAME*, where
    *xrefname* is the name of an externally referenced drawing. The following terms are used in the list:

    * *User Blocks:* Number of user-defined blocks in the list.
    * *External References:* Number of xrefs in the list.
    * *Dependent Blocks:* Number of externally dependent blocks in the list.
    * *Unnamed Blocks:* Number of unnamed (anonymous) blocks in the drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*