# REVCLOUD (Command)

Creates a revision cloud using a polyline.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Rev-Cloud drop-down.
![](../images/GUID-0B452EB5-92EF-4067-8975-D5E37FA6B515-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Revision Cloud.

You can create a new revision cloud by selecting two corner points or polygonal points, dragging your cursor, or you can
convert an object such as a circle, polyline, spline, or an ellipse into a revision cloud. Use revision clouds to highlight
parts of a drawing that are being reviewed.

![](../images/GUID-B8EFF7DE-9DFE-4C34-ADED-D9796EFD1E58-low.gif)

NOTE:The first time you create a revision cloud in a drawing, the size of the arcs are determined based on percentage the diagonal
length of the current view. This ensures that the revision cloud starts at a reasonable size.

The following prompts are displayed.

## Rectangular ![](../images/GUID-0B452EB5-92EF-4067-8975-D5E37FA6B515-low.png)

Creates a rectangular revision cloud using the specified points as diagonally opposite corners.

First corner point
:   Specifies a corner point of the rectangular revision cloud.

Opposite corner
:   Specifies the diagonally opposite corner of the rectangular revision cloud.

## Polygonal ![](../images/GUID-AED9A9A0-B6B6-446C-877A-2B82130417D6-low.png)

Creates a nonrectangular revision cloud defined by three or more points as vertices of the revision cloud.

Start point
:   Sets the starting point for the polygonal revision cloud.

Next point
:   Specifies the next point to define the polygonal shape of the revision cloud.

## Freehand ![](../images/GUID-D89B6B5D-B3EF-41D0-B1CE-E350C57B8922-low.png)

Draws a freehand revision cloud.

## Common Prompts

Arc Length
:   Specifies an approximate value for the
    *chord* length of each arc. The chord length of an arc is the distance between the endpoints of the arc. The default value for the
    arc chord length is automatically determined the first time you create a revision cloud in a drawing.

Object
:   Specifies an object to be converted to a revision cloud.

    Reverse direction
    :   Reverses the direction of sequential arcs on the revision cloud.

Style
:   Specifies the style of the revision cloud.

    Normal
    :   Creates revision clouds using default typeface.

    Calligraphy
    :   Creates revision clouds as if drawn with a calligraphy pen.

Modify
:   Adds or removes sides from an existing revision cloud.

    Select polyline
    :   Specifies which revision cloud you want to modify.

    Reverse direction
    :   Reverses the direction of sequential arcs on the revision cloud.

#### Related Tasks

* [To Work With Revision Clouds](To-Work-With-Revision-Clouds.md)

#### Related References

* [REVCLOUDPROPERTIES (Command)](REVCLOUDPROPERTIES-Command.md)
* [REVCLOUDARCVARIANCE (System Variable)](REVCLOUDARCVARIANCE-System-Variable.md)

#### Related Concepts

* [About Revision Clouds](About-Revision-Clouds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*