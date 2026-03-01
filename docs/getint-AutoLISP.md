# getint (AutoLISP)

Pauses for user input of an integer, and returns that integer

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getint [msg])
```

*msg*
:   *Type:* String

    Message to be displayed to prompt the user; if omitted, no message is displayed.

## Return Values

*Type:* Integer or nil

The integer specified by the user; otherwise
nil, if the user presses Enter without entering an integer.

## Remarks

Values passed to
getint can range from -32,768 to +32,767. If the user enters something other than an integer,
getint displays the message, “Requires an integer value,” and allows the user to try again. The user cannot enter another AutoLISP
expression as the response to a
getint request.

## Examples

```
(setq num (getint)) 15
15

(setq num (getint "Enter a number:"))
Enter a number: 25
25

(setq num (getint)) 15.0
Requires an integer value.
15
15
```

#### Related References

* [getreal (AutoLISP)](getreal-AutoLISP.md)
* [atoi (AutoLISP)](atoi-AutoLISP.md)
* [fix (AutoLISP)](fix-AutoLISP.md)
* [itoa (AutoLISP)](itoa-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*