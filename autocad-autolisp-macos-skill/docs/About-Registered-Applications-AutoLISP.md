# About Registered Applications (AutoLISP)

An application must register its name or names to be recognized by AutoCAD.

Extended data must contain an application name before it can be attached to an entity and that application name must also
exist in the APPID symbol table. Registration is done with the regapp function, which specifies a string to use as an application name. If it successfully adds the name to APPID, it returns the
name of the application; otherwise it returns nil. A result of nil indicates that the name is already present in the symbol table. This is not an actual error condition but an expected return
value, because the application name needs to be registered only once per drawing.

Before you register an application, you should first check to see if the name is not already in the APPID symbol table. If
the name is not there, the application must register it. Otherwise, it can simply go ahead and attach the extended data to
an entity for the application.

The following example code demonstrates the typical use of regapp.

```
(setq appname "MYAPP_2356")                            ; Unique application name.
(if (tblsearch "appid" appname)                        ; Checks if already registered.
  (princ (strcat "\
" appname " already registered."))

  (if (= (regapp appname) nil)                         ; Some other problem.
    (princ (strcat "\
Can't register XDATA for " appname ". "))
  )
)
```

The regapp function provides a measure of security, but it cannot guarantee that two separate applications have not chosen the same
name. One way of ensuring this is to adopt a naming scheme that uses the company or product name and a unique number (like
your telephone number or the current date and time).

#### Related Concepts

* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)
* [About Management of Extended Data Memory Use (AutoLISP)](About-Management-of-Extended-Data-Memory-Use-AutoLISP.md)
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*