# trans (AutoLISP)

Translates a point (or a displacement) from one coordinate system to another

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(trans pt from to [disp])
```

*pt*
:   *Type:* List

    A list of three reals that can be interpreted as either a 3D point or a 3D displacement (vector).

*from*
:   *Type:* Integer, List, or Ename (entity name)

    An integer code, entity name, or 3D extrusion vector identifying the coordinate system in which
    *pt* is expressed. The integer code can be one of the following:

    *0* -- World (WCS)

    *1* -- User (current UCS)

    *2* -- If used with code 0 or 1, this indicates the Display Coordinate System (DCS) of the current viewport. When used with code
    3, it indicates the DCS of the current model space viewport.

    *3* -- Paper space DCS (used
    *only* with code 2)

*to*
:   *Type:* Integer, List, or Ename (entity name)

    An integer code, entity name, or 3D extrusion vector identifying the coordinate system of the returned point. See the
    *from* argument for a list of valid integer codes.

*disp*
:   *Type:*List

    If present and is not
    nil, this argument specifies that
    *pt* is to be treated as a 3D displacement rather than as a point.

## Return Values

*Type:* List

A 3D point (or displacement) in the requested
*to* coordinate system.

## Remarks

If you use an entity name for the
*from* or
*to* argument, it must be passed in the format returned by the
entnext,
entlast,
entsel,
nentsel, and
ssname functions. This format lets you translate a point to and from the Object Coordinate System (OCS) of a particular object.
(For some objects, the OCS is equivalent to the WCS; for these objects, conversion between OCS and WCS is a null operation.)
A 3D extrusion vector (a list of three reals) is another method of converting to and from an object's OCS. However, this does
not work for those objects whose OCS is equivalent to the WCS.

The
trans function can also transform 2D points. It does this by setting the
*Z* coordinate to an appropriate value. The
*Z* component used depends on the
*from* coordinate system that was specified and on whether the value is to be converted as a point or as a displacement. If the
value is to be converted as a displacement, the
*Z* value is always 0.0; if the value is to be converted as a point, the filled-in
*Z* value is determined as shown in the following table:

| Converted 2D point *Z* values | |
| From | Filled-in *Z* value |
| WCS | 0.0 |
| UCS | Current elevation |
| OCS | 0.0 |
| DCS | Projected to the current construction plane (UCS *XY* plane + current elevation) |
| PSDCS | Projected to the current construction plane (UCS *XY* plane + current elevation) |

## Examples

In the following examples, the UCS is rotated 90 degrees counterclockwise around the WCS
*Z* axis:

```
(trans '(1.0 2.0 3.0) 0 1)
(2.0 -1.0 3.0)

(trans '(1.0 2.0 3.0) 1 0)
(-2.0 1.0 3.0)
```

For example, to draw a line from the insertion point of a piece of text (without using Osnap), you convert the text object's
insertion point from the text object's OCS to the UCS.

```
(trans text-insert-point text-ename 1)
```

You can then pass the result to the From Point prompt.

Conversely, you must convert point (or displacement) values to their destination OCS before feeding them to
entmod. For example, if you want to move a circle (without using the AutoCAD MOVE command) by the UCS-relative offset (1,2,3), you
need to convert the displacement from the UCS to the circle's OCS:

```
(trans '(1 2 3) 1 circle-ename)
```

Then you add the resulting displacement to the circle's center point.

For example, if you have a point entered by the user and want to find out which end of a line it looks closer to, you convert
the user's point from the UCS to the DCS.

```
(trans user-point 1 2)
```

Then you convert each of the line's endpoints from the OCS to the DCS.

```
(trans endpoint line-ename 2)
```

From there you can compute the distance between the user's point and each endpoint of the line (ignoring the
*Z* coordinates) to determine which end looks closer.

#### Related References

* [inters (AutoLISP)](inters-AutoLISP.md)
* [polar (AutoLISP)](polar-AutoLISP.md)
* [osnap (AutoLISP)](osnap-AutoLISP.md)

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)
* [About Coordinate System Transformations (AutoLISP)](About-Coordinate-System-Transformations-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*