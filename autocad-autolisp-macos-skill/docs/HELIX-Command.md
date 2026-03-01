# HELIX (Command)

Creates a 2D spiral or 3D spring.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Helix.
![](../images/GUID-0242F2CF-6CD3-4C35-9C8B-C2D12D3F2998-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

*Menu*:
Draw ![](../images/ac.menuaro.gif) Helix.

Use a helix as a sweep path for the SWEEP command to create springs, threads, and circular stairways.

![](../images/GUID-4EF5F62D-9C7E-41A1-801D-81B8034F7E67-low.gif)

The following prompts are displayed.

Center point of base
:   Sets the center of the helix base point.

Base radius
:   Specifies the radius of the base of the helix.

    Initially, the default base radius is set to 1. During a drawing session, the default value for the base radius is always
    the previously entered base radius value for any solid primitive or helix.

Diameter (base)
:   Specifies the diameter of the base of the helix.

    Initially, the default base diameter is set to 2. During a drawing session, the default value for the base diameter is always
    the previously entered base diameter value.

Top radius
:   Specifies the radius of the top of the helix. the default value is always the value for the base radius.

    The base radius and the top radius cannot both be set to 0 (zero).

Diameter (top)
:   Uses a diameter value to set the size of the helix top. The default value for the top diameter is always the value of the
    base diameter.

Helix height
:   Sets the height of the helix.

Axis endpoint
:   Specifies the endpoint location for the helix axis. The axis endpoint can be located anywhere in 3D space. The axis endpoint
    defines the length and orientation of the helix.

Turns
:   Specifies the number of turns (revolutions) for the helix. The number of turns for a helix cannot exceed 500.

    Initially, the default value for the number of turns is three. During a drawing session, the default value for the number
    of turns is always the previously entered number of turns value.

Turn height
:   Specifies the height of one complete turn within the helix.

    The number of turns in the helix will automatically update accordingly when a turn height value is specified. If the number
    of turns for the helix has been specified, you cannot enter a value for the turn height.

Twist
:   Specifies the direction in which the helix is twisted.

    * *CW.* Draws the helix in a clockwise direction.
    * *CCW.* Draws the helix in a counterclockwise direction.

#### Related Concepts

* [About Helixes](About-Helixes.md)
* [About Modifying Helixes](About-Modifying-Helixes.md)

#### Related Information

* [About Curved Objects](About-Curved-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*