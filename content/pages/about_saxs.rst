:title: Macromolecular Solution Small-Angle X-ray Scattering (SAXS)
:category: about
:slug: about-saxs

.. image:: {filename}/images/about_saxs.jpg
    :class: img-responsive
    :align: center

.. lead::
    A significant number of proteins can not be crystallized. For those proteins,
    it is possible to acquire valuable structural information (size and shape)
    by analyzing the manner in which they scatter X-rays known as Small Angle
    X-ray Scattering (SAXS). This technique is used to study how the macromolecules
    in our cells  interact with each other and function as “molecular machines.”

Basic information obtained from the typical SAXS experiment is radius of gyration (Rg)
and the electron pair distance distribution function (P(r)), which in turn can be
used to generate ab initio low-resolution molecular envelopes of macromolecules in solution.
To learn more about designing and carrying out SAXS experiments at BioCAT see
our `user guides <{filename}/pages/users_howto.rst>`_.


Equilibrium SAXS
===================

The BioCAT standard experimental set-up includes a Pilatus 1M detector from
Dectris (Switzerland) and a camera of 3.5 m sample-to-detector distance to
access a range of momentum transfer, q, from ~0.004 to 0.36 Å\ :sup:`-1`. This range
of q allows not only accurate determination of radius of gyration, but also
detailed modeling using ab initio and rigid body approaches. A temperature controlled
quartz capillary (1.0 mm ID) flow cell with `coflow sample geometry <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5137223/>`_
is used for SEC-SAXS and SEC-MALS-SAXS sample measurement. The coflow
setup minimizes radiation damage on the sample, ensuring optimum signal to noise
and baseline stability for consistently high quality data. For batch mode SAXS
a temperature controlled quartz capillary (1.5 mm ID, 1.52 mm OD) flow cell
is used for sample measurement.

Note: Currently, switching between SEC-SAXS/SEC-MALS-SAXS and batch mode
experiments takes ~1 shift and must be arranged with a beamline scientist
prior to your beamtime.

The BioCAT beamline provides the following three modes of equilibrium SAXS.

SEC-SAXS
^^^^^^^^^

.. _sec-saxs:

The standard mode of SAXS data collection uses in-line Size Exclusion
Chromatography (SEC) coupled to SAXS (SEC-SAXS). The sample runs through a
size exclusion column to separate potential aggregates or different oligomeric
states immediately before flowing through the capillary for X-ray exposure.

BioCAT provides an AKTA Pure FPLC with two pumps, column and loop valves, and a
multi-wavelength UV detector. The beamline also has the following GE columns available
for users, though users are encouraged to bring their own columns to address potential
cross contamination and reproducibility issues:

*   Superdex 200 Increase, both 10/300 and 5/150 (MW ~10-600 kDa)
*   Superdex 75, both 10/300 and 5/150 (MW ~3-70 kDa)
*   Superose 6, 10/300 (MW ~5-5,000 kDa)

SEC-MALS-SAXS
^^^^^^^^^^^^^^

.. _sec-mals-saxs:

BioCAT also provides a data collection mode where SEC is coupled to MALS (multi-angle
light scattering), DLS (dynamic light scattering), and RI (refractive index) detectors
in addition to the SAXS flow-cell. The additional light scattering detectors provide
accurate measurement of molecular weight, which is often hard to determine via
SAXS methods. The measurement of the hydrodynamic radius in combination with
Rg from SAXS informs on the particle shape. SAXS and MALS-DLS-RI are measured on
the same SEC elution, which goes through the UV, MALS/DLS, and RI detectors
and then to the SAXS flow-cell. This approach provides all of the sample prep
benefits of SEC-SAXS and eliminates possible ambiguity about differences between
non-identical separate SAXS and MALS-DLS measurements. Sample quality pre-requisites for
this system are considerably more stringent than the simpler SEC-SAXS setup and
the suitability of your sample must be determined through discussion with beamline
personnel.

