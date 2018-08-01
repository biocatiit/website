:title: How design and perform a microprobe experiment
:category: users
:slug: how-to-design-microprobe

.. page-header::

    .. alert:: Please note that at this time XFM is not available through the  GU system and is only available to collaborators.
        :type: info

In this section, you will find instructions for operating the X-ray Fluorescence
microprobe once it has been setup by BioCAT staff members. If you find the
microprobe is not working properly, there are a number of ways to determine which
component is not working and how to fix it. If these instructions are not clear
or you cannot solve the problem by your own, please call your scientific contact.

The microprobe setup consists of the following components:

#.  Optics

    *   KB mirrors
    *   Collimator slits
    *   Ion chambers
    *   Video camera 1
    *   Video camera 2

#.  Sample Holder System

    *   XYZ high precision positioner
    *   Rotary stage
    *   Linkam cryostage
    *   Cryostream
    *   Sample holders

#.  Detector System

    *   Ketek single element detector
    *   Ketek 7 element detector
    *   XIA Saturn electronics
    *   XIA xMap electronics

#.  Software

    *   BioCAT-FMAP, scanning software
    *   BioCAT-ROI, on-the-fly-analysis software
    *   BioCAT-FIT, peak fitting and calibration software

This document is organized by microprobe components. First you need to know how
to operate the microprobe under normal conditions. If any of these components
fail then you will need to go to the troubleshooting section of this document.

How to run the microprobe
==========================

Optics
-------

When you arrive at the BioCAT beamline 18ID to perform a microprobe experiment,
the main components of the microprobe will have been set up beforehand. The
x-ray beam energy will be set to your requested value, the beam will be
collimated, and the KB mirrors will be set to focus the beam at the sample
position. Two ion chambers are in the beam path: one upstream of the mirrors
to monitor the incoming beam and to provide a signal to the feedback control
system and another ion chamber immediately downstream of the KB mirrors to
monitor the focused beam intensity delivered to the sample. Finally, the Hitachi
video camera will have been aligned and focused on the x-ray focal point. This
is your reference point for sample alignment.

**Please do not adjust the optical configuration.**

Adjusting the optical configuration could result in losing the alignment and
several hours of your beamtime. If you cannot find the beam or you suspect the
system is not properly aligned and focused, please call your scientific contact.

Sample holder system
-----------------------

XYZ high precision positioner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The sample holder system is based on a high precision (0.1 micron step
size) XYZ positioner. The positioners are driven by stepper motors
controlled by the MEDM screens already opened in one of the workspaces of
the main control computer. The positioners are named:

*   Sample Vertical
*   Sample Horizontal
*   Sample Focus

Each motor is associated with a particular stepper motor channel. These have
been already calibrated and preselected in the scanning software.

The video selector box above the computer monitor allows you to change the
source of the video input. To align the sample, select VideoCamera 1 to view
the focal spot and the sample in a close-up view. Move the sample focus
positioner while following the video camera 1 image on the monitor on the
left side of the main computer.

There is a second camera mounted on the table that allows you to visualize
a larger area of the sample, although it is not intended to be used as a
position reference. Use this camera to locate your sample near the focal
point. The beam position has been marked on the screen to help you find the
right spot for your samples. Once the sample is located near the focal spot
you need to select the scanning range for the BioCAT-FMAP software.

Move the sample horizontally to define the borders of your sample. Always
add a few microns more to the position of the edge of the sample. Repeat the
same procedure in the vertical direction.

If you have more than one sample on the same sample holder, you can define
multiple regions for the scanning software. Move your sample manually and
repeat the previously described procedure to determine the limits of each
region selected. Once you have the positions for each region selected you
are ready to setup a mapping scan.

Rotary Stage
^^^^^^^^^^^^^^

There is a rotary stage available that can be easily mounted on the XYZ
positioner. The rotary stage is driven by a high-precision stepper motor
and the channel on the step pak is preselected. The stage allows the rotation
of samples to perform tomography-like experiments.

Linkam Cryostage
^^^^^^^^^^^^^^^^^

A Linkam cryostage is also available for users. The cryostage is attached
to a kinematic mount allowing to mount it easily on the XYZ positioner. The
cryostage can be programmed in several modes. In most of these experiments
the samples are previously frozen, therefore the cryostage should be
constantly running at low temperatures to keep the sample temperature
constant. The cryostage cold finger has a hole at the center that allows
the beam to pass through it without striking the metal. When using the
cryostage the XYZ positioner cannot be use for scanning for that reason.
Instead you have two additional motors mounted on the cryostage to perform
the scans. These motors are already setup and their channels are preselected.

Cryostream
^^^^^^^^^^^^

If your sample holder does not allow you to use the Linkam cryostage for
low temperature experiments, the option is to use a cryostream. Currently
BioCAT has no cryostream available for users, although it is planned to
incorporate one in the near future. A cryostream can be borrowed from the
APS detector pool if scheduled in advance. Please contact your scientific
contact in advance if you are planning to use a cryostream.

Detector System
------------------

