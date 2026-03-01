# About Working With Blocks (AutoLISP)

There is no direct method for an application to check whether a block listed in the BLOCK table is actually referenced by
an insert object in the drawing. You can use the following code to scan the drawing for instances of a block reference:

```
(ssget "x" '((2 . "BLOCKNAME")))
```

You must also scan each block definition for instances of nested blocks.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*