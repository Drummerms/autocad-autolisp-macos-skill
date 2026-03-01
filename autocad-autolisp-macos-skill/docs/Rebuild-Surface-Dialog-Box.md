# Rebuild Surface Dialog Box

Rebuilds the CV hull of a NURBS surface.

CVREBUILD (Command)

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface CV - Rebuild.
![](../images/GUID-D9D6A3B2-A70F-4681-B7DA-490B4F064C35-low.png)

## Summary

Reshapes a NURBS surface by rebuilding the CV hull.

## List of Options

The following options are displayed.

Control Vertices Count

Specifies the number of control vertices in the U and V directions.

In U Direction
:   Specifies the number of control vertices in the
    *U* direction. (REBUILDU system variable)

In V Direction
:   Specifies the number of control vertices in the
    *V* direction. (REBUILDV system variable)

Degree

Specifies the number of control vertices available per span. The higher the number, the more complex the surface.

In U Direction
:   Specifies the degree of the NURBS surface in the
    *U* direction. (REBUILDDEGREEU system variable)

In V Direction
:   Specifies the degree of the NURBS surface in the
    *V* direction. (REBUILDDEGREEV system variable)

Options

Specifies the build options. (REBUILDOPTIONS system variable)

Delete Input Geometry
:   Specifies whether the original surface is retained along with the rebuilt surface. (REBUILDOPTIONS system variable)

Retrim Previously Trimmed Surface
:   Specifies whether trimmed areas from the original surface are applied to the rebuilt surface. (REBUILDOPTIONS system variable)

Maximum Deviation

Displays the maximum deviation between the original surface and the new one.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*