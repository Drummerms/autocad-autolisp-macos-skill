# About Loading ObjectARX Applications

An ObjectARX application must be loaded before you can use any of its defined commands or functions.

You can load an ObjectARX application using one of the following approaches:

* Load option of the ARX or APPLOAD command and manually specify which ObjectARX application to load
* Startup Suite of the APPLOAD command to automatically load an ObjectARX file
* *arxload*  AutoLISP function and specify which ObjectARX application to load

NOTE:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

NOTE:Some ObjectARX applications use large amounts of system memory. If you are finished using an application and want to remove
it from memory, use the Unload option of the ARX or APPLOAD command.

## Automatically Load ObjectARX Applications

Some ObjectARX samples contain an
*acad.rx* file, which lists ObjectARX application files that are loaded automatically when you start an AutoCAD-based product.

You can create or edit this file with a text editor or word processor that produces files in ASCII text format, adding to
or deleting from its contents to make the appropriate ObjectARX applications available for use. As an alternative, the APPLOAD
command provides a Startup Suite option that loads the specified applications without the need to edit any files.

Because AutoCAD-based products search for the
*acad.rx* file in the order specified by the library path, you can have a different
*acad.rx* file in each drawing directory. This makes specific ObjectARX applications available for certain types of drawings. For example,
you might keep 3D drawings in a directory called
*AcadJobs/3d\_dwgs*. If that directory is set up as the current directory, you could copy the
*acad.rx* file into that directory and modify it in the following manner:

```
myapp1
otherapp
```

If you place this new
*acad.rx* file in the
*AcadJobs/3d\_dwgs* directory and you start the program with that as the current directory, these new ObjectARX applications are then loaded
and are available from the command prompt. Because the original
*acad.rx* file is still in the AutoCAD-based program files directory, the default
*acad.rx* file will be loaded if you start the program from another directory that does not contain an
*acad.rx* file.

You can load ObjectARX applications from an MNL file using the
arxload function. This ensures that an ObjectARX application, required for proper operation of a menu, will be loaded when the menu
file is loaded.

## Load an ObjectARX Application with AutoLISP

The syntax for the
arxload function is almost identical to that of the
load function used with AutoLISP files. If the
arxload function loads the ObjectARX application successfully, it returns the program name. The syntax for the
arxload function is as follows:

```
(arxload filename [onfailure])
```

The two arguments for the
arxload function are
*filename* and
*onfailure*. As with the
load function, the
*filename* argument is required and must be the complete path name description of the ObjectARX application file to load. The
*onfailure* argument is optional and typically not used when you load ObjectARX applications from the Command prompt. The following example
loads the ObjectARX application
*myapp.arx*.

```
(arxload "myapp")
```

As with AutoLISP files, the program searches the library path for the specified file. If you need to load a file that is not
in the library path, you must provide the full path name description of the file.

NOTE:When specifying a directory path, you must use a slash (/) or two backslashes (\\) as the separator, because a single backslash
has a special meaning in AutoLISP.

Attempting to load an application that has previously been loaded results in an error. Before using
arxload you should use the
arx function to check the currently loaded applications.

To unload an application with AutoLISP, use the
arxunload function. The following example unloads the
*myapp* application.

```
(arxunload "myapp")
```

Using the
arxunload function not only removes the ObjectARX application from memory but also removes the command definitions associated with
that application.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About ObjectARX Applications](About-ObjectARX-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*