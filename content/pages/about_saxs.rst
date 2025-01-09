Macromolecular Solution Small-Angle X-ray Scattering (SAXS)
############################################################

:category: about
:slug: about-saxs

.. image:: {static}/images/about_saxs.jpg
    :class: img-responsive
    :align: center

.. lead::
    For those proteins, it is possible to acquire valuable structural
    information (size and shape) by analyzing the manner in which they scatter
    X-rays in solution, known as Small Angle X-ray Scattering (SAXS). This
    technique is used to study how the macromolecules in our cells interact
    with each other and function as “molecular machines.”

Small-angle X-ray scattering (SAXS) is a popular structural and biophysical
technique used to study the solution state of biological macromolecules and
complexes. SAXS can provide information including, but not limited to, size
and molecular weight, flexibility, degree of folding, overall shape, and even
pseudo-atomic structural models. Over the past 25 years, driven by new
high-brilliance synchrotron beamlines, advances in detector technology, and
the development of a wide range of powerful software analysis tools, SAXS has
become a mainstream structural biology/biophysical technique. Key to the growing
popularity of SAXS have been new experimental approaches able to probe challenging
systems, specifically in-line purification techniques coupled to SAXS, including
size-exclusion chromatography, ion-exchange chromatography and, very recently,
asymmetric flow field-flow fractionation (SEC-SAXS, IEC-SAXS, and AF4-SAXS). Having in-line
purification allows high-quality measurements on less stable and more
heterogeneous biological samples that were previously intractable for SAXS.
The increasing automation of data collection and analysis and a growing
awareness that SAXS is highly complementary to other structural and biophysical
techniques such as X-ray crystallography (MX), nuclear magnetic resonance (NMR),
cryo-electron microscopy (cryo-EM) and multi-angle and dynamic light scattering
(MALS and DLS) also contribute to the popularity of the technique. Additionally,
SAXS has proven invaluable for studying intrinsically disordered proteins (IDPs)
and liquid-liquid phase separating (LLPS) systems, which are not amenable to
common high resolution structural techniques such as MX and cryo-EM.

To learn more about designing and carrying out SAXS experiments at BioCAT see
our `user guides <{filename}/pages/users_howto.rst>`_.

.. contents::


Equilibrium SAXS
===================

Basic characteristics of the equilibrium SAXS setup at BioCAT:

.. class:: table-hover

    ===================================================== =============================================================================
    Energy                                                12 keV
    Flux                                                  ~7*10\ :sup:`12` ph/s
    Energy Resolution (dE/E)                              2 x 10\ :sup:`-4` (Si <111>)
    Beam size (FWHM)                                      ~25 x 16 µm\ :sup:`2` (V x H), focused at the detector
    Sample to detector distance                           ~3.7 m
    q range                                               ~0.0027 - 0.43 Å\ :sup:`-1`
    Detector                                              EIGER2 XE 9M (Dectris)
    Sample cell                                           Coflow cell with a 1.0 mm ID quartz capillary
    Temperature range                                     4 - 40 ˚C (more extreme temperatures may be possible upon request)
    ===================================================== =============================================================================

While data acquisition during a typical SAXS experiment is relatively simple,
data quality and interpretability are largely dependent on sample homogeneity
and monodispersity, which is often compromised due to the limited shelf-lives
of biological macromolecules. A majority of BioCAT users prefer to use the
in-line SEC-SAXS instrument, which separates by size the sample from potential
contaminants such as aggregates or breakdown products immediately before exposure
to X-rays. BioCAT also provides other in-line purification techniques: IEC-SAXS
for charged-based separation of samples and AF4-SAXS for size-based separation
without the matrix of a column. AF4-SAXS is of particular interest for systems
like lipid nanoparticles (LNPs) and liposomes, which tend to behave poorly on
SEC columns but are of great interest currently for drug delivery purposes.
BioCAT also has a newly built batch mode autosampler capable of low volume batch
mode measurements from 96- and 384-well plates. For all of these experiments
BioCAT offers in-line full-spectrum UV absorption measurements.

