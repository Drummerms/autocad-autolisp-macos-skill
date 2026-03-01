# getstring (AutoLISP)

Pauses for user input of a string, and returns that string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getstring [cr] [msg])
```

*cr*
:   *Type:* T or nil

    If supplied and not
    nil, this argument indicates that users can include blanks in their input string (and must terminate the string by pressing Enter).
    Otherwise, the input string is terminated by entering a space or pressing Enter.

*msg*
:   *Type:* String

    Message to be displayed to prompt the user.

## Return Values

*Type:* String

The string entered by the user; otherwise
nil, if the user pressed Enter without typing a string.

If the string is longer than 132 characters,
getstring returns only the first 132 characters of the string. If the input string contains the backslash character (\),
getstring converts it to two backslash characters (\\). This allows you to use returned values containing file name paths in other
functions.

## Remarks

The user cannot enter another AutoLISP expression as the response to a
getstring request.

## Examples

```
(setq s (getstring "What's your first name? "))
What's your first name? Gary
"Gary"

(setq s (getstring T "What's your full name? "))
What's your full name? Gary Indiana Jones
"Gary Indiana Jones"

(setq s (getstring T "Enter filename: "))
Enter filename: c:\my documents\vlisp\secrets
"c:\\my documents\\vlisp\\secrets"
```

#### Related References

* [getkword (AutoLISP)](getkword-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*