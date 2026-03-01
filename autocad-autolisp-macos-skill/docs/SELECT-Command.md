# SELECT (Command)

Places selected objects in the Previous selection set.

## Summary

A small box, called the object selection target or
*pickbox*, replaces the crosshairs on the graphics cursor.

![](../images/GUID-81C8A514-20D7-486B-BF12-B9074A7CE26A-low.png)

At the Select Objects prompt in a subsequent command, use the Previous option to retrieve the previous selection set.

You can also press and hold the Ctrl key to select original individual forms that are part of composite solids or vertices,
edges, and faces on 3D solids. You can select one of these
*subobjects*, or create a selection set of more than one subobject. Your selection set can include more than one type of subobject.

To view all options, enter
*?* at the Command prompt.

## List of Prompts

The following prompts are displayed.

Select objects: *Use an object selection method*

Expects a point or

[Window](SELECT-Command.md)/[Last](SELECT-Command.md)/[Crossing](SELECT-Command.md)/[BOX](SELECT-Command.md)/[ALL](SELECT-Command.md)/[Fence](SELECT-Command.md)/[WPolygon](SELECT-Command.md)/[CPolygon](SELECT-Command.md)/[Group](SELECT-Command.md)/[Add](SELECT-Command.md)/[Remove](SELECT-Command.md)/[Multiple](SELECT-Command.md)/[Previous](SELECT-Command.md)/[Undo](SELECT-Command.md)/[AUto](SELECT-Command.md)/[SIngle](SELECT-Command.md)/[SUbobject](SELECT-Command.md)/[Object](SELECT-Command.md)

Select objects:
*Specify a point or enter an option*

Window
:   Selects all objects completely inside a rectangle defined by two points. Specifying the corners from left to right creates
    a window selection. (Specifying the corners from right to left creates a crossing selection.)

    ![](../images/GUID-99A300E9-322D-4F14-B7AA-51B291AB2F33-low.png)

Last
:   Selects the most recently created visible object. The object must be in the current space, that is, model space or paper space,
    and its layer must not be set to frozen or off.

Crossing
:   Selects objects within and crossing an area defined by two points. A crossing selection is displayed as dashed or otherwise
    highlighted to differentiate it from window selection.

    ![](../images/GUID-EB6D919A-DFB1-4D6E-A7DC-603B951258BF-low.png)

Box
:   Selects all objects inside or crossing a rectangle specified by two points. If the rectangle's points are specified from right
    to left, Box is equivalent to Crossing. Otherwise, Box is equivalent to Window.

All
:   Selects all objects in either model space or the current layout, except those objects on frozen or on locked layers.

    ![](../images/GUID-7C58B2F2-CC1F-494C-BC68-4C0CE9287DEE-low.png)

Fence
:   Selects all objects crossing a selection fence. The Fence method is similar to CPolygon except that that the fence is not
    closed, and a fence can cross itself. Fence is not affected by the
    [PICKADD](PICKADD-System-Variable.md) system variable.

    ![](../images/GUID-8C6239CB-5140-4A9C-AFCD-9D507D4FDAFE-low.png)

WPolygon
:   Selects objects completely inside a polygon defined by points. The polygon can be any shape but cannot cross or touch itself.
    The last segment of the polygon is drawn so that it is closed at all times. WPolygon is not affected by the
     [PICKADD](PICKADD-System-Variable.md) system variable.

    ![](../images/GUID-C00BC31E-0086-4D97-9156-F210481E394D-low.png)

CPolygon
:   Selects objects within and crossing a polygon defined by specifying points. The polygon can be any shape but cannot cross
    or touch itself. The last segment of the polygon is drawn so that it is closed at all times. CPolygon is not affected by the
     [PICKADD](PICKADD-System-Variable.md) system variable.

    ![](../images/GUID-3558FA8F-15BD-4E19-8AC0-DFB47F4C96CE-low.png)

Group
:   Selects all objects within a specified group.

Add
:   Switches to the Add method: selected objects can be added to the selection set by using any of the object selection methods.
    Auto and Add are the default methods.

    ![](../images/GUID-BFDF4ED0-5DD9-422C-B318-A3439F0A6AC3-low.png)

Remove
:   Switches to the Remove method: objects can be removed from the current selection set using any object selection method. An
    alternative to Remove mode is to hold down Shift while selecting single objects or use the Automatic option.

Multiple
:   Selects objects individually without highlighting them during object selection. This speeds up object selection for highly
    complex objects.

Previous
:   Selects the most recent selection set. The Previous selection set is cleared by operations that delete objects from the drawing.

    NOTE:The Previous selection set is ignored if you switch spaces.

Undo
:   Cancels the selection of the object most recently added to the selection set.

Auto
:   Switches to automatic selection: pointing to an object selects the object. Pointing to a blank area inside or outside an object
    forms the first corner of a box defined by the Box method. Auto and Add are the default methods.

Single
:   Switches to the Single method: selects the first object or set of objects designated rather than continuing to prompt for
    further selections.

Subobject
:   Allows you to select original individual forms that are part of composite solids or vertices, edges, and faces on 3D solids.
    You can select one of these
    *subobjects*, or create a selection set of more than one subobject. Your selection set can include more than one type of subobject.

    Pressing and holding the Ctrl key is the same as selecting the SELECT command’s Subobject option.

    ![](../images/GUID-176CE1F2-F663-4900-A849-BC8F9A115FB8-low.png)

Object
:   Ends the ability to select subobjects. Allows you to use object selection methods.

#### Related Concepts

* [About Selecting Objects Based on Shared Properties](About-Selecting-Objects-Based-on-Shared-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*