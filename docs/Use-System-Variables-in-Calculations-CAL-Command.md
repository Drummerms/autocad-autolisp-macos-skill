# Use System Variables in Calculations (CAL Command)

You can use the
 *getvar*  function to read the value of a system variable.

The syntax is

*getvar(*    *variable\_name*  )

The following example uses
 *getvar*  to obtain the point that is the center of the view in the current viewport.

*getvar(viewctr)*

With this method, you can also access the user system variables, USERI1-5 and USERR1-5. For example, to retrieve the value
stored in USERR2, enter the following:

*getvar(userr2)*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*