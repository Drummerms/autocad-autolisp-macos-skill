# Tutorial: Debugging LSP Files with the AutoLISP Extension (AutoLISP/VS Code)

After you create an AutoLISP (LSP) file and add code statements to the file, you can connect Visual Studio Code to AutoCAD
and step through your custom functions using many of the debug tools that Visual Studio Code offers.

NOTE:Debugging AutoLISP programs in AutoCAD LT isn't supported with the AutoLISP Extension for Microsoft Visual Studio (VS) Code.

## Prerequisites

1. [Install Visual Studio Code on your workstation.](To-Download-and-Install-VS-Code-AutoLISP-VS-Code.md)
2. [Install and configure the AutoCAD AutoLISP Extension.](Tutorial-Installing-and-Configuring-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

## Topics in this Tutorial

* [Open an AutoLISP (LSP) File](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_9714790A968F4219B23663500741BA3B)
* [Attach to AutoCAD and Load an AutoLISP (LSP) File for Debugging](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_D4C74979157E4D47A759BD1E1B5DA6BE)
* [Add Breakpoints to Statements](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_3A32B039E4CB49EBA58E2FEBCB101DEC)
* [Watch Variable Values and Return Values of Statements](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_F0DD106E16424586B6D9F4986F800A61)
* [Reload an AutoLISP (LSP) File while Debugging](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_1FDB3CF9EA914BE1BF064DE33AEEBFBD)
* [End Debugging](GUID-F4E0BB17-5846-43C9-9417-E78DE4E6A129.htm#SECTION_1D06D86877A64A1B8B4C196D9C47C616)

## Open an AutoLISP (LSP) File

Before debugging an LSP file, it is recommended to first open the LSP file you want to debug. The LSP file open in the current
editor window will be loaded into AutoCAD when Visual Studio Code is initially connected to AutoCAD for debugging.

The following steps explain how to open the
*Create-LSP-Tutorial.lsp* file in Visual Studio Code.

1. Launch Visual Studio Code.
2. In Visual Studio Code, on the Activity Bar, click Explorer.
3. On the Explorer view, under LSP Files, click
   *Create-LSP-Tutorial.lsp* to open and make it the current editor window.

   If the
   *LSP Files* folder is not open, click File menu > Open Folder/Open. Then browse to and select the
   *LSP Files* folder.

## Attach to AutoCAD and Load an AutoLISP (LSP) File for Debugging

After the AutoLISP Extension has been properly configured and an LSP file is open in the current editor window, you are ready
to debug the AutoLISP code statements stored in the LSP file with Visual Studio Code.

The following steps explain how to attach Visual Studio Code to AutoCAD for debugging.

1. Launch
   AutoCAD 2026.
2. Switch to Visual Studio Code.
3. In Visual Studio Code, click Run menu > Start Debugging.
4. From the Configurations menu, choose AutoLISP Debug: Attach.
5. In the Processes menu, choose the process that represents your running instance of
   AutoCAD 2026.

   Visual Studio Code should now be attached to AutoCAD with the LSP file in the current editor window loaded into the current
   drawing window.

   You can tell if Visual Studio Code has successfully been attached to AutoCAD by the change in color to Visual Studio Code's
   status bar, it will change from Blue to Orange in color.

   ![](../images/GUID-CA8F095A-7225-48F1-A83F-2948AFEE71C9-low.png)
6. Switch back to AutoCAD.
7. At the Command prompt, enter
   *hello*.
8. At the
   *Enter a message:* prompt, type
   *Hello from AutoCAD!* and press Enter.

   A message box appears with the text "Hello from AutoCAD!".

   ![](../images/GUID-8EFAAD5D-B5D7-4F1C-A1F2-002DFBE8611B-low.png)
9. Click OK to close the message box.
10. At the Command prompt, enter
    *drawline*. Specify the two endpoints for the line.

    A line is drawing between the specified points and is placed on the current layer.

## Add Breakpoints to Statements

Breakpoints allow for the interruption of code statements as they are being executed. When execution is interrupted, you can:

* Step through the current and next statements in your custom program one line at a time
* Evaluate the current value assigned to a variable or returned by a function

The following steps explain how to add breakpoints to the
*Create-LSP-Tutorial.lsp* file open in the current editor window.

Line Breakpoint
:   1. Switch to Visual Studio Code.
    2. In the editor window, in the left margin, click to the left of Line 3 to add a breakpoint at the beginning of the code statement
       on that line.

       A red circle appears indicating a breakpoint has been added.

       ![](../images/GUID-259FDED1-2871-4D67-89FF-930E3124BD2D-low.png)
    3. Switch to AutoCAD.
    4. At the Command prompt, enter
       *hello*.

       The
       hello function is started and code execution is interrupted at the line with the breakpoint.
    5. Switch back to Visual Studio Code.
    6. On the Debug toolbar, click Continue to resume execution.

       ![](../images/GUID-3AD93DA0-5E93-49CA-B91D-18A1F580C42D-low.png)
    7. Switch back to AutoCAD and enter a text string to display in the message box.
    8. Click OK to close the message box.

Inline Breakpoint
:   1. Switch to Visual Studio Code.
    2. In the editor window, on Line 11, click to the left of the opening parenthesis.
    3. Right-click and choose Add Inline Breakpoint to add a breakpoint at the beginning of the nested AutoLISP expression.

       ![](../images/GUID-C95689A7-146F-4B4A-8323-84F9F7EF4534-low.png)
    4. Switch to AutoCAD.
    5. At the Command prompt, enter
       *drawline*.
    6. Specify a point for the start point of the line.

       After specifying the first point, execution is interrupted by the inline breakpoint.
    7. Switch back to Visual Studio Code.
    8. On the Debug toolbar, click Continue to resume execution.

       ![](../images/GUID-3AD93DA0-5E93-49CA-B91D-18A1F580C42D-low.png)
    9. Switch back to AutoCAD and specify a point for the endpoint of the line.

## Watch Variable Values and Return Values of Statements

When execution is interrupted by a breakpoint, you can see the current value assigned to a variable or the value returned
by a code statement.

In the previous section, you set two different breakpoints. The following steps utilize those breakpoints to interrupt code
execution and view the value assigned to a variable.

1. Switch to AutoCAD.
2. At the Command prompt, enter
   *drawline*.
3. Specify the start point of the line.
4. Switch to Visual Studio Code.
5. Move the cursor over the
   *pt1* variable above or in the highlighted statement to view the current value assigned to the variable.

   ![](../images/GUID-5145E6FD-8E07-4621-9C08-7C43EF751A64-low.png)
6. On the Debug toolbar, click Step Into.

   ![](../images/GUID-B9972651-57BC-47B8-9ECD-F677BDDEF5C3-low.png)
7. Switch back to AutoCAD and specify the second point.
8. Switch back to Visual Studio Code and click Step Into again on the Debug toolbar.
9. View the value assigned to the
   *pt2* variable.

   Along with positioning the cursor over a variable to view its current assigned value in a tooltip, the values assigned to
   all local variables can be viewed in the Variables section on the Run view.

   ![](../images/GUID-3FA0DEDB-311E-4563-B1BD-53530F418458-low.png)
10. On the Debug toolbar, click Continue to resume execution.

    ![](../images/GUID-3AD93DA0-5E93-49CA-B91D-18A1F580C42D-low.png)

## Reload an AutoLISP (LSP) File while Debugging

It is inevitable, while debugging your custom programs that you will encounter an error that needs to be fixed. Once fixed,
you will want to test the changes made.

The following steps explain how to make a change to the
drawline function and the reload the LSP file into AutoCAD while debugging with Visual Studio Code.

1. Switch to Visual Studio Code.
2. In the editor window for the
   *Create-LSP-Tutorial.lsp* file, make the following changes in bold below:

   ```
   ;; Draws a line between two points
   (defun c:drawline ( / pt1 pt2 sv_clayer) ;; Declared local variables
   ;; Store the current and create a new layer
   (setq sv_clayer (getvar "clayer"))
   (command "_.-layer" "_m" "Object" "_c" "5" "" "")

   ;; Prompt for two points
   (setq pt1 (getpoint "\
   Specify start point of line: ")
   pt2 (getpoint pt1 "\
   Specify end point of line: ")
   )

   ;; Check to see if the user specified two points
   (if (and pt1 pt2)
   (command "_.line" pt1 pt2 "")
   (prompt "\
   Invalid or missing point(s)")
   )

   ;; Restore the previous layer
   (setvar "clayer" sv_clayer)

   ;; Exit quietly
   (princ)
   )
   ```
3. Save the changes to the LSP file.
4. On the Debug toolbar, click Restart.

   ![](../images/GUID-492CF694-950B-4DAE-B9A2-F12476512D1F-low.png)

   Visual Studio Code disconnects from AutoCAD and then re-attaches to the same AutoCAD process before loading the LSP file in
   the current drawing.
5. Switch back to AutoCAD.
6. At the Command prompt, enter
   *drawline*.
7. Specify the first and second points of the line.

   Notice this time the line is placed on the Objects layer which is assigned the color of Blue.

## End Debugging

After you are done debugging an LSP file, you should disconnect Visual Studio Code from AutoCAD.

The following steps explain how to disconnect Visual Studio Code from AutoCAD.

1. Switch to Visual Studio Code.
2. On the Debug toolbar, click Disconnect.

   ![](../images/GUID-94734FB1-FAED-43E3-B83C-12CC5A3414D9-low.png)

   The Debug toolbar closes and the status bar changes from Orange back to Blue in color.

#### Related Information

* [Debugging AutoLISP Files (AutoLISP/VS Code)](Debugging-AutoLISP-Files-AutoLISP-VS-Code.md)
* [To Launch and Attach an Instance of AutoCAD to VS Code for Debugging (AutoLISP/VS Code)](To-Launch-and-Attach-an-Instance-of-AutoCAD-to-VS-Code-for-Debugging-AutoLISP-VS-Code.md)
* [To Add, Remove, or Disable a Breakpoint while Debugging an LSP File (AutoLISP/VS Code)](To-Add,-Remove,-or-Disable-a-Breakpoint-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Watch Variables and Expressions while Debugging an LSP File (AutoLISP/VS Code)](To-Watch-Variables-and-Expressions-while-Debugging-an-LSP-File-AutoLISP-VS-Code.md)
* [To Load an LSP File into AutoCAD while Debugging (AutoLISP/VS Code)](To-Load-an-LSP-File-into-AutoCAD-while-Debugging-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*