For SEC-SAXS and AF4-SAXS, BioCAT provides the option of additional coupled
biophysical measurements, MALS, DLS, and RI, as part of the same
experiment (SEC-MALS-SAXS or AF4-MALS-SAXS). MALS plus RI provides a more
accurate determination of molecular weight than SAXS, which is particularly
valuable for determining the oligomeric state of macromolecules and the
stoichiometry of multicomponent complexes. Having both UV absorption and RI
measurements allows the use of conjugate analysis to calculate the mass
fraction of different components in a complex. This is particularly useful for
determining the mass fraction of lipids in detergent solvated membrane protein
systems, the degree of glycosylation for glycoproteins and binding
stoichiometries for complexes between nucleic-acids and proteins. The Rh from
DLS measurements in ratio with the Rg value from SAXS measurements provides
information on the overall particle shape.

Besides these data collection modalities, BioCAT provides additional experimental
capabilities that enhance SAXS data collection at the beamline. An in-vacuum
coflow cell is used for all equilibrium techniques to minimize background
scattering and radiation damage to samples, providing optimal signal-to-noise
ratio measurements, and all systems are fully temperature controlled (including
the HPLC, columns, and fluidic lines) for experiments anywhere between 4-40 ˚C.
BioCAT also has a robust data processing pipeline that provides real-time data
reduction, so experiments can be monitored while being run, and that provides
initial automated analysis, including background subtraction, Guinier fits, P(r)
calculation, and ab initio modeling, shortly after the experiment finishes,
allowing users a quick look at preliminary results. Taken as a whole, BioCAT
provides a mature, state-of-the-art facility for equilibrium SAXS capable of
tackling the most challenging systems.


SEC-SAXS, SEC-MALS-SAXS, and IEC-SAXS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _sec-saxs:

.. _sec-mals-saxs:

.. _iec-saxs:


BioCAT provides a custom designed HPLC system with two Agilent 1260 Infinity II bioinert
pumps, an Agilent 1260 Infinity II bioinert multisampler, and customized valves and
control software that allow for measurement by a column on one pump while simultaneously
equilibrating a column on the other. Users can switch between the two flow paths
with the click of a button, providing highly automated sample measurement. The
entire system is housed in a temperature controlled and variable incubator, and
water jacketed lines feed the temperature controlled sample cell for optimal
stability and variability. Full spectrum UV absorbance measurements are collected during
every elution using a fiber coupled flow cell, a balanced Halogen-Deuterium light source
(Ocean Insight) and a Black-Comet spectrometer (StellarNet). This custom HPLC is
used for SEC-SAXS, SEC-MALS-SAXS, and IEC-SAXS.

The beamline also has the following SEC columns available for users, though users
may also bring their own columns to address potential cross contamination and
reproducibility issues:

*   Superdex 30 Increase 10/300 (MW ~0.1-7 kDa)
*   Superdex 75 Increase, both 10/300 and 5/150 (MW ~3-70 kDa)
*   Superdex 200 Increase, both 10/300 and 5/150 (MW ~10-600 kDa)
*   Superose 6 Increase, both 10/300 and 5/150 (MW ~5-5,000 kDa)
*   Wyatt 010S5 100Å (MW range 0.1-100 kDa)
*   Wyatt 015S5 150Å (MW range 0.5-150 kDa)
*   Wyatt 030S5 300Å (MW range 5-1,250 kDa)

SEC-SAXS
-----------

The standard mode of SAXS data collection uses in-line Size Exclusion
Chromatography (SEC) coupled to SAXS (SEC-SAXS). The sample runs through a
size exclusion column to separate potential aggregates or different oligomeric
states immediately before flowing through the capillary for X-ray exposure.

SEC-MALS-SAXS
--------------

BioCAT provides a data collection mode where SEC is coupled to MALS (multi-angle
light scattering), DLS (dynamic light scattering), and RI (refractive index) detectors
in addition to the SAXS flow-cell, a technique called SEC-MALS-SAXS. A Wyatt
DAWN HELEOS II MALS+DLS (17 channels LS, plus 1 DLS) detector, and a Wyatt Optilab
T-rEX dRI detector are used for these measurements. The MALS and RI detectors
are temperature controlled from 4-40 C. This approach  provides all of the
sample quality benefits of SEC-SAXS and eliminates possible ambiguity about
differences between non-identical separate SEC-SAXS and SEC-MALS-DLS-RI measurements.
There is a small loss of resolution compared to SEC-SAXS due to the additional
detectors, so this method should only be used if the MALS and DLS data are needed
for the experiment.


