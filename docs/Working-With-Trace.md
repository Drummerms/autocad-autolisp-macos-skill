# Working With Trace

Create traces in the AutoCAD desktop (Windows or Mac), the AutoCAD web app, or the AutoCAD mobile app, then send or share
the drawing to collaborators so they can view the trace and its contents.

## Create a Trace

1. Go to the Traces palette.
   ![](../images/GUID-6D904CCC-34D3-4316-A84B-69498A1FEC28-low.png)
2. Choose New trace.
   ![](../images/GUID-3EAB823E-1F86-4116-A4B6-2981908A1D8D-low.png)

   This opens the Trace environment.
3. Use drawing and editing commands to add markups, text, and additional geometry.
4. When finished, close the trace by clicking the X in the Trace visor.

## Switch between Editing the Trace and Editing the Drawing

In the Trace toolbar, click Trace (TRACEEDIT)
![](../images/GUID-0DE20098-57EC-4630-9233-93E0253214A4-low.png) or Drawing (TRACEVIEW)
![](../images/GUID-35A9FC14-7228-4331-B5B5-2B767A86B812-low.png) to toggle whether you are modifying the trace or the drawing itself.

## Save a Trace

QSAVE, SAVEAS, and SAVE are disabled while a trace is open. Close the trace, then save the drawing.

## Edit a Trace

To edit your own trace contributions, simply open the trace and add or modify any geometry.

You cannot edit or modify someone else’s contributions. However, you can add your own contributions to the trace.

While viewing a trace, visibility of other's trace contributions can be toggled using the Avatar drop-down in the Trace toolbar.

## Add Contributions to a Trace Created by Someone Else

1. Go to the Traces palette.
   ![](../images/GUID-6D904CCC-34D3-4316-A84B-69498A1FEC28-low.png)
2. Choose an existing trace.

   This opens the Trace environment.
3. Use drawing and editing commands to add markups, text, and additional geometry.
4. When finished, close the trace by clicking the X in the Trace toolbar.

## Copy From Trace

Use the COPYFROMTRACE command to copy objects from a trace into the drawing. To copy objects from a trace:

1. While a trace is open, with Edit Drawing
   ![](../images/GUID-35A9FC14-7228-4331-B5B5-2B767A86B812-low.png) on, start the COPYFROMTRACE command.
2. Select objects in the trace, and press Enter. The objects remain in the trace and are copied into the drawing in the same
   location.

## Share a Trace

Traces are part of the drawing file itself, so when you share a drawing, any traces within that drawing are shared as well.
Simply use your preferred method for sharing drawings with others. Anyone with the access to the file can view the traces
in the drawing.

## View a Trace

Open the Traces palette, then select the trace from the list of traces.

## Delete a Trace

Open the Traces palette, then right-click the trace (desktop and web) or tap the options button next to the trace (mobile)
and select Delete.

NOTE:You cannot delete traces that were created by others. However, you can remove the contributions that you added to any trace.

## Delete My Contributions

You can remove the contributions that you added to a trace.

Open the Traces palette, then right-click the trace (desktop and web) or tap the options icon next to the trace (mobile)
and select Remove My Contributions.

## Rename a Trace

*Desktop and Web:*Open the Traces palette, then right-click the trace and select Rename.

*Mobile:* Open the Traces palette, then tap the options icon next to the trace and select Rename.

NOTE:You cannot rename traces that were created by others.

## *Tips for Working With Trace*

* Use TRACEOSNAP to control whether object snaps apply to trace geometry while viewing a trace. When trace geometry consists
  of low fidelity markups, supporting osnaps on trace geometry while viewing a trace may make it more difficult to update the
  host drawing's geometry. But when viewing high fidelity geometry in traces, osnaps may be useful.

  NOTE:TRACEOSNAP only applies when Edit Trace is on. When Edit Drawing is on, object snaps always apply to trace geometry.
* Use TRACEFADECTL to control the amount of fading on the geometry in the drawing.
* Use TRACEPAPERCTL to control the opaqueness of the tracing paper effect.
* When creating traces, it's good practice to choose a distinct color that makes the geometry in the trace easy to locate.
* When you add geometry to a trace and then exit the Trace environment, the trace maintains the last view. It's good practice
  to exit the Trace environment with the view you want to share with others, to make trace geometry easier to identify.

#### Related References

* [Commands for Working With Trace](Commands-for-Working-With-Trace.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*