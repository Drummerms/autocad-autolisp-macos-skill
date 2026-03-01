# REGENAUTO (Command)

Controls automatic regeneration of a drawing.

## Access Methods

![](../images/ac.keyboard.gif) Command entry:  *'regenauto* for transparent use

## List of Prompts

The following prompts are displayed.

Enter mode [[ON](REGENAUTO-Command.md)/[OFF](REGENAUTO-Command.md)] <*current*>: *Enter* *on* *or* *off**, or press* Enter

On
:   Regenerates the drawing immediately if any suppressed regenerations exist in the queue and continues to regenerate automatically
    whenever you perform an action that requires regeneration.

Off
:   Inhibits regeneration of the drawing until you use the [REGEN](REGEN-Command.md) or [REGENALL](REGENALL-Command.md) command, or set REGENAUTO to on.

    If you perform an action that requires a regeneration and that action is irrevocable (such as thawing layers), the following
    message is displayed:

    Regen queued

    If you perform an action that requires a regeneration and that action is revocable, the following message is displayed:

    About to regen—proceed?

    If you click OK, the drawing is regenerated. If you click Cancel, the last action is cancelled and the drawing is not regenerated.

#### Related Concepts

* [About Improving Speed by Displaying Simplified Objects](About-Improving-Speed-by-Displaying-Simplified-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*