# acet-sys-keystate (AutoLISP/Express Tools)

Checks the state of a virtual key.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-sys-keystate keycode)
```

keycode
:   *Type:* Integer

    Code for the virtual key to test.

## Return Values

*Type:* Integer

Status of the specified virtual key.

* If the high-order bit is 1, the key is down; otherwise, it is up.
* If the low-order bit is 1, the key is toggled. A key, such as the CAPS LOCK key, is toggled if it is turned on. The key is
  off and untoggled if the low-order bit is 0. A toggle key's indicator light (if any) on the keyboard will be on when the key
  is toggled, and off when the key is untoggled.

## Remarks

See the documentation for the
GetKeyState() Win32 function for additional details.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*