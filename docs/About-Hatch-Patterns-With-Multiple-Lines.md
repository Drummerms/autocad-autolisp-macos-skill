# About Hatch Patterns With Multiple Lines

Complex hatch patterns can contain multiple definition lines and can have an origin that passes through offsets from the origin.

Not all hatch patterns use origin points of 0,0. In composing more complex patterns, you need to carefully specify the following
of each line family to form the hatch pattern correctly:

* Starting point
* Offsets
* Dash-length, dot, and gap patterns

Hatch patterns defined using multiple definition lines describe the length and angle in which each line segment is to be drawn.
The following shows the definition lines that describe the AR-B816 hatch pattern:

```
*AR-B816, 8x16 Block elevation stretcher bond
0, 0,0, 0,8
90, 0,0, 8,8, 8,-8
```

An area hatched with this pattern would look like this:

![](../images/GUID-866734B3-16E5-4F21-838E-A21525305C9F-low.png)

## Example: Inverted-U Pattern

An inverted-U (one line up, one over, and one down) is a pattern that repeats every one unit, and is made up of line segments
that are 0.5 units in length followed by a gap of 0.5 units wide.

An area hatched with this pattern would look like this:

![](../images/GUID-2F86D925-A2B1-4E0B-9CBC-B3E05A1A45E4-low.png)

This pattern would be defined as follows:

```
*IUS, Inverted U's
90, 0,0, 0,1, .5,-.5
0, 0,.5, 0,1, .5,-.5
270, .5,.5, 0,1, .5,-.5
```

The following provides a visual breakdown of how the pattern is drawn:

![](../images/GUID-76679117-C1B3-4206-9D07-7C2F423588F5-low.png)

* The first dash line represents the up bar which starts at the 0,0 origin and is drawn at 90 degrees.
* The second dash line represents the horizontal bar which starts at the 0,0.5 origin and is drawn at 0 degrees.
* The third dash line represents the down bar which starts at the 0.5,0.5 origin and is drawn at 270 degrees. The third line
  of the pattern could have also been entered as the following:

  ```
  90, .5,0, 0,1, .5,-.5
  ```

  or

  ```
  270, .5,1, 0,1, -.5,.5
  ```

## Example: Six-Pointed Star

A six-pointed star pattern can be created with three dashed lines that start at the origin point and continue along the vector
direction specified by the angle specification.

An area hatched with this pattern would look like this:

![](../images/GUID-F8E03A48-9620-4093-9513-757CCFC5C37D-low.png)

This pattern would be defined as follows:

```
*STARS, Six-pointed star
0, 0,0, 0,.866, .5,-.5
60, 0,0, 0,.866, .5,-.5
120, .25,.433, 0,.866, .5,-.5
```

NOTE:0.866 is the sine of 60 degrees.

#### Topics in this section

* [To Create a Hatch Pattern with Multiple Lines](To-Create-a-Hatch-Pattern-with-Multiple-Lines.md)

#### Related Tasks

* [To Create a Hatch Pattern with Multiple Lines](To-Create-a-Hatch-Pattern-with-Multiple-Lines.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [FAQ: Why can't I use my custom hatch pattern (PAT) files?](FAQ-Why-can't-I-use-my-custom-hatch-pattern-PATfiles.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*