# start\_list (AutoLISP/DCL)

Starts the processing of a list in the list box or in the pop-up list dialog box tile

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(start_list key [operation [index]])
```

*key*
:   *Type:* String

    Value that specifies a tile. This argument is case-sensitive.

*operation*
:   *Type:* Integer

    A numeric value indicating the type of list operation to perform. You can specify one of the following:

    *1* -- Change selected list contents

    *2* -- Append new list entry

    *3* -- Delete old list and create new list (the default)

*index*
:   *Type:* Integer

    A number indicating the list item to change by the subsequent
    add\_list call. The first item in the list is index 0. If not specified,
    *index* defaults to 0.

    The
    *index* argument is ignored if
    start\_list is not performing a change operation.

## Return Values

*Type:* String

The name of the list that was started.

## Remarks

Subsequent calls to
add\_list affect the list started by
start\_list until the application calls
end\_list.

NOTE:Do not use the
set\_tile function between
start\_list and
end\_list function calls.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [add\_list (AutoLISP/DCL)](add_list-AutoLISP-DCL.md)
* [end\_list (AutoLISP/DCL)](end_list-AutoLISP-DCL.md)

#### Related Concepts

* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*