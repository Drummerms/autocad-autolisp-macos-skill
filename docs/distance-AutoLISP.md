# distance (AutoLISP)

Returns the 3D distance between two points

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(distance pt1 pt2)
```

*pt1*
:   *Type:* List

    A 2D or 3D point list.

*pt2*
:   *Type:* List

    A 2D or 3D point list.

## Return Values

*Type:* Real

The distance. If one or both of the supplied points is a 2D point, then
distance ignores the
*Z* coordinates of any 3D points supplied and returns the 2D distance between the points as projected into the current construction
plane.

## Examples

```
(distance '(1.0 2.5 3.0) '(7.7 2.5 3.0))
6.7

(distance '(1.0 2.0 0.5) '(3.0 4.0 0.5))
2.82843
```

#### Related References

* [angle (AutoLISP)](angle-AutoLISP.md)

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*