# SKETCH (Command)

Creates a series of freehand line segments.

## Summary

Sketching is useful for creating irregular boundaries or for tracing with a digitizer. Specify the object type (line, polyline,
or spline), increment, and tolerance before sketching.

![](../images/GUID-11042CD0-FD78-4F00-A191-CAB4434C87B7-low.gif)

## List of Prompts

The following prompts are displayed.

[Specify Sketch](SKETCH-Command.md) or [[Type](SKETCH-Command.md)/[Increment](SKETCH-Command.md)/[toLerance](SKETCH-Command.md)]:

Sketch
:   Creates a sketch.

Type
:   Specifies the object type for the sketch line. (SKPOLY system variable)

    * Line
    * Polyline
    * Spline

Increment
:   Defines the length of each freehand line segment. You must move the pointing device a distance greater than the increment
    value to generate a line. (SKETCHINC system variable)

Tolerance
:   For Splines, specifies how closely the spline’s curve fits to the freehand sketch. (SKTOLERANCE system variable)

#### Related Concepts

* [About Lines](About-Lines.md)
* [About Polylines](About-Polylines.md)
* [About Splines](About-Splines.md)
* [About Freehand Sketches](About-Freehand-Sketches.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*