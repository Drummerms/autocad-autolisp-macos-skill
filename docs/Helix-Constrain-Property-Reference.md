# Helix Constrain Property Reference

With the Constrain property, you can specify that the Height, Turns, or Turn Height properties of the helix are constrained.
The Constrain property affects how the helix changes when the Height, Turns, or Turn Height properties are changed either
through the Properties palette or through grip editing. The table below shows the behavior of the helix depending on which
property is constrained.

| Constrained property | Changed property | Effect on these helix properties | | |
|  |  | Height | Turns | Turn Height |
| Height | Height | Changed | Fixed | Changed |
|  | Turns | Fixed | Changed | Changed |
|  | Turn Height | Fixed | Changed | Changed |
| Turns | Height | Changed | Fixed | Changed |
|  | Turns | Fixed | Changed | Changed |
|  | Turn Height | Changed | Fixed | Changed |
| Turn Height | Height | Changed | Changed | Fixed |
|  | Turns | Changed | Changed | Fixed |
|  | Turn Height | Fixed | Changed | Changed |

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Concepts

* [About Modifying Helixes](About-Modifying-Helixes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*