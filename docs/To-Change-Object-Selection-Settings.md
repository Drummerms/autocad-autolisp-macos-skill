# To Change Object Selection Settings

You can customize many aspects of how objects are selected in order to speed up your work.

1. Right-click in the drawing area, and choose Preferences.
2. On the Cursor and Selection tab in the Application Preferences dialog box, choose the settings you want.

## Select the Command First

When you use an editing command, a Select Objects prompt is displayed and the crosshairs is replaced with a pickbox. You can
respond to the Select Objects prompt in various ways:

* Select objects one at a time.
* Click an empty area. Drag the cursor to define a rectangular selection area.
* Enter a selection option. Enter ? to display all selection options.
* Combine selection methods. For example, to select most of the objects in the drawing area, select all objects and then remove
  the objects that you do not want selected.

## Highlight Objects to Be Selected

1. Roll the pickbox cursor over the object.

   Click the preview of the object to be selected.
2. Specify an area to select multiple objects, the background of the area becomes transparent.

NOTE:These selection previewing effects are turned on by default. You can turn them off with the SELECTIONPREVIEW system variable.
When the PICKBOX system variable is set to 0, selection previewing of objects is not available.

## Select Objects First

You can use one of two methods to select objects before starting a command:

1. Use the SELECT command, and enter ? to display all selection options.

   All objects selected are put into the Previous selection set.
2. Enter p at the Select Objects prompt of any subsequent command to use the Previous selection set.,
3. When noun/verb selection is turned on, select objects at the Command prompt before entering a command such as MOVE , COPY
   , or ERASE . With this method, you can only select objects by clicking them individually or by using automatic selection.

#### Related Concepts

* [About Selecting Objects Based on Shared Properties](About-Selecting-Objects-Based-on-Shared-Properties.md)

#### Related Information

* [To Select Objects](To-Select-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*