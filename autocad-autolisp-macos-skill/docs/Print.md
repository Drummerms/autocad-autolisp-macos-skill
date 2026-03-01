# Print

Output a drawing layout to a printer, a plotter, or a file. Save and restore the printer settings for each layout.

Originally, people
*printed* text from printers and
*plotted* drawings from plotters. Now, you can do both with either. So this guide will also use the terms print and plot interchangeably
as everyone else does.

The command to output a drawing is PLOT and you can access it from the toolbar.

![](../images/GUID-C22FE792-B267-4D4A-987E-060ADBD2EB25-low.png)

To control whether all of the options in the Plot dialog box are hidden or displayed, click the arrow indicated to expand.

![](../images/GUID-7534834F-DBD9-4540-A4EE-5EE3213CA19A-low.png)

When all of the options are displayed, there are a lot of settings and options available for your use.

![](../images/GUID-DAA050E2-3D1F-49C2-8E1D-BCE7DBBB3655-low.png)

For convenience, you can save and restore collections of these settings by name. These are called
*page setups*. With page setups you can store the settings that you need for different printers, printing in gray scales, creating a PDF
file from your drawing, and so on.

## Create a Page Setup

To open the Page Setup Manager, select Page Setup Manager from the toolbar. The command is PAGESETUP.

![](../images/GUID-0FC0E68A-36BF-44BD-A0E6-952B7C314A27-low.png)

Each layout tab in your drawing can have an associated page setup. This is convenient when you use more than one output device
or format, or if you have several layouts with different sheet sizes in the same drawing.

![](../images/GUID-5529BF43-0B54-456E-A28A-0F0F51F1FDB1-low.png)

To create a new page setup, click
![](../images/GUID-9174311E-7DC8-49C8-B39F-991EC3DAD0E2-low.png) and enter the name of the new page setup. The Page Setup Edit dialog box that displays next looks like the Plot dialog box.
Choose all the options and settings that you want to save.

When you are ready to plot, you simply specify the name of the page setup in the Plot dialog box, and all your plot settings
will be restored.

TIP: You can save page setups in your drawing template files, or you can import them from other drawing files.

## Output to a PDF File

The following example shows you how to create a page setup for creating PDF files.

From the Printer/plotter drop-down list, choose
*AutoCAD PDF (General Documentation).pc3*:

![](../images/GUID-64402F69-20E9-45C0-B3B1-F956D54B603E-low.png)

Next, choose the size and scale options that you want to use:

* Paper Size. The orientation (portrait or landscape) is built into the choices in the drop-down list.
* What to Print. You can clip the area to be plotted with these options, but usually you plot everything.
* Plot Offset. This setting changes based on your printer, plotter, or other output. Try centering the plot or adjusting the
  origin, but remember that printers and plotters have a built-in margin around the edges.
* Plot Scale. Choose your plot scale from the drop-down list. A scale such as 1/4” = 1’-0” is meant for printing to scale from
  the Model tab. On a layout tab, you normally print at a 1:1 scale.

The plot style table provides information about processing colors. Colors that look good on your monitor might not be suitable
for a PDF file or for printing. For example, you might want to create a drawing in color, but create monochrome output. Here
is how you specify monochrome output:

![](../images/GUID-BEBDF196-C545-48D5-94BF-362A1A975B66-low.png)

After you are satisfied with your plot settings, save them to a page setup with a descriptive name such as "PDF-monochrome."
Then, whenever you want to output to a PDF file, all that you need to do is click Print, choose the PDF-monochrome page setup,
and click OK.

## Final Thoughts

Congratulations, you've learned the basics of AutoCAD with the minimum set of commands. From here, simply practice what you've
learned, review the chapters as needed, and expand your collection of commands. For additional information, you can do the
following:

* Study the topic links to the Help system
* Ask questions and receive tips on AutoCAD discussion forums (*https://forums.autodesk.com/)*
* From within AutoCAD for Mac, press F1 during a command to get help on that command
* Browse through blog posts on the Autodesk and AutoCAD-related websites (<https://www.autodesk.com/blogs>)
* View videos from various AutoCAD learning websites
* Get help from local support providers or experts right away if you encounter any difficulties

Best wishes from Autodesk for excellent productivity and success!

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Dimension](GUID-889618FA-6287-4B34-8684-A38A98065522.htm " Create several types of dimensions and save dimension settings by name.
")

#### Related References

* [PAGESETUP (Command)](PAGESETUP-Command-2.md)
* [PLOT (Command)](PLOT-Command-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*