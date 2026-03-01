# To Export a Layout to Model Space in a New Drawing

1. At the command prompt, enter EXPORTLAYOUT.
   ![](../images/GUID-ECDF3CA9-9E0D-45FC-AC7F-BCFDEACE42DD-low.png)
2. In the dialog box, enter a file name.

   The default file name combines the names of the current drawing and the current layout.
3. Specify the location where you want to save the file.
4. Click Save.

NOTE:Objects that are outside the boundaries of “paper” in the layout are also exported.

## Troubleshooting

* The performance of the EXPORTLAYOUT command may be slower if a model space viewport is active.
* In the exported drawing, the viewport displays the original linetype, which may not match the look of the original drawing.
  If this happens, assign “Continuous” linetype to viewports in the original drawing.
* Linetype scaling may not be accurately maintained for objects in xrefs and blocks if PSLTSCALE is 0.
* If you have a problem with xrefs during export, detach unresolved xrefs or manually bind xrefs and then use the EXPORTLAYOUT
  command.
* Superhatch objects (from Express Tools) are exported, but the hatching may not stay within the original boundaries. You can
  use the TRIM command in the exported drawing to correct any problems with visual appearance.

#### Related Tasks

* [To Work With Layout Tabs](To-Work-With-Layout-Tabs.md)

#### Related Concepts

* [About Exporting a Layout to Model Space in a New Drawing](About-Exporting-a-Layout-to-Model-Space-in-a-New-Drawing.md)
* [About Layouts](About-Layouts.md)

#### Related Information

* [EXPORTLAYOUT (Command)](EXPORTLAYOUT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*