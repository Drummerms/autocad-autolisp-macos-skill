# To Add or Edit Code Snippet Definitions (AutoLISP/VS Code)

Code snippets are stored in the
*snippets.json* file that is part of the AutoCAD AutoLISP Extension; you can add new or edit existing code snippets to improve your efficiency
when writing AutoLISP programs. The
*snippets.json* file is written in JSON and supports C-style comments. Each code snippet should contain the following attributes:

* *name* – A unique name for the code snippet; used if no description is provided
* *prefix* – Defines the name to be typed and displayed in the IntelliSense list to insert the code snippet
* *body* – Expressions that define the code snippet, can contain new lines, tabs, and placeholders
* *description* – Defines the text that should be displayed in the IntelliSense tooltip for the code snippet

The following shows the basic definition of a code snippet:

```
"ifprogn":
  {
    "prefix": "ifp",
    "body":
      [
        "(if (${1:testexpr})",
            "\t(progn",
            "\t\t(${2:thenexpr})",
            "\t)",
        ")"
      ],
    "description": "if progn expression"
  }
```

1. In Visual Studio Code or another text editor, open the
   *snippets.json* file.

   Based on your OS, the
   *snippets.json* file can be found in one of these locations:

   * *Windows* –
     *%USERPROFILE%\.vscode\extensions\autodesk.autolispext-n.n.n\snippets*
   * *Mac OS* –
     *~/.vscode/extensions/autodesk.autolispext-n.n.n/snippets*

   NOTE:*n.n.n* in the previous paths is a placeholder, the actual version of the AutoCAD AutoLISP Extension will vary over time as the extension
   is updated.
2. In the
   *snippets.json* file, add your new code snippet or change an existing one.

   NOTE:Be careful about where you insert new text or which text you change, the formatting of the file is critical to it being properly
   parsed.
3. Save the
   *snippets.json* file and test the code snippet changes.

#### Related Information

* [Creating and Opening AutoLISP Files (AutoLISP/VS Code)](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md)
* [Editing AutoLISP Files (AutoLISP/VS Code)](Editing-AutoLISP-Files-AutoLISP-VS-Code.md)
* [To Insert a Code Snippet (AutoLISP/VS Code)](To-Insert-a-Code-Snippet-AutoLISP-VS-Code.md)
* [To Add and Remove Comments from Selected AutoLISP Expressions (AutoLISP/VS Code)](To-Add-and-Remove-Comments-from-Selected-AutoLISP-Expressions-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*