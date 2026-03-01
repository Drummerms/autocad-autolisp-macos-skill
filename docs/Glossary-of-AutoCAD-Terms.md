# Glossary of AutoCAD Terms

These glossary entries span AutoCAD-based products on both Windows and Mac. While some features and types of objects are not
available in all products, drawing files can be shared between products and might contain objects or involve features from
other products.

Commands associated with definitions are shown in parentheses at the end of the definition.

3Dconnexion
:   A set of navigation tools used to control the current view of a model with a 3Dconnexion device.

3D mesh primitive
:   Basic mesh objects such as a box, cone, cylinder, pyramid, wedge, sphere, and torus defined by faceted rather than smooth
    surfaces. (MESH)

absolute coordinates
:   Coordinate values measured relative to the coordinate system's origin point (0,0,0). See also
    *origin, relative coordinates, user coordinate system (UCS), world coordinates,* and
    *world coordinate system (WCS).*

ACB
:   *For AutoCAD Color Book.* The XML file format used to store color book data that can be used in AutoCAD-based products. Some commercial color book
    files contain encrypted data to protect proprietary settings.

acquired point
:   An intermediate location used as a reference when you use the tracking or object snap tracking methods of locating a point.

acquisition marker
:   The temporary plus sign displayed at the location of an acquired point when you use the tracking or object snap tracking
    methods of locating a point.

action (AutoCAD on Windows only)
:   The smallest task or user interaction that can be recorded with the Action Recorder.

Action bar
:   A toolbar-like interface that displays the actions associated with a parameter object.

action macro (AutoCAD on Windows only)
:   A series of recorded actions that can be played back in the active drawing.

action macro file (AutoCAD on Windows only)
:   A file that stores all the actions contained in an action macro. Action macro files have the file extensions
    *.actm* or
    *.actmx*.

    NOTE:ACTM files created in AutoCAD 2024 and earlier releases must be migrated to the ACTMX file format before they can be played
    back.

Action tree (AutoCAD on Windows only)
:   A control used to display the recorded actions in an action macro.

adaptive degradation
:   A method of managing graphics performance by turning off graphic features when performance falls below a specified number
    of frames per second.

adaptive sampling
:   A method to accelerate the anti-aliasing process within the bounds of the sample matrix size. See also
    *anti-aliasing.*

add-ins
:   Libraries of content that extend the functionality of the product. Add-ins are created by third party developers and can
    be accessed either for free or at a small cost from the App tab in Autodesk Exchange web page.

adjacent cell selection
:   A selection of table cells that share at least one boundary with another cell in the same selection.

affine calibration
:   A calibration method for digitizing tablets that provides an arbitrary linear transformation in 2D space. Affine calibration
    requires three calibration points to allow a tablet transformation that combines translation, independent
    *X* and
    *Y* scaling, rotation, and some skewing. Use affine calibration if a paper drawing or map has been stretched differently in the
    horizontal or vertical direction. (TABLET)

alias
:   A shortcut for a command entered at the Command prompt. For example,
    *CP* is an alias for COPY, and
    *Z* is an alias for ZOOM. You define aliases in a product-specific .*pgp* file such as
    *acad.pgp* or
    *aclt.pgp*.

aliasing
:   The effect of picture elements, or pixels, aligned as a diagonal or curved edge that appearing jagged or stepped. See also
    *anti-aliasing.*

aligned dimension
:   A dimension that measures the distance between two points at any angle. The dimension line is parallel to the line connecting
    the dimension's definition points. (DIMALIGNED)

alpha channel
:   Alpha is a type of data, found in 32-bit bitmap files, that assigns transparency to the pixels in the image. A 24-bit truecolor
    file contains three channels of color information: red, green, and blue, or RGB. Each channel of a truecolor bitmap file is
    defined by 8 bits, providing 256 levels of intensity. The intensity of each channel determines the color of the pixel in the
    image. Thus, an RGB file is 24-bit with 256 levels each of red, green, and blue. By adding a fourth, alpha channel, the file
    can specify the transparency, or opacity, of each of the pixels. An alpha value of 0 is transparent, an alpha value of 255
    is opaque, and values in between are semi-transparent. An RGBA file (red, green, blue, alpha) is 32-bit, with the extra 8
    bits of alpha providing 256 levels of transparency. To output a rendered image with alpha, save in an alpha-compatible format
    such as PNG, TIFF, or Targa.

ambient color
:   The color reflected by an object when it is illuminated only by ambient light rather than direct light. Ambient color is
    the color of an object where it is in shadow.

ambient light
:   Light that illuminates all surfaces of a 3D model with equal intensity. Ambient light has no single source or direction and
    does not diminish in intensity over distance.

angular dimension
:   A dimension that measures angles or arc segments and consists of text, extension lines, and leaders. (DIMANGULAR)

angular unit
:   The unit of measurement for an angle. Angular units can be measured in decimal degrees, degrees/minutes/seconds, grads, and
    radians.

annotational constraint
:   A type of dimensional constraint that serves as a dimension object in addition to controlling the size of the geometry. See
    also
    *dynamic constraint.*

annotations
:   Text, dimensions, tolerances, symbols, notes, and other types of explanatory symbols or objects.

annotation scale
:   A setting that is saved with model space, layout viewports, and model views. When you create annotative objects, they are
    scaled based on the current annotation scale setting and automatically displayed in a view at the correct size.

annotative
:   An object property that is assigned to objects that are used to annotate drawings. This property automates the process of
    scaling annotations in layout viewports and in model space. Annotative objects are defined at a paper height.

anonymous block
:   An unnamed block created by several features, including associative and nonassociative dimensions.

anti-aliasing
:   A method that reduces aliasing by shading the pixels adjacent to the primary pixels that define a line or boundary. See also *aliasing.*

Application menu
:   The Windows-based menu that is displayed when you click the Application button in the upper-left corner of the application
    window. The application menu contains common tools for creating, saving, and publishing a file.

approximation points
:   Point locations that a B-spline must pass near, within a fit tolerance. See also
    *fit points* and
    *interpolation points.*

array
:   1. Multiple copies of selected objects in a rectangular or polar (radial) pattern. (ARRAY) 2. A collection of data items,
    each identified by a subscript or key, arranged so a computer can examine the collection and retrieve data with the key.

arrowhead
:   The symbol at the end of a dimension line showing where a dimension begins or ends.

aspect ratio
:   The ratio of width to height commonly associated with graphic displays and with images.

associative dimension
:   A dimension that automatically adjusts its size and value when the associated geometry is modified. (DIMASSOC system variable)
    See also
    *nonassociative dimension* and *exploded dimension.*

associative hatch
:   Hatching that conforms to its bounding objects such that modifying the bounding objects automatically adjusts the hatch.
    (BHATCH)

associative surfaces
:   Associative surfaces automatically adjust their location and shape when the geometric objects associated with them are modified.
    (SURFACEASSOCIATIVITY system variable)

attenuation
:   The diminishing of light intensity over distance.

attribute definition
:   An object that is included in a block definition to store alphanumeric data. Attribute values can be predefined, or they
    can be specified when the block is inserted. Attribute data can be extracted from a drawing and saved to a text file. (ATTDEF)

attribute extraction file
:   A text file to which extracted attribute data is written. The contents and format are determined by the attribute extraction
    template file. See also
    *attribute extraction template file.*

attribute extraction template file
:   A text file that determines what attribute data is extracted, and how the data is formatted when it is written to an attribute
    extraction file. See also
    *attribute extraction file.*

attribute prompt
:   The text prompt displayed when you insert a block containing an attribute that needs a value entered. See also
    *attribute definition, attribute tag,* and *attribute value.*

attribute tag
:   The identifying name given to an attribute, which is used during extraction of attribute data from a drawing. See also
    *attribute definition, attribute prompt,* and
    *attribute value.*

attribute value
:   The text or numeric information stored in an attribute. See also
    *attribute definition, attribute prompt,* and *attribute tag.*

AutoCAD Color Book
:   See
    *ACB*.

auxiliary projected view or auxiliary view
:   In the model documentation feature, auxiliary projected views display the true shape and relationship of features that are
    not located on planes parallel to any of the principal planes of projection.

axis tripod
:   An icon with
    *X*,
    *Y*, and
    *Z* coordinates that is used to visualize the viewpoint (view direction) of a drawing without displaying the drawing. (VPOINT)

baseline
:   An imaginary line on which text characters appear to rest. Individual characters can have descenders that drop below the
    baseline. See also *baseline dimension.*

baseline dimension
:   Multiple dimensions measured from the same baseline. Also called
    *parallel dimensions*. See also
    *baseline.*

base point
:   1. In the context of editing grips, the grip that changes to a solid color when selected to specify the focus of the subsequent
    editing operation. 2. A point for relative distance and angle when copying, moving, and rotating objects. 3. The insertion
    base point of the current drawing. (BASE) 4. The insertion base point for a block definition. (BLOCK)

base view
:   a drawing view that is projected directly from a 3D model.

basic wheels
:   A reference to the View Object wheel and Tour Building wheel.

Bezier curve
:   A polynomial curve defined by a set of control points, representing an equation of an order one less than the number of points
    being considered. A Bezier curve is a special case of a B-spline curve. See also
    *B-spline curve.*

big wheels
:   The large version of the SteeringWheels. Labels are displayed on each wheel wedge and they are larger than the size of the
    cursor.

