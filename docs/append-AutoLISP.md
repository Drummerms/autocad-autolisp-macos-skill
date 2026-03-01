# append (AutoLISP)

Takes any number of lists and appends them together as one list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(append [list ...])
```

*list*
:   *Type:* List

    A list.

## Return Values

*Type:* List or nil

A list with all arguments appended to the original. If no arguments are supplied,
append returns
nil.

## Examples

```
(append '(a b) '(c d))
(A B C D)

(append '((a)(b)) '((c)(d)))
((A) (B) (C) (D))
```

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*