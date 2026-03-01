# About Setting the Scale for Dimensions

Dimension scale affects the size of the dimension geometry relative to the objects in the drawing. Dimension scale affects
sizes, such as text height and arrowhead size, and offsets, such as the extension line origin offset.

You should set these sizes and offsets to values that represent their actual size on paper. Dimension scale does *not* apply the overall scale factor to tolerances or measured lengths, coordinates, or angles.

NOTE: You can use annotative scaling to control the overall scale of dimensions displayed in layout viewports. When you create
annotative dimensions, they are scaled based on the current annotation scale setting and automatically displayed at the correct
size.

Setting dimension scale depends on how you lay out your drawing. There are three methods used to create dimensions in a drawing
layout:

* *Dimension in model space for plotting in model space*. This is the traditional method used with single-view drawings. To create dimensions that are scaled correctly for printing
  or plotting, set the DIMSCALE system variable to the inverse of the intended plot scale. For example, if the plot scale is
  1/4, set DIMSCALE to 4.
* *Dimension in model space for printing or plotting in paper space*. This was the preferred method for complex, multiple-view drawings prior to the 2002 products. Use this method when the dimensions
  in a drawing need to be referenced by other drawings (xrefs) or when creating isometric dimensions in 3D isometric views.
  To prevent the dimensions in one layout viewport from being displayed in other layout viewports, create a dimensioning layer
  for each layout viewport that is frozen in all other layout viewports. To create dimensions that are scaled automatically
  for display in a paper space layout, set the DIMSCALE system variable to 0.
* *Dimension in layouts*. This is the simplest dimensioning method. Dimensions are created in paper space by selecting model space objects or by specifying
  object snap locations on model space objects. By default, associativity between paper space dimensions and model space objects
  is maintained. No additional scaling is required for dimensions created in a paper space layout: DIMLFAC and DIMSCALE do not
  need to be changed from their default value of 1.0000.

NOTE:When you dimension model space objects in paper space using associative dimensions, dimension values for the display scale
of each viewport are automatically adjusted. This adjustment is combined with the current setting for DIMLFAC and is reported
by the LIST command as a dimension style override. For nonassociative dimensions, you must set DIMLFAC manually.

#### Related Tasks

* [To Set Dimension Scale for Creating Dimensions in a Layout](To-Set-Dimension-Scale-for-Creating-Dimensions-in-a-Layout.md)
* [To Set the Dimension Scale for Model Space Dimensions in Layouts](To-Set-the-Dimension-Scale-for-Model-Space-Dimensions-in-Layouts.md)
* [To Set the Overall Dimension Scale](To-Set-the-Overall-Dimension-Scale.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*