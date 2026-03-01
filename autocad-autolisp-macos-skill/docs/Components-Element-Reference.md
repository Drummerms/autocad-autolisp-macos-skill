# Components Element Reference

The
Components element is used to specify the components that make up one version of the plug-in.

More than one
Components element can be used to identify the components for a plug-in; each
Components element can identify one or more components. Platform and product information for a
Components element is defined with the
RuntimeRequirements element.

If all the components defined within a
Components element apply to the same platform, you do not need to add a
RuntimeRequirements element to each individual
ComponentEntry element.

Along with the
RuntimeRequirements element, the
Components element can contain one or more of the following elements

* ComponentEntry
* RegistryEntries
* SystemVariables
* EnvironmentVariables

NOTE:A
Components element can only have one
RegistryEntries,
SystemVariables, and
EnvironmentVariables elements but can contain multiple
ComponentEntry elements.

The following outlines the basic relationship of the
Components element and any elements it can contain.

```
<Components>
  <RuntimeRequirements ... />

  <RegistryEntries>
    <RegistryEntry ... />
  </RegistryEntries>

  <SystemVariables>
    <SystemVariable ... />
  </SystemVariables>

  <EnvironmentVariables>
    <EnvironmentVariable ... />
  </EnvironmentVariables>

  <ComponentEntry ... >
    <RuntimeRequirements ... />

    <AssemblyMappings>
      <AssemblyMapping ... />
      <AssemblyMappingFolder ... />
    </AssemblyMappings>

    <Commands ...>
      <Command ... />
    </Commands>
  </ComponentEntry>

  <ComponentEntry ... />
</Components>
```

## ComponentEntry Element (AutoCAD 2013-Based Products and Later, AutoCAD LT 2024 and Later)

The
ComponentEntry element is required and is used to specify details about each individual component in the
Components element.

You can specify as many
ComponentEntry elements as needed. Component types can be one of the following file formats:

| File Format | Windows | | Mac OS | |
| AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT |
| AutoLISP Source Code (LSP) | ✓ | ✓ | ✓ | -- |
| Fast-load AutoLISP (FAS) | ✓ | ✓ | ✓ | -- |
| Compiled Visual LISP Project (VLX) | ✓ | ✓ | -- | -- |
| ObjectARX (ARX/CRX) | ✓ | -- | ✓ | -- |
| ObjectDBX (DBX) | ✓ | -- | ✓ | -- |
| Extensible Application Markup Language (XAML) | ✓ | ✓ | -- | -- |
| JavaScript (JS) | ✓ | -- | -- | -- |
| Managed or Mixed Mode .NET Assembly (DLL) | ✓ | -- | -- | -- |
| Partial Customization (CUI/CUIx) | ✓ | ✓ | -- | -- |
| Tool Palette (ATC) | ✓ | ✓ | -- | -- |
| VBA Project (DVB) | ✓ | -- | -- | -- |

A
ComponentEntry element may contain a
Commands element if the
LoadReasons attribute is set to
LoadOnCommandInvocation.

NOTE:ComponentEntry elements are loaded in the order they are listed, but from the bottom up. Therefore, any files that other components are
dependent on must be lower down the list. For example, if an ObjectARX module is dependent on an ObjectDBX module, then the
ObjectARX module will need to appear above the ObjectDBX module in the list.

A
ComponentEntry element can have any of the following attributes attached to it:

