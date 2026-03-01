# vl-get-resource (AutoLISP/Visual LISP IDE)

Returns the text stored in a .*txt* file packaged in a VLX

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-get-resource text-file)
```

*text-file*
:   *Type:* String

    Name of a
    *.txt* file packaged with the VLX. Do not include the
    *.txt* extension when specifying the file name.

## Return Values

*Type:* String

A textual value containing the text in
*text-file*.

## Remarks

VLX files are supported on Windows only.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

## Examples

Assume the
*getres.vlx* file contains a LISP program defining a function named
print-readme, and a text file named
*readme.txt*. The
print-readme function is defined as follows:

```
(defun print-readme ()
   (princ (vl-get-resource "readme"))
   (princ)
)
```

After loading
*getres.vlx*, invoke
print-readme:

```
(print-readme)
Product Readme text
Product Readme text 2
```

#### Related References

* [vlisp-compile (AutoLISP/Visual LISP IDE)](vlisp-compile-AutoLISP-Visual-LISP-IDE.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*