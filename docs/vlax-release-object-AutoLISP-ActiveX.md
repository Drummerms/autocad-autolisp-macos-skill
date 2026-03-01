# vlax-release-object (AutoLISP/ActiveX)

Releases a drawing object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-release-object obj)
```

*obj*
:   *Type:* VLA-object

    An object.

After release, the drawing object is no longer accessible through
*obj*.

## Return Values

*Type:* Integer or error

A numeric value if the object is successfully released; otherwise, an error occurs if the object is already released.

## Remarks

When an AutoLISP routine no longer uses an object outside AutoCAD, such as a Microsoft Excel object, call the
vlax-release-object function to make sure that the associated application closes properly. Objects released with
vlax-release-object may not be released immediately. The actual release may not happen until the next automatic garbage collection occurs. You
can call
gc directly to force the garbage collection to occur at a specific location within your code. However, calling
gc may degrade performance, and it is recommended that you avoid placing calls to
gc in locations where it is likely to be called many times in a row, such as within loops.

If an object-associated application does not close after calling the
gc function, the
vlax-release-object function was not called for all objects outside AutoCAD.

## Examples

N/A

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-erased-p (AutoLISP/ActiveX)](vlax-erased-p-AutoLISP-ActiveX.md)
* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-object-released-p (AutoLISP/ActiveX)](vlax-object-released-p-AutoLISP-ActiveX.md)
* [vlax-read-enabled-p (AutoLISP/ActiveX)](vlax-read-enabled-p-AutoLISP-ActiveX.md)
* [vlax-write-enabled-p (AutoLISP/ActiveX)](vlax-write-enabled-p-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Object-Handling Functions Reference (AutoLISP/ActiveX)](Object-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*