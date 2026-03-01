# Switch Between Dialog Boxes and the Command Line

You can display prompts on the command line instead of using a dialog box, or switch back again. This option is useful primarily
when using scripts.

Some functions are available both in the Command Line and in a dialog box. In many cases, you can enter a hyphen before a
command to suppress the dialog box and display prompts in the Command Line instead.

For example, entering *layer* on the command line displays the Layers palette. Entering *-layer* on the command line displays the equivalent Command Line options.

Suppressing a dialog box is useful for familiar operation with earlier versions of the program, and for using script files.
There may be slight differences between the options in the dialog box and those available in the Command Line.

These system variables also affect the display of dialog boxes:

* ATTDIA controls whether the INSERT command uses a dialog box for entering block attribute values.
* EXPERT controls whether certain warning dialog boxes are displayed.
* FILEDIA controls the display of dialog boxes used with commands that read and write files. For example, if FILEDIA is set
  to 1, SAVEAS displays the Save Drawing As dialog box. If FILEDIA is set to 0, SAVEAS displays prompts on the command line.
  The procedures in this documentation assume that FILEDIA is set to 1. Even when FILEDIA is set to 0, you can display a file
  dialog box by entering a tilde (~) at the first prompt.

FILEDIA and EXPERT are useful when you use scripts to run commands.

#### Related Tasks

* [To Work With Entering Commands](To-Work-With-Entering-Commands.md)
* [To Work With Entering System Variables](To-Work-With-Entering-System-Variables.md)
* [To Use the Command Line Version of a Command](To-Use-the-Command-Line-Version-of-a-Command.md)

#### Related Concepts

* [About Navigating and Editing in the Command Window](About-Navigating-and-Editing-in-the-Command-Window.md)

#### Related Information

* [About Entering Commands on the Command Line](About-Entering-Commands-on-the-Command-Line.md)
* [Enter System Variables on the Command Line](Enter-System-Variables-on-the-Command-Line.md)
* [To Work With the Command Window](To-Work-With-the-Command-Window.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*