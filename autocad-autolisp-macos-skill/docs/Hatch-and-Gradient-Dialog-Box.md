# Hatch and Gradient Dialog Box

Defines the boundaries, pattern, or fill properties, and other parameters for hatches and fills.

HATCH (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Hatch panel ![](../images/ac.menuaro.gif) Hatch
![](../images/GUID-6968D6F8-F92C-458E-B670-6599C70B316E-low.png): Specify the settings option at the prompt.

## List of Options

The dialog box includes the following:

* Hatch tab
* Gradient tab
* More Options section
* Add: Pick Points
* Add: Select Objects
* Remove Boundaries
* Recreate Boundary
* View Selections
* Display Boundary Objects
* Options
* Preview

Add: Pick Points

Determines a boundary from existing objects that form an enclosed area around the specified point.

![](../images/GUID-BDD473C0-2427-4810-9E79-30702A267D5E-low.png)

If you turn on Island Detection, objects that enclose areas within the outermost boundary are detected as islands. How HATCH
detects objects using this option depends on which island detection method is specified.

NOTE:Red circles are displayed at unconnected endpoints of boundary objects to identify gaps in the hatch boundary. These circles
are temporary and can be removed with REDRAW or REGEN.

Add: Select Objects

Determines a boundary from selected objects that form an enclosed area.

Interior objects are not automatically detected. You must select the objects within the selected boundary to hatch or fill
those objects according to the current island detection style.

![](../images/GUID-B6761C2D-D44B-47A0-9903-436718221D11-low.png)

Each time you click Add: Select Objects, HATCH clears the previous selection set.

![](../images/GUID-130AF57F-78E9-4EB5-93F4-A3171BC056E7-low.png)

Remove Boundaries

Removes from the boundary definition any of the objects that were added previously.

![](../images/GUID-830B55ED-340A-4134-AE50-56EF03AE5DE2-low.png)

Recreate Boundary

Creates a polyline or region around the selected hatch or fill, and optionally associates the hatch object with it.

View Selections

Displays the currently defined boundaries with the current hatch or fill settings. This option is available only when a boundary
has been defined.

Display Boundary Objects

Selects the objects that form the boundaries of the selected associative hatch object. Use the displayed grips to modify the
hatch boundaries.

NOTE:This option is available only in the
[Hatch Edit dialog box](GUID-2290F6B9-08B7-407B-8CF6-B8EC9BA231BA.htm#WSC30CD3D5FAA8F6D8FC9944FFC2D60571-7FCD) and replaces the View Selections option.

When you select an
*associative* hatch, a single, circular grip called the
*control grip* is displayed. No boundary grips are displayed because the boundaries of an associative hatch can be modified only by changing
its associated boundary objects. Use the Select Boundary Objects option to select and grip-edit the boundary objects.

To modify the boundaries of a
*nonassociative* hach, you modify the boundaries of the hatch object itself. Thus, when you select a nonassociative hatch, both the control
grip and the boundary grips are displayed.

Options

Controls several commonly used hatch or fill options.

Annotative
:   Specifies that the hatch is annotative. This property automates the process of scaling annotations so that they plot or display
    at the correct size on the paper. (HPANNOTATIVE system variable)

Associative
:   Specifies that the hatch or fill is associative. A hatch or fill that is associative is updated when you modify its boundary
    objects. (HPASSOC system variable)

Separate Hatches
:   Controls whether a single hatch object or multiple hatch objects are created when several separate closed boundaries are specified.
    (HPSEPARATE system variable)

Draw Order
:   Assigns a draw order to a hatch or fill. You can place a hatch or fill behind all other objects, in front of all other objects,
    behind the hatch boundary, or in front of the hatch boundary. (HPDRAWORDER system variable)

Layer
:   Assigns new hatch objects to the specified layer, overriding the current layer. Select Use Current to use the current layer.
    (HPLAYER system variable)

Transparency
:   Sets the transparency level for new hatch or fills, overriding the current object transparency. Select Use Current to use
    the current object transparency setting. (HPTRANSPARENCY system variable)

Inherit Properties
:   Hatches or fills specified boundaries using the hatch or fill properties of a selected hatch object.

    After selecting the hatch object whose properties you want the hatch to inherit, right-click in the drawing area and use the
    options on the shortcut menu to switch between the Select Objects and Pick Internal Point options.

    The HPINHERIT system variable controls whether the hatch origin of the resulting hatch is determined by HPORIGIN or by the
    source object.

Preview

Displays the currently defined boundaries with the current hatch or fill settings. Click in the drawing area or press Esc
to return to the dialog box. Right-click or press Enter to accept the hatch or fill.

More Options

Expands the dialog box to display more options.

#### Related Tasks

* [To Hatch or Fill Objects or Areas](To-Hatch-or-Fill-Objects-or-Areas.md)
* [To Create an Unbounded Hatch](To-Create-an-Unbounded-Hatch.md)

#### Related References

* [HATCH (Command)](HATCH-Command.md)
* [Hatch Visor](Hatch-Visor.md)
* [HPMAXLINES (System Variable)](HPMAXLINES-System-Variable.md)
* [HPLINETYPE (System Variable)](HPLINETYPE-System-Variable.md)
* [OSOPTIONS (System Variable)](OSOPTIONS-System-Variable.md)

#### Related Concepts

* [-HATCH (Command)](HATCH-Command-2.md)
* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)
* [About Hatch Islands](About-Hatch-Islands.md)
* [About Hatch Pattern Scaling](About-Hatch-Pattern-Scaling.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*