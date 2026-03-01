# MVSETUP on the Model Layout

The Model layout is most useful for plotting multiple views of a drawing within a single border.

On the Model layout, you set the units type, drawing scale factor, and paper size at the Command prompt using MVSETUP. Using
the settings you provide, a rectangular border is drawn at the grid limits.

## List of Prompts

When the TILEMODE system variable is on (the default), the following prompt are displayed:

Enable paper space? [No/Yes] <Y>: *Enter* *n* *or press*Enter

Pressing Enter turns off TILEMODE and proceeds as described in MVSETUP on a Named Layout.

Entering
*n* displays the following prompt:

Enter units type [Scientific/Decimal/Engineering/Architectural/Metric]: *Enter an option*

A list of available units and prompts for the scale factor and paper size are displayed.

Enter the scale factor:
*Enter a value*

Enter the paper width:
*Enter a value*

Enter the paper height:
*Enter a value*

A bounding box is drawn and the command ends.

#### Related References

* [TILEMODE (System Variable)](TILEMODE-System-Variable.md)

#### Related Concepts

* [About Drawings and Templates](About-Drawings-and-Templates.md)
* [About Units of Measurement](About-Units-of-Measurement.md)

#### Related Information

* [MVSETUP on a Named Layout](MVSETUP-on-a-Named-Layout.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*