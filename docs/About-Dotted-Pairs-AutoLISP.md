# About Dotted Pairs (AutoLISP)

Dotted pair lists must always contain two members and is the method AutoLISP uses to maintain entity definition data.

When representing a dotted pair, members of the list are separated by a period ( *.* ). Most list-handling functions do not accept a dotted pair as an argument, so you should be sure you are passing the right
kind of list to a function.

Dotted pairs are an example of an "improper list." An improper list is one in which the last cdr is not nil. In addition to adding an item to the beginning of a list, the cons function can create a dotted pair. If the second argument to the cons function is anything other than another list or nil, it creates a dotted pair.

```
(setq sublist (cons 'lyr "WALLS"))
(LYR . "WALLS")
```

The following functions are useful for handling dotted pairs:

* car - Returns the first member of the specified dotted pair.
* cdr - Returns the second member of the specified dotted pair.
* assoc - Searches an association list for a member and returns that association list entry.
* nth - Returns the nth element of a list.

The following code creates an association list of dotted pairs:

```
(setq wallinfo (list sublist (cons 'len 240.0) (cons 'hgt 96.0)))
((LYR . "WALLS") (LEN . 240.0) (HGT . 96.0))
```

The assoc function returns a specified list from within an association list regardless of the specified list's location within the
association list. The assoc function searches for a specified key element in the lists and returns the first instance, as follows:

```
(assoc 'len wallinfo)
(LEN . 240.0)

(cdr (assoc 'lyr wallinfo))
"WALLS"

(nth 1 wallinfo)
(LEN . 240.0)

(car (nth 1 wallinfo))
LEN
```

#### Related Concepts

* [About Lists (AutoLISP)](About-Lists-AutoLISP.md)
* [About Entity Names (AutoLISP)](About-Entity-Names-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*