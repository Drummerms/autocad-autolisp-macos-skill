# To Manage Command Aliases

A command alias is an abbreviation of a command name, which you can enter at the Command prompt instead of entering the entire
command name. Edit the Program Parameters (PGP) File to manage command aliases.

Windows
:   1. Do one of the following:
       * Click Manage tab ![](../images/ac.menuaro.gif) Customization panel ![](../images/ac.menuaro.gif) Edit Aliases (flyout) ![](../images/ac.menuaro.gif) Edit Aliases.
         ![](../images/GUID-DCB0D245-0620-4583-AC6E-8F98D53D4E8F-low.png) Find
       * At the Command prompt, enter
         *ai\_editcustfile* and press Enter. Then enter
         *acad.pgp* (AutoCAD) or
         *acadlt.pgp* (AutoCAD LT), and press Enter.

       NOTE:The default PGP file can also be opened by launching File Explorer, and navigating to your user folder and then double-clicking
       the
       *Application Data* or
       *AppData* folder. Continue to navigate to
       *Roaming\Autodesk\<product name>\<release>\<language>\Support*. Double-click
       *acad.pgp* (or
       *acadlt.pgp* for AutoCAD LT) to edit the file. If prompted for an application to use, select NotePad.
    2. In the text editor, scroll to the bottom and add your new command aliases under the User Defined Command Aliases section.

       ![](../images/GUID-6FC987D5-F5E0-4258-ABC6-4367B4EB15CC-low.png)

       NOTE:If you want to replace an existing command alias, such as C to start the COPY command instead of the CIRCLE command, it is
       best to not change the existing command alias definition but rather to add a new entry under the User Defined Command Aliases
       section. The last definition is the one the product loads.
    3. Save the PGP file after you have made the desired changes.
    4. In AutoCAD or the AutoCAD-based product, at the Command prompt, enter
       *reinit* and press Enter.
    5. In the Re-initialization dialog box, click PGP file. Click OK.
    6. Test your new command alias and edit the PGP file as needed.

Mac OS
:   1. Click
       Tools menu ![](../images/ac.menuaro.gif) Customize ![](../images/ac.menuaro.gif) Edit Command Aliases (PGP). (*ALIASEDIT* command)

       ![](../images/GUID-1D305E56-1C01-43B6-B824-04B62B46C8D1-low.png)
    2. Do any of the following:
       * Click
         ![](../images/GUID-9174311E-7DC8-49C8-B39F-991EC3DAD0E2-low.png) to add an alias.
       * Click
         ![](../images/GUID-A140F0E8-0D4A-41B4-8078-48722E2E2CDB-low.png) to remove an alias.
       * Select an alias, right-click, and select Edit to change an existing alias.
       * Click
         *Load* to load a legacy .pgp file to add the custom aliases to the current list.
       * Click
         *Reveal in Finder* to locate the acaduser.pgp file if you want to copy the file to another computer.
    3. Click Apply to apply the changes and continue making changes or click OK to apply the changes and exit the dialog.

    NOTE:Changes to the command aliases are saved to the
    *acaduser.pgp* file (or
    *acadltuser.pgp* for AutoCAD LT).

#### Related Tasks

* [To Customize Shortcut Keys](To-Customize-Shortcut-Keys.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)
* [Aliases Tab (Customize Dialog Box)](Aliases-Tab-Customize-Dialog-Box.md)

#### Related Concepts

* [About Creating Command Aliases](About-Creating-Command-Aliases.md)
* [About Customization](About-Customization.md)
* [About Creating and Customizing of Shortcut Keys](About-Creating-and-Customizing-of-Shortcut-Keys.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*