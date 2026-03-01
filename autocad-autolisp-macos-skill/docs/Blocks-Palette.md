# Blocks Palette

Allows you to access and insert blocks from the current drawing, recently used, or block libraries.

CONTENT (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Blocks Palette.
![](../images/GUID-6857E103-73A1-42F1-AA87-3265189DB33B-low.png)

*Menu*:
Window ![](../images/ac.menuaro.gif) Blocks.

![](../images/GUID-C997FCC0-1B2F-4EC2-ACBC-B488CD780FE3-low.png)

## List of Options

The following options are displayed.

### Toolbar

* ![](../images/GUID-D864EF4F-F367-4F19-A0F0-FEC90A9016BB-low.png) Displays the blocks in the current drawing.
* ![](../images/GUID-74621D09-5D97-4EB8-AD0F-63B2FCA60602-low.png) Displays recently inserted or created blocks. The recent list persists across drawings and sessions.

  NOTE:The name of an external file that's inserted as a block includes an asterisk (\*) in the Blocks palette.
* ![](../images/GUID-A9E5F9C7-C2A7-4C8A-B730-E7600EE4DFA2-low.png) Displays the blocks from a block library. Click browse to specify a drawing file or folder.
  ![](../images/GUID-D803F078-FF46-4D80-895E-A476EB77DD99-low.png)

#### Block Libraries Navigation

* Specify a cloud storage file or folder that contains the blocks. Use this method to share blocks across devices. A block library
  located on the cloud is indicated on the palette.

  ![](../images/GUID-FB3291C6-CE4A-4F2A-BE12-52CD58F3A011-low.png)
* Double-click a subfolder to display the contents of that folder.

  ![](../images/GUID-B91FC5AB-21CA-4EFD-A242-06EAD46A5188-low.png)
* Click Back to Library to return to the previous drawing or folder.
  ![](../images/GUID-741CB467-ECF5-4CD9-A008-9A1772E9CEE5-low.png)
* Select Sample Libraries from the drop-down menu to access the legacy block libraries.

  ![](../images/GUID-77D7A4CF-9252-4E61-BE92-81993574B4BF-low.png)

### Blocks List

Displays the blocks for the selected category. To insert a block do one of the following:

* Drag and drop a block from the list
* Double-click on a block thumbnail
* Right-click on a block thumbnail and select Insert in Drawing
* Click the block icon from the current drawing view to browse to any DWG file to insert

  ![](../images/GUID-5C9A34CE-37E9-48E4-BAC0-9844D5B941F7-low.png)

NOTE:The Block shortcut menu is displayed when you right-click over a block thumbnail, while the Blocks List shortcut menu is displayed
when you right-click an empty area of the Blocks list.

### Block Shortcut Menu

The following options are available when you right-click a block thumbnail in the Blocks list:

* *Insert in Drawing* - Starts the insertion of the block in the current drawing.
* *Rename* - Renames the block definition in the current drawing. Available only when viewing the current drawing list.
  ![](../images/GUID-D864EF4F-F367-4F19-A0F0-FEC90A9016BB-low.png)
* *Remove* - Removes the selected block from the recent Blocks list. Available only when viewing the recent Blocks list.
  ![](../images/GUID-74621D09-5D97-4EB8-AD0F-63B2FCA60602-low.png)
* *Clear All* - Removes all blocks from the recent Blocks list. Available only when viewing the recent Blocks list.
  ![](../images/GUID-74621D09-5D97-4EB8-AD0F-63B2FCA60602-low.png)
* *Small Thumbnails* - Small thumbnails for the blocks are displayed in the Blocks list.
* *Medium Thumbnails* - Medium thumbnails for the blocks are displayed in the Blocks list.
* *Medium Thumbnails with Title* - Medium thumbnails for the blocks and the block name are displayed in the Blocks list.
* *Large Thumbnails* - Large thumbnails for the blocks are displayed in the Blocks list.
* *Large Thumbnails with Title* - Large thumbnails for the blocks and the block name are displayed in the Blocks list.

### Blocks List Shortcut Menu

The following options are available when you right-click in an empty area of the Blocks list:

* *Small Thumbnails* - Small thumbnails for the blocks are displayed in the Blocks list.
* *Medium Thumbnails* - Medium thumbnails for the blocks are displayed in the Blocks list.
* *Medium Thumbnails with Title* - Medium thumbnails for the blocks and the block name are displayed in the Blocks list.
* *Large Thumbnails* - Large thumbnails for the blocks are displayed in the Blocks list.
* *Large Thumbnails with Title* - Large thumbnails for the blocks and the block name are displayed in the Blocks list.
* *Clear All* - Removes all blocks from the recent Blocks list. Available only when viewing the recent Blocks list.
  ![](../images/GUID-74621D09-5D97-4EB8-AD0F-63B2FCA60602-low.png)

## Search

Filters the blocks displayed in the Blocks list. Click the ‘X’ in the text box to clear the current filter.

Enter a text string to control which blocks are displayed in the Blocks list. Only the blocks with names that contain the
text string are displayed in the Blocks list. Search results include blocks from the current drawing, recently used, and the
active block library.

## Insertion Options

Insertion Point
:   Specifies the insertion point for the block. When checked, you specify the insertion point when inserting the block, using
    either your pointing device or manually entering coordinates. When cleared, specified coordinates are used.

    NOTE:Does not apply when you drag to place a block.

Scale
:   Specifies the scale for the inserted block. When checked, you specify the scale factors in the X, Y, and Z directions. If
    you enter a negative value for the
    *X*,
    *Y*, and
    *Z* scale factors, the block is inserted as mirror image around that axis. When cleared, specified scales are used.

    NOTE:When checked, the last entered values are used when you drag to insert a block. You are not prompted for the scale.

Rotation
:   Specifies the rotation angle for the inserted block in the current UCS. When checked, you specify the rotation angle of the
    block using the pointing device or entering an angle. When cleared, the specified rotation angle is used.

    NOTE:When checked, the last entered values are used when you drag to insert a block. You are not prompted for the rotation.

Repeat Placement
:   Controls whether the block insertion automatically repeats. When checked, you will be prompted automatically for additional
    insertion points until you press Esc to cancel the command. When cleared, the block you specified is inserted once.

    NOTE:Does not apply when you drag to place a block.

Explode
:   Controls whether the block is automatically exploded into its component objects when inserted.

    NOTE:Does not apply when you drag to place a block.

    When checked, the component objects in the block are disassociated and revert to their original properties. As an indication
    that the block will be exploded on insertion, the preview of the block at the cursor is automatically suppressed. Objects
    using the BYBLOCK color are white. Objects with BYBLOCK linetype use the CONTINUOUS linetype.

    When this option is cleared, the specified block is inserted without being exploded.

    NOTE:You can specify this option with a uniform scale factor only. If you need to explode a non-uniformly scaled block, you can
    still do so manually with the EXPLODE command.

#### Related References

* [CONTENT (Command)](CONTENT-Command.md)

#### Related Concepts

* [About Inserting Blocks](About-Inserting-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*