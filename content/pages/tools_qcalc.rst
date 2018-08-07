:title: Q Calculator
:category: tools
:slug: tools/q-calc

The q calculator spreadsheet was created to make it easy to select a camera
length to suit your experiment needs.  You need to specify the beam energy
(in keV)  in cell F11. This will almost always be 12 keV. The pixel size
will be set by which detector you use. The pixel sizes and the dimensions
of the active area of detectors at BioCAT are given in the Table on the right.
The pixel size in mm should be entered in cell H12.  sdd stands for Sample to
Detector Distance (in mm). This is usually what you want to determine for a
particular sample and experiment. Initially this can be set to a trial value
(typical camera lengths are 2 -3 m).  This trial value (in mm) should be put
in cell G11.

The task is to decide is what the maximum and minimum d spacing you want to
observe in your X-ray  patterns (column A).  Once this is decided you read
across to column C for distance from the center (s)  in mm or column D for
the distance from the center. Then you need to decide whether or not this will
fall on the active area of the detector that you plan to use. If it is off
the edge of the detector you need to  shorten the camera, if it is not near
the edge of the detector, you need to lengthen it. You do this by adjusting
sdd. The other concern is the first order resolution i.e. the largest structural
feature that you wish to observe.   This will be mainly set by the backstop
size, typically 4 mm.

Then it is a simple matter to try different values for sdd to give you the
d-spacing range that you want.

q (Column B) is the momentum transfer vector and is commonly used for solution
scattering. It  is equal to 4π*sin(θ)/λ where θ is the Bragg  angle. This is
equal to 2π/d where d is from column A

.. lead::
    `Click here to download the q calculator spreadsheet. <{filename}/files/q_calculator.xls>`_
