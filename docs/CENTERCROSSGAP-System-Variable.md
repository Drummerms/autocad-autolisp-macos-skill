# CENTERCROSSGAP (System Variable)

Determines the gap between the center mark and its centerlines.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | "0.05x" |

The CENTERCROSSGAP system variable applies only to center marks created using the CENTERMARK command. A center mark has a
default relative size of
*0.1x* and gap of
*0.05x*.

NOTE:The CENTERCROSSSIZE and CENTERCROSSGAP system variable settings are related to one another. It is recommended that both system
variables use the same value type (absolute, relative, or ByLineType).

The CENTERCROSSGAP system variable setting is ignored when the radius of the circle is less than the sum of half the center
mark size and the gap distance. You can avoid this problem by specifying relative values to both CENTERCROSSSIZE and CENTERCROSSGAP
system variables.

| Value | Description |
| Absolute value (any positive real number) | Specifies the distance between the line segment of the center mark and its centerlines in units. |
| Relative value (any positive real number specified as a scale factor) | Specifies a value relative to the diameter of a circle or an arc. Enter a positive real number followed by *x*.  For example, *0.1x* is 1/10th of the circle's diameter. |
| "ByLineType" | The gap between the center mark and its centerlines is derived from linetype assigned to it.  NOTE:When the linetype of the center mark has only dash and gap, the size of the last dash and gap of the pattern is used as the center mark size and gap. If the linetype pattern of the center mark has other kinds of elements, the default setting is used. |

![](../images/GUID-EE686AA8-64F1-4A98-B439-5E9737525746-low.png)

#### Related References

* [CENTERCROSSSIZE (System Variable)](CENTERCROSSSIZE-System-Variable.md)
* [Center Mark Size and Gap Reference](Center-Mark-Size-and-Gap-Reference.md)
* [Commands for Center Marks and Centerlines](Commands-for-Center-Marks-and-Centerlines.md)

#### Related Concepts

* [About Center Marks and Centerlines](About-Center-Marks-and-Centerlines.md)

#### Related Information

* [About Editing Center Marks and Centerlines](About-Editing-Center-Marks-and-Centerlines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*