BioCAT provides two Agilent Infinity II HPLCs each with a Wyatt DAWN HELEOS II MALS+DLS
(17 channels LS, plus 1 DLS) detector, and a Wyatt Optilab T-rEX dRI detector.
The beamline also has the following Wyatt columns available for users:

*   010S5 100Å (MW range 0.1-100 kDa)
*   015S5 150Å (MW range 0.5-150 kDa)
*   030S5 300Å (MW range 5-1,250 kDa)

Batch Mode
^^^^^^^^^^^^^^^

.. _batch-saxs:

Batch mode samples are directly loaded into the sample cell, rather than
first passing through a sizing column. This reduces the volume and concentration
required, but aggregates and other large species are not separated from the
sample, increasing requirements on sample prep. At BioCAT, these measurements
take ~100 µl of sample. However, in some cases smaller volumes
can also yield usable SAXS data. In order to reduce radiation damage, the
sample flows through or oscillates in the X-ray beam using a Hamilton
programmable dual-syringe pump.


Time-Resolved SAXS
====================

The high flux and efficient detectors at BioCAT enable time-resolved SAXS
experiments that investigate the dynamic behavior of the macromolecules
during processes such as protein and RNA folding, and enzyme-substrate/co-factor
binding. BioCAT provides two different modes of time-resolved SAXS.

Continuous Flow
^^^^^^^^^^^^^^^^

BioCAT has been developing advanced microfluidic mixers, including a chaotic/turbulent
mixer and a laminar flow mixer, to collect SAXS data on reactions as fast
as ~100 µs. Rapid mixing devices for SAXS have fallen into two broad categories --
chaotic/turbulent and laminar. These devices facilitate rapid and efficient
mixing events between multiple fluid streams containing the biological
macromolecule of interest and small solutes that engender structural
changes in the macromolecule.

Laminar mixing utilizes hydrodynamic focusing to reduce the central flow channel
to a narrow (typically ~0.1-10 µm) sheath. A version of this mixer is currently
under development at BioCAT. For chaotic/turbulent mixing, chaotic/turbulent
flow breaks the solution into eddies small enough for reactants to diffuse
rapidly. Chaotic/turbulent flow mixers have the advantage of being able to use
all of the delivered photon flux in the X-ray beam for the best signal to noise
ratio. The plug flow in this kind of mixer also makes the reaction time uniform
orthogonally to the flow-direction thus making its incorporation into a SAXS camera
quite straight forward. In its current iteration, the BioCAT mixer can access
time regimes as low as 50 µs and a complete experiment can be performed with
as little as 10 mg of sample.

Currently experiments are collaborations with beamline staff, and users are
encouraged to discuss possible experiments with the `SAXS scientific contact <{filename}/pages/contact.rst>`_.

Stopped Flow
^^^^^^^^^^^^^

The BioCAT stopped flow setup uses a Biologic SFM-400 stopped flow mixer
with an MEC 22998 micro-volume mixer, allowing 0.5 ms dead time, and an
x-ray observation cell. Because of the limitations in time resolution and
possibility of radiation damage, unless you specifically know your experiment
requires stopped flow mixing, BioCAT recommends using the continuous flow systems.


Instrumentation for SAXS
==========================

In addition to the instrumentation described above, BioCAT has a fully equipped
`wet lab <{filename}/pages/about_support.rst#wetlab>`_ for sample preparation. In addition
to the `beamline instrumentation described elsewhere <{filename}/pages/about_beamline.rst>`_,
a set of in-vacuum JJ x-ray slits are used as the collimating beam slits, and a
set of in-vacuum Xenocs scatterless x-ray slits are used as the guard slits.
An in-line sample camera is located just after the guard slits, using a mirror
with a 6 mm through hole for the x-ray beam. BioCAT also has two ISCO model
500D and four Harvard Instrument model PHD 4400 programmable, high-pressure
pumps for the continuous flow mixer project. Normalization of data is done using
an `active beamstop which uses indirect detection on a photodiode
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4344362/>`_.