bitcode
:   An integer representation of a binary value or the sum of multiple values. A bitcode is often associated with system variables,
    such as OSMODE and DIMZIN, but is also used to represent the current state of objects like layers and viewports. For example,
    entering a value of 3 for the OSMODE system variable specifies the Endpoint (bitcode 1) and Midpoint (bitcode 2) running object
    snaps.

bitmap
:   The digital representation of an image having bits referenced to pixels. In color graphics, a different value represents
    each red, green, and blue component of a pixel.

block
:   A generic term for one or more objects that are combined to create a single object. Commonly used for either block definition
    or block reference. (BLOCK) See also
    *block definition* and
    *block reference.*

block action
:   Defines how the geometry of a dynamic block reference will move or change when the custom properties of a block reference
    are manipulated in a drawing. A dynamic block definition usually contains at least one action that is associated with a parameter.
    (BACTION)

block authoring object
:   A dimensional constraint, parameter, or action that adds intelligence to a block definition.

block authoring palettes
:   Tool palettes used in the Block Editor to add actions and parameters to dynamic block definitions.

block authoring tools
:   Actions, parameters, and parameter sets on the tabs of the Block Authoring Palettes window. Used in the Block Editor to create
    dynamic blocks.

block constraint parameter
:   A dimensional constraint that has block authoring information associated with it. See also
    *dynamic constraint* and
    *annotational constraint .*

block definition
:   The name, base point, and set of objects that are combined and stored in the block definition table of a drawing. See also
    *block* and
    *block reference.*

block definition table
:   The nongraphical data in a drawing file that stores block definitions. Sometimes called the
    *block symbol table* or
    *block table*. See also
    *named object.*

block instance
:   *See*block reference.

block properties table
:   A table that enables users to define different values for a set of properties for the block definition. Replacement for lookup
    properties in the future.

block reference
:   A compound object that is inserted in a drawing and displays the data stored in a block definition. Also called an
    *instance*. (INSERT) See also
    *block* and
    *block definition.*

bounded area
:   A closed area that consists of a single object such as a circle or closed polyline, or of multiple, coplanar objects that
    overlap. Bounded areas are used to create objects such as hatches.

B-spline curve
:   A blended piecewise polynomial curve passing near a given set of control points. (SPLINE) See also
    *Bezier curve.*

bulge magnitude
:   The amount of curvature where two surfaces meet. This only applies to surfaces that have G1 or G2 continuity.

bump map
:   A map in which brightness values are translated into apparent changes in the height of the surface of an object.

button menu
:   The menu for a pointing device with multiple buttons. Each button on the pointing device (except the pick button) can be
    defined in the customization file, which is
    *acad.cuix* for AutoCAD and aclt.cui for AutoCAD LT.

BYBLOCK
:   A special object property used to specify that the object inherits the color or linetype of any block containing it. See
    also
    *BYLAYER.*

BYLAYER
:   A special object property used to specify that the object inherits the color or linetype associated with its layer. See also
    *BYBLOCK.*

callout block
:   A block used as symbol to reference another sheet. Callout blocks have many industry-specific terms, such as reference tags,
    detail keys, detail markers, and so on. See also
    *label block.*

camera
:   Defines the current eye-level position in a 3D model. A camera has a location
    *XYZ* coordinate, a target
    *XYZ* coordinate, and a field of view or lens length, which determines the magnification or zoom factor.

camera target
:   Defines the point you are viewing by specifying the coordinate at the center of the view.

candela
:   The SI unit of luminous intensity (perceived power emitted by a light source in a particular direction) (Symbol: cd). Cd/Sr

cell
:   The smallest available table selection.

cell boundary
:   The four gridlines surrounding a table cell. An adjacent cell selection can be surrounded with a cell boundary.

cell style
:   A style that contains specific formatting for table cells.

chain actions
:   In a dynamic block definition, a property of point, linear, polar, XY, and rotation parameters. When set to Yes, a change
    in an action that contains the parameter in the action's selection set triggers any actions associated with that parameter,
    just as if you had edited the parameter in the block reference through a grip or custom property.

change set
:   A cluster of differences within the margin distance of the revision cloud that's automatically generated by the DWG Compare
    feature.

circular external reference
:   An externally referenced drawing (xref) that references itself directly or indirectly. The xref that creates the circular
    condition is ignored.

clamp curve
:   A smooth, closed curve such as a circle. Because it has a vertex that is tangent to the object, if the curve is reshaped,
    it may create kinks. See also
    *periodic curve*.

clamp surface
:   A smooth, closed surface such as a cylinder. Because it has a vertex that is tangent to the object, if the surface is reshaped,
    it may create kinks. See also
    *periodic surface.*

clipping planes
:   The boundaries that define or clip the field of view.

cloud computing
:   Refers to executing software and storing data on shared servers over the internet.

CMYK
:   For
    *cyan, magenta, yellow, and key color*. A system of defining colors by specifying the percentages of cyan, magenta, yellow, and the key color, which is typically
    black.

coincident grip
:   A grip shared by multiple objects.

Color bleed scale
:   Increases or decreases the saturation of the reflected color from the material.

color map
:   A table defining the intensity of red, green, and blue (RGB) for each displayed color.

column (table)
:   A vertically adjacent table cell selection spanning the height of the table. A single column is one cell in width.

command line
:   A text area reserved for keyboard input, prompts, and messages.

comparison drawing
:   The drawing file that you specify to compare with the current drawing using the DWG Compare feature.

compass
:   A visual aid that indicates the directions North, South, East, and West in the current model.

composite solid
:   A solid created from two or more individual solids. (UNION, SUBTRACT, INTERSECT)

constraint bar
:   Displays the geometric constraints associated with objects or with points on objects.

constraint point
:   Point on an object that can be geometrically or dimensionally constrained (for example, an endpoint or an insertion point).

constraints
:   1. A form of parametric design. 2. Rules that govern the position, slope, tangency, dimensions, and relationships among objects
    in a geometry.

construction plane
:   *See* work plane.

context menu
:   *See* shortcut menu.

contextual ribbon tab
:   In products that use Microsoft Windows, a ribbon tab that is displayed only when a certain type of object is selected, or
    when a certain command is started. For example, selecting a hatch or table, or starting the MTEXT command displays a corresponding
    contextual ribbon.

continued dimension
:   A type of linear dimension that uses the second extension line origin of a selected dimension as its first extension line
    origin, breaking one long dimension into shorter segments that add up to the total measurement. Also called
    *chain dimension*. (DIMCONTINUE)

continuity
:   A measure of how smoothly two curves or surfaces merge into each other where they are joined. Continuity is defined as G0
    (position), G1 (tangency), and G2 (curvature).

    * *G0 (Position)* - The curves or surfaces join in the same location (position only); they touch. But the tangency and curvature do not match.
    * *G1 (Tangent)* - The position and tangency between the surfaces match. This indicates G1 (position and tangency) continuity between the
      surfaces.
    * *G2 (Curvature)* - The position, tangency, and curvature between the surfaces match. This indicates G2 (position, tangency, and curvature)
      continuity between the two surfaces.

control frame
:   A series of point locations used as a mechanism to control the shape of a B-spline. These points are connected by a series
    of line segments for visual clarity and to distinguish the control frame from fit points. The CVSHOW and CVHIDE commands must
    be turned on to display and hide control frames.

control vertices (CVs)
:   The most basic way to shape a NURBS surface or spline. These points act as grips that can be dragged to reshape the object.

Coons patch
:   In 3D surface meshes, the bicubic surface (one curved in the M direction and another in the N direction) interpolated between
    four edges.

coordinate filters
:   Functions that extract individual
    *X*,
    *Y*, and
    *Z* coordinate values from different points to create a new, composite point. Also called
    *X,Y,Z point filters*.

coordinate system or coordinate reference system
:   In the geolocation feature, a spatial reference system that consists of a map projection and datum. Coordinate systems come
    in various types such as geographic, projected, etc. A CS always specifies the units of measurement.

coordination model
:   A model used for virtual coordination of various trades through the pre-construction and construction phases of a project.
    It specifically refers to an NWD or NWC file.

crease
:   A sharpened ridge that defines one or more edges of a mesh face subobject. (MESHCREASE)

crosshairs
:   A type of cursor consisting of two lines that intersect.

crossing selection
:   A rectangular area drawn to select objects fully or partly within its borders.

cross sections
:   Generally, curves or lines that define the profile (shape) of a lofted solid or surface. Cross sections can be open or closed.
    A lofted solid or surface is drawn in the space between the cross sections. (LOFT)

CTB file
:   For
    *Color-Dependent Plot Style Table* file. Contains plot styles and their characteristics defined by their color assignments.

ctrl-cycle
:   A method for cycling between different behaviors while editing geometry, either in a command or when grip-editing. Pressing
    and releasing the Ctrl key cycles the behavior. For constrained geometry, Ctrl-cycling switches between enforcing and relaxing
    constraints.

current directory
:   See
    *working folder*.

current drawing
:   A drawing file that is open in the program, and receives any command or action that you enter.

current location indicator
:   In the geolocation feature, a transient blue pin placed in model space that indicates the current location of a device. A
    concentric circle drawn at its base denotes the margin of error in its location. Location sensors must be enabled to view
    the current position indicator.

cursor
:   *See*pointer and crosshairs.

cursor menu
:   *See*shortcut menu.

curve-fit
:   A smooth curve consisting of arcs joining each pair of vertices. The curve passes through all vertices of the polyline and
    uses any tangent direction you specify.

custom grips
:   In a dynamic block reference, used to manipulate the geometry and custom properties.

