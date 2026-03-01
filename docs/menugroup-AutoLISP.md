# menugroup (AutoLISP)

Verifies that a menugroup is loaded

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(menugroup groupname)
```

*groupname*
:   *Type:* String

    Menu group name.

## Return Values

*Type:* String or nil

If
*groupname* matches a loaded menu group name, the function returns the
*groupname* string; otherwise, it returns
nil.

NOTE:*groupname* is always returned on Mac OS and Web.

## Examples

N/A

#### Related References

* [menucmd (AutoLISP)](menucmd-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*