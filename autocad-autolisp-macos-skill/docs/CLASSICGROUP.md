# CLASSICGROUP

Creates and manages saved sets of objects called groups.

## List of Prompts

The following prompts are displayed.

Enter a group option [?/Order/Add/Remove/Explode/REName/Selectable/Create] <Create>:
*Enter an option or press* Enter

?—List Groups

Lists names and descriptions of groups defined in the drawing.

Order

Changes the numerical order of objects within a group. Reordering is useful when creating tool paths. For example, you can
change the cut order for the horizontal and vertical lines of a tool path pattern.

Position Number
:   Specifies the position number of the object to reorder. To reorder a range of objects, specify the first object's position
    number.

Reverse Order
:   Reverses the order of all members in a group.

Add

Adds objects to a group.

Remove

Removes objects from a group.

If you remove all the group's objects, the group remains defined. You can remove the group definition from the drawing by
using the Explode option.

Explode

Deletes a group definition by exploding the group into its component objects.

Ungroup

Removes the group name and the association of objects in the group.

Rename

Assigns a new name to an existing group.

Selectable

Specifies whether a group is selectable. When a group is selectable, selecting one object in the group selects the whole group.
Objects on locked or frozen layers are not selected.

Create

Creates a group.

Group names can be up to 31 characters long and can include letters, numbers, and special characters dollar sign ($), hyphen
(-), and underscore (\_) but not spaces. The name is converted to uppercase characters.

#### Related Information

* [About Groups](About-Groups.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*