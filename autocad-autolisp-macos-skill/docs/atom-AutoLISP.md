# atom (AutoLISP)

Verifies that an item is an atom

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(atom item)
```

*item*
:   *Type:* Symbol

    Any AutoLISP element.

    Some versions of LISP differ in their interpretation of
    atom, so be careful when converting from non-AutoLISP code.

## Return Values

*Type:* T or nil

nil if
*item* is a list; otherwise
T. Anything that is not a list is considered an atom.

## Examples

```
(setq a '(x y z))
(X Y Z)

(setq b 'a)
A

(atom 'a)
T

(atom a)
nil

(atom 'b)
T

(atom b)
T

(atom '(a b c))
nil
```

#### Related References

* [atoms-family (AutoLISP)](atoms-family-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*