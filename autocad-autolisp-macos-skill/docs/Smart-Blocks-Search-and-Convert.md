# Smart Blocks: Search and Convert

Convert repetitive geometry, including text variations, into blocks for improved efficiency and organization.

AutoCAD 2026 offers more
*smart block* solutions to streamline your design process. In this release, BSEARCH finds all instances of the same geometry in a drawing
for efficient block conversion.

When you select geometry for conversion, AutoCAD finds and highlights all instances of the same geometry. The Search and Convert
feature also finds text variations to convert into block attributes. This capability is helpful for classifying repetitive
but variable types of text, such as hotel room numbers or room names.

![](../images/GUID-D0188781-3243-4668-8CF3-BBA10C8ABE60-low.png)

## Using existing block definitions

Once you decide to convert matching instances to a block, you see the preview thumbnail, allowing you to easily view the selected
object and text variation.

To convert the geometry based on an existing block, select a block from the list or click
![](../images/GUID-8FE3247D-F38B-430C-897E-CC866E46BC92-low.png) in the dialog box to choose a block from the drawing.

![](../images/GUID-160B580A-2615-4F92-AC5D-EAB1966D6858-low.png)

If you use an existing block definition, you can adjust the scale and rotation to determine how the selected block definition
replaces the found instances.

![](../images/GUID-B64ADFAF-D6A0-44B8-A5D2-30EAD0EAF6FD-low.png)

## Converting to a new block

You can also convert the source object or the selected instances to a new block. In the Convert to block dialog box, define
the new block by specifying a block name and insertion point. By default, the insertion point is set to the center of the
selected geometry.

![](../images/GUID-5647943F-9CD1-447A-A43F-36FE5432A722-low.png)

Along with converting matching instances to a block, you can then specify attribute tags for text variations by clicking Define
attribute tags.

![](../images/GUID-C4FE8E4D-C463-48DE-8D1B-0653B2F1CA21-low.png)

## Easy to access and use

You can now start Search and Convert by easily accessing it from the Tool Sets tab.

![](../images/GUID-4EE9A562-5509-4481-A5DD-413BF9C5EFE3-low.png)

Once you run BSEARCH, the new Search review mode highlights all matching instances.

From the Search review toolbar, you can:

* See the total number of matching instances
* Navigate to the previous or next instance in the drawing
* Adjust filters to include existing blocks or text variations
* Convert to block

![](../images/GUID-926BA195-BE7D-4B2C-9471-D646815D7DF5-low.png)

## New Commands

[BSEARCH](BSEARCH-Command-2.md) - Displays the Convert to block dialog box, which provides options to convert selected entities and identical instances into
blocks.

[-BSEARCH](BSEARCH-Command.md) - At the Command prompt, converts the selected entities and identical instances into blocks.

## New System Variables

[TEXTTOATTRIBUTE](TEXTTOATTRIBUTE-System-Variable.md) - Controls whether the BSEARCH command searches for text variations to convert into block attributes when text objects are
selected.

[BSEARCHINCLUDEEXISTINGBLOCKS](BSEARCHINCLUDEEXISTINGBLOCKS-System-Variable.md) - Controls whether BSEARCH selects existing block instances by default. Adjustments to the selection can be still be made
during the review process.

#### Related Concepts

* [What's New in AutoCAD for Mac 2026](What's-New-in-AutoCAD-for-Mac-2026.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*