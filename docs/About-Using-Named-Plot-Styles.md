# About Using Named Plot Styles

Named plot styles are assigned to objects and layers in the same way that linetype and color are assigned to objects.

An object whose plot style is set to BYLAYER inherits the plot style assigned to its layer.

Use the Properties palette to change an object's plot style and the Layer Properties Manager to change the plot style for
a layer.

Because different plot style tables can be assigned to each layout and a named plot style table can contain any number of
plot styles, an object or layer may have a plot style assigned to it that is not in every plot style table. In this case,
the plot style is missing in the Select Plot Style dialog box; the object's default plotting properties are used. For example,
named plot style table Style1 contains plot styles A and B. Named plot style table Style2 contains plot styles B and C. In
a layout that uses Style1, any objects that use plot style C are listed as having a missing plot style. Objects that are assigned
plot style C in this layout are plotted using their default settings.

#### Related Tasks

* [To Rename a Plot Style Table](To-Rename-a-Plot-Style-Table.md)

#### Related Concepts

* [About Managing Named Plot Styles](About-Managing-Named-Plot-Styles.md)

#### Related Information

* [To Copy a Named Plot Style](To-Copy-a-Named-Plot-Style.md)
* [To Create a Named Plot Style](To-Create-a-Named-Plot-Style.md)
* [To Delete a Named Plot Style](To-Delete-a-Named-Plot-Style.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*