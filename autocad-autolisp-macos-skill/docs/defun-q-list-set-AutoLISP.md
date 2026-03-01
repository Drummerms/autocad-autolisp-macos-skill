# defun-q-list-set (AutoLISP)

Sets the value of a symbol to be a function defined by a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(defun-q-list-set 'sym list)
```

*sym*
:   *Type:* Symbol

    A symbol naming the function

*list*
:   *Type:* List

    A list containing the expressions to be included in the function.

## Return Values

*Type:* List, Symbol, or nil

The
*sym* defined.

## Examples

```
(defun-q-list-set 'foo '((x) x))
FOO

(foo 3)
3
```

The following example illustrates the use of
defun-q-list-set to combine two functions into a single function with
defun-q:

```
(defun-q s::startup (x) (print x))
S::STARTUP

(defun-q my-startup (x) (print (list x)))
MY-STARTUP
```

Use
defun-q-list-set to combine the functions into a single function:

```
(defun-q-list-set 's::startup (append
   (defun-q-list-ref 's::startup)
   (cdr (defun-q-list-ref 'my-startup))))
S::STARTUP
```

The following illustrates how the functions respond individually, and how the functions work after being combined using
defun-q-list-set:

```
(defun-q foo (x) (print (list 'foo x)))
FOO

(foo 1)
(FOO 1) (FOO 1)

(defun-q bar (x) (print (list 'bar x)))
BAR

(bar 2)
(BAR 2) (BAR 2)

(defun-q-list-set
  'foo
  (append (defun-q-list-ref 'foo)
              (cdr (defun-q-list-ref 'bar))
  ))
FOO

(foo 3)
(FOO 3)
(BAR 3) (BAR 3)
```

#### Related References

* [defun-q-list-ref (AutoLISP)](defun-q-list-ref-AutoLISP.md)
* [defun-q (AutoLISP)](defun-q-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*