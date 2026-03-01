# About Referencing Variables in Document Namespaces (AutoLISP)

Variables defined in a separate-namespace VLX are not known to the document namespace associated with the VLX.

However, a separate-namespace VLX can access variables defined in a document namespace using the vl-doc-ref and vl-doc-set functions. The vl-doc-set function is the same as using the setq function.

The vl-doc-ref function copies the value of a variable from a document namespace. The function requires a single argument, a symbol identifying
the variable to be copied. For example, the following copies the value of a variable named aruhu:

```
(vl-doc-ref 'aruhu)
```

If executed within a document namespace, vl-doc-ref is equivalent to the eval function.

The vl-doc-set function sets the value of a variable in a document namespace. The function requires two arguments: a symbol identifying
the variable to be set, and the value to set for the variable.

For example, the following sets the value of a variable named ulus:

```
(vl-doc-set 'ulus "Go boldly to noone")
```

If executed within a document namespace, vl-doc-set is equivalent to the setq function. Use the vl-propagate function to set the value of a variable in all open document namespaces.

For example, the following sets a variable named fooyall in all open document namespaces:

```
(setq fooyall "Go boldly and carry a soft stick")
(vl-propagate 'fooyall)
```

The vl-propagate function not only copies the value of fooyall into all currently open document namespaces, but also causes fooyall to automatically be copied to the namespace of any new drawings opened during the current AutoCAD session.

#### Topics in this section

* [To set and retrieve variables from a document namespace (AutoLISP)](To-set-and-retrieve-variables-from-a-document-namespace-AutoLISP.md)

  Values can be stored and retrieved from AutoLISP variables while a drawing remains open.

#### Related Tasks

* [To set and retrieve variables from a document namespace (AutoLISP)](To-set-and-retrieve-variables-from-a-document-namespace-AutoLISP.md)

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Sharing Data Between Namespaces (AutoLISP)](About-Sharing-Data-Between-Namespaces-AutoLISP.md)
* [About Namespaces (AutoLISP)](About-Namespaces-AutoLISP.md)
* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*