customization file
:   An XML-based file such as
    *acad.cuix* or
    *acadlt.cuix* that stores customization data. You modify a customization file through the Customize User Interface Editor (Windows) or
    the Customize dialog box (Mac). CUIx files replace MNU, MNS, and MNC files that were used to define menus in earlier releases.
    CUIx and CUI files are not interchangeable between Mac and Windows.

custom object
:   A type of object that is created by an ObjectARX application and that typically has more specialized capabilities than standard
    objects. Custom objects include parametric solids (AutoCAD Mechanical Desktop), intelligently interactive door symbols (AutoCAD
    Architecture), polygon objects (AutoCAD Map 3D), and associative dimension objects (AutoCAD and AutoCAD LT). See also
    *proxy object* and
    *object enabler.*

CV hull
:   A NURBS surface is modified through its control vertices (CV) hull. It consists of the control vertices and the lines that
    connect them in the U and V directions The hull sits outside of (not on) the surface. NURBS
    *curves*do not have a CV hull; they only have control vertices.

data link
:   A connection between a table and an external source of data.

datum
:   In the geolocation feature, a reference point from which measurements are made for a coordinate system.

decimal degrees
:   A notation for specifying latitude and longitude. For example, 35.1234°, 100.5678°. Latitude always precedes longitude.

default
:   A predefined, assumed value for a program input, setting, or parameter. Default values and options for commands are denoted
    by angle brackets (<>). See also
    *default value.*

default drawing
:   See *initial environment.*

default lighting
:   The lighting in a shaded viewport when the sun and user lights are turned off. Faces are lighted by two distant light sources
    that follow the viewpoint as you move around the model.

default value
:   The value that is accepted when you press Enter at a sub-prompt. The default value is displayed in angle brackets <>. See
    also
    *default.*

definition (symbol) table
:   The nongraphical data area in a drawing file that stores definitions of blocks, dimension styles, layers, and other named
    objects. See also
    *named objects.*

definition point
:   A node located at the end of an extension line corresponding to the location on the object being dimensioned. Definition
    points, also called
    *defpoints*, are stored on the reserved, non-plotting Defpoints layer.

degree
:   A mathematical property of a curve or a surface that indicates the type of polynomial equation being used. For example, equations
    of degree 1 are linear, degree 2 are quadratic, and degree 3 are cubic.

dependency highlighting
:   In a dynamic block definition, how associated objects are displayed when you select a parameter, grip, or action.

dependent named objects (in xrefs)
:   Named objects brought into a drawing by an xref. See also
    *named object* and *symbol table.*

dependent symbols
:   *See*dependent named objects (in xrefs).

Design Coordinate System
:   In the geolocation feature, an AutoCAD specific coordinate system that provides flexibility in choosing a different unit of
    measure, insertion point, and orientation than that specified by the coordinate system (CS).

detail view
:   In the model documentation feature, refers to a projected view that displays a specified portion of another drawing view,
    typically at an enlarged scale.

detail view label
:   In the model documentation feature, refers to the customizable text that identifies a detail view, often indicating the scale.

DGN underlay
:   *See* underlay.

DIESEL
:   For
    *Direct Interpretively Evaluated String Expression Language*. A macro language for altering the status line with the MODEMACRO system variable and for customizing menu items. DIESEL
    is available for AutoCAD-based products running under Windows.

diffuse color
:   The color that an object reflects when illuminated by direct daylight or artificial light that makes the object easy to see.

digital signature
:   An encrypted digital code added to a file for assuring the authenticity of digital messages, documents, and programs, and
    that they have not been altered.

dimensional constraint
:   A parametric dimension that controls the size, angle, or position of geometry relative to the drawing or to other objects.
    When the value of a dimensional constraint is changed, the constrained object resizes. See also *annotational constraint* and
    *dynamic constraint*.

dimension line arc
:   An arc, which usually has arrowheads at each end, that spans the angle formed by the extension lines of the angle being measured.
    The dimension text near this arc sometimes divides it into two arcs. See also
    *angular dimension.*

dimension style
:   A named group of dimension settings that determines the appearance of the dimension and simplifies the setting of dimension
    system variables. (DIMSTYLE)

dimension text
:   The measurement value of dimensioned objects.

dimension variables
:   A set of numeric values, text strings, and settings that control dimensioning features. (DIMSTYLE)

direct distance entry
:   A method to specify a second point by first moving the cursor to indicate direction, and then entering a distance.

dithering
:   Combining color dots to give the impression of displaying more colors than are actually available.

dockable window
:   In AutoCAD-based products under Windows, a user interface element that can be docked, anchored, or floating in the drawing
    area. Dockable windows include the command window, tool palettes, the Properties palette, and so on.

drawing area
:   The area in which your drawings are displayed and modified.

drawing extents
:   The smallest rectangular area that contains all objects in a drawing. (ZOOM)

drawing folder
:   The drive and folder path of the current drawing. (DWGPREFIX system variable)

drawing limits
:   See
    *grid limits.*

drawing set
:   A collection of drawings assembled using the Publish dialog box.

drawing state
:   A collection of known settings that define the behavioral properties of the drawing environment and/or drawing at a known
    period of time, such as when an action macro was recorded or before the playback of an action macro.

drawing template (DWT) file
:   A drawing file with preestablished settings for new drawings such as
    *acad.dwt*,
    *acadlt.dwt*,
    *acadiso.dwt*, or
    *acadltiso.dwt*. Any drawing file can be saved as a DWT file. See also *initial environment.*

drawing view
:   A rectangular object that contains a 2D projection of a 3D model.

driving dimension
:   A parametric dimension that determines the size of geometry and resizes the object when its value changes.

driving property
:   A lookup property is considered invertible when a manual change in the lookup value for a block reference causes other properties
    values change.

DSD
:   For
    *drawing set descriptions*. A file format for saving a description of a drawing set that has been assembled using the Publish dialog box.

DST
:   For
    *sheet set data*. The XML file format used to store the associations and information that define a sheet set.

DWF
:   An open, published, and secure file format developed by Autodesk, DWF enables you to combine and publish design data and
    share it with others.

DWF underlay
:   See
    *underlay.*

DWFx
:   A version of DWF based on the XML Paper Specification (XPS) from Microsoft. DWFx enables DWF files to be viewed using the
    free Microsoft XPS Viewer. Generically referred to as DWF.

DWG
:   The standard file format for saving AutoCAD-based vector graphics. See also
    *DWF* and
    *DXF.*

DXF
:   For
    *drawing interchange format*. An ASCII or binary file format of a drawing file for exporting drawings to other applications or for importing drawings
    from other applications. See also
    *DWF* and
    *DWG.*

dynamic constraint
:   A type of dimensional constraint that adjusts its size automatically, and can be displayed or hidden. See also
    *annotational constraint .*

dynamic dimension
:   Temporary dimensions that appear on objects, including dynamic block references, when they are edited with grips.

edge
:   The boundary of a face.

edge modifiers
:   Effects such as overhang and jitter that control how edges are displayed in a shaded model.

electronic drawing set
:   The digital equivalent of a set of plotted drawings. You create an electronic drawing set by publishing drawings to a multi-sheet
    DWF file.

embed (OLE)
:   An embedded object is a copy of the information from a source document that is placed in the destination document, and is
    not linked to the source document. See also
    *link*.

empty selection set
:   A selection set that contains no objects.

enterprise customization file
:   A CUIx file that is typically controlled by a CAD manager. It is often accessed by many users and is stored in a shared network
    location. The file is read-only to users to prevent the data in the file from being changed. A CAD manager creates an enterprise
    CUxI file by modifying a main CUIx file and then saving the file to the support location defined in the Options dialog box,
    Files tab.

environment map
:   A bitmap that is used to simulate reflections in materials that have reflective properties. The map is “wrapped” around the
    scene and any reflective object will show the appropriate portion of the map in the reflective parts of its material.

environment variable
:   A setting stored in the operating system that controls the operation of a program.

expanded panel
:   In AutoCAD-based products on Windows, an area on the ribbon associated with a ribbon panel. An expanded panel contains additional
    tools and controls. See also
    *ribbon panel* and
    *ribbon.*

explode
:   To disassemble a complex object, such as a block, dimension, solid, or polyline, into simpler objects. In the case of a block,
    the block definition is unchanged. The block reference is replaced by the components of the block. (EXPLODE) See also
    *block, block definition,* and
    *block reference.*

exploded dimension
:   A set of objects that have the appearance of a dimension but are not associated with the dimensioned object or each other.
    Controlled by the DIMASSOC system variable. (EXPLODE) See also
    *associative dimension, nonassociative dimension,* and
    *explode*.

extended command history
:   An  expanded list of commands and prompts that extends up or down from the command line. If the command line window is undocked,
    you can display this history by pressing F2 or by clicking the arrow at the right end of the Command Line window. The extended
    command history contains the same information as the text screen, which can be displayed by entering TEXTSCR or by pressing
    F2 when the window is docked. See also
    *extended prompt history.*

extended tooltips
:   In AutoCAD-based products on Windows, displays additional information in a tooltip when the cursor hovers over a tool for
    a specific length of time.

extents
:   See
    *drawing extents.*

external reference
:   A file referenced from a drawing file. An external reference is a link to the referenced file. Supported external references
    include the following file types: DWG, raster images, DWF, DWFx, DGN, PDF, and PCG (point cloud). (EXTERNALREFERENCES) See
    also
    *xref.*

