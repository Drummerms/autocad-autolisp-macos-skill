# DATE (System Variable)

Stores the current date and time in Modified Julian Date format.

(Read-only)

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Not-saved |
| Initial value: | Varies |

This value is represented as a Modified Julian Date (MJD), which is the Julian day number and decimal fraction of a day in
the format:

<Julian day number>.<Decimal fraction of a day>

The Modified Julian Date, conventionally called UT1, is a worldwide scientific standard that assigns day numbers beginning
at an essentially arbitrary date and time of 12:00 a.m. on 1 January 4713 B.C. (B.C.E.). With this system, 4 July 1997 at
2:29:58 p.m. corresponds to 2450634.60387736, and 1 January 1998 at 12:00 noon corresponds to 2450815.50000000.

You can compute differences in date and time by subtracting the numbers returned by DATE. To extract the seconds since midnight
from the value returned by DATE, use AutoLISP expressions:

```
(setq s (getvar "DATE"))
(setq seconds (* 86400.0 (- s (fix s))))
```

Because your computer clock provides the date and time, the DATE system variable returns a true Julian date only if the system
clock is set to UTC/Zulu (Greenwich Mean Time). [TDCREATE](TDCREATE-System-Variable.md) and [TDUPDATE](TDUPDATE-System-Variable.md) have the same format as DATE, but their values represent the creation time and last update time of the current drawing.

#### Related Concepts

* [Get Information from Drawings](Get-Information-from-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*