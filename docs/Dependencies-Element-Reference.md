# Dependencies Element Reference

The
Dependencies element is used to specify which plug-in bundles must be available in order for another plug-in bundle to load.

There are times when one plug-in bundle might depend on the files of another plug-in bundle to run correctly. Using a
Dependencies element, you can instruct AutoCAD and AutoCAD LT to only load a plug-in bundle when a bundle with a specific upgrade code
or version is installed and loaded.

The
Dependencies element is optional, and can contain one or more
Dependency elements.
Dependency elements are used to identify which plug-in bundles must be installed and loaded before your plug-in bundle can be loaded.

Dependency Element

| Attribute | Description |
| UpgradeCode | Must be identical to the UpgradeCode attribute in the ApplicationPackage element of the dependent plug-in bundle. |
| Optional | Optional; determines whether the plug-in bundle is required, ignored if found missing.  Valid values:   * True – Bundle is required * False – Bundle is not required |
| VersionMin | Optional; defines the minimum version of the plug-in bundle in which this plug-in bundle has a dependency on.  The value is compared against the AppVersion attribute in the ApplicationPackage element of the dependent plug-in bundle. |
| VersionMax | Optional; defines the maximum version of the plug-in bundle in which this plug-in bundle has a dependency on.  The value is compared against the AppVersion attribute in the ApplicationPackage element of the dependent plug-in bundle. |

A
Dependency element can contain, or encapsulate, a
Component element. Adding a
Component element allows you to define a dependency on a specific component entry within a plug-in bundle. The
Name attribute of the
Component element must match that of the
AppName attribute of the
ComponentEntry in which this plug-in bundle has a dependency on.

The following example defines multiple dependencies on different components of the plug-in bundles with an
UpgradeCode that matches "GUID-Value":

```
<Dependencies>
  <Dependency UpgradeCode="GUID-Value" Optional="True" VersionMin="1.0"/>
  <Dependency UpgradeCode="GUID-Value" Optional="False" VersionMin="2.0" VersionMax="5.0">
      <Component AppName="App1" />
      <Component AppName="App2" />
  </Dependency>
</Dependencies>
```

#### Related References

* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [ApplicationPackage Element Reference](ApplicationPackage-Element-Reference.md)
* [Components Element Reference](Components-Element-Reference.md)
* [RuntimeRequirements Element Reference](RuntimeRequirements-Element-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*