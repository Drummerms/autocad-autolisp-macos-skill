# Insert Field Dialog Box

Inserts a field in the drawing.

FIELD (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Table panel ![](../images/ac.menuaro.gif) Insert Field.
![](../images/GUID-CC21923E-59F3-4EBE-B889-5DE61360D96C-low.png)

![](../images/GUID-D854B134-107D-4568-BFBB-7AAA67D2987E-low.png)

## Summary

The options available change based on the selected field category and field name.

## List of Options

The following options are displayed.

Field Category
:   Sets the types of fields to be listed under Field Names (for example, Date & Time, Document, and Objects).

Field Names
:   Lists the fields that are available in a category. Select a field name to display the options available for that field.

Preview
:   Displays the current value of the field, or displays an empty string (----) if the field value is invalid.

    The label for this item can vary based on the selected field name. For example, when Date is selected in the Field Names list,
    the label is Format and the selected date format is displayed; for example, M/d/yyyy.

Format List
:   Lists options for display of the value of the field. For example, date fields can display the name of the day or not, and
    text strings can be uppercase, lowercase, first capital, or title case. The value displayed in the Fields dialog box reflects
    the format that you select.

Field Expression
:   Displays the expression that underlies the field. The field expression cannot be edited, but you can learn how fields are
    constructed by reading this area.

### Options for Sheet Set and Sheet View Fields

SheetSet
:   Specifies the name of the sheet set.

    Use the list to choose one of the loaded sheet set data (DST) files or click Load Sheet Set to load a sheet set data file
    that is not currently loaded in the Sheet Set Manager.

Sheet Navigation Tree
:   Displays a tree view of sheets or sheet views in the selected sheet set data (DST) file, from which you can select an item
    for the field.

Property
:   Displays the properties available as fields for the item selected in the tree.

NOTE:If you recreate the field, because the sheet is already in a sheet set, you should use a sheet set property field, not a placeholder
field.

Sheet set fields (fields that were selected from the sheet set category) behave differently than other types of fields. By
default, other types of fields update automatically when you save the drawing or when you use
[REGEN](REGEN-Command.md). In contrast, sheet set fields store the last values that were used, and they display these stored values if the information
referenced by the sheet set field is not accessible. To update the value in a sheet set field, use
[UPDATEFIELD](UPDATEFIELD-Command.md) command.

NOTE:If the information referenced by a sheet set field is not accessible, the value for the field will be displayed as “####.”

### Options for SheetSetPlaceholder Fields

Type
:   Displays a list of available placeholder fields.

Custom
:   When Type is set to Custom, you can enter the name of a custom property.

### Options for Fields in the Objects Field Category

Named Object Type/Object Type
:   When NamedObject is selected in Field Names, lists the types of named objects in the drawing. When Object is selected, displays
    the type of object selected. Use the Select Object button to temporarily close the dialog box and select an object in the
    drawing.

Property/Name
:   When NamedObject is selected in Field Names, lists the names of all the objects in the drawing of the selected type. When
    Object is selected in Field Names, lists the properties of the selected object that are available as fields. When a block
    with attributes is selected, the attribute names are displayed in the list of properties.

### Formula

When Formula is selected in Field Names, provides a place for creating a formula to insert in text or in a table cell.

Average/Sum/Count
:   When Formula is selected in Field Names, closes the Field dialog box temporarily while you specify table cells. The result
    is appended to the formula.

Cell
:   When Formula is selected in Field Names, closes the Field dialog box temporarily while you specify a table cell. The cell
    address is appended to the formula.

Precision
:   Specifies precision for fields based on the selected format. Select Current Precision to use the current setting of the
    [LUPREC](LUPREC-System-Variable.md) system variable.

Additional Format
:   Displays the
    [Additional Format dialog box](Additional-Format-Dialog-Box.md).

#### Related References

* [Edit Text Dialog Box](Edit-Text-Dialog-Box.md)
* [DDEDIT (Command)](DDEDIT-Command.md)
* [TEXT (Command)](TEXT-Command.md)
* [TEXTED (System Variable)](TEXTED-System-Variable.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*