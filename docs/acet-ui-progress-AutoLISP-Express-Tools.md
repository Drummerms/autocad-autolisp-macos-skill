# acet-ui-progress (AutoLISP/Express Tools)

Displays a progress meter.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-ui-progress [label [max]])
(acet-ui-progress current)
(acet-ui-progress)
```

label
:   *Type:* String

    If provided, a text string that will appear as a label for the progress meter.

max
:   *Type:* Integer

    If provided, the maximum value in the range to be displayed (starting with 0).

current
:   *Type:* Integer

    If provided, gives the current value, which should be less than max; positive values are absolute while negative values increment
    the current position.

NOTE:If no arguments are provided, the progress meter is removed.

## Return Values

*Type:* Integer,
T, or
nil

The return value depends on the action performed:

* *Initialize:* Returns
  T if successful, otherwise
  nil
* *Update:* Returns the current progress as an integer
* *Restore:* Returns
  nil

## Example

```
;;  Initialize the meter
(acet-ui-progress "Working:" (length theList))

;;  Process each item
(foreach item theList
  ;;  Perform action
  (doSomethingTo item)

  ;;  Update the meter by one item
  (acet-ui-progress -1)
)

;;  Remove the meter
(acet-ui-progress)
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*