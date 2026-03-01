# About Logical Grouping of Selection Filter Tests (AutoLISP)

You can define test groups with nested Boolean expressions to filter objects from a selection set created with ssget.

The following table lists the grouping operators that you can use to filter selection sets:

| Grouping operators for selection set filter lists | | |
| Starting operator | Encloses | Ending operator |
| "<AND" | One or more operands | "AND>" |
| "<OR" | One or more operands | "OR>" |
| "<XOR" | Two operands | "XOR>" |
| "<NOT" | One operand | "NOT>" |

The grouping operators are specified by -4 dxf group codes, like the relational operators. They are paired and must be balanced
correctly in the filter list or the ssget call will fail.

```
(ssget "X"
  '(
    (-4 . "<OR")
      (-4 . "<AND")
        (0 . "CIRCLE")
        (40 . 1.0)
      (-4 . "AND>")
      (-4 . "<AND")
        (0 . "LINE")
        (8 . "ABC")
      (-4 . "AND>")
    (-4 . "OR>")
  )
)
```

This filter list allows the selection of all circles with a radius of 1.0 plus all lines on layer "ABC". The grouping operators
are not case-sensitive; for example, you can specify "and>", "<or", instead of "AND>", "<OR". Grouping operators are not allowed within the -3 dxf group code. Multiple application names specified in a -3 dxf group
code use an implied AND operator. If you want to test for extended data using other grouping operators, specify separate -3 dxf group codes and group
them as desired.

The following example code demonstrates how to select all circles having extended data for either application "APP1" or "APP2"
but not both:

```
(ssget "X"
  '((0 . "CIRCLE")
    (-4 . "<XOR")
      (-3 ("APP1"))
      (-3 ("APP2"))
    (-4 . "XOR>")
  )
)
```

You can simplify the coding of frequently used grouping operators by setting them equal to a symbol. The previous example
could be rewritten as follows (notice that in this example you must explicitly quote each list):

```
(setq <xor '(-4 . "<XOR")
         xor> '(-4 . "XOR>"))

(ssget "X"
  (list
    '(0 . "CIRCLE")
    <xor
    '(-3 ("APP1"))
    '(-3 ("APP2"))
    xor>
  )
)
```

#### Related Concepts

* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*