# Boundary Creation Dialog Box

Defines the object type, boundary set, and island detection method for creating a region or polyline using a specified point
within an area enclosed by objects.

BOUNDARY (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Hatch panel ![](../images/ac.menuaro.gif) Boundary.
![](../images/GUID-D54FC086-4D7A-4EAA-8243-41FF6509F5EC-low.png)

![](../images/GUID-B117ABC8-C1ED-454A-8CA2-8F25A0DDFBE8-low.png)

## List of Options

The following options are displayed.

Pick Points

Determines a boundary from existing objects that form an enclosed area around the specified point.

Boundary Retention

Defines the type of boundary object that will be created from the enclosed area and how enclosed areas are detected.

Object Type
:   Controls the type of the new boundary object.
    *boundary* creates the boundary as a region or a polyline object.

Retain Boundaries
:   Controls whether the objects created are retained after the dialog box is closed.

Island Detection
:   Controls whether
    *boundary* detects internal closed boundaries, called islands.

Boundary Set

Defines the set of objects
*boundary* analyzes when defining a boundary from a specified point.

Current Viewport
:   Defines the boundary set from everything in the current viewport extents. Selecting this option discards any current boundary
    set.

New
:   Prompts you to select the objects that define the boundary set.
    *boundary* includes only the objects that can be used to create a region or closed polyline when it constructs the new boundary set.

#### Related References

* [HATCH (Command)](HATCH-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*