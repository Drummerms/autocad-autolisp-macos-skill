# getreal (AutoLISP)

Pauses for user input of a real number, and returns that real number

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getreal [msg])
```

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return Values

*Type:* Real or nil

The number entered by the user and expressed as a real.

## Remarks

The user cannot enter another AutoLISP expression as the response to a
getreal request.

## Examples

```
(setq val (getreal))
(setq val (getreal "Scale factor: "))
```

#### Related References

* [getint (AutoLISP)](getint-AutoLISP.md)
* [atof (AutoLISP)](atof-AutoLISP.md)
* [rtos (AutoLISP)](rtos-AutoLISP.md)
* [float (AutoLISP)](float-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*