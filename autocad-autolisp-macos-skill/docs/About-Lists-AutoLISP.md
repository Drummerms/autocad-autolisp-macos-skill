# About Lists (AutoLISP)

A list is a group of related values separated by spaces and enclosed in parentheses.

Lists provide an efficient method of storing numerous related values. After all, LISP is so-named because it is the LISt
Processing language. Once you understand the power of lists, you will find that you can create more powerful and flexible
applications. Lists are used to represent 2D and 3D coordinate values, and entity data.

Examples of lists are (1.0 1.0 0.0), ("this" "that" "the other"), and (1 . "ONE").

AutoLISP provides many functions for working with lists. The following are some of the most commonly used functions:

* list - Creates a new list with any number of values.
* append - Appends values to an existing list, and returns a new list.
* cons - Adds an element to the beginning of a list, or constructs a dotted list.
* length - Returns an integer indicating the number of elements in a list.
* assoc - Searches an association list for an element and returns that association list entry.
* car - Returns the first element of a list.
* cdr - Returns a list containing all but the first element of the specified list.
* nth - Returns the nth element of a list.
* subst - Searches a list for an old item and returns a copy of the list with a new item substituted in place of every occurrence
  of the old item.

## Creating a List

The list function provides a simple method of grouping related items. These items do not need to be of similar data types and can
even be other lists. The following code groups three items as a list:

```
(setq lst1 (list 1.0 "One" 1))
(1.0 "One" 1)
```

A list can also be created using the quote (or  *'* ) function.

```
(setq lst1 '(1.0 "One" 1))
(1.0 "One" 1)
```

## Adding to or Changing an Item in a List

The append function allows you to add new items to the end of a list, and the cons function allows you to add new items to the beginning of a list. The subst function can be used to substitute a new item for every occurrence of an old item. These functions do not modify the original
list; they return a modified list. If you need to modify the original list, you explicitly replace the old list with the new
list.

The append function takes any number of lists and runs them together as one list. Therefore, all arguments to this function must be
lists. The following code adds another "One" to the list stored in lst1.

```
(setq lst2 (append lst1 '("One")))
(1.0 "One" 1 "One")
```

The cons function combines a single element with a list. You can add another string "One" to the beginning of a list, lst2, with the cons function.

```
(setq lst3 (cons "One" lst2 ))
("One" 1.0 "One" 1 "One")
```

You can substitute all occurrences of an item in a list with a new item using the subst function. The following code replaces all strings "One" with the string "one".

```
(setq lst4 (subst "one" "One" lst3))
("one" 1.0 "one" 1 "one")
```

## Retrieving an Item from a List

You can retrieve a specific item from a list with the nth function. This function accepts two arguments. The first argument is an integer that specifies which item to return. Lists
start with a 0 index. A 0 specifies the first item in a list, 1 specifies the second item, and so on. The second argument
is the list itself. The following code returns the second item in lst1.

```
(nth 1 lst1)
"One"
```

The car function returns the first item of a list. For example:

```
(car lst1)
1.0
```

The cdr function returns all items from a list as a new list, except the first item. For example:

```
(cdr lst1)
("One" 1)
```

AutoLISP also offers a number of additional functions that are variations of the car and cdr functions. For example, the cadr function returns the second element of a list and the caddr function returns the third item of a list. The cadr function is like using the cdr function on a list and then car on the resulting list.

```
(cadr lst1)
"One"

(car (cdr lst1))
"One"
```

#### Related Concepts

* [About Dotted Pairs (AutoLISP)](About-Dotted-Pairs-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*