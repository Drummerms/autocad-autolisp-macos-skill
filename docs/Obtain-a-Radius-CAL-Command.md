# Obtain a Radius (CAL Command)

The
*rad* function determines the radius of a selected object.

rad
:   Determines the radius of a selected object. The object can be a circle, an arc, or a 2D polyline arc segment.

    The following example uses
    *rad* with the
    [CIRCLE](CIRCLE-Command.md) command. The radius of the new circle is two-thirds of the radius of the selected polyline arc segment:

    Command:
    *circle*

    Specify center point for circle or [3P/2P/Ttr (tangent tangent radius)]:
    *cen*

    of
    *Select the circle*

    Specify radius of circle or [Diameter] <*last*>: '*cal*

    >> Expression:
    *2/3\*rad*

    >> Select circle, arc or polyline segment for RAD function:
    *Select the circle*

    ![](../images/GUID-013536BF-35D0-41BA-84CD-454F825EAE93-low.png)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*