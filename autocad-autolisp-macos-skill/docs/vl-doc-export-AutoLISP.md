# vl-doc-export (AutoLISP)

Makes a function available to the current document

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-doc-export 'function)
```

*'function*
:   *Type:* Subroutine

    A symbol naming the function to be exported.

## Return Values

*Type:* T

Always returns
T.

## Remarks

When issued from a VLX that runs in its own namespace,
vl-doc-export exposes the specified function to any document namespace that loads the VLX.

The
vl-doc-export function should be used only at the top level in a file, and never inside other forms (for example, not within a
defun).

NOTE:While the function is supported on Mac OS and Web, VLX files are not supported on Mac OS and Web which results in different
behavior than when used on Windows.

## Examples

The following code shows the contents of a file named
*kertrats.lsp*. This file is compiled into a VLX that runs in its own namespace. The VLX file is named
*kertrats.vlx*. The
vl-doc-export call makes the
kertrats function visible to any document that loads
*kertrats.vlx*:

```
(vl-doc-export 'kertrats)
(defun kertrats ()
  (princ "This function goes nowhere")
)
```

#### Related References

* [vl-doc-import (AutoLISP)](vl-doc-import-AutoLISP.md)
* [vl-arx-import (AutoLISP)](vl-arx-import-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*