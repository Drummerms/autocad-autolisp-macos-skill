# Sun & Sky Properties

Sets the properties of the sun and sky.

## List of Options

The following options are displayed.

Sun - Sun Angle

Source Vector
:   Displays the coordinates of the direction of the sun. This setting is read-only.

Date and Time
:   Displays the current date and time setting.

Longitude
:   Displays the longitude of the current location. You can enter a value or select a location on the map. ([LONGITUDE](LONGITUDE-System-Variable.md) system variable)

    The valid range is -180 to +180 as a floating point number.

Latitude
:   Sets the latitude of the current location. You can enter a value or select a location on the map. ([LATITUDE](LATITUDE-System-Variable.md) system variable)

    The valid range is -90 and +90 as a floating point number.

Daylight Saving
:   Displays the current setting for daylight saving time.

Azimuth
:   Displays the angle of the sun along the horizon clockwise from due north. This setting is read-only.

Altitude
:   Displays the angle of the sun vertically from the horizon. The maximum is 90 degrees, or directly overhead. This setting is
    read-only.

Display Sun Light
:   Turns the sun on and off. If lighting is not enabled in the drawing, this setting has no effect.

Intensity Factor
:   Sets the intensity or brightness of the sun. The range is from 0 (no light) to maximum. The higher the number, the brighter
    the light.

Color
:   Controls the color of the light.

Cast Shadows
:   Turns display and calculation of shadows for the sun on and off. Turning shadows off increases performance.

Sun - Sun Disk Appearance

Disk Scale
:   Specifies the scale of the sun disk (1.0 = correct size).

Glow Intensity
:   Specifies the intensity of the sun glow. Values are 0.0-25.0.

Disk Intensity
:   Specifies the intensity of the sun disk. Values are 0.0-25.0.

Sky

Display Sky
:   Determines if the sky illumination is computed at render time. This has no impact on the viewport illumination or the background.
    It simply makes the sky available as a gathered light source for rendering. Note this does not control the background.

Intensity Factor
:   Provides a way to magnify the effect of the skylight. Values are 0.0-MAX. [1.0] is default.

Haze
:   Determines the magnitude of scattering effects in the atmosphere. Values are 0.0-15.0. [0.0] is default.

Sky - Sky Horizon

Height
:   Determines the absolute position of the ground plane relative to world zero. This parameter represents a world-space length
    and should be formatted in the current length unit. Values are -10.0 to +10.0 [0.0] is default.

Blur
:   Determines the amount of blurring between ground plane and sky. Values are 0-10. [.1] is default.

Ground Color
:   Determines the color of the ground plane.

Sky - Advanced Sky

Night Color
:   Specifies the color of the night sky.

Aerial Perspective
:   Specifies if aerial perspective is applied. Values are On/Off.

Visibility Distance
:   Specifies the distance at which 10% haze occlusion results. Values are 0.0-MAX.

Rendered Shadow Details

Type
:   Displays the setting for shadow type. This setting is read-only when display of shadows is turned off. The selections are
    Sharp, Soft (mapped) which display the Map size option and Soft (area) which displays the Samples option. Soft (area) is the
    only option for the sun in photometric workflow (LIGHTINGUNITS = 1 or 2).

Samples
:   Specifies the number of samples to take on the solar disk. This setting is read-only when display of shadows is turned off.
    Values are 0-1000.

Softness
:   Displays the setting for the appearance of the edges of shadows. This setting is read-only when display of shadows is turned
    off. Values are 1-10.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*