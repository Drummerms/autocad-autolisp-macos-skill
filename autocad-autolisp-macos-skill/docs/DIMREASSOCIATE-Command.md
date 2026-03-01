# DIMREASSOCIATE (Command)

Associates or reassociates selected dimensions to objects or points on objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Reassociate Dimension.
![](../images/GUID-0ECE9C4A-4293-4C60-81CF-31CAC64275A7-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Reassociate Dimensions.

## Summary

Each selected dimension is highlighted in turn, and prompts for association points appropriate for the selected dimension
are displayed.

A marker is displayed for each association point prompt.

* If the definition point of the current dimension is not associated to a geometric object, the marker appears as an X
* If the definition point is associated, the marker appears as an X inside a box.

NOTE:The marker disappears if you pan or zoom.

## List of Prompts

The following prompts are displayed.

Select dimensions to reassociate...

Select objects or [Disassociated]:
*Select the dimension objects to reassociate or press* D
*to select all disassociated dimensions.*

Press Esc to terminate the command without losing the changes that were already specified. Use
[UNDO](UNDO-Command.md) to restore the previous state of the changed dimensions.

The prompts for the different types of dimensions are:

Linear
:   Specify first extension line origin or [Select object] <next>:
    *Specify an object snap location, enter**s* *and select a geometric object, or press*Enter
    *to skip to the next prompt*

    Specify second extension line origin <next>:
    *Specify an object snap location, or press*Enter
    *to skip to the next dimension object, if any*

Aligned
:   Specify first extension line origin or [Select object] <next>:
    *Specify an object snap location, enter**s* *and select a geometric object, or press*Enter
    *to skip to the next prompt*

    Specify second extension line origin <next>:
    *Specify an object snap location, or press*Enter
    *to skip to the next dimension object, if any*

Angular (Three Point)
:   Specify angle vertex or [Select arc or circle] <next>:
    *Specify an object snap location, enter**s* *and select an arc or a circle, or press*Enter
    *to skip to the next prompt*

    Specify first angle endpoint <next>:
    *Specify an object snap location or press*Enter
    *to skip to the next prompt*

    Specify second angle endpoint <next>:
    *Specify an object snap location or press*Enter
    *to skip to the next dimension object, if any*

Angular (Two Line)
:   Select first line <next>:
    *Select a line, or press*Enter
    *to skip to the next prompt*

    Select second line <next>:
    *Select another line, or press*Enter
    *to skip to the next dimension object, if any*

Diameter
:   Select arc or circle <next>:
    *Select an arc or a circle, or press*Enter
    *to skip to the next dimension object, if any*

Leader
:   Specify leader association point <next>:
    *Specify an object snap location, or press*Enter
    *to skip to the next dimension object, if any*

Ordinate
:   Specify feature location <next>:
    *Specify an object snap location, or press*Enter
    *to skip to the next dimension object, if any*

Radius
:   Select arc or circle <next>:
    *Select an arc or a circle, or press*Enter
    *to skip to the next dimension object, if any*

NOTE:DIMREASSOCIATE does not change the setting of
[DIMLFAC](DIMLFAC-System-Variable.md) in a dimension. Use
[DIMOVERRIDE](DIMOVERRIDE-Command.md) to clear dimension linear factors in legacy drawings.

#### Related Concepts

* [About Associative Dimensions](About-Associative-Dimensions.md)
* [About Changing Dimension Associativity](About-Changing-Dimension-Associativity.md)
* [About Dimensioning](About-Dimensioning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*