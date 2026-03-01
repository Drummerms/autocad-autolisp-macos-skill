# About Passing Selection Sets Between AutoLISP and ObjectARX Applications (AutoLISP)

NOTE:ObjectARX is not available in AutoCAD LT.

When passing selection sets between AutoLISP and ObjectARX applications, the following should be observed:

If a selection set is created in AutoLISP and stored in an AutoLISP variable, then overwritten by a value returned from an
ObjectARX application, the original selection set is eligible for garbage collection (it is freed at the next automatic or
explicit garbage collection).

This is true even if the value returned from the ObjectARX application was the original selection set. In the following example,
if the
 *adsfunc*  ObjectARX function returns the same selection set it was fed as an argument, then this selection set will be eligible for
garbage collection even though it is still assigned to the same variable.

```
(setq var1 (ssget))
(setq var1 (adsfunc var1))
```

If you want the original selection set to be protected from garbage collection, then you must not assign the return value
of the ObjectARX application to the AutoLISP variable that already references the selection set. Changing the previous example
prevents the selection set referenced by
var1 from being eligible for garbage collection.

```
(setq var1 (ssget))
(setq var2 (adsfunc var1))
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*