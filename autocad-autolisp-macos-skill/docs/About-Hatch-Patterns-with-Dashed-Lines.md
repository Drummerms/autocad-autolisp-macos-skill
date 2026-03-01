# About Hatch Patterns with Dashed Lines

Hatch patterns can contain dashed-lines by adding dash-lengths to a hatch pattern definition line.

Each dash-length specifies the length of a segment making up a line. If a length is positive, a pen-down segment is drawn.
If a length is negative, the segment is pen-up and it is not drawn resulting in the creation of a space, also known as a
*gap*. The pattern starts at the origin point with the first segment and cycles through the segments in circular fashion. A dash
length of 0 draws a dot. You can specify up to six dash-lengths per definition line.

The standard hatch pattern ANSI33 looks like:

![](../images/GUID-68E74455-D653-4656-B7BA-E7BD5165C666-low.png)

and is defined as follows:

```
*ANSI33, ANSI Bronze, Brass, Copper
45, .176776695,0, 0,.25, .125,-.0625
```

For example, to create a pattern that draws dashed lines at 45-degrees with a dash-length of 0.5 units and a gap after each
dash of 0.5 units, the definition would look similar to

```
*DASH45, Dashed lines at 45 degrees
45, 0,0, 0,.5, .5,-.5
```

If you wanted to draw a 0.5-unit dash, a 0.25-unit gap, a dot, and a 0.25-unit gap before the next dash, the definition would
look similar to

```
*DDOT45,Dash-dot-dash pattern: 45 degrees
45, 0,0, 0,.5, .5,-.25, 0,-.25
```

## Offset Lines in a Hatch Pattern Definition

Lines of a hatch pattern can be offset using the
*delta-x* specification in a dashed-line family. The following example draws a family of lines separated by a gap of 0.5 units and
a
*delta-x* specification value of zero which results in each line lining up

```
*GOSTAK
0, 0,0, 0,.5, .5,-.5
```

An area hatched with this pattern would look like this:

![](../images/GUID-1B4F2268-A593-474D-A16A-39F9AE166F28-low.png)

The following example shows the previous hatch pattern definition with an offset along the
*X* axis

```
*SKEWED
0, 0,0, .5,.5, .5,-.5
```

The hatch pattern definition is similar, except the
*delta-x* specification is set to 0.5. This offsets each successive family member by 0.5 in the direction of the line (in this case,
parallel to the
*X* axis). Because the lines are infinite, the dash pattern slides down the specified amount. An area hatched with this pattern
would look like this:

![](../images/GUID-446282E2-DE51-40AD-B3A0-33677E3BF009-low.png)

#### Topics in this section

* [To Create a Hatch Pattern with Dashed Lines](To-Create-a-Hatch-Pattern-with-Dashed-Lines.md)

#### Related Tasks

* [To Create a Hatch Pattern with Dashed Lines](To-Create-a-Hatch-Pattern-with-Dashed-Lines.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [FAQ: Why can't I use my custom hatch pattern (PAT) files?](FAQ-Why-can't-I-use-my-custom-hatch-pattern-PATfiles.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*