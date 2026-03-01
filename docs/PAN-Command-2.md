# -PAN (Command)

Moves the view planar to the screen by specifying a distance and direction the view should be moved in.

## List of Prompts

The following prompts are displayed.

Specify base point or displacement: *Specify a point*

You can specify a single point, indicating the relative displacement of the drawing with respect to the current location,
or (more commonly) you can specify two points, in which case the displacement is computed from the first point to the second
point.

![](../images/GUID-4CE36F4B-FA36-4115-A8CB-E838A1E1021A-low.png)

If you press Enter, the drawing is moved by the amount you specified in the Specify Base Point or Displacement prompt. For
example, if you specify *2,2* at the first prompt and press Enter at the second prompt, the drawing is moved 2 units in the *X* direction and 2 units in the *Y* direction. If you specify a point at the Specify Second Point prompt, the location of the first point is moved to the location
of the second point.

You cannot use PAN transparently during [VPOINT](VPOINT-Command.md) or [DVIEW](DVIEW-Command.md), or while another [ZOOM](ZOOM-Command.md), PAN, or [VIEW](VIEW-Command-2.md) command is in progress.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*