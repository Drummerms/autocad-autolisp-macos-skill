# To set and retrieve variables from a document namespace (AutoLISP)

Values can be stored and retrieved from AutoLISP variables while a drawing remains open.

1. At the AutoCAD Command prompt or in an AutoLISP program, enter an AutoLISP statement that uses the setq function and press Enter.
2. Enter the name of the variable you assigned a value to and prefix it with an ! (exclamation point) to return the value assigned to the variable and press Enter.

## Example

1. In the AutoCAD drawing environment, create or open two new drawings.
2. Do one of the following:
   * In Windows, on the ribbon, click View tab ![](../images/ac.menuaro.gif) User Interface panel ![](../images/ac.menuaro.gif) Tile Vertically.

     You should see two open document windows shown side by side.
   * In Mac OS, resize each drawing window so they can be seen side by side.
3. At the AutoCAD Command prompt, enter *(setq draw1foo "I am drawing 1")* and press Enter.

   Returns:

   ```
   "I am drawing 1"
   ```
4. Activate the second drawing by clicking in the window's title bar.
5. At the AutoCAD Command prompt, enter *!draw1foo* and press Enter.

   Returns:

   ```
   nil
   ```

   The variable is nil because it has not been set in this document’s.
6. At the AutoCAD Command prompt, enter *(setq draw2foo "I too am a drawing, but number 2")* and press Enter.

   Returns:

   ```
   "I too am a drawing, but number 2"
   ```
7. Activate the previous drawing.
8. At the AutoCAD Command prompt, enter *!draw1foo* and press Enter.

   Returns:

   ```
   "I am drawing 1"
   ```
9. At the AutoCAD Command prompt, enter *!draw2foo* and press Enter.

   Returns:

   ```
   nil
   ```

   The draw1foo variable contains the value you set in Step 3, but draw2foo is nil because you did not set it to a value in the current document; you set a different variable of the same name in the
   second drawing's namespace.

#### Related Concepts

* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)
* [About Namespaces (AutoLISP)](About-Namespaces-AutoLISP.md)
* [VLX Namespace Functions Reference (AutoLISP)](VLX-Namespace-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*