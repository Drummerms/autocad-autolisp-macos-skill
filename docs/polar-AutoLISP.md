# polar (AutoLISP)

Returns the UCS 3D point at a specified angle and distance from a point

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(polar pt ang dist)
```

*pt*
:   *Type:* List

    A 2D or 3D point.

*ang*
:   *Type:* Integer or Real

    An angle expressed in radians relative to the world
    *X* axis. Angles increase in the counterclockwise direction, independent of the current construction plane.

*dist*
:   *Type:* Integer or Real

    Distance from the specified
    *pt*.

## Return Values

*Type:* List

A 2D or 3D point, depending on the type of point specified by
*pt*.

## Examples

Supplying a 3D point to
polar:

```
(polar '(1 1 3.5) 0.785398 1.414214)
(2.0 2.0 3.5)
```

Supplying a 2D point to
 *polar* :

```
(polar '(1 1) 0.785398 1.414214)
(2.0 2.0)
```

#### Related References

* [inters (AutoLISP)](inters-AutoLISP.md)
* [osnap (AutoLISP)](osnap-AutoLISP.md)

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*