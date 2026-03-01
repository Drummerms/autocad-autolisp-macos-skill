# About Revision Clouds

Revision clouds are closed polylines that form cloud-shaped objects consisting of arc segments.

If you review or markup drawings, you can use the revision cloud feature to call attention to portions of each drawing.

## Create Revision Clouds

You can create a revision cloud by moving the mouse, or you can convert objects, such as a circle, ellipse, closed polyline,
or a closed spline, to a revision cloud. A style is available to make the revision cloud appear similar to calligraphy.

![](../images/GUID-F6D93B15-35DC-427F-8C0D-6D54F3F62FAB-low.png)

You can control whether the arcs in each revcloud are created with varying or uniform chord lengths with the REVCLOUDARCVARIANCE
system variable.

## Modify Revision Clouds with Grips

Revision clouds offer specific options when you hover over a grip on a selected revision cloud. The options change depending
on the grip location and the setting of the REVCLOUDGRIPS system variable. When REVCLOUDGRIPS system variable is turned off,
you can use the grips to edit the individual arc lengths and chords in a revision cloud. Otherwise, the grips display options
to add or remove a vertex, or stretch the revision cloud or its vertex.

## Modify the Size of the Arcs

Use the Arc length option of REVCLOUD to specify the approximate chord lengths of the arcs in a revision cloud. You can modify
the approximate chord lengths for selected revision clouds from the shortcut menu, from the Properties Inspector palette when
a revision cloud is selected, or directly with the REVCLOUDPROPERTIES command.

#### Related References

* [REVCLOUD (Command)](REVCLOUD-Command.md)

#### Related Information

* [To Work With Revision Clouds](To-Work-With-Revision-Clouds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*