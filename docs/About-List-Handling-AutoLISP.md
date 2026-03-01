# About List Handling (AutoLISP)

AutoLISP provides functions for working with lists. This section provides examples of the append, assoc, car, cons, list, nth, and subst functions. A summary of all list-handling functions is in AutoLISP Function Synopsis (AutoLISP), under the heading List Manipulation
Functions(AutoLISP).

Lists provide an efficient and powerful method of storing numerous related values. After all, LISP is so-named because it
is the LISt Processing language. Once you understand the power of lists, you'll find that you can create more powerful and
flexible applications.

Several AutoLISP functions provide a basis for programming two-dimensional and three-dimensional graphics applications. These
functions return point values in the form of a list.

The list function provides a simple method of grouping related items. These items do not need to be of similar data types. The following
code groups three related items as a list:

```
(setq lst1 (list 1.0 "One" 1))

(1.0 "One" 1)
```

You can retrieve a specific item from the list in the lst1 variable with the nth function. This function accepts two arguments. The first argument is an integer that specifies which item to return. A 0
specifies the first item in a list, 1 specifies the second item, and so on. The second argument is the list itself. The following
code returns the second item in lst1.

```
(nth 1 lst1)

"One"
```

The cdr function returns all elements, except the first, from a list. For example:

```
(cdr lst1)

("One" 1)
```

The car function provides another way to extract items from a list. For more examples using car and cdr, and combinations of the two, see About Point Lists (AutoLISP).

Three functions let you modify an existing list. The append function returns a list with new items added to the end of it, and the cons function returns a list with new items added to the beginning of the list. The subst function returns a list with a new item substituted for every occurrence of an old item. These functions do not modify the
original list; they return a modified list. To modify the original list, you must explicitly replace the old list with the
new list.

The append function takes any number of lists and runs them together as one list. Therefore, all arguments to this function must be
lists. The following code adds another "One" to the list lst1. Note the use of the quote (or  *'* ) function as an easy way to make the string "One" into a list.

```
(setq lst2 (append lst1 '("One")))

(1.0 "One" 1 "One")
```

The  *cons*  function combines a single element with a list. You can add another string "One" to the beginning of this new list, lst2, with the cons function.

```
(setq lst3 (cons "One" lst2 ))

("One" 1.0 "One" 1 "One")
```

You can substitute all occurrences of an item in a list with a new item with the subst function. The following code replaces all strings "One" with the string "one".

```
(setq lst4 (subst "one" "One" lst3))

("one" 1.0 "one" 1 "one")
```

#### Topics in this section

* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)

  AutoLISP utilizes the list data type to represent graphical coordinate values.
* [About Dotted Pairs (AutoLISP)](About-Dotted-Pairs-AutoLISP.md)

  Dotted pair lists must always contain two members and is the method AutoLISP uses to maintain entity definition data.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*