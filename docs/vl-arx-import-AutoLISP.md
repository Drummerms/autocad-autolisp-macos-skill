# vl-arx-import (AutoLISP)

Imports ObjectARX functions into a separate-namespace VLX

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-arx-import ['function | application])
```

*function*
:   *Type:* String

    Symbol name for the function to import.

*application*
:   *Type:* String

    Application name whose functions are to be imported.

## Return Values

*Type:* nil

By default, separate-namespace VLX applications do not import any functions from ObjectARX applications. Use
vl-arx-import to explicitly import functions from ObjectARX applications.

If executed from a document VLX, this function does nothing and returns
nil, as all ADS-DEFUN function names are automatically imported to document VLX applications.

## Remarks

If no argument (or
nil) is specified,
vl-arx-import imports all function names from the current document namespace.

NOTE:While the function is supported on Mac OS and Web, VLX files are not supported on Mac OS and Web which results in different
behavior than when used on Windows.

## Examples

To see how
vl-arx-import works, try the following:

1. Copy the following code into your AutoLISP editor and save the file:

   ```
   (vl-doc-export 'testarx)
   (defun testarx ()
      (princ "This function tests an ObjectARX application ")
      (vl-arx-import 'c:cal)
      (c:cal)
   )
   ```
2. Use Make Application to build a VLX with this code. Select Separate-Namespace Application Options.
3. Load
   *geomcal.arx*, if it is not already loaded.
4. Load and run the application.

   To verify the effect of
   vl-arx-import, comment out the
   vl-arx-import call in the code, save the change, then rebuild and run the application. Without the
   vl-arx-import call, the
   c:cal function will not be found.

In the example above, you could have replaced the
vl-arx-import call with the following:

```
(vl-arx-import "geomcal.crx")
```

This would import all functions defined in
*geomcal.crx*, including
c:cal.

#### Related References

* [vl-doc-import (AutoLISP)](vl-doc-import-AutoLISP.md)
* [arxload (AutoLISP)](arxload-AutoLISP.md)

#### Related Concepts

* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*