# STRETCH (Command)

Stretches objects crossed by a selection window or polygon.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Stretch.
![](../images/GUID-9C413D4F-E14A-425C-AC00-CAABC1582429-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Stretch.

Objects that are partially enclosed by a crossing window are stretched. Objects that are completely enclosed within the crossing
window, or that are selected individually, are moved rather than stretched. Some types of objects such as circles, ellipses,
and blocks, cannot be stretched.

![](../images/GUID-40FB91F4-653E-402D-BD9D-95D6ADD76C75-low.gif)

The following prompts are displayed.

## Select objects

Specifies the portion of the object that you want to stretch. Use the cpolygon option or the crossing object selection method.
Press Enter when the selection is complete.

![](../images/GUID-E44BC370-86F5-48D7-91CB-D1F6F383FD98-low.png)

STRETCH moves only the vertices and endpoints that lie inside the crossing selection, leaving those outside unchanged. STRETCH
does not modify 3D solids, polyline width, tangent, or curve-fitting information.

## Base Point

Specifies the base point from which the offset for the stretch is calculated. This base point can be outside the area being
stretched.

Second point
:   Specifies a second point that defines the distance and direction of the stretch. The distance and direction of this point
    from the base point defines how far the and in what direction the selected portions of the object will be stretched.

    ![](../images/GUID-A615C212-792B-4B4F-B9C3-4450FAC6B161-low.png)

Use first point as displacement
:   Specifies that the stretch distance and direction will be based on the distance and direction of the base point you specified
    from the 0,0,0 coordinates in the drawing.

## Displacement

Specifies the relative distance and direction of the stretch.

* To set a displacement based on the relative distance from the current location, enter distances in *X,Y, Z* format. For example, enter 5,4,0 to stretch the selection to a point that is 5 units along the X axis and 4 units along the
  Y axis from the original point.
* To set the displacement based on the distance and direction from the 0,0,0 coordinates in the drawing, click a location in
  the drawing area. For example, click a point at 1,2,0 to stretch the selection to a point that is 1 unit along the X axis
  and 2 units along the Y axis from its current location.

#### Related Tasks

* [To Stretch an Object](To-Stretch-an-Object.md)
* [To Move Objects With the Stretch Command](To-Move-Objects-With-the-Stretch-Command.md)
* [To Stretch Multiple Objects Using Grips](To-Stretch-Multiple-Objects-Using-Grips.md)
* [To Lengthen an Object](To-Lengthen-an-Object.md)
* [To Extend an Object](To-Extend-an-Object.md)

#### Related Concepts

* [About Editing with Grips](About-Editing-with-Grips.md)
* [About Resizing or Reshaping Objects](About-Resizing-or-Reshaping-Objects.md)
* [About Moving Objects](About-Moving-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*