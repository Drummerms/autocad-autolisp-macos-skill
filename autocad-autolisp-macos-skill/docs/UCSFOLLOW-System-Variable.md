# UCSFOLLOW (System Variable)

Generates a plan view whenever you change from one UCS to another.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

The UCSFOLLOW setting is saved separately for each viewport. If UCSFOLLOW is on for a particular viewport, a plan view is
generated in that viewport whenever you change coordinate systems.

Once the new UCS has been established, you can use [DVIEW](DVIEW-Command.md), [PLAN](PLAN-Command.md), [VIEW](VIEW-Command-2.md), or [VPOINT](VPOINT-Command.md) to change the view of the drawing. It will change to a plan view again the next time you change coordinate systems.

| 0 | UCS does not affect the view |
| 1 | Any UCS change causes a change to the plan view of the new UCS in the current viewport |

The setting of UCSFOLLOW is maintained separately for paper space and model space and can be accessed in either, but the setting
is ignored while in paper space (it is always treated as if set to 0). Although you can define a non-world UCS in paper space,
the view remains in plan view to the world coordinate system.

#### Related Concepts

* [About the User Coordinate System (UCS)](About-the-User-Coordinate-System-UCS.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*