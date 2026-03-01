# To Specify a Virtual Pen Number

Many plotters that do not use pens can simulate the performance of a pen plotter by using virtual pens. If you allow software
to control the pens, the Plot Style Table values for the Lineweight, Linetype, Screening, Line End Style, Line Join Style,
and Fill Style settings are effective and override the settings on the plotter's control panel.

If you turn off software control of the pen attributes (typically done on the plotter), then the software can select virtual
pens but can't control lineweight, linetype, end style, join style, fill style, or color. In the program, you select hardware
(virtual pen) control over software (normal) control by selecting 255 Virtual Pens in the Color Depth area of the Vector Graphics
option on the Device and Document Settings tab in the Plotter Configuration Editor. Selecting any other color depth specifies
software control.

When you create a plot style table, it is important to remember that it can be used with many different plotters and that
the plotter and mode determine what parts of the plot style table are enabled.

1. Click
   Format menu ![](../images/ac.menuaro.gif) Plot Style.
2. In the Edit Plot Style Table, Select the plot style table that you want to modify and click Edit.
3. In the Plot Style Table Editor, under Virtual Pen #, enter a number between 1 and 255 or enter
   *0* or
   *Automatic* to have the program assign the ACI color of the object you are plotting to the virtual pen.
4. When finished, click Save & Close.

   You can edit properties for multiple plot styles while in the Plot Style Table Editor.

#### Related Information

* [To Assign a Fill Style](To-Assign-a-Fill-Style.md)
* [To Assign a Plot Style Color](To-Assign-a-Plot-Style-Color.md)
* [To Enable or Disable Conversion to Grayscale](To-Enable-or-Disable-Conversion-to-Grayscale.md)
* [To Enable or Disable Dithering](To-Enable-or-Disable-Dithering.md)
* [To Work With Removing Hidden Lines When Plotting](To-Work-With-Removing-Hidden-Lines-When-Plotting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*