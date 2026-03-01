# About Managing Dialog Boxes (DCL)

You can use dialog boxes to respond to user input.

With AutoCAD® , you can design and implement dialog boxes to use with your applications. The appearance of a dialog box is defined by dialog
control language (DCL) files, as described in About Designing Dialog Boxes (AutoLISP). You control the functionality of a
dialog box with an AutoLISP® application. The topics listed describe how to control dialog boxes using AutoLISP. Although this chapter shows some examples
of DCL files, you may find it helpful to read About Designing Dialog Boxes (AutoLISP) before reading this chapter.

#### Topics in this section

* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)

  Setting up a DCL dialog box requires the use of several AutoLISP functions that need to be called in a specific order.
* [About Controlling Dialog Boxes With AutoLISP Programs (DCL)](About-Controlling-Dialog-Boxes-With-AutoLISP-Programs-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)

  An action is performed when a certain tile in a dialog box is selected and an AutoLISP expression is assigned to the tile
  by calling the
  action\_tile function.
* [About Handling Tiles (DCL)](About-Handling-Tiles-DCL.md)
* [About Displaying Nested Dialog Boxes (DCL)](About-Displaying-Nested-Dialog-Boxes-DCL.md)

  You create and manage nested dialog boxes by calling
  new\_dialog and
  start\_dialog from within an action expression or callback function.
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)

  A user cannot interact with the graphics screen while a dialog box is active.
* [About Application-Specific Data (DCL)](About-Application-Specific-Data-DCL.md)

  The
  client\_data\_tile function assigns application-specific data to a tile.
* [About DCL Error Handling (DCL)](About-DCL-Error-Handling-DCL.md)

  The PDB feature checks a DCL file for errors the first time you load it. If a syntax error, a misuse of attributes, or any
  other error is encountered (such as failure to specify a key attribute for an active tile), the PDB does not load the DCL
  file.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*