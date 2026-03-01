# Special Handling of Date/Time Variables (DXF)

The CDATE and DATE system variables provide access to the current date and time. The TDCREATE, TDINDWG, TDUPDATE, and TDUSRTIMER
system variables (and the $TDCREATE, $TDUCREATE, $TDUPDATE, and $TDUUPDATE DXF header variables) provide access to times and
dates associated with the current drawing. The values are represented as real numbers with special meanings, as described
below.

DATE is the current date and time represented as a Julian date and fraction of a day in a real number.

<*Julian date*>.<*Fraction of day*>

For example, on December 31, 1999, at 9:58:35 p.m. GMT, the DATE variable contains

2451544.91568287

The date and time are taken from the computer's clock when the variable is read. The time is represented as a fraction of
a day, and the times returned by DATE may be truly subtracted to compute differences in time. To extract the seconds since
midnight from the value returned by DATE, use the AutoLISP expressions

```
(setq s (getvar "DATE"))
(setq seconds (* 86400.0 (- s (fix s))))
```

Note that DATE returns only a true Julian date if the system's clock is set to UTC/Zulu (Greenwich Mean Time). TDCREATE and
TDUPDATE have the same format as DATE, but their values represent the creation time and last update time of the current drawing.

TDINDWG and TDUSRTIMER (and the $TDINDWG and $TDUSRTIMER DXF header variables) use a format similar to that of DATE, but their
values represent elapsed times, as in

<*Number of days*>.<*Fraction of day*>

CDATE is the current date and time in calendar and clock format. The value is returned as a real number in the form

YYYYMMDD.HHMMSShsec

where

YYYY = year

MM = month (01-12)

DD = day (01-31)

HH = hour (00-23)

MM = minute (00-59)

SS = second (00-59)

hsec = hundredths of a second (00-99)

For example, if the current date is December 31, 2005, and the time is 9:58:35.75 p.m., CDATE would return the value:

20051231.21583575

Note that CDATE values can be compared for later and earlier values but that subtracting them yields numbers that are not
meaningful.

#### Related References

* [About the DXF HEADER Section](About-the-DXF-HEADER-Section.md)
* [HEADER Section Group Codes (DXF)](HEADER-Section-Group-Codes-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*