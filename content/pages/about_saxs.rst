:title: Macromolecular Small-Angle Solution Scattering (SAXS)
:category: about
:slug: about-saxs

.. image:: {filename}/images/FPLC_SAXS.jpg
    :class: img-responsive
    :align: center

.. lead::
    Most proteins can not be crystallized. For those proteins, it is possible to
    study their structure by analyzing the manner in which they scatter X-rays.
    This technique is used to study how the proteins and nucleic acids in our cells
    function as “molecular machines.”




Small-angle x-ray scattering (SAXS) is a widely used technique for the
measurement of the radius of gyration (Rg) and the electron pair distance
distribution function (P(r)), as well as for ab initio modeling of
low-resolution molecular envelopes of macromolecules in solution.


Equilibrium SAXS
===================

The BioCAT standard experimental set-up includes a Pilatus 1M detector from
Dectris (Switzerland) and a camera of 3.5 m sample-to-detector distance to
access a range of momentum transfer, q, from ~0.04 to 3.3 nm-1. This range
of q allows not only accurate determination of radius of gyration, but also
detailed modeling using ab initio and rigid body approaches.

For static or equilibrium SAXS, a quartz capillary flow cell which is
temperature controlled through a water bath can be used. It takes usually
about 50-100 microliter of sample. However, in some cases smaller volume
(< 20 microliter) can also yield usable SAXS data. In order to reduce
radiation damage, the sample flows through the X-ray beam using a Hamilton
programmable dual-syringe pump.

We also offer SAXS data collection coupled with online Size Exclusion
Chromatography (SEC). The sample runs through a size exclusion column to
separate potential aggregates or different oligomeric states intermediately
before flowing through the capillary for X-ray exposure.

The high flux and efficient detectors at BioCAT allow collection of scattering
patterns and permits time-resolved experiments on the ms time scale using
the stopped-flow apparatus. We are also developing advanced microfluidic
mixers, including the chaotic mixer and laminar flow mixer, to collect SAXS
data on the tens of ms and sub-ms time regime. Friendly users are welcome to
submit proposals to conduct pilot time-resolved SAXS experiments on their systems.


Time-Resolved SAXS
====================

The utility of SAXS in no more limited to the structural characterization
of biological macromolecules in equilibrium. We are actively developing
technologies to investigate the dynamic behavior of the macromolecules using
SAXS during processes such as protein and RNA folding, and enzyme-substrate/co-factor
binding. Studying structural changes in time regimes ranging from ~50µs to
seconds requires the use of a variety of mixers that can interface with the
SAXS instrument. Stopped flow mixers have been used by several groups and
have shown dead-times less than 1ms (Jacob, Krantz et al. 2004, Roh, Guo
et al. 2010). However, continuous flow mixers have emerged as the best option
for SAXS in sub-millisecond time-scales.

.. image:: {filename}/images/LaminarFlowFigure.jpg
    :class: img-responsive
    :align: center

Rapid mixing devices for SAXS have fallen into two broad categories --
turbulent and laminar (Pollack and Doniach 2009, Kathuria, Guo et al. 2011,
Kathuria, Chan et al. 2013). These devices facilitate rapid and efficient
mixing events between multiple fluid streams containing the biological
macromolecule of interest and small solutes that engender structural
changes in the macromolecule. Laminar mixing utilizes hydrodynamic focusing
to reduce the central flow channel to a narrow (typically ~0.1-10 µm)
sheath. A version of this mixer is currently under development at BioCAT
(See Figure). For turbulent mixing, turbulent flow that breaks the solution
into eddies small enough for reactants to diffuse rapidly. Turbulent flow
mixers have the advantage of being able to use all of the delivered photon
flux in the X-ray beam for the best signal to noise ratio. The plug flow
in this kind of mixer also makes the reaction time uniform orthogonally
to the flow-direction thus making its incorporation into a SAXS camera
quite straight forward. The progress we have made in terms of time
resolution and sample consumption are well documented (Wu, Kondrashkina
et al. 2008, Graceffa, Nobrega et al. 2014, Kathuria, Kayatekin et al.
2014, and Nobrega, Arora et al. 2014). In its' current iteration, we can
access time regimes as low as 50µs and a complete experiment can be
performed with as little as 10mgs of sample.

