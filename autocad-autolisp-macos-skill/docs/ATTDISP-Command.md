# ATTDISP (Command)

Controls the visibility overrides for all block attributes in a drawing.

## Access Methods

*Menu*:
View ![](../images/ac.menuaro.gif) Attribute Display.

*'attdisp* for transparent use

## Summary

![](../images/GUID-D2B0D0CD-5DBF-4FD3-9203-998310D4B8B6-low.png)

![](../images/GUID-420BDEAB-88B0-4C92-97D5-14512AC7F6B5-low.png)

The drawing is regenerated after you change the visibility settings unless
[REGENAUTO](REGENAUTO-Command.md), which controls automatic regeneration, is off. The current visibility of attributes is stored in the
[ATTMODE](ATTMODE-System-Variable.md) system variable.

## List of Prompts

The following prompts are displayed.

Enter attribute visibility setting [[Normal](ATTDISP-Command.md)/[ON](ATTDISP-Command.md)/[OFF](ATTDISP-Command.md)] <*current*>:

Normal
:   Restores the visibility settings of each attribute. Visible attributes are displayed. Invisible attributes are not displayed.

On
:   Makes all attributes visible, overriding the original visibility settings.

Off
:   Makes all attributes invisible, overriding the original visibility settings.

#### Related References

* [-ATTDEF (Command)](ATTDEF-Command-2.md)
* [ATTDEF (Command)](ATTDEF-Command.md)
* [AFLAGS (System Variable)](AFLAGS-System-Variable.md)
* [TEXT (Command)](TEXT-Command.md)
* [MTEXT (Command)](MTEXT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*