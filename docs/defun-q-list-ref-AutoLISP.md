# defun-q-list-ref (AutoLISP)

Displays the list structure of a function defined with
defun-q

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(defun-q-list-ref 'function )
```

*function*
:   *Type:* Symbol

    A symbol naming the function.

## Return Values

*Type:* List, Symbol, or nil

The list definition of the function; otherwise
nil, if the argument is not a list.

## Examples

Define a function using
defun-q:

```
(defun-q my-startup (x) (print (list x)))
MY-STARTUP
```

Use
defun-q-list-ref to display the list structure of
my-startup:

```
(defun-q-list-ref 'my-startup)
((X) (PRINT (LIST X)))
```

#### Related References

* [defun-q-list-set (AutoLISP)](defun-q-list-set-AutoLISP.md)
* [defun-q (AutoLISP)](defun-q-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*