IEC-SAXS
-----------

Ion exchange chromatography (IEC) allows separation of particles by charge
rather than size, making it useful in cases where SEC cannot resolve between
different components in solution. BioCAT offers IEC in-line with SAXS (IEC-SAXS)
for samples that are not separable by SEC-SAXS. Because IEC requires a changing
buffer during elution (typically a slope or step gradient in salt or pH), data
analysis is more involved than for SEC-SAXS, but analysis algorithms are now
widely available, making this a routine technique at the beamline. These
experiments are more involved, and often require some work to optimize an
appropriate gradient, so it is important to discuss your potential IEC-SAXS
experiments with beamline personnel before requesting beamtime.

The custom HPLC used for SEC-SAXS is also capable of IEC-SAXS as each pump is
a quaternary pump able to create the necessary gradient for elution. BioCAT has the
following IEC columns available for users:

*   Capto HiRes Q 5/50
*   Capto HiRes S 5/50

Batch Mode
^^^^^^^^^^^^^^^

.. _batch-saxs:

Batch mode samples are directly loaded into the sample cell, rather than
first passing through a sizing column. This reduces the volume and concentration
required, but aggregates and other large species are not separated from the
sample, increasing requirements on sample prep. BioCAT has a custom built
batch mode autosampler capable of loading samples from 96 and 384 well plates.
The plates are temperature controlled, and the measurements are done in the coflow
sample cell to minimize radiation damage. This autosampler can run one sample
every ~3 minutes.

At BioCAT, these measurements batch mode measurements take ~10 µl of sample.
However, in some cases smaller volumes can also yield usable SAXS data.

AF4-MALS-SAXS
^^^^^^^^^^^^^^^^

.. _af4-mals-saxs:

Asymmetric flow field-flow fractionation (AF4) is a method for size-based
separation of macromolecules with no stationary phase and almost no shear.
This makes it a power alternative separation technique for systems that are
challenging to separate on an SEC, either due to column interactions, or
stability issues due to the shear and high hydrostatic pressures of columns.
BiocAT profiles AF4 in-line with MALS, DLS, RI, and SAXS (AF4-MALS-SAXS).
AF4-SAXS is of particular interest for systems like lipid nanoparticles (LNPs)
and liposomes, which tend to behave poorly on SEC columns but are of great
interest currently for drug delivery purposes.

BioCAT uses a Wyatt Eclipse NEON with dilution control module (DCM) for optimal
separation. This is coupled to a Wyatt DAWN HELEOS II MALS+DLS (17 channels LS,
plus 1 DLS) detector, and a Wyatt Optilab T-rEX dRI detector for the MALS-DLS-RI
measurements. BioCAT provides the following channels, spacers, and membranes for
users:

*   Wyatt Short Channel
*   Wyatt Long Channel
*   Wyatt Dispersion Inlet Channel
*   Polyethersulfone (PES) membranes with 5, 10 and 30 kDa MW cutoffs
*   Regenerated cellulose (RC) membranes with 2, 5, 10 and 30 kDa MW cutoffs
*   275, 400 and 525 µm spacers

These experiments are more involved, and often require some work to optimize an
appropriate elution program, so it is important to discuss your potential AF4-MALS-SAXS
experiments with beamline personnel before requesting beamtime.


Time-Resolved SAXS
====================

Basic characteristics of the time-resolved SAXS setup at BioCAT:

.. class:: table-hover

    ===================================================== =============================================================================
    Energy                                                12 keV
    Flux                                                  ~2*10\ :sup:`12` ph/s
    Energy Resolution (dE/E)                              2 x 10\ :sup:`-4` (Si <111>)
    Beam size (FWHM)                                      ~3 x 2 µm\ :sup:`2` (V x H), focused at the sample
    Sample to detector distance                           ~2 m
    q range                                               ~0.01 - 0.65 Å\ :sup:`-1`
    Detector                                              EIGER2 XE 9M (Dectris)
    Temperature                                           RT
    Time range (chaotic mixer)                            45 μs to 60 ms
    Time range (laminar mixer)                            5 ms to 1.5 s
    Time range (stopped flow)                             >1 ms
    ===================================================== =============================================================================