| Attribute | Description |
| AppName | Optional for AutoLISP; Required for ObjectARX and .NET - Component name; same as AppName in the ObjectARX API AcadAppInfo class. |
| AppDescription | Component description; same as AppDescription in the ObjectARX API AcadAppInfo class. |
| AppType | Component type; overrides the type derived from the file extension provided in the ModuleName attribute.  The component type can be one of the following:   * *.Net* – Managed or Mixed .NET assembly * *Arx* – ObjectARX NOTE:Required to load an ARX file from a bundle into AutoCAD for Mac. * *Atc* – Tool palette * *Bundle* - Bundle package * *Cui* or   *CuiX* – Partial customization * *Dbx* – ObjectDBX * *Dependency* – Resource DLL (not to be loaded into the AutoCAD-based product) * *JavaScript* – JavaScript * *Lisp* or   *CompiledLisp* – AutoLISP/Visual LISP * *Mnu* – Menu customization * *VBA* – VBA Project * *Xaml* – XAML file used to implement a contextual ribbon tab |
| ModuleName | Relative path to the component within the bundle; same as ModuleName in the ObjectARX API AcadAppInfo class.  The component type is determined from the file extension:   * *.atc* – Tool palette * *.arx* – ObjectARX * *.cuix* – Partial customization * *.dbx* – ObjectDBX * *.dll* – Managed .NET assembly * *.dvb* – VBA Project (AutoCAD 2015-based products and later) NOTE:DVB files require the VBA Enabler to be installed first. When loaded, the user needs to click "Enable Macros" before the project   and its macros can be accessed.  IMPORTANT:Currently, VBA Project files can only be loaded when a drawing file is open at startup which is accomplished by setting the   STARTUP system variable to a value of 0 or 1. * *.js* – Javascript (AutoCAD 2015-based products and later) * *.lsp*,   *.fas*, or   *.vlx* – AutoLISP/Visual LISP NOTE:VLX files are supported on Windows only. * *.xaml* – Extensible Application Markup Language (AutoCAD 2015-based products and later) NOTE:Attribute   XamlType must be set to "ContextualTabRule"   If your application will handle multiple languages, different versions of a specific component can be specified by combining ModuleName with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes.  NOTE:All path specifiers are '/' and not '\', and paths are relative to the root *.bundle* folder. |
| PerDocument | AutoLISP only - When True, the AutoLISP file is loaded once per document. Default is True. |
| Loadreasons | Multiple values can be specified - Defines the load behavior parameters for the component with LoadReasons and the exception of the LoadOnCommandInvocation parameter.  By default, LoadOnAutoCADStartup, LoadOnAppearance, and LoadOnProxy are enabled (set to True) if LoadReasons is not specified. If parameters need to be disabled (set to False), the LoadReasons element must be specified along with the parameters set to False.  By default, LoadOnCommandInvocation is disabled, enabling it will disable LoadOnAutoCADStartup and LoadOnAppearance unless they are explicitly enabled. If one or more Command elements is defined as part of the Components element, LoadOnCommandInvocation is implicitly enabled.  See the ObjectARX Reference Guide for full details on AcadAppInfo LoadReasons.  Valid parameter values:   * True – Parameter is enabled * False – Parameter is disabled   The following parameters are available:   * *LoadOnCommandInvocation.* Load only when a custom commands is invoked. When using this parameter, a ‘Commands’ element must be included. If   LoadOnCommandInvocation is enabled,   LoadOnAutoCADStartup and   LoadOnAppearance are assumed to be disabled unless explicitly enabled. Only applies to AutoLISP, ObjectARX, and .NET files. NOTE:For startup performance reasons, it is very important to use this option when your components define commands. * *LoadOnAutoCADStartup.* Load when the AutoCAD-based product starts up. When specified, this parameter has precedence over all other parameters. It   is recommended only to use   LoadOnAutoCADStartup when none of the other parameters are suitable, disable it (set it to False) whenever possible. If the   LoadOnAutoCADStartup parameter is omitted, then it defaults to enabled (set to True) unless   LoadOnCommandInvocation is enabled, in which case   LoadOnAutoCADStartup defaults to False. Only applies to VBA Project, ObjectARX, and .NET files. * *LoadOnProxy.* Load when a proxy for a custom entity is detected. By default, this parameter is enabled unless explicitly disabled (set   to False). When enabled (set to True),   LoadOnAutoCADStartup should be disabled. Only applies to ObjectDBX files. * *LoadOnAppearance.* Load when the product detects the application bundle in one of the   *ApplicationPlugins* folders, thereby supporting instant load on installation with no need to restart the AutoCAD-based product. The parameter   behaves the same way as   LoadOnAutoCADStartup except the load context is relevant to when an application is installed while the product is running, for instance if installed   via the Autodesk App Store website. |
| XamlType | XAML type; currently the only supported value is "ContextualTabRule" and it is required when a XAML file is assigned to the ModuleName attribute. The application file that uses the XAML file should be listed after the ComponentEntry element that contains the XAML file. |

