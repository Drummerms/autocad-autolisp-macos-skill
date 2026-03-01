# To Create a Script that Changes Settings in a Drawing

This script turns on the grid, sets the global linetype scale factor to 3.0, and sets layer 0 as the current layer with red
as the layer's color.

1. Launch a text editor that saves in ASCII format (for example, Notepad on Windows or TextEdit on Mac OS).
2. In the text editor, enter *grid on*.
3. On the next line, enter *ltscale 3.0*.
4. On the next line, enter *layer set 0 color red 0*.
5. Add a blank line.
6. Save the file in the ASCII text format (TXT file), with a file extension of .*scr*.

   The script file may contain comments, as follows:

```
; Turn grid on
grid on
; Set scale for linetypes
ltscale 3.0
; Set current layer and its color
layer set 0 color red 0

; Blank line above to end the LAYER command
```

#### Related Concepts

* [About Command Scripts](About-Command-Scripts.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*