While studying biological macromolecules in equilibrium remains the predominant
use of SAXS, the focus of considerable effort at BioCAT over the past 15 years
has been the development of instruments for time-resolved SAXS (TR-SAXS) that
allow real time measurement of macromolecules while they undergo conformational
transformations. Of particular interest are transient states too short lived to
be studied using most techniques. In order to answer these questions, BioCAT
provides general users access to routine experiments with two different continuous
flow microfluidic mixers, which together provide access to time ranges after
mixing from sub-50 μs to 1.5 s. BioCAT also has a stopped flow instrument and
on-plate mixing in the batch mode autosampler for access to longer time ranges.
BioCAT provides all of the necessary hardware and the control and analysis software,
so all users have to do is provide their sample and buffer, just like an
equilibrium SAXS experiment.

Mixing-based TR-SAXS experiments occupy a unique spot in the landscape of X-ray
techniques studying time resolved changes in biological macromolecules. While
laser pump-probe SAXS/WAXS experiments at XFELs and synchrotrons can access
much faster time ranges (fs and ps respectively), these types of experiments
are limited in the range of reactions that can be studied to only samples with
light induced conformation changes or, more recently, temperature jump and caged
compound triggered reactions (though these tend to be on slower timescales).
While not amenable to ultra-fast timescales, mixing can study any process
initiated by a change in solution conditions, such as these conditions explored
by BioCAT users: salt jump, pH jump, addition of a ligand/substrate/co-factor,
addition of another macromolecule and renaturation by dilution of denaturant. The
sample consumption for the mixer experiments is also typically much lower than
pump probe experiments, often <1 mg for slower reactions, whereas XFEL and
synchrotron pump probe experiments can use 50-100 mg or more. While
higher-resolution techniques such as time resolved MX, freeze-quench
time-resolved cryo-EM, and time-resolved NMR are also used to study these
types of reactions and can provide vital information, they all have
limitations such as restrictions on large conformation changes (MX), limited
time ranges to generally >1 ms (mixing-based MX, cryo-EM), and restrictions on
size (NMR, cryoEM) and flexibility (cryo-EM, MX). As with most structural biology
questions, there is no perfect technique for every system, but mixing-initiated
TR-SAXS serves an important role by providing fast time points, a wide range of
conditions, and a time range well suited to many interesting biological dynamics,
including many large conformational motions, oligomerization, complexation, and
refolding in macromolecules of essentially any size.

The biological questions that originally motivated the development of TR-SAXS
technology at BioCAT were protein and RNA folding, key to understanding many
human diseases like Alzheimer’s disease, Parkinson’s disease and ALS which are
caused due to mis-folding of proteins. This included user projects looking at
the transient intermediate structural states and the refolding kinetics of
various proteins and RNA. This early focus has expanded, and now a wide variety
of systems are studied, including published work on conformational changes
induced by ligand binding, kinetics of micelle formation, and the kinetics of
liquid-liquid phase separation.

Continuous Flow
^^^^^^^^^^^^^^^^

BioCAT has been developing advanced microfluidic mixers, including a chaotic/turbulent
mixer and a laminar flow mixer, to collect SAXS data on reactions as fast
as ~45 µs. Rapid mixing devices for SAXS have fallen into two broad categories --
chaotic/turbulent and laminar. These devices facilitate rapid and efficient
mixing events between multiple fluid streams containing the biological
macromolecule of interest and small solutes that engender structural
changes in the macromolecule.

Laminar mixing utilizes hydrodynamic focusing to reduce the central flow channel
to a narrow (typically ~1-10 µm) sheath. A version of this mixer based on
a design from the Pollack group at Cornell) is currently
available at BioCAT and can provide access to time ranges from ~5 ms to 1.5 s.
These experiments use modest amounts of sample, ~1 mg per time series
(~100 time points).

