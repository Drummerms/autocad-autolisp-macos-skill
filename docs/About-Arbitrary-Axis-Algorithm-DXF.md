# About Arbitrary Axis Algorithm (DXF)

The arbitrary axis algorithm is used by the
AutoCAD program internally to implement the arbitrary but consistent generation of object coordinate systems for all entities that
use object coordinates.

Given a unit-length vector to be used as the
*Z* axis of a coordinate system, the arbitrary axis algorithm generates a corresponding
*X* axis for the coordinate system. The
*Y* axis follows by application of the right-hand rule.

The method is to examine the given
*Z* axis (also called the
*normal vector*). If it is close to the positive or negative world
*Z* axis, cross the world
*Y* axis with the given
*Z* axis to arrive at the arbitrary
*X* axis. If it is not close, cross the world
*Z* axis with the given
*Z* axis to arrive at the arbitrary
*X* axis. The boundary at which the decision is made was chosen to be both inexpensive to calculate and completely portable across
machines. This is achieved by having a sort of “square” polar cap, the bounds of which are 1/64, which is precisely specifiable
in six decimal-fraction digits and in six binary-fraction bits.

The algorithm does the following (all vectors are assumed to be in 3D space and specified in the world coordinate system):

```
Let the given normal vector be called N.
Let the world Y axis be called Wy, which is always (0,1,0).
Let the world Z axis be called Wz, which is always (0,0,1).
```

Here we are looking for the arbitrary
*X* and
*Y* axes to go with the normal
*N*. They will be called
*Ax* and
*Ay*.
*N* could also be called
*Az* (the arbitrary
*Z* axis) as follows:

```
If (abs (Nx) < 1/64) and (abs (Ny) < 1/64) then
     Ax = Wy X N (where “X” is the cross-product operator).
Otherwise,
     Ax = Wz X N.
Scale Ax to unit length.
```

The method of getting the Ay vector is as follows:

```
Ay = N X Ax. Scale Ay to unit length.
```

#### Related References

* [About Advanced DXF Issues (DXF)](About-Advanced-DXF-Issues-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*