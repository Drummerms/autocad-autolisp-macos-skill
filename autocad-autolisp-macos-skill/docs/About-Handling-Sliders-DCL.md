# About Handling Sliders (DCL)

When you handle actions and callbacks from sliders, your application should check the reason code that it receives along with
the callback. This is not required, but it is a good idea because it can reduce processing.

A callback occurs when an increment boundary on a slider is crossed. For example, if the slider is defined with a minimum
value of 0, a maximum value of 10, and both small and big increments of 1, a callback is issued 10 times as the user traverses
from one end of the slider to the other.

The following function shows the basic scheme of a function to handle a slider. It is called from an action expression associated
with the slider tile. The
slider\_info tile used by the function displays the slider's current value in decimal form. Often such a tile is an edit box as well,
which gives users the choice of either manipulating the slider or entering its value directly. If a user enters a value in
slider\_info, your edit box callback should update the value of the slider as follows:

```
(action_tile
  "myslider"
  "(slider_action $value $reason)"
)

(action_tile
  "slider_info"
  "(ebox_action $value $reason)"
)

.
.
.

(defun slider_action(val why)
  (if (or (= why 2) (= why 1))   ; Check reason code.
    (set_tile "slider_info" val) ; Show interim result.
  )
)

(defun ebox_action(val why)
  (if (or (= why 2) (= why 1))   ; Check reason code.
    (set_tile "myslider" val)    ; Show interim result.
  )
)
```

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [slider Tile (DCL)](slider-Tile-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*