*   How to perform a SAXS experiment and analyze the data
*   SAXS Resource Links
*   Useful References

    *   Books:

        *   Glatter, O. and Kratky, O. Small-angle X-ray scattering, Academic Press, London, 1982.

    *   Reviews:

        *   Vachette P, Koch MH, and Svergun DI., “Looking behind the
            beamstop: X-ray solution scattering studies of structure and
            conformational changes of biological macromolecules,” Methods
            Enzymol., 374, 584-615. (2003)
        *   Koch MH, Vachette P, and Svergun DI., “Small-angle scattering:
            a view on the properties, structures and structural changes of
            biological macromolecules in solution,” Rev Biophys., 36, 147-227. (2003)
        *   Svergun DI. and Koch MH., “Advances in structure analysis using
            small-angle scattering in solution,” Curr. Opin. Struct. Biol.,
            12(5), 654-60 (2002)
        *   Doniach S., “Changes in biomolecular conformation seen by small
            angle X-ray scattering,” Chem Rev., 101, 1763-78 (2001)

Instrumentation for SAXS
==========================

For static SAXS We have a custom flow cell with a water-jacketed 1.5 mm
diameter quartz capillary for sample observation. This can either be connected
to one of several Hamilton Microlab 500 series programmable syringe pumps or
to the output of one of the FPLC’s. We have an AKTA and Akta Pure FPLC apparatus
for liquid chromatography and a Malvern Zetasizer Dynamic Light Scattering
apparatus. We have two ISCO model 500D and four Harvard Instrument model PHD
4400 programmable, high-pressure pumps for the continuous flow mixer project.
We have two Biologic SFM-400 stopped flow mixers, one with an MEC 22998
microvolume mixer allowing 0.5 ms dead time and an x-ray observation cell.
We have recently re-commissioned our autosampler system that can provide
automated sample handling for systems that do not require inline size exclusion
chromatography. The system consists of a Sparks-Holland sample robot that is
used to select particular samples from 96 well plates (with temperature control)
and deliver them to a Hamilton Microlab ML560 dispenser system that can inject
them into the standard sample chamber. Labview based software controls the
sequence of operations required for unattended data acquisition including
cleaning the sample cell, loading samples, flowing samples and triggering
the CCD and recovering the sample after exposure.


Standard SAXS Camera Configurations
========================================

SAXS cameras are used for both Small-Angle X-ray Solution Scattering (SAXS)
and fiber diffraction studies of muscle and connective tissue. While cameras
as short as 0.2 m and as long as 5.5 m are possible with the beamline optics,
we have standardized on a few selected camera lengths that match our available
detectors and commonly required Q-ranges. These camera lengths and Q-ranges
(detector offset) at 12 keV X-ray energy are given in Table 1. At the current
stage of development there is no great benefit in using cameras longer than
3.5 m. If the developments described in Technical R&D project 2 are successful
this can be revisited. Various combinations of stainless steel flight tube
sections allow a range of sample to detector distances. The flight tubes can
be moved in and out of position using overhead cranes. Mica windows are used
throughout except for the rear exit window, which is composed of 0.127 mm
thick Kapton film. The setup routinely uses a 4 mm diameter backstop with
an integrated single-element PIN photodiode for transmission measurements.
For SAXS experiments, the beam is defined by the collimator slits described
above. Three meters downstream of these slits are the guard slits Xenocs
"scatterless" slits) mounted on motorized horizontal and vertical
translation stages. This allows for accurate positioning and profiling of
the beam for diagnostic purposes. A number of different sample holders,
either supplied by the user or by BioCAT, can be mounted on crossed-roller
horizontal and vertical translation slides with 100 mm of travel and capable
of carrying up to 258 kg loads. Control of the sample holder position is
integrated with the detector control and data acquisition systems.

.. class:: table-hover

    ================= ================================ ================================ ======================================= ===================================
    Camera Length (m) Q\ :sub:`min`\  (A\ :sup:`-1`\ ) Q\ :sub:`max`\  (A\ :sup:`-1`\ ) First Order Resolution (A\ :sup:`-1`\ ) Maximum Resolution (A\ :sup:`-1`\ )
    ================= ================================ ================================ ======================================= ===================================
    1.5               0.009                            0.6                              700                                     10
    2.0               0.0075                           0.42                             840                                     15
    2.5               0.006                            0.35                             1050                                    18
    3.0               0.005                            0.3                              1260                                    20
    3.5               0.0045                           0.2                              1400                                    30
    ================= ================================ ================================ ======================================= ===================================
