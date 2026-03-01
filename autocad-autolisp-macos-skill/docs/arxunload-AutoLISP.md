# arxunload (AutoLISP)

Unloads an ObjectARX application

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(arxunload application [onfailure])
```

*application*
:   *Type:* String

    A quoted string or a variable that contains the name of a file that was loaded with the
    arxload function. You can omit the extension from the file name;
    *.arx/.crx* (Windows) or
    *.bundle* (Mac OS).

*onfailure*
:   *Type:* String

    An expression to be executed if the unload fails.

## Return Values

*Type:* String

The application name, if successful. If unsuccessful and the
*onfailure* argument is supplied,
arxunload returns the value of this argument; otherwise, failure results in an error message.

Note that locked ObjectARX applications cannot be unloaded. ObjectARX applications are locked by default.

## Examples

Unload the Autoloader application that was loaded in the
arxload function example:

```
(arxunload "autoloader")
"autoloader"
```

#### Related References

* [arx (AutoLISP)](arx-AutoLISP.md)
* [arxload (AutoLISP)](arxload-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*