# About List Operations for List Boxes and Pop-Up Lists (DCL)

Lists in a dialog box require you to follow a specific sequence to populate them with items.

A dialog box list operation always begins with a
start\_list function call. The function syntax is as follows:

```
(start_list key [operation [index]])
```

The
*key* argument is a string that identifies the dialog box tile. The
*key* argument is case-sensitive. The
*operation* argument is an integer value that indicates whether you are creating a new list, changing a list, or appending to a list.
The following are valid
*operation* arguments:

| Operation codes for start\_list | |
| Value | Description |
| 1 | Change selected list contents |
| 2 | Append new list entry |
| 3 | Delete old list and create new list (the default) |

The
*index* argument is only used in change operations. The index indicates the list item to change by a subsequent
add\_list call. The first item in a list is index 0. If you do not specify operation, it defaults to 3 (create a new list). If you
do not specify an index, the index value defaults to 0.

You implement the list operations as follows:

Creating a New List (3)
:   After the
    start\_list call, call
    add\_list repeatedly to add new items to the list. End list handling by calling
    end\_list.

Changing an Item in a List (1)
:   After calling
    start\_list, call
    add\_list once to replace the item whose index was specified in the
    start\_list call. (If you call
    add\_list more than once, it replaces the same item again.) End list handling by calling
    end\_list.

Appending an Item to a List (2)
:   After calling
    start\_list, call
    add\_list to append an item to the end of the list. If you continue to call
    add\_list, more items are appended until you call
    end\_list.

Regardless of which list operation you are doing, you must call the three functions in sequence:
start\_list, then
add\_list (possibly more than once), and then
end\_list.

The
mapcar function is useful for turning a “raw” AutoLISP list into a list box display. In the following example, the
appnames list contains strings that you want to appear in a list box called selections. You can use this code fragment to set up the
list and display it as follows:

```
(start_list "selections")    ;Specify the name of the list box.
(mapcar ' add_list appnames) ;Specify the AutoLISP list.
(end_list)
```

Because list creation (3) is the default, this example does not specify it.

The value of a
list\_box tile is the index of the selected item (or the indexes of selected items, if multiple selections are allowed). If your program
needs to know the actual text associated with an index, it must save the original list. It must also track changes to the
list.

Appending list items is similar to creating a new list. If, for example,
appnames has 12 items in it, and you want to append another list, called
newnames, you could use the following code:

```
(start_list "selections" 2)
(mapcar 'add_list newnames)
(end_list)
```

Changing a single item requires only one
add\_list call. In this case, you specify the index of the item to change:

```
(start_list "selections" 1 5) ;Change the sixth item in the list.
(add_list "SURPRISE!")        ;Remember that the first index is 0.
(end_list)
```

You cannot delete a list item or insert an item without rebuilding the list from scratch.

#### Topics in this section

* [About Processing List Elements (DCL)](About-Processing-List-Elements-DCL.md)

  Because the value of a
  list\_box tile can contain leading spaces (especially if you are retrieving multiple items), do not test the value as a string
  comparison.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About Processing List Elements (DCL)](About-Processing-List-Elements-DCL.md)
* [list\_box Tile (DCL)](list_box-Tile-DCL.md)
* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*