### Commands Element (AutoCAD 2013-Based Products and Later, AutoCAD LT 2024 and Later)

The
Commands element is optional unless the
LoadOnCommandInvocation parameter is enabled for the
LoadReasons attribute. Used to specify which commands to register for
LoadOnCommandInvocation.

You can specify more than one
Command element as needed.

A
Commands element can have the following attribute attached to it:

| Attribute | Description |
| GroupName | Name used to organize related commands. |

#### Command Element (AutoCAD 2013-Based Products and Later, AutoCAD LT 2024 and Later)

Specifies the global and local names for each command.

A
Command element can have any of the following attributes attached to it:

| Attribute | Description |
| Global | Global command name. |
| Local | Local command name.  Commands can be defined for multiple languages by combining Local with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |
| HelpTopic | Help topic to open when the command is active and F1 is pressed.  NOTE:To display the help topic, a help file must be assigned to the plug-in. The help file location for the plug-in is specified with the HelpFile attribute under the ApplicationPackage element. |
| StartupCommand | Executes the command at startup when True. |

The following example adds two commands that are defined in a group named ADSKCMDS:

```
<Commands GroupName="ADSKCMDS">
    <Command Global="HELLOWORLD" Local="ADSKHELLOWORLD"/>
    <Command Global="DRAWLINE" Local="ADSKDRAWLINE"/>
</Commands>
```

### AssemblyMappings Element (AutoCAD 2013-Based Products and Later)

The
AssemblyMappings element is optional, and can contain one or more
AssemblyMapping or
AssemblyMappingFolder elements.
AssemblyMapping and
AssemblyMappingFolder elements are used to add assembly files and folder paths to internal lists that are used by AutoCAD to resolve assemblies
not found in the product installation folder.

AssemblyMapping Element (AutoCAD 2013-Based Products and Later)

| Attribute | Description |
| Name | Name of the ComponentEntry for which the assembly is associated and with which should be loaded. |
| Path | Relative path to the assembly within the bundle. |

AssemblyMappingFolder Element (AutoCAD 2022-Based Products and Later)

| Attribute | Description |
| Path | Relative path to the assemblies within the bundle. |

The following example adds two folders that contain assemblies used by a component:

```
<AssemblyMappings>
    <AssemblyMappingFolder Path="./Content/Assemblies" />
    <AssemblyMappingFolder Path="./Content/MoreAssemblies" />
</AssemblyMappings>
```

## RegistryEntries Element (AutoCAD 2015-Based Products and Later, AutoCAD LT 2024 and Later)

The
RegistryEntries element is optional, and can contain one or more
RegistryEntry elements. A
RegistryEntry element contains the definition of a registry entry that the plug-in should create or modify. Registry entries are stored
in the Windows Registry or in a property list (PLIST) file on Mac OS.

NOTE:On Windows, registry entries are created under HKEY\_CURRENT\_USER\Software\Autodesk\AutoCAD\*<release>*\ACAD-*<product>*:*<language>*. It is not possible to create registry entries in other locations. The equivalent location is used in the PLIST files on
Mac OS.

RegistryEntry Element

