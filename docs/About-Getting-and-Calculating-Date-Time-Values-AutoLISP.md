# About Getting and Calculating Date\Time Values (AutoLISP)

The AutoCAD environment provides several system variables that can be used to get the current system date\time along with
date\time related information about the current drawing.

Getting the current system date\time can be helpful when populating a date field in a title block, while calculating elapsed
time can be beneficial when you want to let a user know how long a process took to complete or provide a basic return on investment
(ROI) analysis for a custom program. Date\time values in the AutoCAD environment are stored as real numbers, and those values
represent dates\times in two different formats; Gregorian Calendar and Modified Julian Date. The integer part of the real
number (what is to the left of the decimal) represents a date, while the fraction part of the real number (what is to the
right of the decimal) represents time.

For example, the following is an example of the current system date\time returned by the CDATE system variable:

```
20170306.15023500
```

20170306 = Date: 03/06/2017

15023500 = Time: 3:02:25:00 P.M.

NOTE:Starting with AutoCAD 2017-based products, all date\time related system variables are only accurate to the nearest second
with the exception of MILLISECS; whereas in previous releases time also included milliseconds. If you need to track time changes,
be warned that you will no longer see a change in time until one second has elapsed even though 0 to 999 milliseconds might
have passed. When needing to calculate differences in time smaller than one second, consider using the value returned by the
MILLISECS system variable.

## Date\Time Related System Variables

This section lists the system variables that are related to getting the current system date\time or date\time values associated
with the current drawing.

Current System
:   * CDATE - Stores the current date and time in coded decimal format.
    * DATE - Stores the current date and time in Modified Julian Date format.
    * MILLISECS - Stores the number of milliseconds that have elapsed since the system was started.

Associated with the Current Drawing
:   NOTE:Values returned by these system variables are in Modified Julian Date format.

    * TDCREATE - Stores the local time and date the drawing was created.
    * TDINDWG - Stores the total editing time, which is the total elapsed time between saves of the current drawing.
    * TDUCREATE - Stores the universal time and date that the drawing was created.
    * TDUPDATE - Stores the local time and date of the last update/save.
    * TDUSRTIMER - Stores the user-elapsed timer.
    * TDUUPDATE - Stores the universal time and date of the last update or save.

## Display the Full Value of a Date\Time Related System Variable

When using the
GETVAR function to obtain the value of a system variable that stores a real number, the value when output to the Command prompt
is displayed in scientific notation. While scientific notation makes it easier for the AutoCAD program to present large decimal
numbers, it doesn't make it easier to read or understand. The
RTOS function can be used to display all significant digits of a real number returned by the
GETVAR function.

```
Command: (getvar "cdate")
2.01703e+07

Command: (rtos (getvar "cdate") 2 6)
"20170306.175302"
```

NOTE:The third argument of the
RTOS function controls the precision in which the real number is returned. A value of 6 indicates that the real number should
be returned with six significant digits after the decimal place. Prior to AutoCAD 2017-based products, the value stored in
CDATE included milliseconds which were represented by the 7th and 8th significant digits after the decimal place.

## Format the Date\Time Value Returned by CDATE

The real number stored in CDATE represents the current system date and time in coded decimal format; converting that real
number to a string makes it much easier to extract specific digits. Using the
SUBSTR function, a portion of a string can be returned.

```
Command: (setq cdate_val (rtos (getvar "cdate") 2 6))
"20170306.175302"

Command: (substr cdate_val 1 4)
"2017"
```

The following breaks down the significance of each digit:

* 1-4: Year
* 5-6: Month
* 7-8: Day
* 10-11: Hours
* 12-13: Minutes
* 14-15: Seconds
* 16-17: Milliseconds (AutoCAD 2016-based products and earlier only)

The following sample code shows an example of a function that you might use to extract the different date and time parts of
the value returned by CDATE:

