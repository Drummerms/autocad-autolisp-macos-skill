# REVERSE (Command)

Reverses the vertices of selected lines, polylines, splines, and helixes, which is useful for linetypes with included text,
or wide polylines with differing beginning and ending widths.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Reverse.
![](../images/GUID-F217A778-77E3-4CA8-A0C2-29429AA7B207-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

Vertices of selected objects are reversed.

For example, when a linetype with text is specified with relative rotation in a LIN file, the text in the linetype might be
displayed upside down. Reversing the vertices of the object changes the orientation of the text.

![](../images/GUID-0AF25E87-6F68-4DC3-839D-E877D0434395-low.png)

The REVERSE command does not change the orientation of text where rotation is specified as upright.

NOTE:Use the PLINEREVERSEWIDTHS system variable to control the direction of the polyline and appearance of polyline segments when
reversed.

#### Related Concepts

* [About Text in Custom Linetypes](About-Text-in-Custom-Linetypes.md)
* [About Polylines](About-Polylines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*