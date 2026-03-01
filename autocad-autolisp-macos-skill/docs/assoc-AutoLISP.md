# assoc (AutoLISP)

Searches an association list for an element and returns that association list entry

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(assoc element alist)
```

*element*
:   *Type:* Integer, Real, or String

    Key of an element in an association list.

*alist*
:   *Type:* List

    An association list to be searched.

## Return Values

*Type:* List or nil

The
*alist* entry, if successful. If
assoc does not find
*element* as a key in
*alist*, it returns
nil.

## Examples

```
(setq al '((name box) (width 3) (size 4.7263) (depth 5)))
((NAME BOX) (WIDTH 3) (SIZE 4.7263) (DEPTH 5))

(assoc 'size al)
(SIZE 4.7263)

(assoc 'weight al)
nil
```

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*