```
; Returns or outputs the current date and time
; bOutput = T - Output the string to the Command prompt
; bOutput = nil - Return a string in the MM/DD/YYYY  HH:MM:SS format
; Usage: (CurDate T)
; Usage: (CurDate nil)

(defun CurDate (bOuput / cdate_val YYYY M D HH MM SS)
  ; Get the current date/time
  (setq cdate_val (rtos (getvar "CDATE") 2 6))

  ; Break up the string into its separate date and time parts
  (setq YYYY (substr cdate_val 1 4)
        M    (substr cdate_val 5 2)
        D    (substr cdate_val 7 2)
        HH   (substr cdate_val 10 2)
        MM   (substr cdate_val 12 2)
        SS   (substr cdate_val 14 2)
  )

  ; Output the current date and time to the Command
  ; prompt or return the formatted output as a string
  (if bOuput
    (progn
      (prompt (strcat "\
Date: " M "/" D "/" YYYY
                      "\
Time: " HH ":" MM ":" SS
              )
      )
      (princ)
    )
    (strcat M "/" D "/" YYYY "  " HH ":" MM ":" SS)
  )
)
```

The output or return value of the
CurDate function will look similar to the following:

```
(CurDate T)
Date: 02/14/2017
Time: 14:38:57

(CurDate nil)
"02/14/2017  14:39:04"
```

## Format Modified Julian Date Values

All other date\time related system variables store time in the Modified Julian Date format with the exceptions of CDATE and
MILLISECS. The date part of the Modified Julian Date format is the integer part of the number (what is to the left of the
decimal) and it represents the number of days since Noon on January 1, 4713 BC, while time is the decimal fraction part of
the number (what is to the right of the decimal) and it represents the time that has elapsed since Midnight which can be calculated
by multiplying the decimal fraction by 86,400.

The calculations required to convert a value in Modified Julian Date format to something more meaningful can be complex, but
there are five date\time related AutoLISP functions in the Express Tools that can be helpful. The date\time related functions
are only available after the
*Julian.lsp* file has been loaded into the AutoCAD environment, which can be done by using the DATE command or AutoLISP
LOAD function.

These are the date\time related AutoLISP functions that are available after the
*Julian.lsp* file is loaded:

* CTOJ - Converts calendar date and time to Julian date
* DTOJ - Converts AutoCAD calendar date/time to Julian date
* JTOC - Converts Julian date to calendar date list
* JTOD - Converts Julian date to AutoCAD calendar date/time
* JTOW - Determines day of the week for a given Julian day

The following are examples of the
JTOC and
JTOD functions:

```
Command: (jtoc (getvar "date"))
(2017 2 22 9 21 27.0)

Command: (rtos (jtod (getvar "date")) 2 6)
"20170222.092127"
```

## Calculate Elapsed Time

The calculation of elapsed time can be accomplished by subtracting two different date and time, or just time only values.
Based on the precision needed, you can use the value stored in the CDATE or MILLISECS system variables. For very small changes
in time, fractions of a second, the value stored in the MILLISECS system variable would be best.

```
Command: (setq start (getvar "MILLISECS"))
25494432

Command: (setq end (getvar "MILLISECS"))
25499471

Command: (- end start)
5039
```

The following sample code shows an example of a function that can be used to get the difference between two values that represent
different start and end times in milliseconds:

```
; Takes two values that represent milliseconds and returns
; the difference as an integer/long or double/float
;
; bMilliseconds = T   - Return value as milliseconds
; bMilliseconds = nil - Return value as seconds
;
; Usage: (TimeDiff T1 T2 T) - Milliseconds example
; Usage: (TimeDiff T1 T2 nil) - Seconds example

(defun TimeDiff (nStart nEnd bReturnMilliseconds / nDiff)

  ; Get the time difference
  (if (> nStart nEnd)
    (setq nDiff (- nStart nEnd))
    (setq nDiff (- nEnd nStart))
  )

  ; Return the time difference in milliseconds or seconds
  (if (= bReturnMilliseconds nil)
    (/ nDiff 1000.0)
    nDiff
  )
)
```

The return value of the
TimeDiff function might look similar to the following:

```
(setq T1 24092498)
(setq T2 24188267)
(TimeDiff T1 T2 T)
95769

(TimeDiff T1 T2 nil)
95.769
```

#### Related Concepts

* [About Using AutoLISP to Communicate With AutoCAD (AutoLISP)](About-Using-AutoLISP-to-Communicate-With-AutoCAD-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)
* [About Device Access and Control (AutoLISP)](About-Device-Access-and-Control-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*