# BPARAMETER (Command)

Adds a parameter with grips to a dynamic block definition.

## Summary

You can use the BPARAMETER command only in the Block Editor. A parameter defines custom properties for the block reference.
After you add a parameter, you must associate an action with the parameter to make the block dynamic.

## List of Prompts

The following prompts are displayed.

Alignment

Rotates the block reference about a point to align with other objects in the drawing.

Specify Base Point of Alignment
:   Specifies the grip about which the block reference will rotate to align with another object in the drawing.

Name
:   Sets the *Name* custom property for this parameter.

Base

Defines a changeable base point for the dynamic block reference in relation to the geometry in the block.

Specify Parameter Location
:   Determines the default location of the basepoint for the block definition. This will be the location of the basepoint grip
    in the block reference.

Point

Defines custom *X* and *Y* properties for the block reference.

Specify Parameter Location
:   Determines the *X* and *Y* location of the point parameter in the block definition. This will be the location of the point grip in the block reference.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Chain
:   Determines whether the parameter is included in the selection set of an action that is associated with a different parameter.

    * *Yes.* A change to an action associated with this parameter will also trigger other actions associated with this parameter, just
      as if you had edited the parameter through a grip or custom property.
    * *No.* Associated actions are not triggered.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties Inspector.

Palette
:   Specifies whether the Label custom property is displayed in the Properties Inspector when the block reference is selected
    in a drawing.

Linear

Defines the distance between two key points in the block definition.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Chain
:   Determines whether the parameter is included in the selection set of an action that is associated with a different parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Base
:   Specifies the Base Location property for the parameter.

    * *Startpoint.* The start point of the parameter remains fixed when the endpoint of the parameter is edited in the block reference.
    * *Midpoint.* The midpoint of the parameter remains fixed, and the start point and endpoint of the parameter move simultaneously equal
      distances from the midpoint.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

Value Set
:   Limits the available values for the parameter to the values specified in the set.

    * *List.* Specifies a list of available values for the parameter in a block reference.
    * *Increment.* Specifies a value increment and minimum and maximum values for the parameter in the block reference.

Polar

Defines a distance and angle for two key points in the block definition.

Specify Base Point
:   Determines the point in the block definition relative to which the grip will be placed.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Chain
:   Determines whether the parameter is included in the selection set of an action that is associated with a different parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

Value Set
:   Limits the available values for the parameter to the values specified in the set.

XY

Defines an *X* and *Y* distance from the base point of a block definition.

Specify Base Point
:   Determines the maximum *X* distance for the parameter.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Chain
:   Determines whether the parameter is included in the selection set of an action that is associated with a different parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

Value Set
:   Value Set

Rotation

Defines an angle for the block reference.

Specify Base Point
:   Determines the point about which the selected block geometry will be rotated.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Chain
:   Determines whether the parameter is included in the selection set of an action that is associated with a different parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

Value Set
:   Value Set

Flip

Mirrors objects or the entire block reference about a reflection line.

Specify Base Point
:   Determines the first point for the line of reflection. The parameter grip will be displayed at this point.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

## Visibility

Defines objects that will either display or not display within the block definition.

Specify Parameter Location
:   Determines a location for the parameter grip. The parameter can be placed anywhere within the block definition.

Name
:   Sets the *Name* custom property for this parameter.

Label
:   Defines a custom descriptive label for the location of the parameter.

Description
:   Defines an extended description of the Label custom property. When the block reference is inserted, this description is displayed
    at the bottom of the Properties palette.

Palette
:   Specifies whether the Label custom property is displayed in the Properties palette when the block reference is selected in
    a drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*