# About Printing From Model Space

For a 2D drawing that has one view, you could create both the model and its annotation entirely in model space, without using
a layout.

This method is simple but has several limitations, including

* It is suitable for 2D drawings only
* It does not support multiple views and view-dependent layer settings
* Scaling the annotation and title block requires computation unless you use annotative objects.

## Process Overview

If you draw and plot from model space, you must determine and apply a scale factor to annotation objects before you plot.
Follow the steps below.

1. Determine the unit of measurement (drawing units) for the drawing.
2. Specify the display style for the drawing unit.
3. Calculate and set the scale for dimensions, annotations, and blocks.
4. Insert the title block in model space, scaled inversely to intended the plotting scale.
5. Draw at full scale (1:1) in model space.
6. Create the dimensions, notes and labels, also scaled inversely to the intended plotting scale.
7. Plot the drawing at the predetermined scale.

## Determine the Unit of Measurement

Before you begin drawing in model space, decide what each unit on the screen represents, such as an inch, a millimeter, or
a kilometer. For example, if you are drawing a motor part, you might decide that one drawing unit equals a millimeter. If
you are drawing a map, you might decide that one unit equals a kilometer.

## Specify the Display Style of Drawing Units

Once you have determined a drawing unit for the drawing, you need to specify the style for displaying the drawing unit, which
includes the unit type and precision. For example, a value of 14.5 can be displayed as 14.500, 14-1/2, or 1'2-1/2".

Specify the display style of drawing units with the UNITS command. The default drawing unit type is decimal.

## Calculate and Set the Scale for Annotations and Blocks

Before you draw, you should set the scale for dimensions, annotations, and blocks in your drawings. Scaling these elements
beforehand ensures that they are at the correct size when you plot the final drawing.

You should enter the scale for the following objects:

* *Text.* Set the text height as you create text or by setting a fixed text height in the text style (STYLE).
* *Dimensions.* Set the dimension scale in a dimension style (DIMSTYLE) or with the DIMSCALE system variable.
* *Linetypes.* Set the scale for noncontinuous linetypes with the CELTSCALE and LTSCALE system variables.
* *Hatch patterns.* Set the scale for hatch patterns in the Hatch and Gradient dialog box (HATCH) or with the HPSCALE system variable.
* *Blocks.* Specify the insertion scale for blocks either as you insert them, or set an insertion scale in the Insert dialog box (INSERT)
  or in DesignCenter (ADCENTER).

  The system variables used for inserting blocks are INSUNITS, INSUNITSDEFSOURCE, and INSUNITSDEFTARGET. This also applies to
  the border and title block of the drawing.

You can also use annotative objects if you want to scale annotations automatically.

## Determine the Scale Factor for Plotting

To plot your drawing from the Model layout, you calculate the exact scale factor by converting the drawing scale to a ratio
of 1:*n*. This ratio compares plotted units to drawing units that represent the actual size of the objects you are drawing.

For example, if you plan to plot at a scale of 1/4 inch = 1 foot, you would calculate the scale factor 48 as follows:

1/4" = 12"

1 = 12 x 4

1 (plotted unit) = 48 (drawing units)

Using the same calculation, the scale factor for 1 centimeter = 1 meter is 100, and the scale factor for 1 inch = 20 feet
is 240.

## Sample Scale Ratios for Printing from Model Space

| Scale | Scale factor | To plot text size at | Set drawing text size to |
| 1 cm = 1 m | 100 | 3 mm | 30 cm |
| 1/8" = 1'-0" | 96 | 1/8" | 12" |
| 3/16" = 1'-0" | 64 | 1/8" | 8" |
| 1/4" = 1'-0" | 48 | 1/8" | 6" |
| 3/8" = 1'-0" | 32 | 1/8" | 4" |
| 1/2" = 1'-0" | 24 | 1/8" | 3" |
| 3/4" = 1'-0" | 16 | 1/8" | 2" |
| 1" = 1'-0" | 12 | 1/8" | 1.5" |
| 1 1/2" = 1'-0" | 8 | 1/8" | 1.0" |

If you are working in metric units, you might have a sheet size of 210 x 297 mm (A4 size) and a scale factor of 20. You calculate
grid limits as follows:

210 x 20 = 4200 mm

297 x 20 = 5900 mm

#### Related Concepts

* [About Model Space and Paper Space](About-Model-Space-and-Paper-Space.md)
* [About Printing From Paper Space](About-Printing-From-Paper-Space.md)

#### Related Information

* [To Specify the Display Style for Drawing Units](To-Specify-the-Display-Style-for-Drawing-Units.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*