# HATCH (Command)

Fills an enclosed area or selected objects with a hatch pattern, solid fill, or gradient fill.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Hatch panel ![](../images/ac.menuaro.gif) Hatch.
![](../images/GUID-6968D6F8-F92C-458E-B670-6599C70B316E-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Hatch.

The Hatch visor or Hatch and Gradient dialog box is displayed. If you prefer using the Hatch and Gradient dialog box, set
the HPDLGMODE system variable to 1.

If you enter
*-hatch* at the Command prompt, options are displayed.

NOTE:

* To prevent memory and performance problems, the maximum number of hatch lines created in a single hatch operation is limited.
  However, you can change the maximum number of hatch lines with the HPMAXLINES system variable.
* To maintain performance for hatches with non-continuous hatch lines, choose a predefined hatch
  *pattern* rather than loading and setting a non-continuous
  *linetype*. The HPLINETYPE system variable suppresses the display of non-continuous linetypes in hatches by default.
* To control whether object snaps ignore hatch objects, add or subtract 1 from the OSOPTIONS system variable.

Choose from several methods to specify the boundaries of a hatch.

* Specify a point in an area that is enclosed by objects.
* Select objects that enclose an area.
* Specify boundary points using the -HATCH Draw option.

![](../images/GUID-10BB1476-0D26-41F7-824E-14B5013ACCB6-low.gif)

The following prompts are displayed.

Pick internal point
:   Determines a boundary from existing objects that form an enclosed area around the specified point.

    ![](../images/GUID-BDD473C0-2427-4810-9E79-30702A267D5E-low.png)

Select objects
:   Determines a boundary from selected objects that form an enclosed area.

    ![](../images/GUID-B6761C2D-D44B-47A0-9903-436718221D11-low.png)

Draw
:   Uses specified points or creates basic geometric shapes to define new boundaries to hatch or fill.

    The Mode option controls how the new boundary is defined, an area or a path.

    As you specify points for the polyline boundary or path, you can define both straight and arc segments using options similar
    to the
    PLINE command. When you done, press Enter to complete the polyline boundary or path.

    NOTE:To close the polyline boundary or path, use the Close option. Do not make the first and last points coincident.

    ![](../images/GUID-BF47AE51-3CC9-4797-AB5F-59AC711C6D9B-low.png)

    The following options are available:

    * *Mode*: Sets the current hatch boundary drawing method.
      + *Area* - Defines a closed boundary from specified points or the basic geometric shape created. The area of the closed boundary defines
        the hatch or fill.
      + *Path* - Defines an open or closed path from which a closed boundary is derived. The Alignment and Width options define the direction
        and area of the closed boundary to hatch or fill.
    * *Rectangle*: Defines a rectangular boundary using the same options as the
      RECTANG command.
    * *Circle*: Defines a circular boundary using the same options as the
      CIRCLE command.
    * *Alignment*: Defines the alignment of the closed boundary to the path drawn. Alignment can be set from the center, inside or outside
      of the path. (Available only when Path mode is active.)
    * *Width*: Defines the width of the closed boundary from the path drawn. (Available only when Path mode is active.)

Undo
:   Removes the last hatch pattern you inserted with the currently active HATCH command.

Settings
:   Opens the Hatch and Gradient dialog box, where you can change settings.

#### Related Tasks

* [To Hatch or Fill Objects or Areas](To-Hatch-or-Fill-Objects-or-Areas.md)
* [To Create an Unbounded Hatch](To-Create-an-Unbounded-Hatch.md)

#### Related References

* [Hatch Visor](Hatch-Visor.md)
* [HPMAXLINES (System Variable)](HPMAXLINES-System-Variable.md)
* [HPLINETYPE (System Variable)](HPLINETYPE-System-Variable.md)
* [OSOPTIONS (System Variable)](OSOPTIONS-System-Variable.md)

#### Related Concepts

* [Hatch and Gradient Dialog Box](Hatch-and-Gradient-Dialog-Box.md)
* [-HATCH (Command)](HATCH-Command-2.md)
* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)
* [About Hatch Islands](About-Hatch-Islands.md)
* [About Hatch Pattern Scaling](About-Hatch-Pattern-Scaling.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*