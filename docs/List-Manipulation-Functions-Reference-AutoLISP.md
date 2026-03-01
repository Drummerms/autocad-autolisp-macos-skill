# List Manipulation Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP list manipulation functions.

| List manipulation functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(acad\_strlsort lst)](acad_strlsort-AutoLISP.md) | Sorts a list of strings by alphabetical order | ✓ | ✓ | ✓ | -- | ✓ |
| [(append lst ...)](append-AutoLISP.md) | Takes any number of lists and runs them together as one list | ✓ | ✓ | ✓ | -- | ✓ |
| [(assoc item alist)](assoc-AutoLISP.md) | Searches an association list for an element and returns that association list entry | ✓ | ✓ | ✓ | -- | ✓ |
| [(caddr lst)](caddr-AutoLISP.md) | Returns the third element of a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(cadr lst)](cadr-AutoLISP.md) | Returns the second element of a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(car lst)](car-AutoLISP.md) | Returns the first element of a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(cdr lst)](cdr-AutoLISP.md) | Returns the specified list, except for the first element of the list | ✓ | ✓ | ✓ | -- | ✓ |
| [(cons new-first-element lst)](cons-AutoLISP.md) | The basic list constructor | ✓ | ✓ | ✓ | -- | ✓ |
| [(foreach name lst [expr ...])](foreach-AutoLISP.md) | Evaluates expressions for all members of a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(last lst)](last-AutoLISP.md) | Returns the last element in a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(length lst)](length-AutoLISP.md) | Returns an integer indicating the number of elements in a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(list [expr ...])](list-AutoLISP.md) | Takes any number of expressions and combines them into one list | ✓ | ✓ | ✓ | -- | ✓ |
| [(listp item)](listp-AutoLISP.md) | Verifies that an item is a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(mapcar function list1 ... listn)](mapcar-AutoLISP.md) | Returns a list of the result of executing a function with the individual elements of a list or lists supplied as arguments to the function | ✓ | ✓ | ✓ | -- | ✓ |
| [(member expr lst)](member-AutoLISP.md) | Searches a list for an occurrence of an expression and returns the remainder of the list, starting with the first occurrence of the expression | ✓ | ✓ | ✓ | -- | ✓ |
| [(nth n lst)](nth-AutoLISP.md) | Returns the nth element of a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(reverse lst)](reverse-AutoLISP.md) | Returns a list with its elements reversed | ✓ | ✓ | ✓ | -- | ✓ |
| [(subst newitem olditem lst)](subst-AutoLISP.md) | Searches a list for an old item and returns a copy of the list with a new item substituted in place of every occurrence of the old item | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-consp list-variable)](vl-consp-AutoLISP.md) | Determines whether or not a list is nil | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-every predicate-function list [ more-lists ...])](vl-every-AutoLISP.md) | Checks whether the predicate is true for every element combination | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-list\* object [more-objects ...])](vl-list-AutoLISP.md) | Constructs and returns a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-list->string char-codes-list)](vl-list-string-AutoLISP.md) | Combines the Unicode characters associated with a list of integers into a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-list-length list-or-cons-object)](vl-list-length-AutoLISP.md) | Calculates list length of a true list | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-member-if predicate-function list)](vl-member-if-AutoLISP.md) | Determines whether the predicate is true for one of the list members | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-member-if-not predicate-function list)](vl-member-if-not-AutoLISP.md) | Determines whether the predicate is nil for one of the list members | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-position symbol list)](vl-position-AutoLISP.md) | Returns the index of the specified list item | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-remove element-to-remove list)](vl-remove-AutoLISP.md) | Removes elements from a list | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-remove-if predicate-function list)](vl-remove-if-AutoLISP.md) | Returns all elements of the supplied list that fail the test function | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-remove-if-not predicate-function list)](vl-remove-if-not-AutoLISP.md) | Returns all elements of the supplied list that pass the test function | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-some predicate-function list [more-lists ...])](vl-some-AutoLISP.md) | Checks whether the predicate is not nil for one element combination | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-sort list comparison-function)](vl-sort-AutoLISP.md) | Sorts the elements in a list according to a given compare function | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-sort-i list comparison-function)](vl-sort-i-AutoLISP.md) | Sorts the elements in a list according to a given compare function, and returns the element index numbers | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string->list string)](vl-string-list-AutoLISP.md) | Converts a string into a list of Unicode character codes | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*