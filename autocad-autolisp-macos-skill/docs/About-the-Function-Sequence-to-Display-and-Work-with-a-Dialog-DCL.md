# About the Function Sequence to Display and Work with a Dialog (DCL)

Setting up a DCL dialog box requires the use of several AutoLISP functions that need to be called in a specific order.

The following outlines the typical sequence that needs to be followed to display and use a DCL dialog box:

1. Load the DCL file with a
   load\_dialog call.
2. Call
   new\_dialog to display a particular dialog box.

   Be sure to check the value returned by
   new\_dialog. Calling
   start\_dialog when the
   new\_dialog call has failed can have unpredictable results.
3. Initialize the dialog box by setting up tile values, lists, and images. Initialize also when you call
   action\_tile to set up action expressions or callback functions. Other functions typically called at this time are
   set\_tile and
   mode\_tile for general tile values and states,
   start\_list,
   add\_list, and
   end\_list for list boxes, and the dimension functions with
   start\_image,
   vector\_image,
   fill\_image,
   slide\_image, and
   end\_image for images. At this time you can also call
   client\_data\_tile to associate application-specific data with the dialog box and its components.
4. Call
   start\_dialog to turn control over to the dialog box, so that the user can enter input.
5. Process user input from within your actions (callbacks). Process input when you are most likely to use
   get\_tile,
   get\_attr,
   set\_tile, and
   mode\_tile. The user presses an exit button, causing an action to call
   done\_dialog, which causes
   start\_dialog to return a value. At this point, unload the DCL file by calling
   unload\_dialog.

   This scheme handles only one dialog box and one DCL file at a time. Applications usually have multiple dialog boxes. The easiest
   and quickest way to handle these dialog boxes is to save all of them in a single DCL file. The
   load\_dialog call then loads all dialog boxes at once, and you can call
   new\_dialog for any dialog box. If memory is limited, however, you may need to create multiple DCL files and use
   unload\_dialog to remove one set of dialog boxes from memory before you load another set.

   NOTE:DCL on Mac OS uses more memory than on Windows, unload DCL file definitions that are not needed to avoid running low on memory.

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Displaying Nested Dialog Boxes (DCL)](About-Displaying-Nested-Dialog-Boxes-DCL.md)
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)
* [About Functions Restricted When a Dialog Box is Open (DCL)](About-Functions-Restricted-When-a-Dialog-Box-is-Open-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*