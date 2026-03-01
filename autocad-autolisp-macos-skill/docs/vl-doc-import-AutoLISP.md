# vl-doc-import (AutoLISP)

Imports a previously exported function into a VLX namespace

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-doc-import application ['function ...])
```

*application*
:   *Type:* String

    Name of the VLX application whose functions are to be imported. Do not include the
    *.vlx* extension in the name.

*function*
:   *Type:* Subroutine

    One or more symbols naming functions to be imported. If no functions are specified, all functions exported by
    *application* will be imported.

## Return Values

*Type:* nil or error

nil if successful; otherwise an error occurs

## Remarks

This function can be used in a separate-namespace VLX to import a function that was previously exported from another VLX loaded
from the same document.

The
vl-doc-import function should be used only at the top level in a file, and never inside other forms (for example, not within a
defun).

NOTE:While the function is supported on Mac OS and Web, VLX files are not supported on Mac OS and Web which results in different
behavior than when used on Windows.

## Examples

Import function
ldataget from the
ldatatest application:

```
(vl-doc-import "ldatatest" 'ldataget)
nil
```

#### Related References

* [vl-doc-export (AutoLISP)](vl-doc-export-AutoLISP.md)
* [vl-arx-import (AutoLISP)](vl-arx-import-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*