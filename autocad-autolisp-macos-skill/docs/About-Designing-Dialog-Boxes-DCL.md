# About Designing Dialog Boxes (DCL)

With the dialog control language (DCL), you can create dialog boxes for use with AutoLISP programs.

Dialog boxes are defined by ASCII files written in
*dialog control language* (DCL), and require some planning to ensure they look and behavior similar to other dialog boxes used by the operating system
and AutoCAD. The tiles or controls you choose to use and their layout in a dialog box should make be fluid and intuitive.

Consider the following guidelines when creating your dialog boxes:

* A dialog box should never appear to be cluttered, it makes for an ineffective and hard to use design. Take advantage of white
  space to spread controls out from each other.
* Individuals often scan a dialog box from upper-left to lower-right, so placing the most commonly used tiles in these areas
  makes for a more effective design.
* Arrange sections of the dialog box logically into rows or columns so users can scan them from left to right or from top to
  bottom.
* Align related entry fields (such as edit boxes or list boxes) both vertically and horizontally, so that when users switch
  fields by pressing Tab, the cursor moves in a straight, orthogonal line.
* If there is a natural order for entering data—such as the
  *X*,
  *Y*, and
  *Z* of coordinates—order the fields in the same way. Align boxed areas both vertically and horizontally. Do not leave a lot of
  white space around or between boxed areas. Extend their width to the right, if necessary.
* Nesting dialog boxes can be helpful in hiding less commonly used options from the user, but avoid going too many nesting levels
  deep. When a nested dialog box is called, the user should return to the calling dialog box.
* The dialog boxes of an application should be internally consistent, and consistent with related applications. A familiar dialog
  box is easier to understand if its design is consistent with other dialog boxes in the application, related applications,
  or the host system.
* Use standard definitions for dialog box controls. This reduces your work, contributes to consistency, and makes it easier
  for users to learn and use your dialog boxes.
* Provide reasonable defaults for all entries and options. Well-chosen defaults can help users complete a dialog box quickly
  and easily. It is recommended that you update the default values—in other words, that you save the user's previous settings
  and use them as the new defaults—each time the dialog box is used.
* You should provide a Help facility. It is recommended that the main dialog box of your application have a Help button that
  displays a basic topic file that describes how to use the options of the dialog box. In most cases, the Help button should
  call the Help facility using the
  help function.

#### Topics in this section

* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)

  A dialog box consists of the box and the components within it.
* [About Using DCL to Define Dialog Boxes (DCL)](About-Using-DCL-to-Define-Dialog-Boxes-DCL.md)
* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)

  By default, tiles automatically resize to fit almost the full width of a dialog box.
* [About Dialog Box Design Guidelines (DCL)](About-Dialog-Box-Design-Guidelines-DCL.md)

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [About Adjusting the Layout of Dialog Boxes (DCL)](About-Adjusting-the-Layout-of-Dialog-Boxes-DCL.md)
* [About Size and Placement of a Dialog (DCL)](About-Size-and-Placement-of-a-Dialog-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Error Handling in Dialog Boxes (DCL)](About-Error-Handling-in-Dialog-Boxes-DCL.md)
* [About Disabling Tiles (DCL)](About-Disabling-Tiles-DCL.md)
* [About Dialog Boxes Compared to Command Line Input (DCL)](About-Dialog-Boxes-Compared-to-Command-Line-Input-DCL.md)
* [About International Language Considerations (DCL)](About-International-Language-Considerations-DCL.md)
* [About Using Capitalization with Tiles (DCL)](About-Using-Capitalization-with-Tiles-DCL.md)
* [About Handling Keyboard Input (DCL)](About-Handling-Keyboard-Input-DCL.md)
* [About Users With Disabilities (DCL)](About-Users-With-Disabilities-DCL.md)
* [About Nested Dialog Boxes (DCL)](About-Nested-Dialog-Boxes-DCL.md)
* [About Referencing DCL Files (DCL)](About-Referencing-DCL-Files-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*