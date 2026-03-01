# Trace

Trace provides a safe space to collaborate on drawing changes without fear of altering the existing drawing. The analogy of
trace is a virtual, collaborative tracing paper that's laid over the drawing, allowing collaborators to add feedback right
in the drawing.

![](../images/GUID-F7D68FE1-A583-4A79-8F0D-AB804DAA098F-low.png)

Create a trace, then send the drawing to collaborators so they can view the trace and add contributions to the trace. You
can contribute to a trace created by anyone but you can only remove your contributions from a collaborator's trace. You can
work with traces on AutoCAD desktop (Windows and Mac), or on the web and mobile apps.

## Create a Trace

1. Do one of the following:
   * At the command prompt, enter TRACE, enter N, and enter the trace name.
   * Click
     Window menu ![](../images/ac.menuaro.gif) Traces. Click Create Trace on the palette.

     ![](../images/GUID-780BE1D6-DD5F-4CD2-A391-155F83B31C5E-low.png)

   The trace is created and you are now in the trace mode.
2. Use drawing and editing commands to add markups, text, and additional geometry.
3. Click Close Trace on the Trace toolbar.
   ![](../images/GUID-9002B3B8-BF54-447F-B816-6EA0CDF91EFC-low.png)

## View and Contribute to an Existing Trace

When you open a drawing containing a trace, you'll see an alert.

![](../images/GUID-7EAE62E9-7AEA-4E04-94F2-211FC34C01D1-low.png)

1. Click Display the Trace Palette on the alert or select
   Window menu ![](../images/ac.menuaro.gif) Traces.

   ![](../images/GUID-10058C92-3ECE-4E87-99F4-D2540021076F-low.png)
2. To view or contribute to an existing trace, select one of the traces on the palette.
3. ![](../images/GUID-92AB34BD-F189-463B-86AD-77669049AD47-low.png)

   While a trace is active, the Trace visor is available.

   ![](../images/GUID-D822F5E3-E63D-40E1-B40A-AA07CD5CD73A-low.png)
4. To contribute to the active trace:
   1. If necessary, switch to edit the trace.

      ![](../images/GUID-45C83874-FDFB-40A2-88C3-3E13101198A6-low.png) - edit mode is active, click to switch to view mode

      ![](../images/GUID-75B683D8-C53B-47ED-A262-85161FBB1EC5-low.png) - view mode is active, click to switch to edit mode
   2. Use drawing and editing commands to add markups, text, and additional geometry.
5. To rename a trace, select the trace on the palette, right-click, and select Rename.
6. To delete a trace, select the trace on the palette, right-click, and select Delete.
7. To remove your contributions, select the trace on the palette, right-click and select Remove My Contribution.
8. Hover over the trace on the palette to see details, such as contributors.

   ![](../images/GUID-AA02BBAB-7481-40EB-BDD1-5609E73A3B3C-low.png)

## Trace Contributions

Now that multiple people can contribute to a trace, click the avatar on the trace visor to display the list of contributors
for the active trace.

![](../images/GUID-15AD9866-6110-4113-B560-2F32D2B087C8-low.png)

If there are contributions from others, you can do the following:

* Hover over the contributor's name on the visor's drop-down to highlight their contribution to the trace.

  ![](../images/GUID-36BA3729-CE28-4A6B-97BE-E330E396D9BF-low.png)
* Click the icon next to the contributor's name to hide or display their contributions.

  ![](../images/GUID-765C581B-C249-49D9-BBEB-118E4B0FBED3-low.png)

## Trace Object Details

Hover over a trace object to see who added it to the trace.

## *New Commands*

[TRACE](TRACE-Command.md) - Opens and manages traces from the command prompt.

[TRACEBACK](TRACEBACK-Command.md) - Displays the host drawing with full saturation, while dimming the trace geometry.

[TRACEEDIT](TRACEEDIT-Command.md) - Changes the active trace to edit mode so you can contribute to the trace.

[TRACEVIEW](TRACEVIEW-Command.md) - Changes the active trace to view mode so you edit the parent drawing.

[TRACEFRONT](TRACEFRONT-Command.md) - Displays the active trace with full saturation, while dimming the host drawing geometry.

[TRACEPALETTECLOSE](TRACEPALETTECLOSE-Command.md) - Closes the Trace palette.

[TRACEPALETTEOPEN](TRACEPALETTEOPEN-Command.md) - Opens the Trace palette where you can view and manage traces in the current drawing.

## *New System Variables*

[TRACECURRENT](TRACECURRENT-System-Variable.md) - Displays the name of the active trace when TRACEMODE=1 or 2.

[TRACEDISPLAYMODE](TRACEDISPLAYMODE-System-Variable.md) - Indicates whether the tracing paper effect is displayed (front) or not (back) while a trace is active.

[TRACEFADECTL](TRACEFADECTL-System-Variable.md) - Controls the amount of fading when TRACEMODE is active. The setting effects only the objects not being edited - the host
drawing geometry or Trace geometry.

[TRACEMODE](TRACEMODE-System-Variable.md) - Indicates whether Trace is active and which mode is current - editing or viewing.

[TRACEOSNAP](TRACEOSNAP-System-Variable.md) - Controls whether object snaps apply to trace geometry while viewing a trace.

[TRACEPALETTESTATE](TRACEPALETTESTATE-System-Variable.md) - Reports whether the Trace palette is open or closed.

[TRACEPAPERCTL](TRACEPAPERCTL-System-Variable.md) - Controls the opaqueness of the tracing paper effect. The lower the number, the more transparent the tracing paper is.

#### Related Tasks

* [Working With Trace](Working-With-Trace.md)

#### Related Concepts

* [What's New in AutoCAD for Mac 2023](What's-New-in-AutoCAD-for-Mac-2023.md)
* [About Trace](About-Trace.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*