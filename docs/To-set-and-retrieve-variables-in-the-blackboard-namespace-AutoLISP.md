# To set and retrieve variables in the blackboard namespace (AutoLISP)

Variables can be stored and retrieved across multiple open drawings using the blackboard namespace.

1. At the AutoCAD Command prompt or from an AutoLISP program, use the vl-bb-set function to set the value of a variable in the blackboard.
2. Use the vl-bb-ref function to retrieve the value of a variable from the blackboard.

## Example

1. At the AutoCAD Command prompt, enter *(vl-bb-set '\*example\* 0)* and press Enter.

   Returns:

   ```
   0
   ```

   The \*example\* variable is set to 0 in the blackboard namespace.
2. At the AutoCAD Command prompt, enter *(vl-bb-ref '\*example\*)* and press Enter.

   Returns:

   ```
   0
   ```
3. At the AutoCAD Command prompt, enter *!\*example\** and press Enter.

   Returns:

   ```
   nil
   ```

   The \*example\* variable returns nil because it has not been set in the document namespace.
4. At the AutoCAD Command prompt, enter *(setq \*example\* -1)* and press Enter.

   Returns:

   ```
   -1
   ```

   The \*example\* variable is set to -1 in the document namespace.
5. At the AutoCAD Command prompt, enter *(vl-bb-ref '\*example\*)* and press Enter.

   Returns:

   ```
   0
   ```

   The blackboard variable named \*example\* is still set to the value assigned in Step 1; setting the document variable of the same name in Step 4 had no effect on the
   variable in the blackboard.

   You can also the vl-doc-set and vl-doc-ref functions to set and retrieve document namespace variables from a separate-namespace VLX, and vl-propagate to set the value of a variable in all open document namespaces.

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Sharing Data Between Namespaces (AutoLISP)](About-Sharing-Data-Between-Namespaces-AutoLISP.md)
* [About Namespaces (AutoLISP)](About-Namespaces-AutoLISP.md)
* [Namespace Communication Functions Reference (AutoLISP)](Namespace-Communication-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*