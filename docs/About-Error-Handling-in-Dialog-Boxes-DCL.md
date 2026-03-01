# About Error Handling in Dialog Boxes (DCL)

Dialog boxes can display error messages and warnings with a
text tile known as an error tile (errtile), or with a nested alert box.

The following guidelines apply to both:

* Error messages should be complete sentences, punctuated as such, with an initial capital and a period at the end.
* Error messages should explain clearly the problem or potential problem.
* After reporting the error, shift the dialog box's focus to the tile that triggered the error, if possible.

## Error Tiles

Use an error tile for minor errors or warnings, especially those that arise from typographical errors. Do not display errors
in text tiles used for status messages. These are easy to overlook. Error tiles should appear at the bottom of a dialog box.

## Error Forgiveness

Make your dialog boxes forgiving, so users feel free to explore without fear of making irreversible mistakes. Report minor
errors by messages in an error tile at the bottom of the dialog box. Report more serious errors by displaying an alert box.
The
alert function displays a simple alert box (with a single OK button). If the user selects a potentially destructive or time-consuming
action, the dialog box should display an alert box that gives the user a choice of proceeding with the operation or canceling
it.

For example, in the Block Definition dialog box, an alert box appears when users attempt to create a block that already exists.
Users can then choose to proceed and overwrite the original block, or cancel the operation without making changes:

![](../images/GUID-DA28057D-996C-43EA-80B1-4D1BB098301F-low.png)

Nested dialog boxes that alert users should return to the previous dialog box. Terminate the current nest of dialog boxes
only in the case of serious or potentially fatal errors.

#### Topics in this section

* [About Alert Boxes (DCL)](About-Alert-Boxes-DCL.md)

  A standard alert box with a single OK button can be displayed by calling the
  alert function.

#### Related Concepts

* [About Customizing Exit Buttons (DCL)](About-Customizing-Exit-Buttons-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [About Alert Boxes (DCL)](About-Alert-Boxes-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*