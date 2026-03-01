# AUDIT (Command)

Evaluates the integrity of a drawing and corrects some errors.

## Summary

For easy access, AUDIT places all objects for which it reports errors in the Previous selection set. However, editing commands
affect only the objects that belong to the current paper space or model space.

If you set the
[AUDITCTL](AUDITCTL-System-Variable.md) system variable to 1, AUDIT creates a text file describing problems and the action taken and places this report in the same
folder as the current drawing, with the file extension .*adt*.

If a drawing contains errors that AUDIT cannot fix, use
[RECOVER](RECOVER-Command.md) to retrieve the drawing and correct its errors.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*