# DIM (Command)

Creates multiple types of dimensions within a single command session.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension.
![](../images/GUID-5EA1A3E0-8630-4E93-9CCA-E6062287F3DD-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Dimension.

When you hover over an object for dimensioning, the DIM command automatically previews a suitable dimension type to use. Select
objects, lines, or points to dimension and click anywhere in the drawing area to draw the dimension.

The supported dimension types range from vertical, horizontal, aligned, and rotated linear dimensions, to angular dimensions,
to radius, diameter, jogged radius, and arc length dimensions, to baseline and continued dimensions. If required, you can
change the dimension type using command line options.

The following prompts are displayed.

Select objects
:   Automatically selects an applicable dimension type for the objects you select and displays the prompts corresponding to that
    dimension type.

    | Selected object type | Action |
    | Arc | Defaults the dimension type to radius dimensions. |
    | Circle | Defaults the dimension type to radius dimensions. |
    | Line | Defaults the dimension type to linear dimensions. |
    | Dimension | Displays options to modify the selected dimension. |
    | Ellipse | Defaults to options set for selecting a line. |

First extension line origin
:   Creates a linear dimension when you select two points.

Angular
:   Creates an angular dimension showing the angle between three points by or the angle between two lines (same as the DIMANGULAR
    command).

    * *Vertex.* Specifies the point to use as the vertex of the angle.
    * *Specify first side of angle.* Specifies one of the lines that form the angle.
    * *Specify second side of angle.*Specifies the other line that forms the angle.
    * *Angular dimension location.* Specifies where to place the dimension arc line. Depending on the position of the dimension, the quadrant for the dimension
      changes.
      + *Mtext.* Displays the Text Editor contextual tab, which you can use to edit the dimension text.
      + *Text.* Customizes the dimension text at the Command prompt. The generated dimension is displayed within angle brackets.
      + *Text angle.* Specifies the angle of the dimension text.
      + *Undo.* Returns to the previous prompt.
    * *Undo.* Returns to the previous prompt.

Baseline
:   Creates a linear, angular, or ordinate dimension from the first extension line of the previous or selected dimension (same
    as the DIMBASELINE command).

    NOTE:By default, the last created dimension is used as the base dimension.

    * *First extension line origin.* Specifies the first extension line of the base dimension as the extension line origin for the baseline dimension.
    * *Second extension line origin.* Specifies the next edge or angle to dimension.
    * *Feature Location.* Uses the endpoint of the base dimension (ordinate dimension) as the endpoint for the baseline dimension.
    * *Select.* Prompts you select a linear, ordinate, or angular dimension to use as the base for the baseline dimension.
    * *Offset.* Specifies the offset distance from which the baseline dimensions are created.
    * *Undo.* Undoes the last baseline dimension created.

Continue
:   Creates a linear, angular, or ordinate dimension from the second extension line of a selected dimension (same as the DIMCONTINUE
    command).

    * *First extension line origin.* Specifies the first extension line of the base dimension as the extension line origin for the continued dimension.
    * *Second extension line origin.* Specifies the next edge or angle to dimension.
    * *Feature location.* Uses the endpoint of the base dimension (ordinate dimension) as the endpoint for the continued dimension.
    * *Select.* Prompts you select a linear, ordinate, or angular dimension to use as the base for the continued dimension.
    * *Undo.* Undoes the last baseline dimension created.

Ordinate
:   Creates an ordinate dimension (same as DIMORDINATE command).

    * *Feature location.* Prompts for a point on a feature such as an endpoint, intersection, or center of an object.
      + *Leader endpoint.* Uses the difference between the feature location and the leader endpoint to determine whether it is an
        *X* or a
        *Y* ordinate dimension. If the difference in the
        *Y* ordinate is greater, the dimension measures the
        *X* ordinate. Otherwise, it measures the
        *Y* ordinate.
      + *Xdatum.* Measures the X ordinate and determines the orientation of the leader line and dimension text.
      + *Ydatum.* Measures the Y ordinate and determines the orientation of the leader line and dimension text.
      + *Mtext.* Displays the Text Editor contextual tab, which you can use to edit the dimension text.
      + *Text.* Customizes the dimension text at the Command prompt. The generated dimension is displayed within angle brackets.
      + *Angle.* Specifies the angle of the dimension text.
      + *Undo.* Returns to the previous prompt.
    * *Undo.* Returns to the previous prompt.

Align
:   Aligns multiple parallel, concentric, or same datum dimensions to a selected base dimension.

    * *Base dimension.* Specifies a dimension to use as basis for the dimensions alignment.
      + *Dimensions to align.* Selects the dimensions to align to the selected base dimension.

Distribute
:   Specifies the method on how to distribute a group of selected isolated linear or ordinate dimensions.

    * *Equal.* Equally distributes all selected dimensions. This method requires a minimum of three dimension lines.
    * *Offset.* Distributes all selected dimensions at a specified offset distance.

Layer
:   Assigns new dimensions to the specified layer, overriding the current layer. Enter Use Current or " . " to use the current
    layer. (DIMLAYER system variable)

Undo
:   Reverses the last dimension operation.

The following options are displayed when you place a dimension in such a way that it overlaps an existing dimension.

Move away
:   Arranges the existing dimension and the newly inserted dimension into a baseline dimension type.

Break up
:   Splits up the existing dimension into two dimensions, and arranges those dimensions into a continued dimension type.

Replace
:   Deletes the existing dimension and replaces it with the one you insert.

None
:   Inserts the new dimension on top of the existing dimension.

#### Related Tasks

* [To Create Multiple Types of Dimensions Within a Single Command Session](To-Create-Multiple-Types-of-Dimensions-Within-a-Single-Command-Session.md)
* [To Work with Radial Dimensions](To-Work-with-Radial-Dimensions.md)
* [To Create an Angular Dimension](To-Create-an-Angular-Dimension.md)
* [To Create an Ordinate Dimension](To-Create-an-Ordinate-Dimension.md)
* [To Create an Arc Length Dimension](To-Create-an-Arc-Length-Dimension.md)

#### Related Concepts

* [About Dimensioning](About-Dimensioning.md)

#### Related Information

* [To Work with Linear Dimensions](To-Work-with-Linear-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*