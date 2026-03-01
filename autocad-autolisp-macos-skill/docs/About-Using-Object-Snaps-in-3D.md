# About Using Object Snaps in 3D

Object snaps function the same way in 3D as they do in 2D with the exception that they can optionally be projected.

By default, the *Z*-value of an object snap location is determined by the object's 3D location. However, if you work with object snaps on the
plan or top view of a 3D model, a constant *Z*-value is more useful.

If you turn on the OSNAPZ system variable, all object snaps are projected onto the *XY* plane of the current UCS or, if ELEV is set to a non-zero value, onto a plane parallel to *XY* plane at the specified elevation.

NOTE:When you create or modify objects, make sure that you know whether OSNAPZ is turned on or off. There is no visual reminder,
and you can get unexpected results.

#### Related Concepts

* [About Using Object Snaps](About-Using-Object-Snaps.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*