extrusion
:   A 3D solid created by sweeping an object that encloses an area along a linear path. (EXTRUDE)

face
:   A triangular or quadrilateral portion of a solid or surface object.

face color mode
:   A setting in the visual style that controls how color is displayed on a face.

face style
:   A setting in the visual style that defines the shading on a face.

facet
:   A triangular or quadrilateral portion of a 3D mesh object. Smoothing a mesh object increases the number of facets.

feature control frame
:   The tolerance that applies to specific features or patterns of features. Feature control frames always contain at least a
    geometric characteristic symbol to indicate the type of control and a tolerance value to indicate the amount of acceptable
    variation.

fence
:   A multi-segmented selection line that selects objects as it passes through them. (SELECT)

field
:   A specialized text object set up to display data that may change during the life cycle of the drawing. When the field is
    updated, the latest value of the field is displayed. (FIELD)

file tab
:   A tab at the top of the drawing window that corresponds to an open drawing.

fill
:   A solid color covering an area bounded by lines or curves. (FILL)

filters
:   See
    *coordinate filters.*

final gathering
:   An optional, additional step for calculating global illumination. Using a photon map to calculate global illumination can
    cause rendering artifacts such as dark corners and low-frequency variations in the lighting. You can reduce or eliminate these
    artifacts by turning on final gathering, which increases the number of rays used to calculate global illumination. Final gathering
    can greatly increase rendering time. It is most useful for scenes with overall diffuse lighting, less useful for scenes with
    bright spots of indirect illumination. You turn on final gathering on the Advanced Render Settings palette. See also *global illumination.*

fit points
:   Locations that a B-spline must pass through exactly or within a fit tolerance. See also
    *interpolation points* and
    *approximation points.*

fit tolerance
:   The setting for the maximum distance that a B-spline can pass for each of the fit points that define it.

floating panel
:   In AutoCAD-based products on Windows, a ribbon panel that is not attached to the rest of the ribbon or file window.

floating viewports
:   See
    *layout viewports.*

font
:   A character set, made up of letters, numbers, punctuation marks, and symbols of a distinctive proportion and design.

footcandle
:   The American unit of illuminance (symbol: fc). Lm/ft^2.

frame
:   An individual, static image in an animated sequence. See also
    *motion path.*

freeze
:   A setting that suppresses the display of objects on selected layers. Objects on frozen layers are not displayed, regenerated,
    or plotted. Freezing layers shortens regenerating time. (LAYER) See also
    *thaw.*

front faces
:   Outward-facing sides of 3D faces.

G0, G1, G2 continuity
:   See
    *continuity.*

general properties
:   Properties that are common between a selection of objects. These include color, layer, linetype, linetype scale, plot style,
    lineweight, transparency, hyperlink, and thickness.

generic surface
:   A 3D surface object with no control vertices, history, or analytic information. Generic surfaces cannot be associative and
    they are created when associative analytic surfaces are separated or by using the BREP command. See also
    *procedural surface* and
    *NURBS surface.*

geographic coordinate system
:   In the geolocation feature, a geographic coordinate system is a reference system that uses a three-dimensional spherical surface
    to determine locations on the earth.

geographic elevation
:   The relative height along the specified up-direction defined for a geographic marker.

geographic marker
:   In the geolocation feature, an annotation that marks a location of known latitude and longitude in model space. The geographic
    marker is used as a reference point for all geographic location data in a drawing file.

geo marker
:   See
    *geographic marker.*

geometric constraint
:   Rules that define the geometric relationships of objects or points on objects, which control how an object can change shape,
    size, or location. Examples include coincident, collinear, concentric, equal, fix, horizontal, parallel, perpendicular, tangent,
    and vertical constraints.

geometry
:   All graphical objects such as lines, circles, arcs, polylines, and dimensions. See also
    *named object.*

gesture
:   Predefined motions such as swiping, pinching, or sliding that perform an action such as panning or zooming an object.

gizmo
:   A tool that permits you to manipulate a 3D object uniformly or along a specified axis or plane. Examples of gizmos include
    the 3D Move, 3D Rotate, and 3D Scale gizmos. They are displayed when you select a 3D object.

global illumination
:   An indirect illumination technique that allows for effects such as color bleeding. As light hits a colored object in the
    model, photons bounce to adjacent objects and tint them with the color of the original object.

Gooch shading
:   A type of shading that uses a transition from cool to warm colors rather than from dark to light.

graphics area
:   See
    *drawing area.*

grid
:   An area covered with regularly spaced dots or lines to aid drawing. The grid spacing is adjustable. The grid is never plotted.
    (GRID) See also
    *grid limits.*

grid limits
:   The user-defined rectangular boundary of the drawing area covered by dots when the grid is turned on. Also called
    *drawing limits*. (LIMITS)

grip menu options
:   *See*multi-functional grip menu options.

grip modes
:   The editing options that you can access from selected grips on selected objects: stretching, moving, rotating, scaling, and
    mirroring.

grips
:   Small squares and triangles that appear on objects that you select. After selecting the grip, you can edit the object by
    clicking or right-clicking the grip instead of entering commands.

grip tool
:   An icon that you use in a 3D view to easily constrain the movement or rotation of a selection set of objects to an axis or
    a plane. (3DMOVE, 3DROTATE)

ground plane
:   The
    *XY* plane of the user coordinate system when perspective projection is turned on. The ground plane displays with a color gradient
    between the ground horizon (nearest to the horizon) and the ground origin (opposite the horizon). See also
    *sky* and
    *underground.*

guide curves
:   Lines or curves that intersect each cross section of a lofted solid or surface and that define the form by adding additional
    wireframe information to the object. (LOFT)

HDI
:   For *Heidi Device Interface*. An interface for developing peripheral device drivers for Autodesk products on Windows.

helix
:   An open 2D or 3D spiral. (HELIX)

HLS
:   A system of defining color by specifying the values for
    *hue, saturation, and luminance*.

Home view
:   A view that is saved with the drawing and is controlled with the ViewCube tool. The Home view is similar in concept to the
    default, initial view presented when a drawing is first opened.

horizontal landing
:   An optional line segment connecting the tail of a leader line with the leader content.

hot grip
:   A selected grip.

i-drop
:   A method by which a drawing file can be dragged from a Web page and inserted into another drawing.

IGES
:   For
    *Initial Graphics Exchange Specification*. A standard format for digital representation and exchange of information between CAD/CAM systems. In AutoCAD-based products,
    the commands to import and export IGES files are available only in AutoCAD Mechanical.

Illuminance
:   In photometry, illuminance is the total luminous flux incident on a surface per unit area.

indirect bump scale
:   Scales the effect of the base material’s bump mapping in areas lit by indirect light.

indirect illumination
:   Illumination techniques such as global illumination and final gathering, that enhance the realism of a scene by simulating
    radiosity, or the interreflection of light between objects in a scene.

initial environment
:   The variables and settings for new drawings as defined by the default drawing template file, such as
    *acad.dwt*,
    *acadlt.dwt*,
    *acadiso.dwt*, or
    *acadltiso.dwt*. See also
    *template drawing.*

input property
:   In a dynamic block definition, a parameter property other than that of a lookup, alignment, or base point parameter that you
    can add as a column to a lookup table. When the parameter values in a dynamic block reference match a row of input property
    values, the corresponding lookup property values in that table row are assigned to the block reference. (BLOOKUPTABLE)

intensity
:   In the reality capture feature, intensity is one type of point attribute contained in the raw scan file which is the reflectance
    of each point from laser return.

    In the rendering feature, intensity specifies the brightness of a light. The number of candelas (cd) is the SI unit of luminous
    intensity (perceived power emitted by a light source in a particular direction).

interpolation points
:   Defining points that a B-spline passes through. See also
    *approximation points* and *fit points.*

island
:   An enclosed area within another enclosed area. Islands may be detected as part of the process of creating hatches, polylines,
    and regions. (BHATCH, BOUNDARY)

isolines
:   Display lines that appear on the curved surfaces of 3D solids with several visual styles including wireframe. Encompasses
    the display lines on both 3D solids (ISOLINES) and surfaces (SURFU, SURFV).

isometric snap style
:   A drafting option that aligns the cursor with two of three isometric axes and displays grid, making 2D isometric drawings
    easier to create.

isoparm
:   Lines of constant
    *U* or
    *V* values that run along a NURBS surface. They show the shape of the surface as defined by the control vertices. AutoCAD uses
    the term
    *isolines*.

key point
:   In a dynamic block definition, the point on a parameter that drives its associated action when edited in the block reference.

KML or keyhole mapping language [reality capture]
:   In the reality capture feature, an XML grammar and file format for modeling and storing geographic features such as points,
    lines, images, polygons, and models for display in Google Earth, Google Maps, and other applications.

KMZ
:   In the reality capture feature, a compressed version of a KML file.

knot parameterization
:   A setting that affects the shape of a fit point spline, which is one of several computational methods that determine how the
    component curves between successive fit points within a spline are blended. (SPLKNOTS system variable).

label block
:   A block used to label views and details. Labels contain data, such as a title, view number, and scale, that is associated
    with the referenced view. See also *callout block.*

landing
:   The portion of a leader object that acts as a pointer to the object being called out. A landing can either be a straight line
    or a spline curve.

landing gap
:   An optional space between a leader tail and the leader content.

layer
:   A logical grouping of data that are like transparent acetate overlays on a drawing. You can view layers individually or in
    combination. (LAYER)

