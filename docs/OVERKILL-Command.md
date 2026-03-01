# -OVERKILL (Command)

Removes duplicate or overlapping lines, arcs, and polylines. Also, combines partially overlapping or contiguous ones.

## List of Prompts

The following prompts are displayed.

Select objects: *Use an object selection method*

Enter an option to change [[Ignore](OVERKILL-Command.md)/[tOlerance](OVERKILL-Command.md)/[optimize Plines](OVERKILL-Command.md)/[combine parTial overlap](OVERKILL-Command.md)/[combine Endtoend](OVERKILL-Command.md)/[Associativity](OVERKILL-Command.md)] <done>:

## List of Options

Ignore
:   Ignores one or more of the following properties during object comparison

    * None
    * All
    * Color
    * LAyer
    * Ltype
    * Ltscale
    * LWeight
    * Thickness
    * TRansparency
    * plotStyle
    * Material

Tolerance
:   Defines the value within which OVERKILL makes numeric comparisons for determining object duplication.

Optimize Polylines
:   Optimize segments within plines [segment wiDth/Break polyline/Yes/No] <Yes>:

    * *Segment Width*: ignore polyline segment width
    * *Break Polyline*: maintains polylines when optimizing polyline segments
    * *Yes*: Enabled by default. Honors polylines as discreet objects and deletes non-polyline objects that overlap polylines.
    * *No*: Forces OVERKILL to examine polyline segments individually. Polyline segments may be deleted as duplicates of non-polyline
      objects.

Combine Partial Overlap
:   Overlapping objects area combined into single objects.

Combine End to End
:   Objects that have common endpoints are combined into single objects.

Associativity
:   Associative objects are not deleted or modified.

#### Related References

* [OVERKILL (Command)](OVERKILL-Command-2.md)

#### Related Concepts

* [Delete Duplicate Objects Dialog Box](Delete-Duplicate-Objects-Dialog-Box.md)
* [About Correcting Mistakes](About-Correcting-Mistakes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*