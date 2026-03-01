# -PURGE (Command)

Removes unused named objects, such as block definitions and layers, from the drawing using the command line.

## Summary

Allows you to remove unused named objects from a drawing at the Command prompt. You can choose to remove nested items all
at once or one level of reference at a time. If removing one level of reference at a time, repeat the command until there
are no unreferenced, named objects.

NOTE:The command will not remove
*unnamed* objects (zero-length geometry or empty text and mtext objects) from blocks or locked layers.

## List of Prompts

The following prompts are displayed.

Type of Unused Objects to Purge

:   You can specify what types of named objects that you want to remove, including blocks, detail view styles, dimension styles,
    groups, layers, linetypes, materials, multileader styles, plot styles, shapes, text styles, multiline styles, section view
    styles, table styles, visual styles, registered applications, zero-length geometry, empty text objects, and obsolete DGN linestyle
    data (orphaned data), or all of these. Enter
    *S* for settings to include or exclude nested items or orphaned data when you purge all.

Enter Name (s) to Purge
:   Enter an object name or
    *\** for all objects of the type selected.

Verify Each Name to Be Purged?
:   Enter
    *y* to verify each name.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*