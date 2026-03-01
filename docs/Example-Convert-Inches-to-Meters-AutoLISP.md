# Example: Convert Inches to Meters (AutoLISP)

This example demonstrates how a user-specified distance in inches can be converted to meters with the cvunit function.

```
(defun C:I2M ( / eng_len metric_len eng metric)
  (princ "\
Converting inches to meters. ")
  (setq eng_len
  (getdist "\
Enter a distance in inches: "))
  (setq metric_len (cvunit eng_len "inches" "meters"))
  (setq eng (rtos eng_len 2 4)
           metric (rtos metric_len 2 4))
  (princ
    (strcat "\
\t" eng " inches = " metric " meters."))
 (princ)
)
```

#### Related Concepts

* [About Unit Conversion (AutoLISP)](About-Unit-Conversion-AutoLISP.md)
* [Unit Definition File Reference (AutoLISP)](Unit-Definition-File-Reference-AutoLISP.md)
* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*