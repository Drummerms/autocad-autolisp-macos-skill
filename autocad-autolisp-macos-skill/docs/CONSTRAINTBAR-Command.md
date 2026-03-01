# CONSTRAINTBAR (Command)

Displays or hides the geometric constraints on an object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Show Constraints.
![](../images/GUID-A302A903-6309-4AA1-B5E4-EA2713DAF5FC-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Constraint Bars ![](../images/ac.menuaro.gif) Select Objects.

## Summary

The selection preview behavior for constraint bars is as follows:

* Placing the cursor over an icon on a constraint bar highlights related geometry.
* Placing the cursor over a constrained object (while constraint bars are displayed) highlights the constraint icons associated
  with the selected object.

The
[CONSTRAINTBARMODE](CONSTRAINTBARMODE-System-Variable.md) system variable or the
[CONSTRAINTSETTINGS](CONSTRAINTSETTINGS-Command.md) command controls the display of geometric constraints on constraint bars, when constraint bar are displayed.

## List of Prompts

The following prompts are displayed.

Select objects:
*Select objects with constraint bars*

Enter an option [[Show](CONSTRAINTBAR-Command.md)/[Hide](CONSTRAINTBAR-Command.md)/[Reset](CONSTRAINTBAR-Command.md)] <Show>:*Enter the appropriate value to show or hide constraint bars in the drawing.*

Show

Displays constraint bars for the selected objects with geometric constraints applied to them.

Hide

Hides constraint bars for the selected objects with geometric constraints applied to them.

Reset

Displays constraint bars for all objects with geometric constraints applied to them and resets them to their default locations
relative to their associated parameters.

#### Related Concepts

* [About Displaying and Verifying Geometric Constraints](About-Displaying-and-Verifying-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*