# Example: Quick Overview of Dialog Boxes (DCL)

This example explains how to create a basic dialog box and display it using AutoLISP.

## Creating the DCL File

This DCL defines a dialog box labeled Sample Dialog Box that contains a text tile and a single OK button. The DCL resides
in a file named
*hello.dcl*.

![](../images/GUID-7EE363F6-A3F3-4F08-A533-40F29083B386-low.png)

```
hello : dialog
{
  label = "Sample Dialog Box";
  : text {
    label = "Hello, world.";
  }
  ok_only;
}
```

Windows
:   1. Highlight the sample DCL code above and press Ctrl+C, or right-click and choose Copy to copy the text to the Clipboard.
    2. Click Start button ![](../images/ac.menuaro.gif) Windows Accessories ![](../images/ac.menuaro.gif) Notepad.
    3. In Notepad, click in the new editor window, and then press Ctrl+V, or right-click and choose Paste to paste the contents from
       the Clipboard.
    4. Click File menu ![](../images/ac.menuaro.gif) Save As.
    5. In the Save As dialog box, browse to the location in which you want to store the DCL file.

       NOTE:Make sure the DCL file is saved to one of the folders in the AutoCAD Support File Search Path.
    6. In the File Name text box, type
       *hello.dcl*.
    7. Click the Save As Type drop-down list and select All Files (\*.\*).
    8. Click the Encoding drop-down list and select ANSI. Click Save.

Mac OS
:   1. Highlight the sample DCL code above and press Command+C, or secondary click and choose Copy to copy the text to the Clipboard.
    2. In Finder, on the Mac OS menu bar, click Go menu ![](../images/ac.menuaro.gif) Applications.
    3. In the Applications window, double-click TextEdit.
    4. In TextEdit, on the Mac OS menu bar, click TextEdit menu ![](../images/ac.menuaro.gif) Preferences.
    5. In the Preferences dialog box, under the Format section, click Plain Text. Click the Close button.
    6. Click in the editor window, and press Command+V, or secondary click and choose Paste.
    7. On the Mac OS menu bar, click File menu ![](../images/ac.menuaro.gif) Save As.
    8. In the Untitled dialog box, browse to the folder in which you want to save the DCL file.

       NOTE:Make sure the DCL file is saved to one of the folders in the AutoCAD Support File Search Path.
    9. In the Save As text box, type
       *hello.dcl* and click Save.
    10. If prompted to use the .dcl file extension, click Use .DCL.

## Displaying the dialog box and responding to the user pressing OK

```
(defun C:HELLO ( / dcl_id )
  (setq dcl_id (load_dialog "hello.dcl")) ; Load the DCL file.
  (if (not (new_dialog "hello" dcl_id))   ; Initialize the dialog.
    (exit)                                ; Exit if this does not work.
  )
  (start_dialog)                          ; Display the dialog box.
  (unload_dialog dcl_id)                  ; Unload the DCL file.
 (princ)
)
```

1. Highlight and copy the sample LSP code above to the Clipboard.
2. Create a new file in Notepad or TextEdit, and save it to the same location as the
   *hello.dcl* file you previously saved with the
   *hello.lsp* filename.
3. In AutoCAD, at the Command prompt, enter
   *appload*.
4. In the Load/Unload Applications dialog box, browse and select
   *hello.lsp* file. Click Load.
5. If the File Loading – Security Concern dialog box is displayed, click Load again.
6. Click Close to return to the application window.
7. At the Command prompt, enter
   *hello*.
8. In Sample Dialog Box, click OK.

The following explains line by line what the AutoLISP program does:

* *Line 1* – Defines a command named
  HELLO with a local variable of
  dcl\_id.
* *Line 2* – Loads the DCL file into memory with the
  load\_dialog function. The
  load\_dialog function returns a DCL identification number. You need this to identify the dialog in subsequent function calls.
* *Lines 3-5* – Initializes the dialog box with the
  new\_dialog function. The dialog box name and DCL identification number are passed as arguments.

  With other dialog boxes, you would also set up tile values, lists, and images. This DCL example above uses a predefined tile
  named
  ok\_only, so you do not have to initialize the tile unless you want to override its default values. The
  ok\_only tile also has an action named
  done\_dialog assigned to it. If the user presses the OK button, AutoCAD passes the
  done\_dialog call to your AutoLISP application and ends the dialog.
* *Line 6* – Control of the dialog is passed to AutoCAD for display with the
  start\_dialog function.
* *Line 7* – Removes the dialog from memory after the finishes responding to it with the
  unload\_dialog function.
* *Line 8*– Exists the command quietly.
* *Line 9* – Ends the definition of the HELLO command.

  For the sake of simplicity, no error processing is included in this example.

Note that the
start\_dialog call remains active until the user selects a tile (usually a button) whose associated action expression calls
done\_dialog. The
done\_dialog call can be issued explicitly by the tile. The
done\_dialog call is also issued by the selected tile if its
is\_cancel attribute is set to
true.

IMPORTANT:In theory, the dialog box facility takes control of input at the time you call
start\_dialog, but the operating system takes control when you call
new\_dialog. This has no effect on writing programs. However, if you invoke these functions interactively (at the AutoCAD Command prompt),
you must enter them as one statement. Enclose them within a
progn or another function. If you do not, the interactive call to
new\_dialog can freeze the screen. Calling
new\_dialog and
start\_dialog interactively can be useful during debugging.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [About Attributes and Attribute Values (DCL)](About-Attributes-and-Attribute-Values-DCL.md)
* [About Tile Definitions (DCL)](About-Tile-Definitions-DCL.md)
* [About Tile References (DCL)](About-Tile-References-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*