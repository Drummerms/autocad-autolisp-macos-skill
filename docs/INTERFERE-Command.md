# INTERFERE (Command)

Creates a temporary 3D solid from the interferences between two sets of selected 3D solids.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Interference Checking.
![](../images/GUID-6A71F6D9-C943-4022-92E5-8DF55C683927-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) 3D Operations
![](../images/ac.menuaro.gif) Interference Checking.

## Summary

Interferences are highlighted with a temporary 3D solid that represents the intersecting volume. You can also choose to retain
the overlapping volumes.

![](../images/GUID-BD42942E-6CFB-46FF-9DCF-1C62FD9A067A-low.gif)

![](../images/GUID-BA386A33-CBDA-4A8E-8413-725CA6958B22-low.png)

If you define a single selection set, INTERFERE checks all the solids in the set against one another. If you define two selection
sets, INTERFERE checks the solids in the first selection set against those in the second selection set. If you include the
same 3D solid in both selection sets, INTERFERE considers the 3D solid part of the first selection set and ignores it in the
second selection set.

Pressing Enter starts the interference testing of pairs of 3D solids and displays the
[Interference Checking dialog box](Interference-Checking-Dialog-Box.md).

If you enter *-interfere* at the Command prompt,
[options are displayed](INTERFERE-Command-2.md).

## List of Prompts

The following prompts are displayed.

First set of objects
:   Specifies a set of objects to be checked. If you do not select a second set of objects, all objects in this selection set
    are checked against each other.

    * [Second set of objects](INTERFERE-Command.md)
    * [Nested selection](INTERFERE-Command.md)
    * [Settings](INTERFERE-Command.md)

Second set of objects
:   Specifies an additional set of objects to be compared against the first set of objects. If you select the same object twice,
    the object is handled as part of the first selection set.

    * [Second set of objects](INTERFERE-Command.md)
    * [Nested selection](INTERFERE-Command.md)
    * *Check first set.* Initiates interference checking for only the first selection set and displays the Interference Checking dialog box.
    * *Check.*Initiates interference checking for both sets of objects and displays the Interference Checking dialog box.

Nested selection
:   Provides access to individual solid objects that are nested in blocks and xrefs.

    * *Select nested objects.*Specifies which nested objects to include in the selection set.
    * *Exit.*Restores normal object selection (not nested).

Settings
:   Displays the
    [Interference Settings dialog box](Interference-Settings-Dialog-Box.md).

#### Related Concepts

* [-INTERFERE (Command)](INTERFERE-Command-2.md)
* [Interference Checking Dialog Box](Interference-Checking-Dialog-Box.md)
* [Interference Settings Dialog Box](Interference-Settings-Dialog-Box.md)
* [About Checking 3D Models for Interferences](About-Checking-3D-Models-for-Interferences.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*