# About Using Object Snaps

Object snaps provide a way to specify precise locations on objects whenever you are prompted for a point within a command.

For example, you can use object snaps to create a line from the center of a circle to the midpoint of another line.

![](../images/GUID-6F584B32-1659-4815-9078-2E600EC78BB7-low.png)

You can specify an object snap whenever you are prompted for a point. By default, a marker and a tooltip are displayed when
you move the cursor over an object snap location on an object. This feature, called AutoSnap ™ , provides visual confirmation that indicates which object snap is in effect.

## Specify an Object Snap

To specify an object snap at a prompt for a point, you can do one of the following:

* Press Shift and right-click to display the Object Snap shortcut menu
* Right-click and choose an object snap from the Snap Overrides submenu
* Click an object snap button on the Object Snap toolbar
* Enter the name of an object snap

When you specify an object snap at a prompt for a point, the object snap stays in effect only for the next point that you
specify. Object snaps work only when you are prompted for a point.

NOTE: If you want object snaps to ignore hatch objects, use the OSOPTIONS system variable.

## Use Running Object Snaps

If you need to use one or more object snaps repeatedly, you can turn on
*running object snaps*, which persist through all subsequent commands. For example, you might set Endpoint, Midpoint, and Center as running object
snaps.

* On the status bar, click the Object Snap button or press F3 to turn running object snaps on and off.
* On the status bar, click the down-arrow next to the Object Snap button, and then click the object snaps that you want to persist.

TIP: If several running object snaps are turned on, more than one object snap may be eligible at a given location. You can press
Tab to cycle through the possibilities before you specify the point.

#### Related Tasks

* [To Snap to a Geometric Location on an Object](To-Snap-to-a-Geometric-Location-on-an-Object.md)
* [To Display the Object Snap Menu](To-Display-the-Object-Snap-Menu.md)
* [To Set Running Object Snaps](To-Set-Running-Object-Snaps.md)
* [To Turn on and Turn off Running Object Snaps](To-Turn-on-and-Turn-off-Running-Object-Snaps.md)

#### Related References

* [Object Snaps (Command Modifier)](Object-Snaps-Command-Modifier.md)
* [MTP (Command Modifier)](MTP-Command-Modifier.md)

#### Related Concepts

* [About Using Object Snaps in 3D](About-Using-Object-Snaps-in-3D.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*