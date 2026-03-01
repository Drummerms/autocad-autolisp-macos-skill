# Loft Settings Dialog Box

Controls the contour of a lofted surface at its cross sections. Also allows you to close the surface or solid.

LOFT (Command)

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling drop-down ![](../images/ac.menuaro.gif) Loft
![](../images/GUID-E0E3CB70-083C-41D2-BEE5-8613DB266A8E-low.png) : Specify the settings option at the prompt

NOTE:The settings option is available after object selection.

![](../images/GUID-9308F071-3863-4E87-ACF8-EBFCD4F4C63F-low.png)

## List of Options

The following options are displayed.

Ruled

Specifies that the solid or surface is ruled (straight) between the cross sections and has sharp edges at the cross sections.
(LOFTNORMALS system variable)

![](../images/GUID-74FBD07C-2B65-4C95-AFDA-B527EBE28256-low.png)

Smooth Fit

Specifies that a smooth solid or surface is drawn between the cross sections and has sharp edges at the start and end cross
sections. (LOFTNORMALS system variable)

![](../images/GUID-9A56D636-32E9-41AF-8690-52D099DFA7A0-low.png)

Start Continuity
:   Sets the tangency and curvature of the first cross section.

Start Bulge Magnitude
:   Sets the size of the curve of the first cross section.

End Continuity
:   Sets the tangency and curvature of the last cross section.

End Bulge Magnitude
:   Sets the size of the curve of the last cross section.

Normal To

Controls the surface normal of the solid or surface where it passes through the cross sections. (LOFTNORMALS system variable)

Start Cross Section
:   Specifies that the surface normal is normal to the start cross section.

End Cross Section
:   Specifies that the surface normal is normal to the end cross section.

Start and End Cross Sections
:   Specifies that the surface normal is normal to both the start and end cross sections.

All Cross Sections
:   Specifies that the surface normal is normal to all cross sections.

Draft Angles

Controls the draft angle and magnitude of the first and last cross sections of the lofted solid or surface. The draft angle
is the beginning direction of the surface. 0 is defined as outward from the plane of the curve. (LOFTNORMALS system variable)

![](../images/GUID-D134DD14-C12A-470A-9BE2-72A8C31B37B8-low.png)

The following illustration shows the affect of using a different draft angle for the first and last cross sections of a lofted
solid. The first cross section is assigned a draft angle of 45 degrees, while the last cross section is assigned a draft angle
of 135 degrees.

![](../images/GUID-3C23BF1D-F7F0-433F-A8C1-31096D1D125B-low.png)

You can also use the draft angle handle to adjust the draft angle (triangular grip) and magnitude (circular grip).

![](../images/GUID-EE734BFD-CD98-4185-822C-27DAA0543C93-low.png)

Start Angle
:   Specifies the draft angle for the start cross section. (LOFTANG1 system variable)

Start Magnitude
:   Controls the relative distance of the surface from the start cross section in the direction of the draft angle before the
    surface starts to bend toward the next cross section. (LOFTMAG1 system variable)

End Angle
:   Specifies the draft angle for the end cross section. (LOFTANG2 system variable)

End Magnitude
:   Controls the relative distance of the surface from the end cross section in the direction of the draft angle before the surface
    starts to bend toward the previous cross section. (LOFTMAG2 system variable)

Close Surface or Solid

Closes and opens a surface or solid. When using this option, the cross sections should form a torus-shaped pattern so that
the lofted surface or solid can form a closed tube. (LOFTPARAM system variable)

![](../images/GUID-574ACF0C-F9CB-4A39-B0ED-4842E4976CDF-low.png)

Periodic (Smooth Ends)

Creates a smooth, closed surface whose seam will not kink if it is reshaped. This option is only available if the loft is
ruled or smooth fit and the Close Surface or solid option is selected.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*