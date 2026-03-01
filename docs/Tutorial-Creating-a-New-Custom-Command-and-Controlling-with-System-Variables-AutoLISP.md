# Tutorial: Creating a New Custom Command and Controlling with System Variables (AutoLISP)

With the AutoLISP programming language, you can control the drawing environment by creating your own command-like functions,
and by setting the values of system variables.

With AutoLISP you can create new commands that can be accessed from the Command prompt, just like you interact with standard
AutoCAD commands, or those defined by a third-party utility. Your custom commands can use standard AutoCAD commands with the
command function, or they can directly manipulate objects using AutoLISP functions. Many developers create AutoLISP functions that
execute several standard AutoCAD commands in a specific order.

AutoLISP programs can also query and change the values of system variables. System variables affect the behavior of commands
and the AutoCAD environment.

## Creating a New Function

You define a new function using the defun AutoLISP function. defun means “define function.”

Here is the signature of the defun function:

```
(defun function_name ([arguments] [/ local_variables ...]) expr ...)
```

As you can see, the first argument is the name of the function that you want to define.

The defun function also allows you to define a list of arguments that can be passed to the function and a list of user-defined variables
that are "local" to the function. When you declare user-defined variables that will be available to your function only while
it is active, make sure you add them to the local variable list as part of the defun expression.

The following is an example of a custom function that outputs a message to either the Command prompt or in a message box:

```
(defun display-msg (msg mode / )
  (if (= mode 0)
    (prompt (strcat "\
" msg))
    (alert msg)
  )
 (princ)
)
```

The custom display-msg function expects two values, a message as a text string and a mode as an integer value of 0 or 1. You
can test the function by entering the code at the AutoCAD Command prompt, and then entering one of the following to execute
the function:

* (display-msg "Hello from AutoLISP!" 0)
* (display-msg "Hello from AutoLISP!" 1)

## Creating a Custom Command

A custom command is a function that is defined with the defun function, but uses a special naming convention: they use the characters c: as a prefix. This distinguishes them from other functions.

You can define a function that accepts arguments, but you should never define a function that will be used as a custom command
to accept arguments. Instead, functions that are defined as custom commands should prompt the user for input with the getXXX, entsel, nentsel, and ssget functions.

After you provide a function name to the defun function, you can then enter which AutoLISP expressions should be executed when the custom command is entered at the Command
prompt.

The following steps explain how to define a custom command named HELLO. This command will prompt the user for a string value
and then display the string entered in a message box:

1. At the Command prompt, enter *!msg* and press Enter.

   The value nil should be returned because the user-defined variable msg is not assigned a value currently. The msg is a user-defined variable that will be defined as part of the HELLO command and should not be available to other programs.
2. At the Command prompt, enter the following code one line at a time. Press Enter after each line. After the last line has been
   entered, you will see the value C:HELLO displayed in the history of the Command Window.

   ```
   (defun c:hello ( / msg)
     (setq msg (getstring T "\
   Enter a message: "))
     (alert msg)
   )
   ```

Now that the HELLO command has been defined, you can execute it by entering its name at the Command prompt. Use these steps
to execute the HELLO command:

1. At the Command prompt, enter *hello*.
2. At the *Enter a message:* prompt, enter *This is my first AutoLISP command!*.

   A message box is displayed that shows the message you entered.

   ![](../images/GUID-70E555EE-20AA-42A0-BC00-370DE184E9D6-low.png)

   Message Box - Windows

   ![](../images/GUID-1E3EC3D5-8AE8-47DD-B163-E3B7AF941323-low.png)

   Message Box - Mac OS
3. Click OK to dismiss the message box.
4. At the Command prompt, enter *!msg* and press Enter.

   The value nil should be returned, and is as expected. Even though you used the setq function to assign the value entered at the *Enter a message:* prompt to the msg variable, the value of the variable is not maintained because it was defined as a local variable to the C:HELLO function.
   If you remove msg from the local variable list in the defun expression for the C:HELLO function, the msg variable would be defined as a global variable then and the value would be retained after the function has finished executing.

Entering expressions directly at the Command prompt makes it easy to learn and work with AutoLISP, but there is a disadvantage
to this convenience. Any functions and user-defined variables you define in a drawing are accessible only from that drawing
until it is closed. You can see this by doing the following:

1. Define the HELLO function shown earlier in the current drawing, if you did not previously do so.
2. Create a new drawing.
3. At the Command prompt, enter *hello*.

   The following message is displayed:

   Unknown command "HELLO". Press F1 for help.

You can save your AutoLISP expressions to a file with the LSP file extension so they can be reused and loaded into other drawings.
For information on creating and loading AutoLISP Source (LSP) files, see *Tutorial: Creating, Loading, and Opening an AutoLISP File*.

## Accessing and Setting System Variable Values

System variables control the behavior of commands, change the settings of the drawing environment, and specify the default
property values of new objects and much more. You can query and set the value for a system variable using the following functions:

* getvar - Returns the current value of a system variable
* setvar - Assigns a new value to a system variable

The following explain how to get and set the value of the OSMODE (Object Snap mode) system variable:

1. At the Command prompt, enter *(setq cur\_osmode (getvar "osmode"))*.

   The current value of the OSMODE system variable is returned and assigned to the user-defined variable of cur\_osmode. While OSMODE returns an integer value, the value is the sum of multiple "bit-code" values. For example, the value 35 indicates
   that the Endpoint (1), Midpoint (2), and Intersection (32) running object snaps are enabled.
2. At the Command prompt, enter *osnap*.

   The Drafting Settings dialog box is displayed with the Object Snap tab current. This tab allows you to see which object snaps
   are enabled. The following image shows what the Drafting Settings dialog box looks like when the OSMODE system variable is
   set to a value of 35.

   ![](../images/GUID-2C802286-49D6-4B3A-AC22-1AA1C091D0AA-low.png)

   Drafting Settings dialog box - Windows

   ![](../images/GUID-F862CD94-678F-49AD-9849-66A52EFB21C7-low.png)

   Drafting Settings dialog box - Mac OS
3. In the Drafting Settings dialog box, change which object snaps are current and click OK.
4. At the Command prompt, enter *(getvar "osmode")*.

   The current value of the OSMODE system variable is returned.
5. At the Command prompt, enter *(setvar "osmode" cur\_osmode)*.

   The value of the OSMODE system variable is restored to the value that was previously assigned to the user-defined variable
   cur\_osmode.
6. Display the Drafting Settings dialog box again. You should see that the object snap settings have been restored.

NOTE:Before you make a change to the drawing environment, it is good practice to store the values of any system variables, and
then restore them before your program ends.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)
* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*