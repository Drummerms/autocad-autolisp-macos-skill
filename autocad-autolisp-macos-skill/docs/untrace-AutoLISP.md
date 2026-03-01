# untrace (AutoLISP)

Clears the trace flag for the specified functions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(untrace [function ...])
```

*function*
:   *Type:* Symbol

    A symbol that names a function. If
    *function* is not specified,
    untrace has no effect.

## Return Values

*Type:* Symbol or nil

The last function name passed to
untrace. If
*function* was not specified,
untrace returns
nil.

## Examples

The following command clears the trace flag for function
foo:

```
(untrace foo)
FOO
```

#### Related References

* [trace (AutoLISP)](trace-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*