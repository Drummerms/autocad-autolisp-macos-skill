# COMPARE (Command)

Compares a specified drawing file with the current drawing file, highlighting the differences with color within revision
clouds.

## Access Methods

*Toolbar*:
![](../images/GUID-F4525FD8-467E-44D9-BD45-AEB73673ADFB-low.png)

*Menu:
File ![](../images/ac.menuaro.gif) DWG Compare*

The drawing selection dialog box is displayed. Select the drawing file you want to compare to the current drawing.

The COMPARE command provides you with a visual comparison between the current drawing and a specified comparison drawing.
Typically, these are different revisions of a drawing, which you can then review and modify. Use the DWG Compare visor to
work with the comparison.

## DWG Compare Visor

![](../images/GUID-FDFCDD98-4629-46D7-AC1A-986AF6D23D58-low.png)

* ![](../images/GUID-0D7CBE9D-323C-4535-9511-31C9029357E6-low.png) Opens the settings palette where you can change comparison options including color, revision clouds, hatch, and text.
* ![](../images/GUID-72DF67CE-5EBB-47F9-8D6E-0E6F7E98C7C8-low.png)Toggles the comparison on and off from the DWG Compare visor.
* ![](../images/GUID-E08DF176-4250-4E77-AD7F-803C79CC4961-low.png) ![](../images/GUID-1022F615-E637-472E-A23E-FE09CAD7F4C0-low.png) Steps through each change set, automatically zooming in to each successive or previous change set.
* *Current Change Set/ Total Number of Change Sets*. Displays the current change set number and total number of change sets. Type a specific change set number and press enter
  to zoom to that particular change set.
* ![](../images/GUID-A25D47BB-899C-49B4-B969-D5E21B7071A1-low.png) Imports the selected objects from the compared drawing into the current drawing. If you do so, these objects will now exist
  in both drawings and will automatically turn gray. Only the objects in the specified area that are
  *not* in the current drawing can be selected for import.
* ![](../images/GUID-D32B0E1E-6551-4A10-8CBD-E8258B398BE8-low.png) Exports both drawings into a new
  *snapshot drawing* that combines the similarities and changes between both drawings. The result of this operation is the same as a drawing comparison
  in the previous release.
* ![](../images/GUID-9002B3B8-BF54-447F-B816-6EA0CDF91EFC-low.png) Closes the drawing comparison.

## Settings Palette

![](../images/GUID-CEA84EDD-B5D4-4A2D-8676-5D1C0062273F-low.png)

## Differences

![](../images/GUID-61CF4160-4C11-43E3-AD80-76B0E9B695CB-low.png) ![](../images/GUID-80E3741D-4176-4F45-8E6E-D110BCACBB78-low.png)Turns on or off the objects only in the current drawing, the compared drawing, or common to both drawings.

*Color Swatch*. Specifies the color for the objects only in the current drawing, the compared drawing, or common to both drawings.

![](../images/GUID-51D58F34-F9F0-43E4-BE79-1F5C34E41DFE-low.png) ![](../images/GUID-003A7B38-A812-4263-9BBB-33FF39C1C415-low.png) Controls the display order of overlapping objects in the comparison.

## Revision Clouds

![](../images/GUID-29BDAE7E-32B2-44B0-9EDE-3A18529ACC98-low.png) ![](../images/GUID-D1DFC475-C416-4B16-A882-F2AA5499EDB1-low.png) Displays or hides the revision clouds around each change set in the comparison. Change sets are the same, whether or not
revision clouds are displayed.

*Shape*

* *Rectangular*. Creates a single rectangular revision cloud around each change set to show the changes.
* *Polygonal*. Creates polygonal revision clouds around each change set to show the changes.

*Margin*. Controls the margin between the change sets and revision clouds.

## Filters

![](../images/GUID-E6623040-7B2A-4D96-8139-754031532DDC-low.png) ![](../images/GUID-57A998C8-399A-4C1B-ADEF-861EEDB2026F-low.png) Controls whether hatch objects are included in the comparison.

![](../images/GUID-6AEDDB35-1B7A-4D11-B2B4-86A1C71AD3CD-low.png) ![](../images/GUID-F5E0C6D2-1EBA-4761-ADA8-1C389DC28BD4-low.png) Controls whether text objects are included in the comparison.

#### Related Tasks

* [To Compare Drawings](To-Compare-Drawings.md)

#### Related References

* [Commands for Working With DWG Compare](Commands-for-Working-With-DWG-Compare.md)

#### Related Concepts

* [About Comparing Differences Between Drawings](About-Comparing-Differences-Between-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*