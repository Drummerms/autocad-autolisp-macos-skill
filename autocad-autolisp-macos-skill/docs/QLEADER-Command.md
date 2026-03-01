# QLEADER (Command)

Creates a leader and leader annotation.

## Summary

It is recommended that you use the workflow available through the [MLEADER](MLEADER-Command.md) command to create leader objects.

You can use QLEADER to

* Specify leader annotation and annotation format
* Set the location where leaders attach to multiline text annotation
* Limit the number of leader points
* Constrain the angle of the first and second leader segments

You can use the [Leader Settings dialog box](Leader-Settings-Dialog-Box.md) to customize the command so that it prompts you for the number of leader points and the annotation type suited to your drawing
needs.

If associative dimensioning is turned on with DIMASSOC, the leader start point can be associated with a location on an object.
If the object is relocated, the arrowhead remains attached to the object and the leader line stretches, but the text or feature
control frame remains in place.

## List of Prompts

The following prompts are displayed.

Specify first leader point, or [Settings] <Settings>: *Specify the first leader point, or press* Enter *to specify leader settings*

First Leader Point

The Number of Points setting on the Leader Line & Arrow tab of the [Leader Settings dialog box](Leader-Settings-Dialog-Box.md) determines the number of leader points you are prompted to specify.

Width
:   If you set the text width value to 0.00, the width of the multiline text is unlimited.

Tolerance
:   If Tolerance is selected on the Annotation tab, the [Geometric Tolerance dialog box](Geometric-Tolerance-Dialog-Box.md) is displayed. Use the dialog box to create the tolerance feature control frame.

Enter block name or [?]: *Enter the name, or enter* *?* *to display a list of blocks defined in the drawing*

Insertion Point
:   For a description of the insertion options, see [INSERT Command Line](INSERT-Command-2.md).

Settings

Displays the [Leader Settings dialog box](Leader-Settings-Dialog-Box.md).

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*