layer index
:   A list showing the objects on each layer. A layer index is used to locate what portion of the drawing is read when you partially
    open a drawing. Saving a layer index with a drawing also enhances performance when you work with external references. The
    INDEXCTL system variable controls whether layer and spatial indexes are saved with a drawing.

layer translation mappings
:   Assignments of a set of layers to another set of layers that defines standards. These standards include layer names and layer
    properties. Also called
    *layer mappings*.

layout
:   The 2D environment in which you create layout viewports and place title blocks for plotting. Multiple layouts can be created
    for each drawing.

layout viewports
:   Objects that are created in paper space that display views. (VPORTS) See also
    *paper space.*

leader tail
:   The portion of a leader line that is connected to the annotation.

lens length
:   Defines the magnification properties of a camera's lens. The greater the lens length, the narrower the field of view.

level of smoothness
:   The property assigned to a mesh object that controls how much the edges of the object are smoothed. Higher levels result in
    more faces and increased smoothness.

library search path
:   The order in which the product looks for a support file: current folder, drawing folder, the folder specified in the support
    path, and the folder containing the executable file.

light glyph
:   The graphic representation of a point light or a spotlight.

limits
:   See
    *drawing limits.*

line font
:   See
    *linetype.*

linetype
:   How a line or curve is displayed. For example, a continuous line has a different linetype than a dashed line. Also called
    *line font*. (LINETYPE)

lineweight
:   A width value that can be assigned to all graphical objects except TrueType ®  fonts and raster images.

link (OLE)
:   To use object linking and embedding (OLE) to reference data in another file. When data is linked, any changes to it in the
    source document are automatically updated in any destination document. See also
    *embed.*

LL84 coordinate system
:   Common latitude longitudinal-based coordinate system where latitude and longitude are both measured from -90 to 90 degrees.
    Longitude begins at 0 degrees at the Prime Meridian in Greenwich, England and is measured from -180 to 180. Latitude is 0
    degrees at the equator and is measured from -90 to 90.

lofted solid or surface
:   A solid or surface that is drawn through a set of two or more cross-section curves. The cross sections define the profile
    (shape) of the resulting solid or surface. Cross sections can be open or closed. (LOFT)

lookup property
:   In a dynamic block definition, a lookup parameter that you add to a lookup table. The lookup parameter label is used as the
    property name. When the parameter values in a dynamic block reference match a row of input property values, the corresponding
    lookup property values in that table row are assigned to the block reference. (BLOOKUPTABLE)

lookup table
:   Defines properties for and assigns property values to a dynamic block. Assigns property values to the dynamic block reference
    based on how the block is manipulated in a drawing. (BLOOKUPTABLE)

lumen
:   The SI unit of luminous flux (Symbol: lm). Cd \* Sr

luminaire
:   The aggregation of a lamp or lamps and its fixture. The fixture may be a simple can or a complex armature with constrained
    joints.

luminance
:   The value of light reflected off a surface. It is a measure of how bright or dark that we perceive the surface.

luminous flux
:   The perceived power in per unit of solid angle. The total luminous flux for a lamp is the perceived power emitted in all directions.

lux
:   The SI unit of illuminance (symbol: lx). Lm/m^2

macro-derived selection
:   A selection set of all the objects that have been created during the playback of an action macro up to the command that is
    requesting a selection set.

magnitude
:   *See* bulge magnitude.

main customization file
:   Windows: The CUIx file that defines most of the user interface elements, including the standard menus, toolbars, keyboard
    accelerators, and so on. The
    *acad.cuix* or
    *acadlt.cuix* file (the default main CUI file) is automatically loaded when you start the product.

map image
:   In the geolocation feature, a transient map retrieved from an online service provider, and displayed in the drawing area to
    cover the region specified by the assigned coordinate system. You can choose whether the map type is aerial, road, survey,
    etc. The map data cannot be saved within the drawing file.

markup
:   A single comment or markup geometry correction inserted into a DWF file using Autodesk Design Review.

markup set
:   A group of markups contained within a single DWF file.

merge
:   In tables, an adjacent cell selection that has been combined into a single cell.

mesh
:   A tessellated, or subdivided object type that is defined by faces, edges, and vertices. Mesh can be smoothed to achieve a
    more rounded appearance and creased to introduce ridges.

mini wheels
:   The small version of SteeringWheels. No labels are displayed on any of the wedges and they are often the size of the cursor.

mirror
:   To create a new version of an existing object by reflecting it symmetrically with respect to a specified line or plane. (MIRROR)

mode
:   A software setting or operating state.

model
:   A 2D or 3D representation of a mechanical part, house or building, piping, electrical circuitry, schematic or diagram, or
    some other entity.

model documentation
:   A feature that generates associative 2D drawings from AutoCAD and Autodesk Inventor 3D models.

model edge
:   In the model documentation feature, refers to the style of the cutout line displayed by a detail view: whether it is smooth
    or jagged, whether it has a border, and whether it includes a connection line.

model space
:   One of the two primary spaces in which objects reside. Typically, a geometric model is created in model space. A layout of
    specific views and annotations of this model is displayed on a layout in paper space. (MSPACE) See also *paper space.*

model viewports
:   A feature that splits the drawing area into one or more adjacent rectangular viewing areas. (VPORTS) See also
    *layout viewports, TILEMODE,* and
    *viewport.*

motion path
:   Defines the path or target of a camera. A path can be a line, arc, elliptical arc, circle, polyline, 3D polyline, or spline.

multi-functional grip menu options
:   Editing options you can access from the grip menu that appears when you hover over an object grip (not available for all
    object types).

multileader
:   A leader object that creates annotations that can have multiple leader lines.

multi-sheet DWF
:   A DWF file that contains multiple sheets.

My Location indicator
:   An indicator in model space that shows your current location in GPS-enabled systems.

named object
:   Describes the various types of nongraphical information, such as styles and definitions, stored with a drawing. Named objects
    include linetypes, layers, dimension styles, text styles, block definitions, layouts, views, and viewport configurations.
    Named objects are stored in definition (symbol) tables.

named objects, dependent
:   *See*dependent named objects (in xrefs).

named path
:   A saved motion path object that is linked to a camera or target.

named range
:   A tool in Microsoft Excel that provides a method to assign a meaningful name to a single cell or a range of cells.

named view
:   A view saved that can be restored later. (VIEW)

navigation bar
:   Navigation tools that are common across multiple Autodesk products that run on the Windows operating system. The unified
    navigation tools include Autodesk® ViewCube®, SteeringWheels®, ShowMotion®, and 3Dconnexion®.

node
:   A type of object snap that locates point objects, dimension definition points, and text origin points.

non-associative dimension
:   A dimension that does not automatically change as the associated geometry is modified. Controlled by the DIMASSOC system
    variable. See also
    *associative dimension* and
    *exploded dimension.*

normal
:   A normal is a vector that defines the direction that a face is pointing, orthogonal to its surface. The direction of the
    normal indicates the front, or outer surface of the face.

noun-verb selection
:   Selecting an object first and then performing an operation on it rather than entering a command first and then selecting
    the object.

NURBS
:   For
    *nonuniform rational B-spline curve*. A B-spline curve or surface defined by a series of weighted control points and one or more knot vectors. See also
    *B-spline curve.*

NURBS surface
:   A smoothly joined set of four-sided patches defined by NURBS curves. The NURBS curves are located along and across the surface
    in the U and V directions, and they intersect in control vertices. See also
    *procedural surface*and
    *generic surface.*

object
:   One or more graphical elements, such as text, dimensions, lines, circles, or polylines, treated as a single element for creation,
    manipulation, and modification. Formerly called
    *entity*.

ObjectARX (Runtime Extensions)
:   A compiled-language programming environment that runs under the Windows operating system used for developing product-specific
    applications and extensions.

object enabler
:   A tool that provides specific viewing and standard editing access to a custom object when the ObjectARX application that
    created the custom object is not present. Available only for AutoCAD-based products that run on the Windows operating system.
    See also
    *custom object* and
    *proxy object.*

Object Snap mode
:   A method for specifying commonly needed point locations on an object when you create or edit objects. With object snaps,
    you can specify the precise location of the center of a selected circle, or the intersection of two curves. See also
    *running object snap* and
    *object snap override.*

object snap override
:   Turning off or changing a running Object Snap mode for input of a single point. See also
    *Object Snap mode* and
    *running object snap.*

OLE
:   For
    *object linking and embedding*. An information-sharing method available in the Windows operating system in which data from a source document can be linked
    to or embedded in a destination document. Selecting the data in the destination document opens the source application so that
    the data can be edited. See also
    *embed* and
    *link.*

online
:   Content and applications accessible from the internet.

opacity map
:   Projection of opaque and transparent areas onto objects, creating the effect of a solid surface with holes or gaps.

origin
:   The point where coordinate axes intersect. For example, the origin of a Cartesian coordinate system is where the
    *X*,
    *Y*, and
    *Z* axes meet at 0,0,0.

orthogonal
:   An orientation of two objects when they have perpendicular slopes or tangents at the point of their intersection.

Ortho mode
:   A setting that limits pointing device input to horizontal or vertical directions relative to the current snap angle and user
    coordinate system. See also
    *snap angle* and
    *user coordinate system (UCS).*

output property
:   A lookup property whose value is determined by input properties (other parameter properties) through the use of a lookup
    table.

page setup
:   A collection of plot device and other settings that affect the appearance and format of the final output. These settings
    can be modified and applied to other layouts.

