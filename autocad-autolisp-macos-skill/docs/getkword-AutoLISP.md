# getkword (AutoLISP)

Pauses for user input of a keyword, and returns that keyword

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(getkword [msg])
```

*msg*
:   *Type:* String

    Message to be displayed to prompt the user; if omitted,
    getkword does not display a prompting message.

## Return Values

*Type:* String or nil

A string representing the keyword entered by the user; otherwise
nil, if the user presses Enter without typing a keyword. The function also returns
nil if it was not preceded by a call to
initget to establish one or more keywords.

If the user enters a value that is not a valid keyword,
getkword displays a warning message and prompts the user to try again.

## Remarks

Valid keywords are set prior to the
getkword call with the
initget function. The user cannot enter another AutoLISP expression as the response to a
getkword request.

## Examples

The following example shows an initial call to
initget that sets up a list of keywords (Yes and No) and disallows null input (*bits* value equal to 1) to the
getkword call that follows:

```
(initget 1 "Yes No")
nil

(setq x (getkword "Are you sure? (Yes or No) "))
Are you sure? (Yes or No) yes
"Yes"
```

The following sequence illustrates what happens if the user enters invalid data in response to
getkword:

```
(initget 1 "Yes No")
nil

(setq x (getkword "Are you sure? (Yes or No) "))
Are you sure? (Yes or No) Maybe
Invalid option keyword.
Are you sure? (Yes or No) yes
"Yes"
```

The user's response was not one of the keywords defined by the preceding
initget, so
getkword issued an error message and then prompted the user again with the string supplied in the
*msg* argument.

#### Related References

* [initget (AutoLISP)](initget-AutoLISP.md)
* [cond (AutoLISP)](cond-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*