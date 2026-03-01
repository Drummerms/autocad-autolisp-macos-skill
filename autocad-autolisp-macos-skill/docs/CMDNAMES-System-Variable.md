# CMDNAMES (System Variable)

Displays the names of the active and transparent commands.

(Read-only)

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Not-saved |
| Initial value: | "" |

For example, LINE'ZOOM indicates that the ZOOM command is being used transparently during the LINE command.

This variable is designed for use with programming interfaces such as AutoLISP and DIESEL.

The following is a simple example that demonstrates how to use DIESEL to display the current command at the status line.

Command: modemacro

New value for MODEMACRO, or . for none <"">: $(getvar, cmdnames)

#### Related Concepts

* [Switch Between Dialog Boxes and the Command Line](Switch-Between-Dialog-Boxes-and-the-Command-Line.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*