palette
:   A Windows-specific, user interface element that can be either docked, anchored, or floating in the drawing area. Dockable
    windows include the command line, status bar, Properties palette, and so on.

pan
:   To shift the view of a drawing without changing magnification. (PAN) See also *zoom.*

paper space
:   One of two primary spaces in which objects reside. Paper space is used for creating a finished layout for printing or plotting,
    in contrast to drafting or designing. You design your model using the Model tab. (PSPACE) See also
    *model space* and
    *viewport.*

parameter
:   In a dynamic block definition, defines custom properties for the dynamic block by specifying positions, distances, and angles
    for geometry in the block.

parameter set
:   A tool on the Parameter Sets tab of the Block Authoring Palettes window that adds one or more parameters and one or more
    associated actions to the dynamic block definition.

parametric design
:   Ability to establish relationships between objects, to drive the size and orientation of geometry with model and user-defined
    parameters.

parametric drawing
:   A feature that assigns constraints to objects, establishing the distance, location, and orientation of objects with respect
    to other objects.

partial customization file
:   Any CUI file that is not defined as the main CUI file. Under Windows, you can load and unload partial CUI files as you need
    them during a drawing session.

path curve
:   Defines the direction and length that a profile curve is lofted, swept, or extruded to create a 3D solid or surface for commands
    such as SWEEP, LOFT, and EXTRUDE.

PC3 file
:   Partial plotter configuration file. PC3 files contain plot settings information such as the device driver and model, the
    output port to which the device is connected, and various device-specific settings, but do not include any custom plotter
    calibration or custom paper size information. See also
    *PMP file, STB file,* and
    *CTB file.*

performance tuning
:   A method of optimizing 3D graphics performance. The performance tuner examines your graphics card and 3D display driver and
    decides whether to use software or hardware implementation for features that support both.

periodic curve
:   A smooth, closed curve such as a circle. Because its control vertices are not tangent to the object, if the curve is reshaped,
    it stays smooth and does not create kinks. See also
    *clamp curve.*

periodic surface
:   A smooth, closed surface such as a cylinder. Because its control vertices are not tangent to the object, if the surface is
    reshaped, it stays smooth and does not create kinks. See also
    *clamp surface.*

perspective view
:   Objects in 3D seen by an observer positioned at the viewpoint looking at the view center. Objects appear smaller when the
    distance from the observer (at the view point) to the view center increases. Although a perspective view appears realistic,
    it does not preserve the shapes of objects. Parallel lines seemingly converge in the view. The program has perspective view
    settings for VPORTS table entries as well as viewport objects.

photometric lights
:   Photometric lights are physically-correct lights. Physically correct lights attenuate as the square of the distance. Photometry
    is the science of measurement of visible light in terms of its perceived brightness.

photon map
:   A technique to generate the indirect illumination effects of global illumination used by the renderer. When it calculates
    indirect illumination, the renderer traces photons emitted from a light. The photon is traced through the model, being reflected
    or transmitted by objects, until it strikes a diffuse surface. When it strikes a surface, the photon is stored in the photon
    map.

photorealistic rendering
:   Rendering that resembles a photograph.

pick button
:   The button on a pointing device that is used to select objects or specify points on the screen. For example, on a two-button
    mouse, it is the left button by default.

pick-first
:   The selection of objects before a command is entered or action macro starts.

pick-first set
:   A selection set of objects that are selected prior to the execution of an action macro or a command.
    *See also* pre-selection set.

pick points
:   The selection of objects before a command is entered or action macro starts.

planar face
:   A flat face that can be located anywhere in 3D space.

planar projection
:   Mapping objects or images onto a plane.

planar surface
:   A flat surface that can be located anywhere in 3D space. (PLANESURF)

plan view
:   A view orientation from a point on the positive
    *Z* axis toward the origin (0,0,0). (PLAN)

playback
:   The process of executing the actions stored in a previously recorded action macro.

pline
:   See
    *polyline.*

plot style
:   An object property that specifies a set of overrides for color, dithering, gray scale, pen assignments, screening, linetype,
    lineweight, endstyles, joinstyles, and fill styles. Plot styles are applied at plot time.

plot style table
:   A set of plot styles. Plot styles are defined in plot style tables and apply to objects only when the plot style table is
    attached to a layout or viewport.

plug-ins
:   See
    *Add-ins.*

PMP file
:   *Plot Model Parameter*. The file containing custom plotter calibration and custom paper size information associated with plotter configuration file.

point
:   1. A location in 3D space specified by
    *X*,
    *Y*, and
    *Z* coordinate values. 2. An object consisting of a single coordinate location. (POINT)

point cloud
:   A large collection of points placed in model space that create a 3D representation of objects, geographic features, or areas.

point cloud segmentation
:   The process of identifying groups of points in a point cloud that represent different surfaces. It occurs during the indexing
    of the scan files in Autodesk ReCap. AutoCAD recognizes planar and cylindrical segments when object snapping to the point
    cloud or when extracting geometry from the point cloud.

pointer
:   A cursor on a video display screen that can be moved around to place textual or graphical information. See also
    *crosshairs.*

point filters
:   See
    *coordinate filters.*

polar array
:   Objects copied around a specified center point a specified number of times. (ARRAY)

Polar Snap
:   A precision drawing tool used to snap to incremental distances along the polar tracking alignment path. See also *polar tracking.*

polar tracking
:   A precision drawing tool that displays temporary alignment paths defined by user-specified polar angles. See also
    *Polar Snap.*

polyface and polygon mesh
:   Legacy mesh types that were available before AutoCAD 2010. Although you can continue to create polygonal and polyface mesh
    (for example, by setting MESHTYPE to 0), the newer, more flexible mesh type is recommended.

polygon window selection
:   A polygonal area specified to select multiple objects. See also
    *crossing selection* and
    *window selection.*

polyline
:   An object composed of one or more connected line segments or circular arcs treated as a single object. Also called
    *pline*.

polysolid
:   A swept solid that is drawn the same way you draw a polyline or that is based on an existing line. By default, a polysolid
    always has a rectangular profile. You can specify the height and width of the profile. (POLYSOLID)

position marker
:   An annotation placed in model space to mark and label a geographic location.

pre-playback drawing environment
:   The drawing state prior to the playback of an action macro.

pre-selection set
:   A selection set of objects that is defined prior to the execution of an action macro.

primary table fragment
:   The fragment of a broken table that contains the beginning set of rows up to the first table break.

primitive
:   Basic 3D forms such as a box, cone, cylinder, pyramid, wedge, sphere, and torus. You can create primitive 3D solids and meshes.

procedural materials
:   Materials that generate a 3D pattern in two or more colors, and apply it to an object. These include marble and wood. Also
    called
    *template materials*.

procedural surface
:   A 3D surface object that has history and analytic information, but no control vertices. Procedural surfaces are the only
    type of surface that can be associative. See also
    *generic surface* and
    *NURBS surface.*

profile curve
:   An object that is swept, extruded, or revolved and defines the shape of the resulting 3D solid or surface. (SWEEP, EXTRUDE,
    REVOLVE)

projected view
:   A drawing view that is projected from another drawing view.

projected view
:   A drawing view that is projected from an existing  drawing view. This term is associated with the model documentation feature.

prompt
:   A message on the command line or in a tooltip that asks for information or requests an action such as specifying a point.

proxy object
:   A substitute for a custom object when the ObjectARX application that created the custom object is not available. See also
    *custom object* and
    *object enabler.*

push pin
:   A push pin-shaped button used on the ribbon and in the application menu for products that run on the Windows operating system.
    On the ribbon, pins keep panels expanded. In the application menu, pins keep an item in the list of recently viewed items.

PWT
:   A template file format used to publish drawings to the Web.

Quick View
:   A tool to preview and switch between open drawings and layouts in a drawing.

Quick View image
:   A thumbnail image of a drawing, layout or model space that is displayed using Quick View.

ray-traced shadows
:   A way that the renderer can generate shadows. Ray tracing traces the path of rays sampled from the light source. Shadows
    appear where rays have been blocked by objects. Ray-traced shadows have sharp edges.

ray tracing
:   The renderer can generate reflections and refractions. Ray tracing traces the path of rays sampled from the light source.
    Reflections and refractions generated this way are physically accurate.

recorded value
:   The input captured during the recording of an action macro for a sub-prompt of a command.

rectangular break
:   To break a table into multiple parts that are evenly spaced and set at a user-specified height using the table breaking grips.

refine
:   To quadruple the number of faces in a mesh object as you reset the baseline level of smoothness. You can also refine specified
    mesh faces without resetting the baseline level of smoothness for the object. (MESHREFINE)

reflectance scale
:   Increases or decreases the amount of energy the material reflects.

reflection color
:   The color of a highlight on shiny material. Also called
    *specular color*.

reflection line
:   In a dynamic block reference, the axis about which a flip action's selection set flips when the associated parameter is edited
    through a grip or the Properties palette.

reflection mapping
:   Creates the effect of a scene reflected on the surface of a shiny object.

refraction
:   How light distorts through an object.

regenerate
:   To update the objects in the drawing area by recomputing the screen coordinates from the database. (REGEN)

region
:   A 2D enclosed area that has physical properties such as centroids or centers of mass. You can create regions from objects
    that form closed loops. They area commonly created in order to apply hatching and shading, and to extrude in 3D. (REGION)

relative coordinates
:   Coordinates specified in relation to previous coordinates.

relax constraints
:   Ability to temporarily ignore constraints while editing geometry. After the geometry is edited, the constraints are either
    removed or retained based on whether the constraint is still valid for the edited geometry.

