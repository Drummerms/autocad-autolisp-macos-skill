# About Overriding a Dimension Style

With dimension style overrides, you can temporarily change a dimensioning system variable without changing the current dimension
style.

A dimension style override is a change made to specific settings in the current dimension style. It is equivalent to changing
a dimensioning system variable without changing the current dimension style.

You can define dimension style overrides for individual dimensions, or for the current dimension style.

* For individual dimensions, you may want to create overrides to suppress a dimension's extension lines or modify text and arrowhead
  placement so that they do not overlap drawing geometry without creating a different dimension style.
* You can also set up overrides to the current dimension style. All dimensions you create in the style include the overrides
  until you delete the overrides, save the overrides to a new style, or set another style current. For example, if you choose
  Override in the Dimension Style Manager, and change the color of extension lines in the Override Current Style dialog box,
  Lines tab, the current dimension style remains unchanged. However, the new value for color is stored in the DIMCLRE system
  variable. The next dimension you create will display its extension lines in the new color. You can save the dimension style
  overrides as a new dimension style.

Some dimension characteristics are common to a drawing or to a style of dimensioning and are therefore suited to be permanent
dimension style settings. Others generally apply on an individual basis and can be applied more effectively as overrides.
For example, a drawing usually uses a single type of arrowhead, so it makes sense to define the arrowhead type as part of
the dimension style. Suppression of extension lines, however, usually applies in individual cases only and is more suited
to a dimension style override.

There are several ways to set up dimension style overrides. You can change options in the dialog boxes or change system variable
settings at the Command prompt. You reverse the override by returning the changed settings to their original values. The overrides
apply to the dimension you are creating and all subsequent dimensions created with that dimension style until you reverse
the override or make another dimension style current.

## Example: Change a Dimension Style Override at the Command Prompt

You can override the current dimension style while creating a dimension by entering the name of any dimensioning system variable
at any prompt. In this example, the dimension line color is changed. The change affects subsequent dimensions you create until
you reverse the override or make another dimension style current.

Command: *dimoverride*

Enter dimension variable name to override or [Clear overrides]: *dimclrd*

Enter new value for dimension variable <BYBLOCK>: *5*

Enter dimension variable name to override: *Enter another dimension variable name or press* Enter

Select objects: *Use an object selection method and press* Enter *when you finish*

#### Related Tasks

* [To Set Up Dimension Style Overrides](To-Set-Up-Dimension-Style-Overrides.md)
* [To Apply Dimension Style Overrides](To-Apply-Dimension-Style-Overrides.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*