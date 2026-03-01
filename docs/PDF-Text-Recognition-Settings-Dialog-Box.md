# PDF Text Recognition Settings Dialog Box

Sets the options for converting the SHX geometry imported from PDF files into individual multiline text objects.

PDFSHXTEXT (Command)

*Tool Sets:*Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Recognition Settings.
![](../images/GUID-3F1648D6-ACDB-4022-9A3D-B8C25954BD66-low.png)

![](../images/GUID-C5B8972D-22C7-4E99-890A-686668CDC8AE-low.png)

## List of Options

The following options are available.

SHX Fonts to Compare
:   * *Use first matching font*. The selected fonts are compared to the selected SHX geometry for a match starting from the top of the list until the specified
      conversion setting percentage is met or exceeded.
    * *Use best matching font*. All selected fonts are compared, and the best match, rather than the first match that exceeds the conversion setting percentage,
      is used.

    Displays a list of SHX fonts from which you can choose the ones most likely to match the selected SHX geometry. The order
    of the selected SHX fonts matters. Drag to move a selected font up or down the list. Unchecked fonts are ignored. Note the
    following points:

    * The letter spacing between characters, called kerning, might be different between similar fonts such as simplex and romans.
    * The punctuation and special characters between similar fonts might be different.
    * Asian-language big fonts are not supported.

Add ![](../images/GUID-9174311E-7DC8-49C8-B39F-991EC3DAD0E2-low.png)
:   Adds an SHX font to the comparison list.

Remove ![](../images/GUID-A140F0E8-0D4A-41B4-8078-48722E2E2CDB-low.png)
:   Removes an SHX font from the comparison list.

Font Preview
:   Displays the characters entered in the box at the top. Several SHX fonts are similar. This box provides a way for you to compare
    certain distinguishing characters in SHX fonts easily.

Conversion Settings
:   Sets the percentage of geometry that must match a font before replacing it with text. The percentage applies to each cluster
    of geometry analyzed during the conversion process. A low value creates text even when some characters aren't recognized.
    A high value ensures the closest matching selected font is used if possible.

Create Text On
:   Specifies the layer of the multiline text objects that are created by the conversion, either the current layer or the original
    layer of the geometry.

#### Related References

* [PDFSHXBESTFONT (System Variable)](PDFSHXBESTFONT-System-Variable.md)
* [PDFSHXLAYER (System Variable)](PDFSHXLAYER-System-Variable.md)
* [PDFSHXTHRESHOLD (System Variable)](PDFSHXTHRESHOLD-System-Variable.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*