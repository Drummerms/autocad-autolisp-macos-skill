# Symbols and Arrows Tab (Dimension Style Manager)

Sets the format and placement for arrowheads, center marks, arc length symbols, and jogged radius dimensions.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-73CE3BB8-A5BC-4F92-9C38-56AF9DA6903B-low.png)

## Summary

Controls the appearance of the dimension arrowheads.

## List of Options

The following options are displayed.

Arrowheads

First
:   Sets the arrowhead for the first dimension line. When you change the first arrowhead type, the second arrowhead automatically
    changes to match it. (DIMBLK1 system variable)

    To specify a user-defined arrowhead block, select User Arrow. The Select Custom Arrow Block dialog box is displayed. Select
    the name of a user-defined arrowhead block. (The block must be in the drawing.)

Second
:   Sets the arrowhead for the second dimension line. (DIMBLK2 system variable)

    To specify a user-defined arrowhead block, select User Arrow. The Select Custom Arrow Block dialog box is displayed. Select
    the name of a user-defined arrowhead block. (The block must be in the drawing.)

Leader
:   Sets the arrowhead for the leader line. (DIMLDRBLK system variable)

    To specify a user-defined arrowhead block, select User Arrow. The Select Custom Arrow Block dialog box is displayed. Select
    the name of a user-defined arrowhead block. (The block must be in the drawing.)

Arrow Size
:   Displays and sets the size of arrowheads. (DIMASZ system variable)

NOTE: Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

Dimension Break

Controls the gap width of dimension breaks.

Break Size
:   Displays and sets the size of the gap used for dimension breaks.

Center Marks

Controls the appearance of center marks and centerlines for diameter and radial dimensions. The DIMCENTER, DIMDIAMETER, and
DIMRADIUS commands use center marks and centerlines. For DIMDIAMETER and DIMRADIUS, the center mark is drawn only if you place
the dimension line outside the circle or arc.

Type

Sets the type of center mark or line to use.

None
:   Creates no center mark or centerline. The value is stored as 0 in the DIMCEN system variable.

Mark
:   Creates a center mark. The size of the center mark is stored as a positive value in the DIMCEN system variable.

Line
:   Creates a centerline. The size of the centerline is stored as a negative value in the DIMCEN system variable.

Size

Displays and sets the size of the center mark or centerline. (DIMCEN system variable)

Radius Jog Dimension

Controls the display of jogged (zigzag) radius dimensions.

Jogged radius dimensions are often created when the center point of a circle or arc is located off the page.

![](../images/GUID-22E403DA-9B38-4B2C-856E-B0E48E74049F-low.png)

Jog Angle
:   Determines the angle of the transverse segment of the dimension line in a jogged radius dimension. (DIMJOGANG system variable)

Arc Length Symbol

Controls the display of the arc symbol in an arc length dimension. (DIMARCSYM system variable)

Preceding Dimension Text
:   Places arc length symbols before the dimension text. (DIMARCSYM system variable)

Above Dimension Text
:   Places arc length symbols above the dimension text. (DIMARCSYM system variable)

None
:   Suppresses the display of arc length symbols. (DIMARCSYM system variable)

Linear Jog Dimension

Controls the display of the jog for linear dimensions.

Jog lines are often added to linear dimensions when the actual measurement is not accurately represent by the dimension. Typically
the actual measurement is smaller than the desired value.

![](../images/GUID-8BB29294-0304-4B42-8A11-06904EE45CC0-low.png)

Jog Height Factor
:   Determines the height of the of the jog, which is determined by the distance between the two vertices of the angles that make
    up the jog.

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*