request user input
:   An item that is assigned to an action node that pauses the playback of an action macro so a user can provide some form of
    input before playback resumes.

reverse lookup (dynamic blocks)
:   Adds a lookup grip to a dynamic block reference. When you click this grip, a drop-down list of the lookup values for that
    lookup property (column in the lookup table) is displayed. When you select a value from the list, the corresponding input
    property values are assigned to the block reference. Depending on how the block was defined, this usually results in a change
    in the block reference's geometry. (BLOOKUPTABLE)

rewind
:   Restores the previous view or movement path created by the Autodesk® ViewCube®, SteeringWheels, or other navigation tool.

RGB
:   For
    *red, green, and blue*. A system of defining colors by specifying percentages of red, green, and blue.

ribbon
:   For products that run under the Windows operating system, a palette that displays buttons and controls used for both 2D drawing
    and annotation and 3D modeling, viewing, and rendering. (RIBBON) See also
    *ribbon tab, ribbon panel,* and *slide-out panel.*

ribbon panel
:   For products that run on the Mac, a set of labeled controls, related to a task, grouped together in a ribbon. Multiple ribbon
    panels, belonging to one workflow, are grouped together under a ribbon tab.

ribbon tab
:   For products that run under the Windows operating system, the highest level of ribbon grouping, based on an action. A ribbon
    tab contains groups of multiple ribbon panels, each belonging to one workflow. A ribbon panel contains buttons and controls,
    related to a task.

roll arrows
:   Curved arrows located above the ViewCube tool with which you can rotate the current view 90 degrees clockwise or counterclockwise.

roughness
:   Simulates how light hitting a face is reflected back to the user. A high roughness value simulates a non-shiny or rough object
    (sandpaper/carpet). A low roughness value simulates a shiny object (metals, some plastics).

row (table)
:   A horizontally adjacent table cell selection spanning the width of the table. A single row is one cell in height.

rubber-band line
:   A line that stretches dynamically within the drawing area with the movement of the cursor. Typically, one endpoint of the
    rubber-band line is attached to a point in your drawing, and the other endpoint is attached to the moving cursor.

running object snap
:   Setting an Object Snap mode so it continues to be applied for subsequent selections. (OSNAP) See also
    *Object Snap mode* and
    *object snap override.*

sampling
:   Sampling is an anti-aliasing technique. It provides a "best guess" color for each rendered pixel. The renderer first samples
    the scene color at locations within the pixel or along the pixel's edge, then uses a filter to combine the samples into a
    single pixel color.

save back
:   To update the objects in the original reference (external or block reference) with changes made to objects in a working set
    during in-place reference editing.

scale representation
:   The display of an annotative object based on the annotation scales that the object supports. For example, if an annotative
    object such as a label supports two annotation scales, it has two separate scale representations in two views displayed at
    two different scales.

script file
:   A set of commands executed sequentially with a single SCRIPT command. Script files are created outside the program using
    a text editor, saved in text format, and stored in an external file with the file extension .*scr*.

search tag
:   A user-defined keyword used to search for commands in the menu browser for products that run under the Windows operating
    system.

secondary table fragment
:   Any fragment of a broken table that does not contain the beginning set of rows.

section line
:   an annotated line that represents the imaginary cutting plane used to generate a section view.

section view
:   A projected view that shows the hidden interior details as though the drawing view it was projected from was sliced through.

selection node
:   A specific type of action tree node that is used to handle selection activities.

selection sensitivity
:   The ability to define the pivot point for reorienting a model based on the current selection.

selection set
:   One or more selected objects that a command can act upon at the same time. In a dynamic block definition, the geometry associated
    with an action.

shadow maps
:   A bitmap that the renderer generates during a pre-rendering pass of the scene. Shadow maps don't show the color cast by transparent
    or translucent objects. In contrast to ray-traced shadows, shadow maps have softer edges, and take less calculation time at
    the expense of accuracy.

ShapeManager
:   The Autodesk technology that provides 3D solid modeling to AutoCAD and other products.

Shared View
:   An online visual representation of the view of the model or design uploaded from an Autodesk product that can be viewed in
    the Autodesk Viewer.

sheet
:   A layout selected from a drawing file and assigned to a sheet set. See also
    *sheet set.*

sheet list table
:   A table listing all sheets in a sheet set. A sheet list table can be generated automatically with the Sheet Set Manager.

sheet selection
:   A named selection of sheets in a sheet set that can be conveniently recalled for archiving, transmitting, and publishing
    operations.

sheet set
:   An organized and named collection of sheets from several drawing files. (SHEETSET) See also
    *sheet.*

shortcut keys
:   Keys and key combinations that start commands. In Windows for example, CTRL+S saves a file. The function keys (F1, F2, and
    so on) are also shortcut keys. On the Mac, Command-S saves a file. The function keys (Fn-F1, Fn-F2, and so on) are also shortcut
    keys.

shortcut menu
:   The menu displayed at your cursor location when you right-click your pointing device. The shortcut menu and the options it
    provides depend on the pointer location and other conditions, such as whether an object is selected or a command is in progress.
    For programs that run under the Windows operating system, shortcut menus are now called
    *context menus*. They are also sometimes called
    *right-click menus*.

shot
:   A saved view that can later be restored by name or with ShowMotion. A shot can contain a static thumbnail of the saved view
    or camera motion that can be played back as an animation.

ShowMotion
:   User interface element where you can access named views (shots) that are stored in the current drawing. The named views (shots)
    are organized by sequences and can contain movements.

sky
:   The background color of the drawing area when perspective projection is turned on. The sky displays with a color gradient
    between the sky horizon (nearest to the horizon) and the sky zenith (opposite the horizon). See also
    *ground plane.*

slide-out panel
:   For AutoCAD-based products that run under the Windows operating system, an area on the ribbon associated with a ribbon panel.
    A slide-out panel contains additional tools and controls. See also *ribbon panel* and
    *ribbon.*

smoothness
:   A property of mesh objects that controls the roundness of the object. Objects with higher levels of smoothness have more
    faces, or tessellations.

smooth shading
:   Smooths the edges between polygon faces.

snap angle
:   The angle that the snap grid is rotated.

snap grid
:   An invisible grid that locks the cursor into a specified spacing, which can be different in the
    *X* and
    *Y* directions. The snap grid does not necessarily correspond to the visible grid, which is controlled separately by GRID. (SNAP)

snap resolution
:   The spacing between points of the snap grid.

solid history
:   A property of a solid that allows you to see and modify the original forms of the solid.

solid object
:   An object that represents the 3D volume of an object, for example a cylinder.

solid primitive
:   A basic 3D shape such as a box, wedge, cone, cylinder, sphere, torus, and pyramid.

spatial index
:   A list that organizes objects based on their location in space. A spatial index is used to locate what portion of the drawing
    is read when you partially open a drawing. Saving a spatial index with a drawing also enhances performance when working with
    external references. The INDEXCTL system variable controls whether layer and spatial indexes are saved with a drawing.

spectrum
:   In the reality capture feature, spectrum is an option to map colors to point cloud intensity to help distinguish the intensity
    details in complex point clouds. See also
    *intensity*.

specular reflection
:   The light in a narrow cone where the angle of the incoming beam equals the angle of the reflected beam.

spline-fit polyline
:   Uses the vertices of the selected polyline as the control points, or frame, of a curve approximating a B-spline. This curve,
    called a spline-fit polyline, passes through the first and last control points unless the original polyline was closed.

split face
:   A mesh face that has been subdivided along a specified vector.

Start In folder
:   The drive and folder path from where the product was started, which is determined either by the Start In attribute of the
    desktop shortcut icon, or by the folder in which a file is double-clicked. (STARTINFOLDER system variable)

STB file
:   For
    *plot style table* file. Contains plot styles and their characteristics.

SteeringWheels
:   A tool set that provides access to 2D and, for AutoCAD, 3D navigation tools.

stretch frame
:   In a dynamic block definition that contains a stretch action or a polar stretch action, determines how the objects within
    or crossed by the frame are edited in the block reference.

subdivision
:   A division, or tessellation in a mesh object. As a mesh object is smoothed, the number of subdivisions increases.

subobject
:   A part of a composite object.

sub-prompt
:   A command prompt that instructs for a form of input to complete a command or alter a property.

subset
:   A named collection of sheets in a sheet set that is often organized by discipline or workflow stage. See also
    *view category.*

surface
:   A surface is a 3D object that is an infinitely thin shell. There are 3 types of surfaces: analytic, generic, and NURBS.

surface associativity
:   See
    *associative surfaces.*

surface indication leader
:   An additional leader (arrowhead, leader and reference line) added to surface texture symbols. The surface indication leader
    (SIL) is used to point to surfaces or faces rather than the edges of components.

surface normal
:   Positive direction perpendicular to the surface of an object.

swept solid or surface
:   A solid or surface created in the shape of the specified profile (the swept object) swept along the specified path. (SWEEP)

symbol
:   A representation of an item commonly used in drawings. Symbols are inserted in drawings as blocks.

symbol library
:   A collection of block definitions stored in a single drawing file.

symbol table
:   See *definition table* and
    *block definition table.*

system variable
:   Similar to a command, it controls operating settings of the product, including modes, sizes, or limits. Read-only system
    variables, such as DWGNAME, cannot be modified directly.

