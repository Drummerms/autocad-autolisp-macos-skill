# Constraint Settings Dialog Box

Allows you to control the geometric constraints, dimensional constraints, and autoconstrain settings.

CONSTRAINTSETTINGS (Command)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Constraint Settings.

![](../images/GUID-02F4C8EC-03D4-415B-84C8-3740E8B6C9FD-low.png)

## List of Options

The following options are displayed.

Geometric Tab

Controls the display of constraint types on constraint bars.

Displayed Constraints
:   Controls the display of constraint bars or constraint point markers for objects in the drawing editor.

    For example, you can hide the display of constraint bars for Horizontal and Vertical constraints.

Select All
:   Selects the geometric constraint types.

Clear All
:   Clears the selected geometric constraint types.

Icon Transparency
:   Sets the transparency level of constraint bars in a drawing.

Display Constraints in the Current Plane Only
:   Displays constraint bars for geometrically constrained objects only on the current plane.

Dimensional Tab

Sets preferences in behavior when displaying dimensional constraints.

Constraint Format
:   Specifies the format for the text displayed when dimensional constraints are applied.

    Set the name format to display: Name, Value, or Name and Expression.

    For example: Width=Length/2

Show Lock Icon for Annotational Constraints
:   Displays a lock icon against an object that has an annotational constraint applied ([DIMCONSTRAINTICON](DIMCONSTRAINTICON-System-Variable.md) system variable).

Show Hidden Constraints on Selected Objects
:   Displays dynamic constraints that have been set to hide when selected.

Autoconstrain Tab

Controls the constraints that are applied to a selection set, and the order in which they are applied when using the
[AUTOCONSTRAIN](AUTOCONSTRAIN-Command.md) command.

The following conditions are checked before multiple geometric constraints are applied:

* Are the objects perpendicular or tangential to each other within the tolerances specified in the AutoConstrain tab?
* Do they also intersect within the specified tolerances?

If the first condition is met, then tangent and perpendicular constraints are always applied if the check boxes are cleared.

If you select the additional check boxes, then the distance tolerance is considered for intersecting objects. If the objects
do not intersect but the nearest distance between them is within the distance tolerance specified, then the constraint will
be applied even if the check boxed are selected.

Autoconstrain Headings
:   * Applied — Controls the constraints that are applied when applying constraints to multiple objects.
    * Constraint — Controls the type of constraint applied to objects.

    NOTE:Drag to change the order.

Constraint Tolerances & Rules
:   Sets the acceptable tolerance values to determine whether a constraint can be applied.

    * Distance — Distance tolerance are applied to coincident, concentric, tangent, and collinear constraints.
    * Angle — Angular tolerance are applied to horizontal, vertical, parallel, perpendicular, tangent, and collinear constraints.

Tangent Objects Must Intersect
:   Specifies that two curves must share a common point (as specified within the distance tolerance) for the tangent constraint
    to be applied.

Perpendicular Objects Must Intersect
:   Specifies that lines must intersect or the endpoint of one line must be coincident with the other line or endpoint of the
    line as specified within the distance tolerance.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*