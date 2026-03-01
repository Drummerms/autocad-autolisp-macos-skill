# Example Using Local Variables (AutoLISP)

The following example shows the use of local variables in a user-defined function (be certain there is at least one space
between the slash and the local variables).

```
(defun LOCAL ( / aaa bbb)
(setq aaa "A" bbb "B")
(princ (strcat "\
aaa has the value " aaa ))
(princ (strcat "\
bbb has the value " bbb))
(princ) )

LOCAL
```

Before you test the new function, assign variables aaa and bbb to values other than those used in the  *LOCAL*  function.

```
(setq aaa 1 bbb 2)

2
```

You can verify that the variables aaa and bbb are actually set to those values.

```
!aaa
1

!bbb
2
```

Now test the LOCAL function.

```
(local)

aaa has the value A
bbb has the value B
```

You will notice the function used the values for aaa and bbb that are local to the function. You can verify that the current values for aaa and bbb are still set to their nonlocal values.

```
!aaa
1

!bbb
2
```

In addition to ensuring that variables are local to a particular function, this technique also ensures the memory used for
those variables is available for other functions.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*