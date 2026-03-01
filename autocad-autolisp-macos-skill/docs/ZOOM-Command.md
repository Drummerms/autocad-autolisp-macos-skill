# ZOOM (Command)

Increases or decreases the magnification of the view in the current viewport.

## Access Methods

*Toolbar*:
![](../images/GUID-E84156EB-BF3B-4230-B80C-9679280DFC65-low.png)

*Menu*:
View ![](../images/ac.menuaro.gif) Zoom ![](../images/ac.menuaro.gif) Realtime.

*Shortcut Menu*: With no objects selected, right-click in the drawing area and choose Zoom to zoom in real time.

## Summary

You can change the magnification of a view by zooming in and out, which is similar to zooming in and out with a camera. Using
ZOOM does not change the absolute size of objects in the drawing. It changes only the magnification of the view.

In a perspective view, ZOOM displays the
[3DZOOM](3DZOOM-Command.md) prompts.

NOTE:You cannot use ZOOM transparently during
[VPOINT](VPOINT-Command.md) or
[DVIEW](DVIEW-Command.md) or while ZOOM,
[PAN](PAN-Command.md), or
[VIEW](VIEW-Command-2.md) is in progress.

## List of Prompts

The following prompts are displayed.

Specify corner of window, enter a scale factor (nX or nXP), or

[All/Center/Dynamic/Extents/Previous/Scale/Window/Object] <real time>

All
:   Zooms to display all visible objects and visual aids.

    Adjusts the magnification of the drawing area to accommodate the extents of all visible objects in the drawing, or visual
    aids such as the grid limits (the
    [LIMITS](LIMITS-Command.md) command), whichever is larger.

    ![](../images/GUID-A8F28485-7367-4C3F-A8AC-A3D97446D6B7-low.png)

    In the illustration on the right, the grid limits are set to a larger area than the extents of the drawing.

    Because it always regenerates the drawing, you cannot use ZOOM All transparently.

Center
:   Zooms to display a view defined by a center point and a magnification value or a height. A smaller value for the height increases
    the magnification. A larger value decreases the magnification. Not available in perspective projection.

    ![](../images/GUID-DBD0B268-E775-4897-BACE-7C09F59E9332-low.png)

Dynamic
:   Pans and zooms using a rectangular view box. The view box represents your view, which you can shrink or enlarge and move around
    the drawing. Positioning and sizing the view box pans or zooms to fill the viewport with the view inside the view box. Not
    available in perspective projection.

    ![](../images/GUID-1D358C20-85AB-4920-8E19-26FACE0B528B-low.png)

    * To change the size of the view box, click, resize it, and click again to accept the new size of the view box.
    * To pan with the view box, drag it to the location you want and press Enter.

Extents
:   Zooms to display the maximum extents of all objects.

    The extents of each object in the model are calculated and used to determine how the model should fill the window.

    ![](../images/GUID-7F35EC01-92C2-49A1-A0C0-AAC9E0634704-low.png)

Previous
:   Zooms to display the previous view. You can restore up to 10 previous views.

    ![](../images/GUID-B2B9D588-AF60-44A6-AF16-7E8E356F6411-low.png)

    NOTE:If you change the visual style, the view is changed. If you enter ZOOM Previous, it restores the previous view, which is shaded
    differently but not zoomed differently.

Scale
:   Zooms to change the magnification of a view using a scale factor.

    * Enter a value followed by
      *x* to specify the scale relative to the current view.
    * Enter a value followed by
      *xp* to specify the scale relative to paper space units.

    For example, entering
    *.5x* causes each object to be displayed at half its current size on the screen.

    ![](../images/GUID-85DA378A-DC99-48D2-9ACD-070E383A1779-low.png)

    Entering
    *.5xp* displays model space at half the scale of paper space units. You can create a layout with each viewport displaying objects
    at a different scale.

    Enter a value to specify the scale relative to the grid limits of the drawing. (This option is rarely used.) For example,
    entering
    *2* displays objects at twice the size they would appear if you were zoomed to the limits of the drawing.

    ![](../images/GUID-0F211BD1-D323-435C-8790-43AD06EC5956-low.png)

Window
:   Zooms to display an area specified by a rectangular window.

    With the cursor, you can define an area of the model to fill the entire window.

    ![](../images/GUID-2BEFE835-CA36-445F-84DF-80489E78BF50-low.png)

Object
:   Zooms to display one or more selected objects as large as possible and in the center of the view. You can select objects before
    or after you start the ZOOM command.

Real Time
:   Zooms interactively to change the magnification of the view.

    The cursor changes to a magnifying glass with plus (+) and minus (-) signs.

    ![](../images/GUID-FE1A7968-AFD5-4B0D-AD0F-0BB7AEBB7E40-low.png)

    Holding down the pick button at the midpoint of the window and moving vertically to the top of the window zooms in to 100%.
    Conversely, holding the pick button down at the midpoint of the window and moving vertically to the bottom of the window zooms
    out by 100%.

    When you reach the zoom-in limit, the plus sign in the cursor disappears, indicating that you can no longer zoom in. When
    you reach the zoom-out limit, the minus sign in the cursor disappears, indicating that you can no longer zoom out.

    When you release the pick button, zooming stops. You can release the pick button, move the cursor to another location in the
    drawing, and then press the pick button again and continue to zoom the display from that location.

    To exit zooming, press Enter or Esc.

#### Related Concepts

* [About Scaling Views in Layout Viewports](About-Scaling-Views-in-Layout-Viewports.md)

#### Related Information

* [About Panning or Zooming the View](About-Panning-or-Zooming-the-View.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*