There are two detectors available at BioCAT.

Ketek Single-Element Silicon Drift Detector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Ketek single-element SDD is a 10 mm\ :sup:`2` actve area detector. It has a thin
polymer window that allows measurment of low atomic weight elements such as
Aluminum or even Oxygen under vacuum conditions. Although we do not operate
our microprobe under vacuum, it is possible to run an experiment in a He
atmosphere (Aluminum is still practical). To avoid permanent damage, the
detector must be operated under dark conditions as it is sensitive to visible
light because of the thin polymer window. There is a protective aluminum cup
with Be windows that can be used to run the detector under normal conditions
where low Z element sensitivity is not needed. The Be windows limit the
ability of low energy photons to reach the detector. Therefore, under these
conditions, sensitivity to light elements is reduced. The detector can only
be connected to the Saturn XIA digital spectrometer.

To start the Saturn follow these instructions:

#.  Open a terminal window
#.  Type: ``start_dxp <Enter>``

    An MEDM screen "DXP Detector Control" will show up.

    Do not change the DXP parameters, since they are already optimized for
    the Ketek detector.

#.  Click on "DXP & MCA Plots" and select MCA plots to open an MCA screen.

#.  In order to prepare the ROIs for the scanning software, you need to
    insert the following information in these fields:


    *Label:* Atomic Symbol

    *Low:* ROI lower channel number

    *High:* ROI higher channel number

#.  Enter as many elements as you want to plot after the scan without
    performing any fitting on the data. The ROI data will be use by the
    Matlab code BioCAT-ROI to plot the image. If you need more elements
    click on "All ROIs" to open a new screen with more options.

#.  Use the top buttons to start and stop counting manually. You don't need
    to start the dxp to run a mapping scan. The BioCAT-FMAP softwary
    controls the detector via EPICS.

#.  You can also open a python program to visualize the mca traces and save
    spectra. This is very useful when measuring calibration standards and
    selected spot on a given sample.

#.  To open the python MCA program follow these instructions:

    #.  Open a terminal window and type: ``python2 <Enter>``
    #.  At the python "``>>>``" prompt, type: ``mcaDisplay.mcaDisplay() <Enter>``

        A new MEDM screen will appear.

Ketek 7-Element Silicon Drift Detector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This device is currently under commissioning.

Software
-----------

There are three programs that allow the user to perform mapping experiments with
the BioCAT microprobe.

BioCAT-FMAP
^^^^^^^^^^^^

BioCAT-FMAP is scanning software written in python. To start the program follow
these instructions:

#.  Open a terminal window and type: ``./BioCAT-FMAP.py`` (case sensitive)
#.  Select the motors channels for X and Y directions.

    By default, MOTOR X is set to channel 20 and MOTOR Y is set to channel 22.
    Motor channel 21 is dedicated for the sample focus motor.

#.  Define the X and Y scan ranges

    You must choose the **Initial** point, **Final** point, and the **Step**
    size. All dimensions are in millimeters.

#.  Select Joerger channels 3 and 4

    The Joerger scaler reads the two ion chambers on these channels. Please
    do not change these channels.

#.  Insert the output file name with extension ``*.stp``, including the full path.
#.  Save the configuration file as ``*.par``.

    This will help to re-run other scans without retyping all the numbers.

    The ASCII configuration file can be edited to add more scanning regions.
    Simply open the file with any text editor of your choice. Add more regions
    by adding a second, third and so on columns with the new information
    separated by commas. Below is an example of a single scan region and a
    multiple scan regions.

BioCAT-ROI
^^^^^^^^^^^

BioCAT-ROI is quick analysis software written in Matlab. This code reads the
``*.stp`` files and plots the images of the ROIs selected in the scanning
software. This is the fastest way to get the image of the measured data. The
program only plots the values stored on the ROI channels. There is no background
removal, peak fitting, or calibration performed at this point. This program is
only intended for quick analysis performed on the floor while you are measuring
the next sample.

Typically the program takes less than a minute to read the data file and plot
the images. You can change the color code or any other parameters of the plots
using Matlab quite easily and the images can be saved as JPEG files.

BioCAT-FIT
^^^^^^^^^^^^

This is Matlab software indended for full analysis of the retrieved data.
This code reads the ``*.stp`` files and performs peak fitting of each measured
spectra for each point of the scan. The peak fitting routine includes: gaussian
shape peak fitting, escape peaks, both theoretical and experimental Ka/Kb ratios
and background removal. The code plots the images of the ROIs selected in the
scanning software. This is the fastest way to get the image of the measured data.

Troubleshooting the Microprobe
--------------------------------

If you experience difficulties during the operation of the microprobe, here are
some hints that may help you fix the problem. If these actions do not solve the
problem, please contact Raul Barrea for assistance.

There is no signal on the MCA screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Ensure that there is current in the storage ring

#.  If the current is zero, there is no beam in the storage ring. You will
    need to wait for the APS to refill the storage ring before x-rays will be
    avaliable. The Floor Coordinator may have information about why the beam
    is down and when the APS expects to return to operations.

    The Ring Current is displayed at the lower right corner of the picture below.
    Typically, beam current is near 102 mA in top-up mode.

