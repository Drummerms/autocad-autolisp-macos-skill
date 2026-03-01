# REVSURF (Command)

Creates a mesh by revolving a profile about an axis.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Modeling, Meshes, Revolved Surface.
![](../images/GUID-D673E1BC-7D8A-4E74-B457-27BD369ECA1A-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Revolved Mesh.

## Summary

Select a line, arc, circle, or 2D or 3D polyline to sweep in a circular path around a selected axis.

![](../images/GUID-DDEFC4D0-6AD3-416F-8B5D-C7667FF6091D-low.gif)

The
[MESHTYPE](MESHTYPE-System-Variable.md) system variable sets which type of mesh is created. Mesh objects are created by default. Set the variable to 0 to create
legacy polyface or polygon mesh.

The density of the generated mesh is controlled by the
[SURFTAB1](SURFTAB1-System-Variable.md) and
[SURFTAB2](SURFTAB2-System-Variable.md) system variables. SURFTAB1 specifies the number of tabulation lines that are drawn in the direction of revolution. If the
path curve is a line, arc, circle, or spline-fit polyline, SURFTAB2 specifies the number of tabulation lines that are drawn
to divide it into equal-sized intervals. If the path curve is a polyline that has not been spline fit, tabulation lines are
drawn at the ends of straight segments, and each arc segment is divided into the number of intervals specified by SURFTAB2.

![](../images/GUID-53242E32-FC1A-4D68-B0D4-688773843543-low.png)

## List of Prompts

The following prompts are displayed.

Current wire frame density: SURFTAB1=*current* SURFTAB2=*current*

Object to revolve
:   Select a line, arc, circle, or 2D or 3D polyline.

Object that defines axis of revolution
:   Select a line or open 2D or 3D polyline. The axis direction cannot be parallel to the plane of the original object.

    ![](../images/GUID-4A412519-F66C-469B-A7BA-F8994655E5CD-low.png)

    The path curve is swept about the selected axis to define the mesh. The path curve defines the
    *N* direction of the mesh. Selecting a circle or a closed polyline as the path curve closes the mesh in the
    *N* direction.

    ![](../images/GUID-FDF731C8-EEF9-4633-8F40-C463686AB683-low.png)

    The vector from the first to the last vertex of the polyline determines the rotation axis. Any intermediate vertices are ignored.
    The axis of revolution determines the
    *M* direction of the mesh.

Start Angle
:   If set to a nonzero value, starts the mesh of revolution at an offset from the generating path curve.

    Specifying a start angle starts the mesh of revolution at an offset from the generating path curve.

Included Angle
:   Specifies how far about the axis of revolution the mesh extends. The included angle is the distance through which the path
    curve is swept.

    Entering an included angle that is less than a full circle prevents the circle from closing.

    ![](../images/GUID-C64AE3A1-7162-4ADC-8883-586675AFBC45-low.png)

    The point you use to select the axis of revolution affects the direction of revolution. The mesh in the following example
    was created by specifying a start angle of 0 degrees and an included angle of 90 degrees.

    ![](../images/GUID-3BC236E2-931E-4BE8-8F27-EA03BD9E9F0C-low.png)

#### Related Concepts

* [About Constructing Meshes From Other Objects](About-Constructing-Meshes-From-Other-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*