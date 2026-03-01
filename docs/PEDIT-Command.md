# PEDIT (Command)

Edits polylines, objects to be joined to polylines, and related objects.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Polyline Edit.
![](../images/GUID-A8FCF43A-F63F-4FCB-AC8D-732FE0F37BBD-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

*Menu*:
Modify ![](../images/ac.menuaro.gif) Object ![](../images/ac.menuaro.gif) Polyline.

Common uses for PEDIT include joining 2D polylines, converting lines and arcs into 2D polylines, and converting polylines
into curves that approximate B-splines (spline-fit polylines).

Different prompts are displayed, depending on the type of object you select to edit.

If you select a line, arc, or spline, you are prompted to convert that object to a polyline. Several system variables affect
this conversion. The PLINECONVERTMODE system variable determines whether the polylines are created with linear or arc segments.
When the PEDITACCEPT system variable is set to 1, this prompt is suppressed, and the selected object is automatically converted
to a polyline. The DELOBJ system variable determines whether the original geometry is retained or removed.

The following prompts are displayed.

Select polyline
:   Specifies a single polyline to work on.

    * *Object selected is not a polyline. Do you want to turn it into one?* Displayed if the object you select is not a polyline. Enter
      *y* to convert the object to a polyline or
      *n* to clear the selection.
    * *Specify a precision.* Displayed if you select a spline and are converting it to a polyline. The precision value determines how accurately the resulting
      polyline is fit to the source spline. Enter an integer between 0 and 99.

      NOTE: A high precision value might cause slower performance.

Multiple
:   Specifies that you want to select more than one object.

    * *Convert lines, arcs, and splines to polylines?* Displayed if any of the objects you select is a line, arc, or spline. Enter
      *y* to convert the objects to a polyline or
      *n* to clear the selection.
    * *Specify a precision for spline conversion.*Displayed if any of the objects you select is a spline and you are converting them to polylines. The precision value determines
      how accurately the resulting polyline is fit to the source spline. Enter an integer between 0 and 99. The entered precision
      value affects all splines in the selection set.

#### Related Tasks

* [To Modify Polylines With PEDIT](To-Modify-Polylines-With-PEDIT.md)
* [To Draw a Polyline with Straight Segments](To-Draw-a-Polyline-with-Straight-Segments.md)
* [To Draw a Line and Arc Polyline](To-Draw-a-Line-and-Arc-Polyline.md)

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Information

* [About Polylines](About-Polylines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*