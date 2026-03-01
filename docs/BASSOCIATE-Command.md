# BASSOCIATE (Command)

Associates an action with a parameter in a dynamic block definition.

## Summary

Associates an *orphaned* action with a parameter. You can only use the BASSOCIATE command in the Block Editor. An action becomes orphaned when the
parameter with which it is associated is removed from the block definition.

NOTE:The BASSOCIATE command is disabled when the BACTIONBARMODE system variable is set to 1.

## List of Prompts

The following prompts are displayed.

Select Action Object
:   Select an action in the current block definition that is not associated with a parameter.

Parameter to Associate with Action
:   Select a parameter to associate with the action (if you selected a lookup action, you can select one or more lookup parameters)

If you selected an action and parameter combination that requires that the action be associated with a key point on the parameter,
prompts are displayed to select the parameter point to associate with the action.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*