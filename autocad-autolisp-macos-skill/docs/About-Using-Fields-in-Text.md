# About Using Fields in Text

A field in text contains instructions to display data that you expect to change during the life cycle of a drawing.

When a field is updated, the latest data is displayed. For example, the value of the FileName field is the name of the file.
If the file name changes, the new file name is displayed when the field is updated.

Fields can be inserted in any kind of text (except tolerances), including text in table cells, attributes, and attribute
definitions. When any text command is active, Insert Field is available on the shortcut menu.

Some project fields can be inserted as placeholders. For example, you can insert LayoutNumberAndTitle as a placeholder. Later,
when the layout is added to a project, the placeholder field displays the correct layout number and title.

Block placeholder fields can be used in block attribute definitions while you're working in the Block Editor.

A field for which no value is available displays hyphens (----). For example, the Author field, which is set in the Drawing
Properties dialog, may be blank.

An invalid field displays pound signs (####). For example, the CurrentLayoutName field, which is valid only in paper space,
displays pound signs if it is placed in model space.

## Change the Appearance of a Field

The field text uses the same text style as the text object in which it is inserted. By default, fields are displayed with
a light gray background that is not plotted FIELDDISPLAY.

Formatting options in the Insert Field control the appearance of the text that is displayed. The options that are available
depend on the type of field. For example, the format for date fields includes options for displaying the day of the week and
the time, and the format for named object fields includes capitalization options.

#### Related Tasks

* [To Insert a Field in a Table](To-Insert-a-Field-in-a-Table.md)

#### Related Information

* [To Insert a Field in Text](To-Insert-a-Field-in-Text.md)
* [To Use a Field to Display an Object Property](To-Use-a-Field-to-Display-an-Object-Property.md)
* [To Insert a Sheet Set Placeholder Field](To-Insert-a-Sheet-Set-Placeholder-Field.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*