# About Adjusting the Spacing Between Dimensions

You can automatically adjust existing parallel linear and angular dimensions in a drawing so they are equally spaced or aligned
at the dimension line with each other.

The DIMBASELINE command uses the DIMDLI system variable to create equally spaced dimensions, but once the dimensions are placed,
changing the value of the system variable has no affect on the spacing of dimensions. If you change the text size or adjust
the scale for the dimensions, they remain in the original position which can cause problems with overlapping dimension lines
and text.

You can space linear and angular dimensions that overlap or are not equally spaced with the DIMSPACE command. The dimensions
that are selected must be linear or angular, of the same type (rotated or aligned), parallel or concentric to one another,
and on the extension lines of each other. You can also align linear and angular dimensions by using a spacing value of 0.

The following illustration shows parallel linear dimensions that are not equally spaced and then those that are equally spaced
after using the DIMSPACE command.

![](../images/GUID-F2B26F91-1ACB-4773-9981-62E7A02E4889-low.png)

#### Related Tasks

* [To Space Parallel Linear and Angular Dimensions Automatically](To-Space-Parallel-Linear-and-Angular-Dimensions-Automatically.md)
* [To Space Parallel Linear and Angular Dimensions at a Specified Distance](To-Space-Parallel-Linear-and-Angular-Dimensions-at-a-Specified-Distance.md)
* [To Align Parallel Linear and Angular Dimensions](To-Align-Parallel-Linear-and-Angular-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*