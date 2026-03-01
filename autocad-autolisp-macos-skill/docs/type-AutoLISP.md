# type (AutoLISP)

Returns the type of a specified item

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(type item)
```

*item*
:   *Type:* Varies

    A symbol.

## Return Values

*Type:* Varies or nil

The data type of
*item*. Items that evaluate to
nil (such as unassigned symbols) return
nil. The data type is returned as one of the atoms listed in the following table:

| Data types returned by the type function | |
| Data type | Description |
| ENAME | Entity names |
| EXRXSUBR | External ObjectARX applications |
| FILE | File descriptors |
| INT | Integers |
| LIST | Lists |
| PAGETB | Function paging table |
| PICKSET | Selection sets |
| REAL | Floating-point numbers |
| SAFEARRAY | Safearray |
| STR | Strings |
| SUBR | Internal AutoLISP functions or functions loaded from compiled (FAS or VLX) files  Functions in LISP source files loaded from the AutoCAD Command prompt may also appear as SUBR |
| SYM | Symbols |
| VARIANT | Variant |
| USUBR | User-defined functions loaded from LISP source files |
| VLA-object | ActiveX objects |

NOTE:

* VLX files are supported on Windows only
* ActiveX objects and Safearrays are available in AutoCAD for Windows only; not available in AutoCAD LT for Windows

## Examples

For example, given the following assignments:

```
(setq a 123 r 3.45 s "Hello!" x '(a b c))
(setq f (open "name" "r"))
```

then

```
(type 'a) returns  SYM
(type a) returns  INT
(type f) returns  FILE
(type r) returns  REAL
(type s) returns  STR
(type x) returns  LIST
(type +) returns  SUBR
(type nil) returns  nil
```

The following code example uses the
type function on the argument passed to it:

```
(defun isint (a) (if (= (type a) 'INT) is TYPE integer? T yes, return T
     nil no, return nil
   ) )
```

#### Related References

* [set (AutoLISP)](set-AutoLISP.md)
* [setq (AutoLISP)](setq-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*