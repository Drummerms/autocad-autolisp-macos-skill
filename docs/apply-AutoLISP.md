# apply (AutoLISP)

Passes a list of arguments to, and executes, a specified function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(apply 'function list)
```

*'function*
:   *Type:* Symbol

    A function.

    The
    *function* argument can be either a symbol identifying a
    defun, or a
    lambda expression.

*list*
:   *Type:* List or nil

    A list.

    If the function accepts no arguments, the value can be
    nil.

## Return Values

*Type:* String, Integer, Real, List, T, or nil

The result of the function call.

## Examples

```
(apply '+ '(1 2 3))
6

(apply 'strcat '("a" "b" "c"))
"abc"
```

#### Related References

* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*