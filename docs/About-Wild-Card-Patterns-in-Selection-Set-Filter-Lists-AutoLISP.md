# About Wild-Card Patterns in Selection Set Filter Lists (AutoLISP)

Symbol names specified in filtering lists can include wild-card patterns.

The wild-card patterns recognized by ssget are the same as those recognized by the wcmatch function. When filtering for anonymous blocks, you must precede the \* character with a reverse single quotation mark ( *`* ), also known as an escape character, because the  *\**  is read by ssget as a wild-card character.

For example, you can retrieve an anonymous block named \*U2 with the following:

```
(ssget "X" '((2 . "`*U2")))
```

#### Related Concepts

* [About Selecting Objects and Selection Sets (AutoLISP)](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)
* [About Modifying Selection Sets (AutoLISP)](About-Modifying-Selection-Sets-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [About Logical Grouping of Selection Filter Tests (AutoLISP)](About-Logical-Grouping-of-Selection-Filter-Tests-AutoLISP.md)
* [About Relational Tests in Filter Lists for Selection Sets (AutoLISP)](About-Relational-Tests-in-Filter-Lists-for-Selection-Sets-AutoLISP.md)
* [About Filtering for Extended Data in a Selection Set (AutoLISP)](About-Filtering-for-Extended-Data-in-a-Selection-Set-AutoLISP.md)
* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*