| Attribute | Description |
| Name | Name of the registry entry to create or modify. |
| Value | Value to assign to the registry entry.  The value can include one of the optional operator prefixes: +, -, &, and |.  See the "Variable Value Operator Prefixes" section for more information.  NOTE:The operator prefix is not retained when the value is applied to the registry entry. |
| Type | Data type to assign to the registry entry. Optional when modifying an existing registry entry.  Valid values are:   * *REG\_SZ* – String; null terminated * *REG\_EXPAND\_SZ* – String containing an unexpanded environment variable, such as %APPDATA%; null terminated * *REG\_DWORD* – 32-bit unsigned integer * *REG\_QWORD* – 64-bit signed integer   If an operator prefix is used as part of the registry entry's value, the appropriate data type must be specified. If the appropriate data type is not used, the operation will be treated as a string operation. |
| Flags | Optional, creation and modification flags. Multiple flags can be specified; use a pipe symbol to separate each flag.  The following flags are supported:   * *Create* – Registry entry is created if it does not exist. (Default behavior) * *Open* – Modifies the value of the registry entry each time the plug-in is loaded, and only when the registry entry exists. * *OpenOnce* – Modifies the value of the registry entry upon the very first time the plug-in is loaded, and only when the registry entry   exists. Uninstalling and reinstalling the plug-in causes the value of the registry entry to be changed again.   NOTE:The Open or OpenOnce flag must be used to modify the value of a registry entry. |

The following example creates the registry key MYREGKEY and adds the values STRING and NUMBER:

```
<RegistryEntries>
    <RegistryEntry
        Key="MYREGKEY"
        Name="STRING"
        Value="Example"
        Type="REG_SZ"
    />

    <RegistryEntry
        Key="MYREGKEY"
        Name="NUMBER"
        Value="123"
        Type="REG_DWORD"
    />
</RegistryEntries>
```

## SystemVariables Element (AutoCAD 2015-Based Products and Later, AutoCAD LT 2024 and Later)

The
SystemVariables element is optional, and can contain one or more
SystemVariables elements. A
SystemVariable element contains the definition of a system variable that the plug-in should create or modify.

SystemVariable Element

| Attribute | Description |
| Name | Name of the system variable to create or modify. |
| Value | Value to assign to the variable.  The value can include one of the optional operator prefixes: +, -, &, and |.  See the "Variable Value Operator Prefixes" section for more information.  NOTE:The operator prefix is not retained when the value is applied to the variable. |
| PrimaryType | Data type to assign to the variable. Optional when modifying an existing system variable.  Valid values are:   * *Int16* – 16-bit signed integer * *Int32* – 32-bit integer * *Real* – Float or double numeric value * *String* – Single or multiple character value   If an operator prefix is used as part of the variable's value, the appropriate data type must be specified. If the appropriate data type is not used, the operation will be treated as a string operation. |
| StorageType | Storage location for the variable's value; when persisted. Optional when modifying an existing system variable.  Valid values are:   * *Database* – Persisted in the drawing file the variable is created * *Profile* – Persisted as part of the current AutoCAD profile * *Session* – Not retained between sessions or in the drawing it is created * *User* – Persisted as part of the FixedProfile for AutoCAD |
| Owner | Optional, AcRX service name.  Used to make a system variable read-only and only modifiable by the application that registers the service name using acrxRegisterService(). |
| Flags | Optional, creation and modification flags. Multiple flags can be specified; use a pipe symbol to separate each flag.  The following flags are supported:   * *Create* – Variable is created if it does not exist. (Default behavior) * *Open* – Modifies the value of the variable each time the plug-in is loaded, and only when the variable exists. * *OpenOnce* – Modifies the value of the variable upon the very first time the plug-in is loaded, and only when the variable exists. Uninstalling   and reinstalling the plug-in causes the value of the variable to be changed again. * *SpacesAllowed* – Allows for the pressing of the Spacebar at the Command prompt. If not specified, pressing the Spacebar is the same as pressing   Enter.  NOTE:Use only with the Create flag and when the   PrimaryType attribute is set to String. * *DotIsEmpty* – Allows for the clearing of a variable's value by entering a "." (period) for the value of the variable.  NOTE:Use only with the Create flag and when the   PrimaryType attribute is set to String. * *NoUndo* – Changes to the variable are not recorded and cannot be undone with the U or UNDO commands.  NOTE:Use only with the Create flag. * *Chatty* – Triggers a reactor notification even when the value of the variable is set to its current value.  NOTE:Use only with the Create flag.   NOTE:The Open or OpenOnce flag must be used to modify the value of a variable. |

The following example creates a system variable named MYVARIABLE:

