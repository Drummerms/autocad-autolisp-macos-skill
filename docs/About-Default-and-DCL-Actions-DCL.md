# About Default and DCL Actions (DCL)

The
action\_tile function is not the only way to specify an action.

A tile's DCL description can include an action attribute in AutoLISP, and the
new\_dialog call can specify a default action for the dialog box as a whole. A tile can have only a single action at a time. If the DCL
and the application specify more than one action, they supersede each other in the following order of priority (lowest to
highest):

* The default action specified by the
  new\_dialog call (used only if no action is explicitly assigned to the tile).
* The action specified by the
  action attribute in the DCL file.
* The action assigned by the
  action\_tile call (highest priority).

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)
* [About Handling Edit Boxes (DCL)](About-Handling-Edit-Boxes-DCL.md)
* [About Handling Image Buttons and Tiles (DCL)](About-Handling-Image-Buttons-and-Tiles-DCL.md)
* [About Handling Radio Clusters (DCL)](About-Handling-Radio-Clusters-DCL.md)
* [About Handling Sliders (DCL)](About-Handling-Sliders-DCL.md)
* [About List Operations for List Boxes and Pop-Up Lists (DCL)](About-List-Operations-for-List-Boxes-and-Pop-Up-Lists-DCL.md)
* [About Processing List Elements (DCL)](About-Processing-List-Elements-DCL.md)
* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*