In chaotic/turbulent mixing, chaotic/turbulent flow breaks the solution into
eddies small enough for reactants to diffuse rapidly. Mixing can be much more
rapid than in laminar flow mixers, but requires much higher flow rates.
In its current iteration, the BioCAT mixer (developed in collaboration with
the Matthews group at U. Mass.) can access time points from
~45 µs to 60 ms and a complete experiment can be performed with ~10 mg of sample.

Time-resolved experiments are more involved than equilibrium experiments, so
interested users should discuss possible experiments with the `SAXS scientific contact <{filename}/pages/contact.rst>`_.

Both of BioCAT's mixers are microfabricated in quartz by
Translume, with X-ray observation regions with 1 mm (laminar) or 250 μm (chaotic)
deep channels and ~50 μm thick quartz windows. For both mixers, the mixer is
mounted on vertical and horizontal scanning motors, and pumps are connected to
the inlet ports on the mixer. The mixer is placed at the focal point of the
microfocusing CRL optics, so that the small beam passes through the
microfluidic channel without scattering from the edges of the channel. A typical
measured time series consists of ~100 timepoints.

After setup and calibration, the basic data collection procedure is as follows:
First, flow of mixing and sample buffers is started. Then, simultaneously, the
X-ray exposure and a continuous scan of the mixer is started. The X-ray beam is
scanned along the observation region, and images are measured while the mixer is
moving (a continuous/fly scan rather than step scan), which is important for
minimizing radiation damage and maximizing throughput. Each exposure along the
observation region corresponds to a different timepoint after mixing. Repeated
scans along the mixer add additional data at the same timepoints, which improves
the signal to noise of the measurement at the timepoint. After sufficient buffer
scans, the sample is injected into the mixer via an injection valve. Measurements
are carried out while all the sample flows through the mixer, yielding multiple
scans with mixed sample measured at every timepoint. Once all the sample has passed
through the mixer, additional scans of just buffer are measured, yielding pre- and
post-sample buffer and sample measurements at every timepoint as part of the same
experiment. If necessary, the measurement is repeated multiple times to provide
good data at each time point. Typically, at least 3 such measurements are made.

Background scattering varies with position on the mixer, so reproducible scanning
and detector triggering are paramount for data quality. The horizontal motor,
‘down’ the channel to different time points is a Newport XMS160-S capable of 1 nm incremental motions,
0.03 μm bidirectional repeatability, and an optimally level scan. The vertical motor,
‘across’ the channel for alignment and during the scan to account for any small
angular offset of the channel from horizontal, is a Newport GTS30V with similar
precision but with lower speeds. Triggering exposure and metadata collection,
such as transmitted intensity for normalization, on the encoder positions provides
highly reproducible data, to the accuracy of the encoders (1 nm) and jitter in
the various trigger systems (<120 ns).

Fluid handling and monitoring for the laminar mixer uses syringe pumps (Pump 11
Pico Plus Elite, Harvard Apparatus), stand-alone chromatography injection valves
(IDEX MXP9900-00), and flow meters (BFS-1 Elveflow). The chaotic
mixer uses much of the same setup, but is driven by three HPLC pumps (ReaXus LD012PRX Teledyne).

Stopped Flow
^^^^^^^^^^^^^

The BioCAT stopped flow setup uses a Biologic SFM-400 stopped flow mixer
with an MEC 22998 micro-volume mixer, allowing ~1 ms dead time, and an
x-ray observation cell. Because of the limitations in time resolution and
possibility of radiation damage, unless you specifically know your experiment
requires stopped flow mixing, BioCAT recommends using the continuous flow systems.


Instrumentation for SAXS
==========================

In addition to the instrumentation described above, BioCAT has a fully equipped
`wet lab <{filename}/pages/about_support.rst#wetlab>`_ for sample preparation. In addition
to the `beamline instrumentation described elsewhere <{filename}/pages/about_beamline.rst>`_,
two sets of scatterless in-vacuum JJ x-ray slits are used as the collimating and
anti-scatter beam slits, and a two sets of in-vacuum Xenocs scatterless x-ray slits
are used as the guard slits. An in-line sample camera is located just after the
guard slits, using a mirror with a 6 mm through hole for the x-ray beam. Normalization
of data is done using an `active beamstop which uses indirect detection on a photodiode
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4344362/>`_.
