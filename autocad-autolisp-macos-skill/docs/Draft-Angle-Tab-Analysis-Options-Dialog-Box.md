# Draft Angle Tab (Analysis Options Dialog Box)

Changes the display settings for the ANALYSISDRAFT command.

ANALYSISOPTIONS (Command)

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Analysis Options.
![](../images/GUID-E43E5959-FA91-43AA-B25D-2754135C2B20-low.png)

## List of Options

The following options are available.

Select objects to analyze

Prompts you to select the surface objects to analyze. When you are done selecting objects, press Enter to return to the dialog
box.

Color Mapping

Maps green to the highest draft angle, red to the medium draft angle, and blue to the lowest draft angle.

Angle
:   Sets the value for the high and low draft angles. The draft angle is the angle in degrees between the surface normal and the
    UCS plane.

    Enter a value for the highest angle allowed ([VSADRAFTANGLEHIGH](VSADRAFTANGLEHIGH-System-Variable.md)). When the object’s angle reaches this value, it displays in green.

    Displays the average value of the high and low angles. When the object’s angle reaches this value, it displays in red.

    Enter a value for the lowest angle allowed ([VSADRAFTANGLELOW](VSADRAFTANGLELOW-System-Variable.md)). When the object’s angle reaches this value, it displays in blue.

Clear Draft Angle Analysis
:   Removes the curvature analysis display from all objects in the current drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*