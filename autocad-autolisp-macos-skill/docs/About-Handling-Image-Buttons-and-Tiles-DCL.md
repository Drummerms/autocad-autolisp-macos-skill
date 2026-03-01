# About Handling Image Buttons and Tiles (DCL)

You can handle an image button simply as a button—that is, you can use it to trigger a single action.

However, you can also use the PDB feature to define regions of the button. With regions defined, the action taken depends
on the part of the image button the user selects. The mechanism for this is straightforward: an image button's action or callback
returns the (*X*,*Y*) location that the user selected. The coordinates are within the range of the particular image button tile (as returned by
the dimension functions). Your application must assign a meaning to select locations by implicitly defining regions of the
image. The Viewpoint Presets dialog box makes good use of this feature. You can view this by running the AutoCAD VPOINT command.

In the following example, your image button has two color swatches created by
fill\_image. You want to select either one or the other, depending on which region the user selects. If the image button is divided horizontally
(dark above and light below), your action needs to test only the one dimension:

```
(action_tile "image_sel" "(pick_shade $key $value $y)")
...
(defun pick_shade (key val y)
  (setq threshold (/ ( dimy_tile key) 2)) ;Image is divided horizontally.
  (if (> y threshold)                     ;Remember that the origin is at
    (setq result "Light")                 ;upper left.
    (setq result "Dark")
  )
)
```

#### Topics in this section

* [About Creating Images (DCL)](About-Creating-Images-DCL.md)

  The calling sequence to create images for image tiles and image buttons is similar to the list-handling sequence.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [image\_button Tile (DCL)](image_button-Tile-DCL.md)
* [image Tile (DCL)](image-Tile-DCL.md)
* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*