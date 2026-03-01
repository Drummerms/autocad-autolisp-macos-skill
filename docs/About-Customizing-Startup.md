# About Customizing Startup

Command line switches can be used to control how the program is started from the Terminal window or a shell script.

You can use command line switches to specify several options when you start the program. For example, you can run a script,
start with a specified drawing template.

Command line switches are parameters you can use to create custom shell scripts to start AutoCAD in a specific way. Valid
switches are listed in the following table.

| -b | Script name | Designates a script to run after you start the program (b stands for batch process). Scripts can be used to set up drawing parameters in a new drawing file. |
| -ld | Load custom *.bundle* file | Designates a custom program with the *.bundle* file extension to load at startup. |
| -t | Template file name | Creates a new drawing based on a template or prototype drawing. |
| -nologo | Suppress logo screen | Starts the program without first displaying the logo screen. |
| -safemode | Prevents executable code from being executed | Starts the program without loading and executing custom AutoLISP programs in the current AutoCAD session, and disables the execution of AutoLISP expressions at the Command prompt. |

The syntax for using command line switches is

pathname/AutoCAD [drawingname] [-switchname]

When using a switch option, you must follow the switch with a space and then the name of a file. For example, the following
entry starts the program from a folder named AutoCAD 2025 with the drawing template arch1.dwt and executes a script filestartup.scr.

"/Applications/Autodesk/AutoCAD 2025/AutoCAD 2025.app/Contents/MacOS/AutoCAD" -t /templates/arch1.dwt -b startup.scr

#### Related Tasks

* [To Start the Program With Script](To-Start-the-Program-With-Script.md)

#### Related References

* [Command Line Switch Reference](Command-Line-Switch-Reference.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*