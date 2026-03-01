# Tutorial: Creating, Loading, and Opening an AutoLISP File (AutoLISP)

AutoLISP is an interpretive language, so it can be stored in a text file, loaded, and then executed directly within AutoCAD.

AutoLISP files typically have an
*.lsp* file extension, but they can also have the
*.mnl* file extension. Both LSP and MNL files can be edited with a text editor, such as Notepad on Windows and TextEdit on Mac OS.

NOTE:AutoLISP is not available in AutoCAD LT for Mac OS.

MNL files are associated with user interface customization and they are automatically loaded into AutoCAD when a customization
(CUI/CUIx) file of the same name is loaded. For example, the
*acad.mnl* is automatically loaded into AutoCAD when the
*acad.cuix* file is loaded.

NOTE:AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
LOAD function from another LISP file.

## Creating an AutoLISP (LSP) File

Here is how to create a file with the
*.lsp* extension and add the C:HELLO function defined in the
*Creating a New Command and Working with System Variables* tutorial.

Windows
:   1. Click the Windows Start button, and then click Windows Accessories ![](../images/ac.menuaro.gif) Notepad.
    2. In Notepad, click File menu ![](../images/ac.menuaro.gif) Save As.
    3. In the Save As dialog box, browse to the
       *Documents* folder. Right-click in an empty area, not over a file or folder, and click New ![](../images/ac.menuaro.gif) Folder. Enter the name
       *LSP Files* for the name of the new folder and press Enter. Double-click the new folder
       *LSP Files* to make sure it is the current folder.
    4. In the File Name text box, enter
       *Create-LSP-Tutorial.lsp*.
    5. Click the Save As Type drop-down list and select All Files (\*.\*).
    6. Click the Encoding drop-down list and select ANSI. Click Save.
    7. In the editor area, enter the following

       ```
       (defun c:hello ( / msg)
         (setq msg (getstring T "\
       Enter a message: "))
         (alert msg)
       )

       (prompt "\
       AutoLISP Tutorial file loaded.")
       (princ) ; Suppress the return value of the prompt function
       ```
    8. Click File menu ![](../images/ac.menuaro.gif) Save.
    9. Close Notepad.

Mac OS
:   NOTE:AutoLISP is not available in AutoCAD LT for Mac OS.

    1. In Finder, on the Mac OS menu bar, click Go menu ![](../images/ac.menuaro.gif) Applications.
    2. In the Applications window, double-click TextEdit.
    3. In TextEdit, on the Mac OS menu bar, click TextEdit menu ![](../images/ac.menuaro.gif) Preferences.
    4. In the Preferences dialog box, do the following:
       * Under the Format section, click Plain Text.
       * Under the Options section, clear the Check Spelling As You Type and Correct Spelling Automatically check boxes.

       TIP:If needed, a rich text file can be switched to a plain text file by clicking Format menu ![](../images/ac.menuaro.gif) Make Plain Text on the Mac OS menu bar.
    5. Click the Close button.
    6. On the Mac OS menu bar, click File menu ![](../images/ac.menuaro.gif) New to create a new document.
    7. With the new document current, on the Mac OS menu bar, click File menu ![](../images/ac.menuaro.gif) Save.
    8. In the Untitled dialog box, browse to the
       *Documents* folder and click New Folder.

       NOTE:The dialog box must be expanded to see the New Folder button.
    9. In the New Folder dialog box, enter
       *LSP Files* and click Create. Select the new folder
       *LSP Files* to make sure it is the current folder.
    10. In the Save As text box, enter
        *Create-LSP-Tutorial.lsp*.
    11. If checked, clear the If No Extension is Provided, Use ".txt" check box.
    12. Click Save.
    13. In the editor area, enter the following

        ```
        (defun c:hello ( / msg)
          (setq msg (getstring T "\
        Enter a message: "))
          (alert msg)
        )

        (prompt "\
        AutoLISP Tutorial file loaded.")
        (princ) ; Suppress the return value of the prompt function
        ```
    14. On the Mac OS menu bar, click File menu ![](../images/ac.menuaro.gif) Save.
    15. Quit TextEdit.

## Loading an AutoLISP (LSP) File

Here is how to load the
*Create-LSP-Tutorial.lsp* file created under the
*Creating an AutoLISP (LSP) File* section.

NOTE:AutoLISP is not available in AutoCAD LT for Mac OS.

1. In AutoCAD, do one of the following:
   * *(Windows)* On the ribbon, click Manage tab ![](../images/ac.menuaro.gif) Applications panel ![](../images/ac.menuaro.gif) Load Application.
   * *(Mac OS)* On the Mac OS menu bar, click Tools ![](../images/ac.menuaro.gif) Load Application.
   * At the Command prompt, enter
     *appload*.
2. In the Load/Unload Applications dialog box, browse to the
   *Documents* ![](../images/ac.menuaro.gif) *LSP Files* folder or the folder in which you stored the
   *Create-LSP-Tutorial.lsp* file.
3. Click Load.
4. If the File Loading – Security Concern dialog box is displayed, click Load again.
5. Click Close to return to the application window.
6. You should see the following message in the Command History window.

   AutoLISP Tutorial file loaded.
7. At the Command prompt, enter
   *hello*.
8. At the
   *Enter a message:* prompt, type a text string and press Enter.

   A message box displays the text string that you entered.

## Opening an AutoLISP (LSP) File

Here is how to open the
*Create-LSP-Tutorial.lsp* file that you created under the
*Creating an AutoLISP (LSP) File* section.

Do one of the following:

* *(Windows)* Double-click the
  *Create-LSP-Tutorial.lsp* file to open the file in Notepad.
* *(Windows)* Click the Windows Start button, and then click Windows Accessories ![](../images/ac.menuaro.gif) Notepad. Click File menu ![](../images/ac.menuaro.gif) Open. From the Save As Type drop-down list, select All Files (\*.\*). Browse to and select the
  *Create-LSP-Tutorial.lsp* file, and click Open.
* *(Mac OS)* Double-click the
  *Create-LSP-Tutorial.lsp* file to open the file in TextEdit.

  NOTE:If prompted for an application, click Choose Application. In the Choose Application dialog box, select TextEdit, and click
  Open.
* *(Mac OS)* In Finder, on the Mac OS menu bar, click Go menu ![](../images/ac.menuaro.gif) Applications. In the Applications window, double-click TextEdit. In TextEdit, on the Mac OS menu bar, click File menu ![](../images/ac.menuaro.gif) Open. Browse to and select the
  *Create-LSP-Tutorial.lsp* file, and click Open.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Source Code Files (AutoLISP)](About-Source-Code-Files-AutoLISP.md)
* [About Comments in AutoLISP Program Files (AutoLISP)](About-Comments-in-AutoLISP-Program-Files-AutoLISP.md)
* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [Tutorial: Creating a New Custom Command and Controlling with System Variables (AutoLISP)](Tutorial-Creating-a-New-Custom-Command-and-Controlling-with-System-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*