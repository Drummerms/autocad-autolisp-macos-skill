# About Handling Tiles (DCL)

Your program has some control over the tiles that are in the current dialog box at initialization time and action (callback)
time. This section introduces the tile-handling functions and shows how to initialize and modify the tiles' modes and values.

#### Topics in this section

* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)

  Tile modes and values can be initialized when a dialog box is displayed or when an action is performed.
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)

  At callback time, you can check the value of a tile. If necessary, you can use
  set\_tile again to modify this value.
* [About Handling Radio Clusters (DCL)](About-Handling-Radio-Clusters-DCL.md)

  Radio buttons appear in radio clusters and allow the user to make a single choice from multiple options.
* [About Handling Sliders (DCL)](About-Handling-Sliders-DCL.md)

  When you handle actions and callbacks from sliders, your application should check the reason code that it receives along with
  the callback. This is not required, but it is a good idea because it can reduce processing.
* [About Handling Edit Boxes (DCL)](About-Handling-Edit-Boxes-DCL.md)

  Actions and callbacks to handle edit boxes allow you to get the current value and know when focus is lost.
* [About List Operations for List Boxes and Pop-Up Lists (DCL)](About-List-Operations-for-List-Boxes-and-Pop-Up-Lists-DCL.md)

  Lists in a dialog box require you to follow a specific sequence to populate them with items.
* [About Handling Image Buttons and Tiles (DCL)](About-Handling-Image-Buttons-and-Tiles-DCL.md)

  You can handle an image button simply as a button—that is, you can use it to trigger a single action.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*