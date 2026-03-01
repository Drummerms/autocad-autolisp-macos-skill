# vl-exit-with-value (AutoLISP)

Returns a value to the function that invoked the
\*error\* handler from another namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-exit-with-value value)
```

*value*
:   *Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

    Any value.

## Return Values

*Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

*value* provided to the function.

## Remarks

An
\*error\* handler can use the
vl-exit-with-value function to return a value to the program that called the function.

## Examples

The following example uses
vl-exit-with-value to return the integer value 3 to the function that invoked the VLX:

```
(defun *error* (msg)
  ... ; processing in VLX-T namespace/execution context
  (vl-exit-with-value  3))
```

#### Related References

* [vl-exit-with-error (AutoLISP)](vl-exit-with-error-AutoLISP.md)
* [\*error\* (AutoLISP)](error-AutoLISP.md)
* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*