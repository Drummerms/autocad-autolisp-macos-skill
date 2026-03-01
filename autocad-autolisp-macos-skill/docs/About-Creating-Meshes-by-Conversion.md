# About Creating Meshes by Conversion

Convert solids, surfaces, and legacy mesh types to mesh objects.

Use the MESHSMOOTH command to convert 3D solids, surfaces, and legacy mesh objects to the enhanced mesh object in order to
take advantage of capabilities such as smoothing, refinement, creasing, and splitting.

![](../images/GUID-B112B3A0-38B5-437E-9365-54CD49661E50-low.png)

## Object Types That Can Be Converted

You obtain the most predictable results when you convert primitive 3D solid objects to mesh objects.

You can also convert other types of objects, although the conversion results may differ from what you expect. These objects
include swept surfaces and solids, legacy polygon and polyface mesh objects, regions, closed polylines, and objects created
with 3DFACE For these objects, you can often improve results by adjusting the conversion settings.

## Adjust Mesh Conversion Settings

If the conversion does not work as expected, try modifying the following system variables:

* FACETERDEVNORMAL
* FACETERDEVSURFACE
* FACETERGRIDRATIO
* FACETERMAXEDGELENGTH
* FACETERMAXGRID
* FACETERMESHTYPE
* FACETERMINUGRID
* FACETERMINVGRID
* FACETERPRIMITIVEMODE
* FACETERSMOOTHLEV

For example, if the smooth mesh optimized mesh type (FACETERMESHTYPE system variable) results in incorrect conversions, you
can set the tessellation shape to be Triangle or Mostly Quads.

You also can control the adherence to the original shape by setting the maximum distance offset, angles, aspect ratios, and
edge lengths for new faces. The following example shows a 3D solid helix that has been converted to a mesh using different
tessellation settings. The optimized mesh version has been smoothed, but the other two conversions have no smoothness. Notice,
however, that the mostly quads conversion with the lower tessellation values creates a mesh object that adheres most closely
to the original version. Smoothing this object improves its appearance even more.

![](../images/GUID-72755806-8094-4B00-8CD1-CE2E201702E2-low.png)

Similarly, if you notice that a converted mesh object has a number of long, slivered faces (which can sometimes cause gaps),
try decreasing the maximum edge length for new faces value (FACETERMAXEDGELENGTH system variable). If you are converting primitive
solid objects, this dialog box also offers the option of using the same default settings used to create primitive mesh objects.

When you select conversion candidates directly from this dialog box, you can preview the results before you accept them.

#### Related Tasks

* [To Convert Objects to Meshes Using Defaults](To-Convert-Objects-to-Meshes-Using-Defaults.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*