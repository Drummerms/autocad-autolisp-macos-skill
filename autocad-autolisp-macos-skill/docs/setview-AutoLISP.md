# setview (AutoLISP)

Establishes a view for a specified viewport

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setview view_descriptor [vport_id])
```

*view\_descriptor*
:   *Type:* Ename (entity name)

    An entity definition list similar to that returned by
    tblsearch when applied to the VIEW symbol table.

*vport\_id*
:   *Type:* Integer

    Viewport to receive the new view. If
    *vport\_id* is 0, the current viewport receives the new view.

    You can obtain the
    *vport\_id* number from the AutoCAD CVPORT system variable.

## Return Values

*Type:* Ename (entity name) or nil

If successful, the
setview function returns the
*view\_descriptor*.

## Examples

N/A

#### Related References

* [tblobjname (AutoLISP)](tblobjname-AutoLISP.md)
* [tblsearch (AutoLISP)](tblsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*