table
:   A rectangular array of cells that contain annotation, primarily text but also blocks. In the AEC industry, a table is often
    referred to as a “schedule” and it contains information about the materials needed for the construction of the building being
    designed. In the manufacturing industry, a table is often referred to as a “BOM” (bill of materials). (TABLE)

table break
:   The point at the bottom of a table row where the table will be split into a supplementary table fragment.

table style
:   A style that contains a specific table format and structure. A table style contains at least 3 cell styles.

tab list
:   The drop-down list that appears only when the file tabs have outgrown the available space in the drawing window. When this
    happens, the tab list button appears.

temporary files
:   Data files created during an program session. The files are deleted by the time you end the session. If the session ends
    abnormally, such as during a power outage, temporary files might be left on your disk drive.

temporary prompt history
:   The list of commands and prompts displayed transparently above the Command prompt in an single-line, undocked Command Line
    window. See also
    *extended command history.*

tessellation lines
:   Display lines that help you visualize a curved mesh surface.

text style
:   A named, saved collection of settings that determines the appearance of text characters—for example, stretched, compressed,
    oblique, mirrored, or set in a vertical column.

texture map
:   The projection of an image (such as a fabric pattern) onto an object (such as a chair).

thaw
:   A setting that displays previously frozen layers. (LAYER) See also *freeze.*

thickness
:   A legacy property of 2D objects that are extruded to provide a 3D appearance. (PROPERTIES, CHPROP, ELEV, THICKNESS)

tiled viewports
:   See *model viewports.*

TILEMODE
:   A system variable that controls whether viewports can be created as movable, resizable objects, called
    *layout viewports*, or as nonoverlapping display elements that appear side-by-side, called
    *model viewports*. See also
    *viewport.*

toolbar
:   Part of the interface containing icons that represent commands in AutoCAD-based products that run under the Windows operating
    system.

tooltip
:   A small box of text that identifies or explains an object or interface element when the cursor hovers near or over it.

tracking
:   A method for determining a point relative to other points on the drawing.

tracking menu
:   A cluster of buttons associated with SteeringWheels that follow the cursor as you move it.

translucency
:   How light diffuses through an object.

transmittance scale
:   Increases or decreases the amount of energy a transparent material transmits out to the scene.

transparency
:   A value that defines how much light passes through an object.

transparent command
:   A command that is started while another one is still in progress. Precede transparent commands with an apostrophe.

trusted locations
:   Specified folders in the File tab of the Options dialog box that are permitted to run executable code. (TRUSTEDPATHS)

two-sided material
:   The positive and negative normal of the material will be considered during the rendering process.

UCS
:   See *user coordinate system (UCS).*

UCS definition
:   A named and saved UCS location and orientation. Each UCS definition can have its own origin and X, Y, and Z axes. Create and
    save as many UCS definitions as you need.

UCS icon
:   An icon that indicates the orientation of the UCS axes. (UCSICON)

underconstrained geometry
:   In parametric drawing, objects with unsolved degrees of freedom are underconstrained.

underground
:   The
    *XY* plane of the user coordinate system when perspective projection is turned on and when viewed from below ground. The underground
    plane displays with a color gradient between the earth horizon (nearest to the horizon) and the earth azimuth (opposite the
    horizon). See also
    *ground plane* and
    *sky.*

underlay
:   An Autodesk DWF, or a Microstation DGN file that is attached to a DWG drawing file to provide visual information and object
    snap locations. See also
    *external reference (xref).*

up direction
:   A vector defining what direction is Up. By default this is the positive
    *Z* – axis (0,0,+1). The up direction and the north direction are always constrained such that they are perpendicular to each
    other.

user coordinate system (UCS)
:   A movable coordinate system that establishes the
    *XY* plane (work plane) and
    *Z*-axis direction for drawing and modeling. You can set the UCS origin and its
    *X*,
    *Y*, and
    *Z* axes to suit your needs. See also
    *world coordinate system (WCS).*

user parameter
:   A named, user-defined variable (real number or an expression) that can be used in expressions for dimensional constraints
    or other user parameters.

UVW
:   The coordinate space for a material. Most material maps are a 2D plane assigned to a 3D surface. The
    *U*,
    *V*, and
    *W* coordinates parallel the relative directions of
    *X*,
    *Y*, and
    *Z* coordinates. If you look at a 2D map image,
    *U* is the equivalent of
    *X*, and represents the horizontal direction of the map.
    *V* is the equivalent of
    *Y*, and represents the vertical direction of the map.
    *W* is the equivalent of
    *Z* and represents a direction perpendicular to the
    *UV* plane of the map.

value node
:   A specific type of action node that is used to handle requests for user input and hold the recorded value that was captured
    during the recording of an action macro.

value set
:   In a dynamic block definition, a range or list of values specified for a linear, polar, XY, or rotation parameter.

vector
:   A mathematical expression with precise direction and magnitude (length) but without a specific location.

vertex
:   A location where edges or polyline segments meet.

view (AutoCAD)
:   A graphical representation of a model from a specific location (viewpoint) in space. (3DORBIT, VPOINT, DVIEW, VIEW) See also
    *viewpoint* and
    *viewport.*

view (AutoCAD LT)
:   A graphical representation of a model from a specific location (viewpoint) in space. (VPOINT, VIEW) See also
    *viewpoint* and
    *viewport.*

view category
:   A named collection of views in a sheet set that is often organized by function. See also
    *subset.*

ViewCube
:   A user interface element that displays the current orientation of a model, and allows you to interactively rotate the current
    view or restore a preset view.

viewpoint (AutoCAD)
:   The location in 3D model space from which you are viewing a model. (3DORBIT, DVIEW, VPOINT) See also
    *view* and *viewport.*

viewpoint (AutoCAD LT)
:   The location in 3D model space from which you are viewing a model. (VPOINT) See also
    *view* and
    *viewport.*

viewport
:   A bounded area that displays some portion of the model space of a drawing. The TILEMODE system variable determines the type
    of viewport created. 1. When TILEMODE is off (0), viewports are objects that can be moved and resized on a layout. (MVIEW)
    2. When TILEMODE is on (1), the entire drawing area is divided into non-overlapping model viewports. (VPORTS) See also
    *TILEMODE, view,* and *viewpoint.*

viewport configuration
:   A named collection of model viewports that can be saved and restored. (VPORTS)

view sketching
:   A state in a model space view for editing and constraining a section line or detail boundary.

virtual screen display
:   The area in which the program can pan and zoom without regenerating the drawing.

visibility mode
:   Displays or does not display geometry (in a dimmed state) that is invisible for a visibility state. (BVMODE)

visibility state
:   In a dynamic block, a custom property that allows only specified geometry to display in the block reference. (BVSTATE)

visual style
:   A collection of settings that control the display of edges and shading in a viewport.

volumetric shadows
:   A photorealistically rendered volume of space cast by the shadow of an object.

watertight
:   A closed 3D solid or mesh that has no gaps.

WCS
:   See *world coordinate system (WCS).*

wheel
:   A reference to one of the individual user interface elements that make up SteeringWheels for products that run on the Windows
    operating system. See also
    *SteeringWheels.*

wheel surface
:   The area of SteeringWheels that is used to organize wedges and other buttons.

wheel wedge
:   A section on the surface of a SteeringWheels that is designated for a specific navigation or orientation tool.

window selection
:   A rectangular area specified in the drawing area to select multiple objects at the same time. See also
    *crossing selection* and *polygon window selection.*

wipeout object
:   A polygonal area that masks underlying objects with the current background color. This area is bounded by the wipeout frame,
    which you can turn on for editing and turn off for printing or plotting.

wireframe model
:   The representation of a 3D object using lines and curves to represent its edges.

workflow
:   A focused component provided for enabling repeatable modeling tasks from one Autodesk product to another within an Autodesk
    suite. When AutoCAD is purchased with a suite, preset workflows and a Workflow Manager are provided to configure and send
    drawings from AutoCAD to Autodesk Showcase and Autodesk 3ds Max.

Workflow Manager
:   Workflow Manager is a user interface that allows you to access, manage, and customize cross-product workflows in an Autodesk
    suite. Use it to send a design from AutoCAD or another product to 3ds Max Design or Showcase for detailed rendering or animation.

working drawing
:   A drawing used for manufacturing or building purposes.

working folder
:   The drive and folder path of the operating system's working folder or
    *current directory* for the process, which can be of interest to developers. (WORKINGFOLDER system variable).

working set
:   A group of objects selected for in-place reference editing.

work plane
:   Another name for the
    *XY* plane of the user coordinate system. See also
    *elevation* and
    *user coordinate system (UCS).*

workspace
:   For products that run on the Windows operating system, a set of menus, toolbars and dockable windows (such as the Properties
    palette, DesignCenter, and the Tool palettes window) that are grouped and organized so that you can work in a custom, task-oriented
    drawing environment.

world coordinates
:   Coordinates expressed in relation to the world coordinate system (WCS).

world coordinate system (WCS)
:   The fixed coordinate system that defines the location of all objects and other coordinate systems in a drawing. In new drawings,
    the user coordinate system (UCS) is initially coincident with the WCS. See also
    *user coordinate system (UCS).*

wrap around
:   Behavior where the cursor wraps around the window and appears on the opposite side to allow the continuation of a drag operation
    instead of stopping at the edge of the drawing area.

*X,Y,Z* point filters
:   See
    *coordinate filters.*

xref
:   A drawing file referenced from another drawing file. This type of external reference is specific to DWG files. See also
    *external reference. (XREF).*

zoom
:   To reduce or increase the apparent magnification of the drawing area. (ZOOM)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*