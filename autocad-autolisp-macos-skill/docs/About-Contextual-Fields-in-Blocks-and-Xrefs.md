# About Contextual Fields in Blocks and Xrefs

Some fields are contextual; that is, their value is different depending on which space or layout they reside in. For example,
because each layout can have a different page setup attached, the value displayed by the PlotOrientation field can be different
in different layouts in the same drawing.

| List of contextual fields | |
| CurrentSheetCategory | CurrentSheetTitle |
| CurrentSheetCustom | DeviceName |
| CurrentSheetDescription | PageSetupName |
| CurrentSheetSubset | PaperSize |
| CurrentSheetIssuePurpose | PlotDate |
| CurrentSheetNumber | PlotOrientation |
| CurrentSheetNumberAndTitle | PlotScale |
| CurrentSheetRevisionDate | PlotStyleTable |
| CurrentSheetRevisionNumber |  |

For compatibility with previous releases, contextual fields in blocks and xrefs are not updated when you insert them in a
drawing; instead, the field displays the last cached value. Therefore, if you want to use a contextual field within a block,
for example, a title block, you must insert the field as an attribute. For example, a title block can use the CurrentSheetNumber
field as an attribute. When you insert the title block, the field displays the sheet number of the sheet on which the title
block is inserted.

Most fields are not contextual and are updated in blocks and xrefs. Fields in xrefs are updated based on the host file, not
the source xref. These fields do not have to be placed in attributes. For example, a field that displays the sheet number
of a particular sheet in a sheet set and that updates if that sheet number changes, is a property of the sheet set. When you
create the field, you select the SheetSet field name, select the sheet set and the sheet that you want in the tree view, and
then select the property SheetNumber for the field value to be displayed. This field displays the sheet number of that sheet,
even if you put the field in a block and insert it in another drawing. If the sheet is removed from the sheet set, it no longer
has a sheet number, and the field becomes invalid and displays pound signs.

Some sheet set fields can be inserted as placeholders. For example, when you create your own callout blocks and label blocks,
you can insert the SheetNumber field as a placeholder. Later, when the block is inserted from the Views List tab shortcut
menu in the Sheet Set Manager, the field displays the sheet number of the drawing.

#### Related Information

* [To Format a Field Value](To-Format-a-Field-Value.md)
* [To Edit a Field](To-Edit-a-Field.md)
* [To Work With Updating Text Fields](To-Work-With-Updating-Text-Fields.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*