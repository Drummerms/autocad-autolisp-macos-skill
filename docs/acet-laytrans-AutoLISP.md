# acet-laytrans (AutoLISP)

Translates drawing layers to standards defined in another drawing or standards file

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows

## Signature

```
(acet-laytrans filename [settings])
```

*filename*
:   *Type:* String

    A string specifying a file containing layer mappings to be used for translation.

*settings*
:   *Type:* Integer

    A bit-coded integer specifying Layer Translator processing options. The bits can be added together in any combination to form
    a value between 0 and 15. If the
    *settings* argument is omitted, a value of 15 (all options selected) is assumed. The bit values are as follows:

    *0* -- No options

    *1* -- Force entity color to BYLAYER

    *2* -- Force entity linetype to BYLAYER

    *4* -- Translate objects in blocks

    *8* -- Write transaction log

## Return Values

*Type:* T or nil

T if translation is successful; otherwise
nil.

## Examples

The following command translates the current drawing using layer mappings saved in
*LayMap.dwg*. No transaction log will be produced, but all other processing options will be in effect.

```
(acet-laytrans "c:/my documents/cad drawings/LayMap.dwg" 7)
T
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*