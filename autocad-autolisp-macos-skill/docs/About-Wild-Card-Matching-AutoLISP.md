# About Wild-Card Matching (AutoLISP)

A string can be compared to a wild-card pattern with the wcmatch function.

This can be helpful when needing to build a dynamic selection set (in conjunction with ssget) or to retrieve extended entity data by application name (in conjunction with entget). The wcmatch function compares a single string to a pattern. The function returns T if the string matches the pattern, and nil if it does not. The wild-card patterns are similar to the regular expressions used by many system and application programs.

The following rules apply to wild-card patterns:

* Alphabetic characters and numerals are treated literally in the pattern.
* Brackets can be used to specify optional characters or a range of letters or digits.
* A question mark ( *?* ) matches a single character.
* An asterisk ( *\** ) matches a sequence of characters; and, certain other special characters have special meanings within the pattern. When you
  use the  *\**  character at the beginning and end of the search pattern, you can locate the desired portion anywhere in the string.

In the following examples, a string variable called matchme has been declared and initialized:

```
(setq matchme "this is a string - test1 test2 the end")
"this is a string - test1 test2 the end"
```

The following code checks whether or not matchme begins with the four characters "this":

```
(wcmatch matchme "this*")
T
```

The following code illustrates the use of brackets in the pattern. In this case, wcmatch returns T if matchme contains "test4", "test5", "test6" (4-6), or "test9" (note the use of the  *\**  character):

```
(wcmatch matchme "*test[4-69]*")
nil
```

In this case, wcmatch returns nil because matchme does not contain any of the strings indicated by the pattern. However, using the pattern "test[4-61]" does match the string
because it contains “test1”.

```
(wcmatch matchme "*test[4-61]*")
T
```

The pattern string can specify multiple patterns, separated by commas. The following code returns T if matchme equals "ABC", or if it begins with "XYZ", or if it ends with "end".

```
(wcmatch matchme "ABC,XYZ*,*end")
T
```

#### Related Concepts

* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)
* [About String Conversions (AutoLISP)](About-String-Conversions-AutoLISP.md)
* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*