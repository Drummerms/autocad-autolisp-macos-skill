# -VIEW (Command)

## List of Prompts

The following prompts are displayed.

Enter an option [?/Delete/Orthographic/Restore/Save/sEttings/Window]:

?—List Views
:   The list includes the name of each specified view and the space in which it was defined.
    *M* designates model space, and
    *P* designates paper space.

Delete
:   Deletes one or more named views.

Orthographic
:   Restores the predefined orthographic view you specify to the current viewport.

    ![](../images/GUID-4181D767-037D-4DA9-A287-487BEEE35931-low.png)

    The view orientation of the specified orthographic view is based on the
    [UCSBASE](UCSBASE-System-Variable.md) system variable, which is set to the world coordinate system by default. When one of the orthographic views is restored,
    the program zooms to the extents in the current viewport.

Restore
:   Restores the view you specify to the current viewport. If a UCS setting was saved with the view, it is also restored.

    The center point and magnification of the saved view are also restored. If you restore a model space view while working in
    paper space, you are prompted to select a viewport in which to restore that view.

    Select the viewport by clicking its border. The viewport you select must be on and active. The program switches to model space
    and restores the view in the selected viewport.

    If you restore a paper space view while working in model space in a layout tab, the program switches to paper space and restores
    the view. You can't restore a paper space view if you are working in the Model tab.

Save
:   Saves the display in the current viewport using the name you supply.

    The current value of the
    [UCSVIEW](UCSVIEW-System-Variable.md) system variable is displayed when you save a view. To change the setting and turn this option on or off, use the UCS option
    of VIEW.

Settings
:   Specifies various settings for the VIEW command.

    * *Categorize*. Specifies a category for the named view.
    * *Layer Snapshot*. Saves the current layer visibility settings with the new named view.
    * *Live Section*. For model views only, specifies the live section applied when the view is restored.
    * *UCS*. Determines whether the current UCS and elevation settings are saved when a view is saved. ([UCSVIEW](UCSVIEW-System-Variable.md) system variable)
    * *Visual Style*. Sets or updates a visual style for a view.

Window
:   Saves a portion of the current display as a view.

    Restoring such a view may display objects outside the window you specified because the shape of the window may differ from
    that of the viewport in which you are restoring the view. However, plotting the view plots only the objects inside the window,
    not the entire viewport display.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*