# add\_list (AutoLISP/DCL)

Adds or modifies a string in the currently active dialog box list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(add_list str)
```

*str*
:   *Type:* String

    Value to be assigned to the list.

## Return Values

*Type:* String or nil

Returns the string added to the list, if successful; otherwise
nil.

## Remarks

Before using
add\_list, you must open the list and initialize it with a call to
start\_list. Depending on the operation specified in
start\_list, the
*string* is either added to the current list or replaces the current list item.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

Assuming the currently active DCL file has a
popup\_list or
list\_box with a key of
longlist, the following code fragment initializes the list and adds to it the text strings in
llist.

```
(setq llist '("first line" "second line" "third line"))
(start_list "longlist")
(mapcar 'add_list llist)
(end_list)
```

After the list has been defined, the following code fragment changes the text in the second line to
"2nd line".

```
(start_list "longlist" 1 0)
(add_list "2nd line")
(end_list)
```

#### Related References

* [end\_list (AutoLISP/DCL)](end_list-AutoLISP-DCL.md)
* [start\_list (AutoLISP/DCL)](start_list-AutoLISP-DCL.md)

#### Related Concepts

* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*