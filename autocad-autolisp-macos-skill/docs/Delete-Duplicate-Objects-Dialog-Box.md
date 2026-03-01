# Delete Duplicate Objects Dialog Box

Removes duplicate geometry as well as overlapping lines, arcs, and polylines. Also, combines partially overlapping or contiguous
ones.

OVERKILL (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Delete Duplicate Objects.
![](../images/GUID-ABBCDD4D-C8FD-4CEB-85E6-93D655CF4CFD-low.png)

![](../images/GUID-018577FF-3371-4BC4-AC4F-20D0BCF3F2F6-low.png)

## List of Prompts

The following options are displayed.

Object Difference Tolerance

Controls the precision with which OVERKILL makes numeric comparisons. If this value is 0, the two objects being compared must
match before OVERKILL modifies or deletes one of them.

Ignore Object Property:

Use these settings to determine which object properties are ignored during comparison.

Color
:   Object color is ignored.

Layer
:   Object layers are ignored.

Linetype
:   Object linetypes are ignored.

Linetype Scale
:   Object linetype scale is ignored.

Lineweight
:   Object lineweight is ignored.

Thickness
:   Object thickness is ignored.

Transparency
:   Object transparency is ignored.

Plot style
:   Object plot style is ignored.

Material
:   Object material is ignored.

Options

Use these settings to control how OVERKILL deals with lines, arcs, and polylines.

Optimize polyline segments
:   When selected, individual line and arc segments within selected polylines are examined. Duplicate vertices and segments are
    removed.

    Also, OVERKILL compares individual polyline segments with completely separate line and arc segments. If a polyline segment
    duplicates a line or arc object, one of them is deleted.

    If this option is not selected, polylines are compared as discreet objects and two sub-options are not selectable.

    * *Ignore polyline segment width.* Ignores segment width, while optimizing polyline segments.
    * *Do not break polylines.* Polyline objects are unchanged.

Combine co-linear objects that partially overlap
:   Overlapping objects are combined into single objects.

Combine co-linear objects when aligned end-to-end
:   Objects that have common endpoints are combined into single objects.

Maintain associative objects
:   Associative objects are not deleted or modified.

#### Related References

* [OVERKILL (Command)](OVERKILL-Command-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*