```
<SystemVariable
    Name="MYVARIABLE"
    PrimaryType="String"
    StorageType="User"
    Value="Example"
    Owner=""
    Flags="Create|DotIsEmpty|SpacesAllowed"
/>
```

The following example changes the value of the CURSORSIZE system variable to 100 when the plug-in is loaded the first time:

```
<SystemVariable
    Name="CURSORSIZE"
    Value="100"
    Flags="OpenOnce"
/>
```

## EnvironmentVariables Element (AutoCAD 2015-Based Products and Later, AutoCAD LT 2024 and Later)

The
EnvironmentVariables element is optional, and can contain one or more
EnvironmentVariable elements. A
EnvironmentVariable element contains the definition of an environment variable that the plug-in should create or modify. Environment variables
are stored in the Windows Registry or in a property list (PLIST) file on Mac OS.

NOTE:The value of an environment variable is always stored as a string, and the name of an environment variable is case sensitive.

EnvironmentVariable Element

| Attribute | Description |
| Name | Name of the environment variable to create or modify. |
| Value | Value to assign to the variable.  The value can include one of the optional operator prefixes: +, -, &, and |.  See the "Variable Value Operator Prefixes" section for more information.  NOTE:The operator prefix is not retained when the value is applied to the variable. |
| Type | Optional, data type that Value represents.  Valid values are:   * *Int16* – 16-bit signed integer * *Int32* – 32-bit signed integer * *Real* – Float or double numeric value * *String* – Single or multiple character value   If an operator prefix is used as part of the variable's value, the appropriate data type must be specified. If the appropriate data type is not used, the operation will be treated as a string operation. |
| Flags | Optional, creation and modification flags. Multiple flags can be specified; use a pipe symbol to separate each flag.  The following flags are supported:   * *Create* – Variable is created if it does not exist. (Default behavior) * *Open* – Modifies the value of the variable each time the plug-in is loaded, and only when the variable exists. * *OpenOnce* – Modifies the value of the variable upon the very first time the plug-in is loaded, and only when the variable exists. Uninstalling   and reinstalling the plug-in causes the value of the variable to be changed again.   NOTE:The Open or OpenOnce flag must be used to modify the value of a variable. |

The following is an example of creating two environment variables named MYNUMVAR and MYSTRVAR:

```
<EnvironmentVariables>
    <EnvironmentVariable
        Name="MYNUMVAR"
        Value="123"
    />

    <EnvironmentVariable
        Name="MYSTRVAR"
        Value="Example"
    />
</EnvironmentVariables>
```

## Operator Prefixes for Variable Values

Operator prefixes are used to modify the current value of a variable when the plug-in is loaded. You can add one of the operator
prefixes listed in the following table to the Value attribute of a
RegistryEntry,
SystemVariable, or
EnvironmentVariable element.

| Prefix | Description |
| + (plus sign) | Adds or appends a value to an existing variable's value.  *Int16, Int32, Real*: Adds *Value* to an existing variable's value.  *String*: Appends *Value* to an existing variable's value. |
| - (hyphen) | Subtracts or removes a value to an existing variable's value.  *Int16, Int32, Real*: Subtracts *Value* from an existing variable's value.  *String*: Removes *Value* from an existing variable's value. |
| & (ampersand) | Bitwise-and operation with the existing value of the variable; only numeric values are supported. |
| | (pipe symbol) | Bitwise-or operation with the existing value of the variable; only numeric values are supported. |

NOTE:If the value of a variable is supposed to start with one of the operator prefixes, add a backslash before the operator. For
example, if the variable's value is supposed to be
+radius, enter the value as
\+radius.

The following always enables the END, MID, CEN, NOD, QUA, and INT running object snaps, and leaves all other object snap settings
as-is:

```
<SystemVariable
    Name="OSMODE"
    Value="|63"
    Flags="Open"
/>
```

#### Related References

* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [RuntimeRequirements Element Reference](RuntimeRequirements-Element-Reference.md)
* [Supported Locale Codes Reference](Supported-Locale-Codes-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*