#.  Ensure that x-rays are being delivered to the experiment station

    First, make sure that the "A," "D," and user shutters are open.

    If x-rays are making it into the experimental station, they should be passing
    through the ion chamber "I0." The signal from this ion chamber is displayed
    on the voltmeter located in the upper left corner of the voltmeter array on
    he main control panel (see picture above). With no beam present, the DVM
    typically reads 0.02-0.03 V. If there is no beam you need to check whether
    the shutters are open and that the intensity feedback system is operating
    correctly.

    The feedback system is located in the second rack on the right of the main
    console. All switches must be on. You can search for the beam by turning the
    offset knob while watching the I0 value until you see the intensity increase.
    Keep turning the knob until you get the maximum value.

#.  Ensure that x-rays are passing through the KB mirrors

    The ion chamber "I1" monitors x-rays exiting the KB mirrors. Again, this
    DVM typically reads 0.02-0.03 V if there is no beam present. If this is
    true, call Raul Barrea for further assistance.

The scanning software is frozen or the motors seem to be stopped
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the scanning software is frozen and the motor positions are not changing, you
must restart the program. Close the BioCAT-FMAP program. There should be a
terminal window in the same working space that contains the BioCAT-FMAP GUI. If
not, simply open a new terminal window and type: ``./BioCAT-FMAP.py <Enter>`` A new
instance of the program should show up immediately. Setup the parameters
following the instructions given in previous sections for the scanning software.
Check that the motors are now moving properly.

The BioCAT-ROI routine does not read the ``*.stp`` files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Matlab program BioCAT-ROI reads ``*.stp`` files only. If the file structure
is not the one expected by the program, it will crash. Make sure you are trying
to read ``*.stp`` files. Contact Raul Barrea to review the file structure and
the routine that reads the file.

The BioCAT-ROI graphs are distorted
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The BioCAT-ROI program reads the header of the file to organize the data by
horizontal and vertical steps. Sometimes there is a missing point at the end of
the line because of rounding errors. The solution is to correct the file header
and insert the proper numbers. Contact Raul Barrea for further assistance.

The BioCAT-FIT routine does not read the ``*.stp`` files.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The BioCAT-FIT program is intended to perform peak fitting of the mca traces on
every measured point of an ``*.stp`` file. The routine is expecting a specific file
format. If it cannot read the file, there might be an additional line or structure
in the file. Contact Raul Barrea to review the file structure and the routine
that reads the file.

The detector is not counting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the ulikely event that the EPICS software which communicates with the detector
via the Saturn electronics hangs, you must restart the EPICS DXP software:

#.  Close the MCA window
#.  Close the DXP Detector control window
#.  In the EPICS terminal window, type: ``exit`` at the ``epics>`` prompt.
#.  Once you return to a command prompt, type: ``start_dxp``. The DXP Detector
    Control window should return. Check that the detector is now working.
#.  Contact your scientific contact for further assistance

FAQs
=====

What is the BioCAT microprobe?
--------------------------------

The BioCAT microprobe is a unique instrument dedicated to microfluorescence
biological applications (Also called X-ray Florescence Microscopy). The microprobe
program is available only in collaboration with BioCAT staff and not via the
General User Program. Investigators wishing to use the microprobe capability
should contact `Tom Irving <{filename}/pages/contact.rst>`_. The main goal of
the microprobe program is to provide the experimenters with a very high efficiency
tool for microfluorescence mapping with or without microdiffraction

What kind of experiments are feasible with the BioCAT microprobe?
-------------------------------------------------------------------

Microfluorescence experiment that require resolutions of 50 microns, 20 microns
down to 5 microns are feasible with the  BioCAT microprobe.  Typically tissue
sections of various kinds are prepared for scanning at the microprobe. The
efficiency of the microprobe allows the experimenter to map a large section of
tissue at low resolution and map of small selected spots at higher resolution.
At this point only freeze and air dried samples are conveniently measure at BioCAT.
We will be developing cryogenic capabilities for studying frozen sections in
the future.

Which elements can be mapped with the microprobe?
---------------------------------------------------

Elemental mapping of elements from K up to U can be mapped with the microprobe.
The detection limit for each element depends on the noise level, the sample
substrate and detector's efficiency. Most of the experiment are performed at
room temperature and normal atmorpheric conditions. There is an SDD detector
for light element detection that is able to detect P and S under proper dark
environment and He atmosphere. These kind of experiments require a special setup.

How do I analyze the data?
-----------------------------

There are two routines available for experimenters written in Matlab. One
routine was designed for quick analysis of the experimental data to allow the
users to visualize the results immediately after the scan is done and to help
them to make decisions regarding the appropriate regions of interest and so
on for their experiment. Another routine was designed for a complete peak fitting
analysis including background removal, peak overlap removal and normalization by
using standards. Both routines are available for the experimenters.


Updated 7/14/15 T. Irving.
