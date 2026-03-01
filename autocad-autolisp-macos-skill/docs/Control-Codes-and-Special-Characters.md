# Control Codes and Special Characters

Unicode characters can be used to enter special characters, overscore and underscore text, or insert a special symbol by including
control information in the text string.

## Summary

Use a pair of percent signs to introduce each control sequence.

You can use this control code with standard AutoCAD 2026 text fonts and Adobe PostScript fonts.

## List of Options

The following options are displayed.

*%%* *nnn*
:   Draws character number *nnn*.

    You can use these control codes with standard AutoCAD 2026 text fonts only:

*%%o*
:   Toggles overscoring on and off.

    ![](../images/GUID-4572C1C1-FE42-40B6-A1D1-5202E8B5591A-low.png)

*%%u*
:   Toggles underscoring on and off.

    ![](../images/GUID-4F556A99-03B7-4B00-9DD3-A0E68E37D040-low.png)

*%%d*
:   Draws degrees symbol (°).

    ![](../images/GUID-BF45EEF3-4C74-4FEF-975F-2BA6FBA1D1EC-low.png)

*%%p*
:   Draws plus/minus tolerance symbol (±).

    ![](../images/GUID-5D8E8FEF-4BC6-4D2B-A6E0-31E054FC0E91-low.png)

*%%c*
:   Draws circle diameter dimensioning symbol (ý).

    ![](../images/GUID-B8F5A385-D761-4EC2-9682-9B1FB3E0C5C5-low.png)

*%%%*
:   Draws a single percent sign (%). This is valid for the TEXT command only.

    ![](../images/GUID-A02F1A88-C141-4A38-AA19-635ABC5F607F-low.png)

    Overscoring and underscoring can be in effect at the same time. Both turn off automatically at the end of the text string.

    ![](../images/GUID-FFDE7475-342E-4828-84A2-B14AAA8E2AF4-low.png)

    You can use the %%*nnn* control sequence to display special characters using the PostScript fonts.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*