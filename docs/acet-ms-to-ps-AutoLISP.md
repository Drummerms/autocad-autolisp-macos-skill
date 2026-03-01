# acet-ms-to-ps (AutoLISP)

Converts a real value from model space units to paper space units

*Supported Platforms:* Windows only

*Prerequisites:* The AcSpaceTrans ObjectARX application must be loaded before the function can be called,
(arxload "acspacetrans.arx") or
(arxload "acspacetrans.crx") based on release.

## Signature

```
(acet-ms-to-ps [value] [viewport])
```

*value*
:   *Type:* Real

    Value to be converted.

*viewport*
:   *Type:* Ename (entity name)

    A viewport entity name.

## Return Values

*Type:* Real or nil

The converted real value on success;
nil on failure.

## Remarks

If both the
*value* and
*viewport* arguments are specified, the value is converted to paper space units using the specified viewport. No user input is required.

If only the
*value* argument is specified, the current viewport is assumed and no user input is required. However, if the current space is model
space, there is no current viewport and the function will fail (returning
nil). If paper space is the current space, the function will either prompt for a viewport if more than one viewport exists in
the current paper space layout, or use the single existing viewport.

If no arguments are specified, the function prompts for a value and converts it if possible.

## Examples

None

#### Related References

* [acet-ps-to-ms (AutoLISP)](acet-ps-to-ms-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*