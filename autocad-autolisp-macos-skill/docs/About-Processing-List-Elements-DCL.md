# About Processing List Elements (DCL)

Because the value of a
list\_box tile can contain leading spaces (especially if you are retrieving multiple items), do not test the value as a string comparison.

Convert
list\_box value to an integer first with the
atoi function, before processing the list box. You can also use the read function, which converts a token to an integer automatically.
For example, for a list named
justone that accepts only a single selection, the following code fragment checks to see if the third item in the list was selected:

```
(setq index ( get_tile "justone"))
(cond
  ((/= index "")                   ;See if string is empty.
    (= 2 (atoi index))
    .                              ; Process the third entry.
    .
    .
  )
)
```

It is necessary to first check if the string is empty, because the
atoi functions return 0 for an empty string as well as the string
"0".

The value of a pop-up list never has a leading space, so you do not have to convert the value. Pop-up lists do not allow for
multiple selection.

If the list box supports multiple selection, your program must do the conversion and step through the multiple values in the
value string. The following definition of
MK\_LIST returns a list containing only items the user has selected from the original
displist. (In this example, the display list
displist is maintained as a global variable.) The
MK\_LIST function expects to be called with the current $value of the list box:

```
(defun MK_LIST (readlist / count item retlist)
  (setq count 1)
  (while (setq item (read readlist))
    (setq retlist (cons (nth item displist) retlist))
    (while (and (/= " " (substr readlist count 1))
                       (/= "" (substr readlist count 1)))
      (setq count (1+ count))
    )
    (setq readlist (substr readlist count))
  )
  (reverse retlist)
)
```

Both preceding examples also work for the case of a single selection.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About List Operations for List Boxes and Pop-Up Lists (DCL)](About-List-Operations-for-List-Boxes-and-Pop-Up-Lists-DCL.md)
* [list\_box Tile (DCL)](list_box-Tile-DCL.md)
* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*