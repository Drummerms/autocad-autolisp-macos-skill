# About Action Expressions and Callbacks (DCL)

An action is performed when a certain tile in a dialog box is selected and an AutoLISP expression is assigned to the tile
by calling the
action\_tile function.

This is known as an action expression. Within the action expression, you often need access to attributes in the DCL file.
The
get\_tile and
get\_attr functions provide this capability.

* *get\_attr* function retrieves the user-defined attributes within the DCL file.
* *get\_tile* function gets the current runtime value of a tile based on user input to that tile.

Action expressions must be defined following the
new\_dialog call and before the
start\_dialog call.

Information relating to how the user has selected a tile or modified a tile's contents is returned to the action expression
as a callback. In most cases, every active tile within a dialog box can generate a callback. As with reactors, the action
expression that responds to the callback is often referred to as a callback function. This function should perform validity
checking on the associated tile and should update information in the dialog box that pertains to the value of the tile. Updating
the dialog box can include issuing an error message, disabling other tiles, and displaying the appropriate text in an edit
box or list box.

Only the OK button (or its equivalent) should query the tile values to permanently save the settings that the user has finally
selected. In other words, you should update the variables associated with tile values within the callback for the OK button,
not the callback for an individual tile. If permanent variables are updated within the individual tile callbacks, there is
no way to reset the values if the user selects the Cancel button. If the OK button's callback detects an error, it should
display an error message and return focus to the tile in error; it should not exit the dialog box.

When a dialog box includes several tiles whose handling is similar, it can be convenient to associate those tiles with a single
callback function. The principle of not committing to the user's changes until the user clicks OK still applies.

There are two ways to define actions other than calling
action\_tile. You can define a default action for the entire dialog box when you call
new\_dialog, and you can define an action by using a tile's
action attribute. These alternative means of defining actions, and the order in which they occur.

#### Topics in this section

* [About Action Expressions (DCL)](About-Action-Expressions-DCL.md)

  An action expression can access the variables that indicate which tile was selected, and describe the tile's state at the
  time of the action.
* [About Callback Reasons (DCL)](About-Callback-Reasons-DCL.md)

  The callback reason, returned in the
  $reason variable, specifies why the action occurred.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Action Expressions (DCL)](About-Action-Expressions-DCL.md)
* [About Application-Specific Data (DCL)](About-Application-Specific-Data-DCL.md)
* [About Callback Reasons (DCL)](About-Callback-Reasons-DCL.md)
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About Handling Edit Boxes (DCL)](About-Handling-Edit-Boxes-DCL.md)
* [About Handling Image Buttons and Tiles (DCL)](About-Handling-Image-Buttons-and-Tiles-DCL.md)
* [About Handling Radio Clusters (DCL)](About-Handling-Radio-Clusters-DCL.md)
* [About Handling Sliders (DCL)](About-Handling-Sliders-DCL.md)
* [About List Operations for List Boxes and Pop-Up Lists (DCL)](About-List-Operations-for-List-Boxes-and-Pop-Up-Lists-DCL.md)
* [About Processing List Elements (DCL)](About-Processing-List-Elements-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*