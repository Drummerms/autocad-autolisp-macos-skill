# About Namespaces (AutoLISP)

A namespace is a LISP environment containing a set of symbols (for example, variables and functions).

The concept of namespaces was introduced to prevent applications running in one drawing window from unintentionally affecting
applications running in other windows. Each open AutoCAD drawing document has its own namespace. Variables and functions defined
in one document namespace are isolated from variables and functions defined in other namespaces.

![](../images/GUID-A31B67C4-8CD2-420B-B8EC-242ADF04C053-low.png)

You can see how this works by trying a simple example.

#### Topics in this section

* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)

  Variables defined in a separate-namespace VLX are not known to the document namespace associated with the VLX.
* [About Sharing Data Between Namespaces (AutoLISP)](About-Sharing-Data-Between-Namespaces-AutoLISP.md)

  A namespace called the blackboard is used for communicating values across all namespaces.
* [To load functions across all document namespaces (AutoLISP)](To-load-functions-across-all-document-namespaces-AutoLISP.md)

  Normally, loading an application file loads it in the current drawing only, but the vl-load-all function can be used to load
  a file in all drawings.

#### Related Tasks

* [To load functions across all document namespaces (AutoLISP)](To-load-functions-across-all-document-namespaces-AutoLISP.md)

#### Related Concepts

* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)
* [About Sharing Data Between Namespaces (AutoLISP)](About-Sharing-Data-Between-Namespaces-AutoLISP.md)
* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)
* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*