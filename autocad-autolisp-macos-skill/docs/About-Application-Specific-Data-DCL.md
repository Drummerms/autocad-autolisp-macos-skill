# About Application-Specific Data (DCL)

The
client\_data\_tile function assigns application-specific data to a tile.

The application-specific data for a tile is available at callback time as the
$data variable and returned as a string. Client data is not represented in a DCL file and is valid only while your application
is running. Using client data is comparable to using user-defined attributes. The main difference is that user-defined attributes
are read-only, while client data can change at runtime. Also, end-users can inspect user-defined attributes in the application's
DCL file, but client data is invisible to them.

Because your program must maintain the list displayed by a list box (or pop-up list), client data is good for handling this
information. The following modification to the
MK\_LIST function makes the list an argument:

```
(defun MK_LIST (readlist displist / )
```

This code eliminates the need for a global list variable. The following calls in the main part of the dialog box handler associate
a short list with the tile by calling
client\_data\_tile, and then pass that list to
MK\_LIST by means of an action expression as follows:

```
(client_data_tile
  "colorsyslist"
  "Red-Green-Blue Cyan-Magenta-Yellow Hue-Saturation-Value"
)
(action_tile
  "colorsyslist"
  "(setq usrchoice (mk_list $value $data))"
)
```

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Action Expressions (DCL)](About-Action-Expressions-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Callback Reasons (DCL)](About-Callback-Reasons-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Application-Specific Data-Handling Function Reference (AutoLISP/DCL)](Application-Specific-Data-Handling-Function-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*