# -XBIND (Command)

Binds one or more definitions of named objects in an xref to the current drawing.

## List of Prompts

The following prompts are displayed.

Enter symbol type to bind [Block/Dimstyle/LAyer/LType/Style]: *Enter an option*

Depending on the option, you are prompted for a xref-dependent named object (symbol) such as a block, dimension style, layer,
linetype, or text style.

Enter dependent *Symbol* name(s): *Enter a name list or* *\** *to bind all xref-dependent named objects (symbols) from that definition table*

The name you specify must be the full name, including the vertical bar character ( | ).

The xref-dependent named objects you specify are added to your drawing. You can manipulate them as you would any other named
object. The vertical bar character ( | ) from each xref-dependent named object is replaced with a number (usually 0) between
two dollar signs ($).

If you specify a layer whose associated linetype is not CONTINUOUS, XBIND also binds the referenced linetype. If you apply
XBIND to a block, any block, dimension style, layer, linetype, or text style that's referenced by objects in the block is
also bound. If the block contains an xref, XBIND binds that xref and all its dependent named objects.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*