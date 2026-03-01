# -INTERFERE (Command)

## Summary

INTERFERE highlights all interfering 3D solids and displays the number of objects selected and the number of interfering pairs.

If you define a single selection set, INTERFERE checks all the solids in the set against one another. If you define two selection
sets, INTERFERE checks the solids in the first selection set against those in the second selection set. If you include the
same 3D solids in both selection sets, INTERFERE considers the 3D solid part of the first selection set and ignores it in
the second selection set.

## List of Prompts

The following prompts are displayed.

Check for interferences between 2 sets of objects or within 1 set of objects...

Select first set of objects or [[Nested selection](INTERFERE-Command-2.md)]: *Use an object selection method or enter an option*

Select second set of objects or [[Nested selection](INTERFERE-Command-2.md)/checK current] <checK>: *Use an object selection method, enter* *n**, or press* Enter *to check for interferences*

Create Interference Objects
:   Creates and highlights new 3D solids on the current layer that are the intersections of the interfering pairs of 3D solids.

    If there are more than two interfering 3D solids, it may not be clear which pairs are interfering if all the interfering 3D
    objects are highlighted at once.

    * Zoom to pairs of interfering objects

Next Pair
:   Cycles through the interfering pairs of 3D solids.

Nested Selection

Allows you to select individual solid objects that are nested in blocks and xrefs.

#### Related References

* [INTERFERE (Command)](INTERFERE-Command.md)

#### Related Concepts

* [Interference Checking Dialog Box](Interference-Checking-Dialog-Box.md)
* [Interference Settings Dialog Box](Interference-Settings-Dialog-Box.md)
* [About Checking 3D Models for Interferences](About-Checking-3D-Models-for-Interferences.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*