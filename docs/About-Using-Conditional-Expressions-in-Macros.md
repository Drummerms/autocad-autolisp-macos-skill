# About Using Conditional Expressions in Macros

You can add conditional expressions to a macro by using a command that introduces macro expressions written in DIESEL (Direct
Interpretively Evaluated String Expression Language).

The format is:

```
$M=expression
```

Introducing the macro with $M= tells the application to evaluate a string as a DIESEL expression, and that  *expression*  is the DIESEL expression. The following example defines a conditional expression in a macro:

```
FILLMODE $M=$(-,1,$(getvar,fillmode))
```

The macro switches the FILLMODE system variable on and off by subtracting the current value of FILLMODE from 1 and returning
the resulting value to the FILLMODE system variable. You can use this method to toggle system variables whose valid values
are 1 or 0.

## Termination of Macros that Contain Conditional Expressions

If you use the DIESEL string language to perform “if-then” tests, conditions might exist where you do not want the normal
terminating space or semicolon (resulting in Enter). If you add ^Z to the end of the macro, the application does not automatically add a space (Enter) to the end of the macro expression.

As with other control characters in commands, the ^Z used here is a string composed of ^ (a caret) and Z and is not equivalent to pressing Ctrl+Z (or Control-Z on Mac OS).

In the following examples, ^Z is used as a macro terminator.

```
^C^C$M=$(if,$(=,$(getvar,tilemode),0),$S=mview _mspace )^Z
^C^C$M=$(if,$(=,$(getvar,tilemode),0),$S=mview _pspace )^Z
```

If these macros did not end with ^Z, the application would automatically add a space (Enter), repeating the last command entered.

#### Related Tasks

* [To Create a Custom Command](To-Create-a-Custom-Command.md)
* [To Edit a Command](To-Edit-a-Command.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Command Macro Strings](About-Command-Macro-Strings.md)
* [About Special Control Characters in Command Macros](About-Special-Control-Characters-in-Command-Macros.md)
* [About Pausing Macros for User Input](About-Pausing-Macros-for-User-Input.md)
* [About Using AutoLISP in Macros](About-Using-AutoLISP-in-Macros.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*