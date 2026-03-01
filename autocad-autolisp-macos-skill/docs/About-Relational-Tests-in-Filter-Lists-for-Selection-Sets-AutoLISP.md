# About Relational Tests in Filter Lists for Selection Sets (AutoLISP)

Unless otherwise specified, an equivalency is implied for each item in the
*filter-list*.

For numeric group codes (integers, reals, points, and vectors), you can specify other relations by including a special -4
group code that specifies a relational operator. The value of a -4 group code is a string indicating the test operator to
be applied to the next group in the
*filter-list*.

The following selects all circles with a radius (group code 40) greater than or equal to 2.0:

```
(ssget "X" '((0 . "CIRCLE") (-4 . ">=") (40 . 2.0)))
```

The possible relational operators are shown in the following table:

| Relational operators for selection set filter lists | |
| Operator | Description |
| "\*" | Anything goes (always true) |
| "=" | Equals |
| "!=" | Not equal to |
| "/=" | Not equal to |
| "<>" | Not equal to |
| "<" | Less than |
| "<=" | Less than or equal to |
| ">" | Greater than |
| ">=" | Greater than or equal to |
| "&" | Bitwise AND (integer groups only) |
| "&=" | Bitwise masked equals (integer groups only) |

The use of relational operators depends on the kind of group code value you are testing:

* All relational operators except for the bitwise operators ("&" and
  "&=") are valid for both real- and integer-valued groups.
* The bitwise operators
  "&" and
  "&=" are valid only for integer-valued groups.

  The bitwise
  AND, "&", is true if
  ((*integer\_group* &
  *filter*) /= 0)—that is, if any of the bits set in the mask are also set in
  *integer\_group*.

  The bitwise masked equals,
  "&=", is true if
  ((*integer\_group* &
  *filter*) = filter)—that is, if all bits set in the mask are also set in
  *integer\_group* (other bits might be set in the
  *integer\_group* but are not checked).
* For point group codes, the
  *X*,
  *Y*, and
  *Z* tests can be combined into a single string, with each operator separated by commas (for example, ">,>,\*"). If an operator is omitted from the string (for example,
  "=,<>" leaves out the
  *Z*test), then the “anything goes” operator,
  "\*", is assumed.
* Direction vectors (group code 210) can be compared only with the operators
  "\*",
  "=", and
  "!=" (or one of the equivalent “not equal” strings).
* You cannot use the relational operators with string group codes; use wild-card tests instead.

#### Related Concepts

* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)
* [About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)](About-Wild-Card-Patterns-in-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*