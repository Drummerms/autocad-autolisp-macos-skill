# About Sharing Data Between Namespaces (AutoLISP)

A namespace called the blackboard is used for communicating values across all namespaces.

The blackboard namespace is not attached to any document or VLX application. You can set and reference variables in the blackboard
from any document or VLX application. Use the vl-bb-set function to set a variable, and use vl-bb-ref to retrieve a variable's value.

For example, the following sets the foobar variable to a string in the blackboard namespace:

```
(vl-bb-set 'foobar "Root toot toot")
"Root toot toot"
```

The vl-bb-ref function returns the specified string. The following uses the vl-bb-ref function to retrieve the value of the foobar variable from the blackboard namespace:

```
(vl-bb-ref 'foobar)
"Root toot toot"
```

Setting or retrieving variable values in the blackboard namespace has no effect on variables of the same name in any other
namespace.

#### Topics in this section

* [To set and retrieve variables in the blackboard namespace (AutoLISP)](To-set-and-retrieve-variables-in-the-blackboard-namespace-AutoLISP.md)

  Variables can be stored and retrieved across multiple open drawings using the blackboard namespace.

#### Related Tasks

* [To set and retrieve variables in the blackboard namespace (AutoLISP)](To-set-and-retrieve-variables-in-the-blackboard-namespace-AutoLISP.md)

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Namespaces (AutoLISP)](About-Namespaces-AutoLISP.md)
* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)
* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*