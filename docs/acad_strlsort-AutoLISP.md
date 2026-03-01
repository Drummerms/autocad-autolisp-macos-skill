# acad\_strlsort (AutoLISP)

Sorts a list of strings in alphabetical order

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(acad_strlsort list)
```

*list*
:   *Type:* List

    The list of strings to be sorted.

## Return Values

*Type:* List or nil

The
*list* in alphabetical order. If the list is invalid or if there is not enough memory to do the sort,
acad\_strlsort returns
nil.

## Examples

Sort a list of abbreviated month names:

```
(setq mos '("Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec"))
("Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec")

(acad_strlsort mos)
("Apr" "Aug" "Dec" "Feb" "Jan" "Jul" "Jun" "Mar" "May" "Nov" "Oct" "Sep")
```

#### Related References

* [vl-sort-i (AutoLISP)](vl-sort-i-AutoLISP.md)
* [vl-sort (AutoLISP)](vl-sort-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*