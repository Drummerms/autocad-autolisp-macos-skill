# vlax-tmatrix (AutoLISP/ActiveX)

Returns a suitable representation for a 4 x 4 transformation matrix to be used in VLA methods

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-tmatrix lst)
```

*lst*
:   *Type:* List

    A value of four lists, each containing four numbers, representing transformation matrix elements.

## Return Values

*Type:* Variant

A variant of type safearray, representing the 4×4 transformation matrix.

## Examples

Define a transformation matrix and assign its value to variable
tmatrix:

```
(setq tmatrix (vlax-tmatrix '((1 1 1 0) (1 2 3 0) (2 3 4 5) (2 9 8 3))))
#<variant 8197 ...>
```

Use
vlax-safearray->list to view the value of
tmatrix in list form:

```
(vlax-safearray->list (vlax-variant-value tmatrix))
((1.0 1.0 1.0 0.0) (1.0 2.0 3.0 0.0) (2.0 3.0 4.0 5.0) (2.0 9.0 8.0 3.0))
```

The following code example creates a line and rotates it 90 degrees using a transformation matrix:

```
(defun Example_TransformBy ( / acadObject acadDocument mSpace lineObj
                               startPt endPt matList transMat)
  (vl-load-com)      ; Load ActiveX support
  (setq acadObject   (vlax-get-acad-object))
  (setq acadDocument (vla-get-ActiveDocument acadObject))
  (setq mSpace       (vla-get-ModelSpace acadDocument))

;;; Create a line
  (setq startPt (getpoint "\
Pick the start point: "))
  (setq endPt   (vlax-3d-point (getpoint startPt "\
Pick the end point: ")))
  (setq lineObj (vla-addline mSpace (vlax-3d-point startPt) endPt))

;;; Initialize the transMat variable with a transformation matrix
;;; that will rotate an object by 90 degrees about the point(0,0,0).
;;; Begin by Creating a list of four lists, each containing four
;;; numbers, representing transformation matrix elements.
  (setq matList (list '(0 -1 0 0) '(1 0 0 0) '(0 0 1 0) '(0 0 0 1)))

;;; Use vlax-tmatrix to convert the list to a variant.
  (setq transmat (vlax-tmatrix matlist))

;;; Transform the line using the defined transformation matrix
  (vla-transformby lineObj transMat)
  (vla-zoomall acadObject)
  (prompt "\
The line has been transformed.")
 (princ)
)
```

#### Related References

* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-variant-type (AutoLISP/ActiveX)](vlax-variant-type-AutoLISP-ActiveX.md)
* [vlax-variant-value (AutoLISP/ActiveX)](vlax-variant-value-AutoLISP-ActiveX.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*