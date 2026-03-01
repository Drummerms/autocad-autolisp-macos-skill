# nentselp (AutoLISP)

Provides similar functionality to that of the
*nentsel* function without the need for user input

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(nentselp [msg] [pt])
```

*msg*
:   *Type:* String

    Message to be displayed as a prompt. If the
    *msg* argument is omitted, the Select object prompt is issued.

*pt*
:   *Type:* List

    A selection point. This allows object selection without user input.

## Return Values

*Type:* List or nil

The
nentselp function returns a 4×4 transformation matrix, defined as follows:

The first three columns of the matrix specify scaling and rotation. The fourth column is a translation vector.

The functions that use a matrix of this type treat a point as a column vector of dimension 4. The point is expressed in
*homogeneous coordinates,* where the fourth element of the point vector is a
*scale factor* that is normally set to 1.0. The final row of the matrix, the vector [*M* 30 *M* 31 *M* 32 *M* 33 ], has the nominal value of [0 0 0 1]; it is currently ignored by the functions that use this matrix format.

## Examples

N/A

#### Related References

* [nentsel (AutoLISP)](nentsel-AutoLISP.md)
* [entsel (AutoLISP)](entsel-AutoLISP.md)
* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssgetfirst (AutoLISP)](ssgetfirst-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*