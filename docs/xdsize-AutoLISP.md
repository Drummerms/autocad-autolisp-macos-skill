# xdsize (AutoLISP)

Returns the size (in bytes) that a list occupies when it is linked to an object (entity) as extended data

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(xdsize lst)
```

*lst*
:   *Type:* List

    A valid list of extended data that contains an application name previously registered with the use of the
    regapp function.

## Return Values

*Type:* Integer

An integer reflecting the size, in bytes. If unsuccessful,
xdsize returns
nil.

Brace fields (group code 1002) must be balanced. An invalid
*lst* generates an error and places the appropriate error code in the AutoCAD ERRNO system variable. If the extended data contains
an unregistered application name, you see this error message (assuming that the AutoCAD CMDECHO system variable is on):

Invalid application name in 1001 group

## Examples

The
*lst* can start with a -3 group code (the extended data sentinel), but it is not required. Because extended data can contain information
from multiple applications, the list must have a set of enclosing parentheses.

```
(-3 ("MYAPP" (1000 . "SUITOFARMOR")
             (1002 . "{")
             (1040 . 0.0)
             (1040 . 1.0)
             (1002 . "}")
   )
)
```

Here is the same example without the -3 group code. This list is just the
cdr of the first example, but it is important that the enclosing parentheses are included:

```
( ("MYAPP" (1000 . "SUITOFARMOR")
           (1002 . "{")
           (1040 . 0.0)
           (1040 . 1.0)
           (1002 . "}")
   )
)
```

#### Related References

* [regapp (AutoLISP)](regapp-AutoLISP.md)
* [xdroom (AutoLISP)](xdroom-AutoLISP.md)

#### Related Concepts

* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*