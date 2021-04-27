How to design an equilibrium SAXS experiment
###############################################################################

:category: users
:slug: how-to-design-saxs-exp


SAXS has emerged as a standard biophysical tool deployed routinely for
characterizing macromolecules of biomedical interest. The relative logistical
simplicity embodied in a technique that provides easy access to the size and
low-resolution shape of macromolecules makes it an essential part of the
biophysicists' tool kit. With the introduction of Size-Exclusion Chromatography
(SEC)-SAXS at BioCAT, which ensures monodispersity of even the most biochemically
challenging molecules, structural parameters such as the Radius of Gyration (Rg),
Maximum Dimension (Dmax), Volume and Molecular weight estimates can be determined
with a high degree of success for a large variety of samples.

There are foure equilibrium data acquisition strategies available at BioCAT:
`SEC-SAXS <{filename}/pages/about_saxs.rst#sec-saxs>`_,
`SEC-MALS-SAXS <{filename}/pages/about_saxs.rst#sec-mals-saxs>`_,
`IEC-SAXS <{filename}/pages/about_saxs.rst#iec-saxs>`_ and
`batch mode SAXS <{filename}/pages/about_saxs.rst#batch-saxs>`_.

Below we give some general guidelines for designing your SAXS experiment. If you
have questions, or are a new user, please `contact a beamline scientist <{filename}/pages/contact.rst>`_.

.. contents:: Topics:


What technique should I use?
=============================

BioCAT strongly encourages all users to use either SEC-SAXS or SEC-MALS-SAXS.
IIf multiple components in solution cannot be separated by size, IEC-SAXS may
be the appropriate choice. There are also some rare cases where
sample concentration and volume are inadequate for SEC-SAXS, in which case you
will use batch mode. Batch mode is also useful if you need to measure a
large number of buffer conditions, such as in a titration experiment.

SEC-MALS-SAXS allows highly accurate quantification of molecular weight,
making it generally superior to SEC-SAXS. However, the equilibration times
for the SEC-MALS system are quite long (at least 6 hours), which limits the
number of buffer changes. Because of the sensitivity of the system,
the requirements on the sample quality are much higher than for SEC-SAXS.

SEC-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Your system has a single well defined peak or several well resolved peaks
    (not including large aggregates that show up in the void)
*   You will need to make several buffer changes during your experiment

SEC-MALS-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have a complicated elution with several overlapping or poorly resolved
    peaks
*   You are measuring a complex or oligomer with unknown stoichiometry
*   You need at most one buffer change
*   There is a small amount of elution in the void

IEC-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have multiple components in solution that cannot be well separated by size
*   You can design an IEC gradient that separates your components

Batch mode SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You can't meet the concentration and volume requirements for SEC-SAXS
    (see below)
*   You need a large number (>~5) buffer changes due to the nature of your
    experiment (e.g. a titration experiment)
*   Your system does not survive the a column, for example some weakly associating
    complexes


What sample concentration and volume do I need?
================================================

Concentration
^^^^^^^^^^^^^^

As a rule of thumb, you will get good SAXS data if you prepare a protein concentration
in mg/ml that is:

*   240/MW in kDa for SEC-SAXS or SEC-MALS-SAXS
*   60/MW in kDa for batch mode SAXS

For example, using SEC-SAXS for a 20 kDa protein you would want a
concentration of ~240/20 = 12 mg/ml whereas for a 150 kDa
protein you would want a concentration of ~240/150 = 1.6 mg/ml. RNA and DNA
samples scatter ~2.5 times more strongly than protein, so you can use a
concentration of ~96/MW and 24/MW for SEC-SAXS and batch mode SAXS respectively.

Note that in SEC-SAXS and SEC-MALS-SAXS experiments the sample is diluted by the column,
and may elute in several peaks. This should be accounted for. The recommendation above
adds a column dilution factor of ~4x for your SEC-SAXS sample preps. If a
significant amount of your sample elutes in other peaks, further increase your
concentration to compensate.

Also, for SEC-SAXS, if your sample has concentration dependent aggregation
that prevents you from achieving the high concentrations needed, you may be
able to compensate by increasing your load volume.

Volume
^^^^^^^

Typical SEC-SAXS and SEC-MALS-SAXS injection volumes are ~250-350 µl.

Batch mode experiments can be done routinely with 50 µl per measurement. Note
that typical batch mode experiments require measuring several concentrations, and
so can actually end up requiring more volume than a SEC-SAXS experiment.


How many samples should I bring?
=================================

When considering how many samples to bring, you need to think both about the
experiment time and the equilibration.

Experiment time
^^^^^^^^^^^^^^^^^^

At BioCAT, users typically use the GE Superdex 200 Increase 10/300 GL column.
This has a column volume of 24 and a flow rates of ~0.7 ml. That means that
a 1.5 column volume (CV) experiment for SEC-SAXS or SEC-MALS-SAXS takes ~50
minutes. If you know that nothing elutes after 1 CV (including small molecules)
you can further reduce this to ~34 minutes. So you should expect to run ~1-2 samples an
hour.

With the coflow cell, BioCAT users now have the ability to run samples on the
GE 5/150 columns without radiation damage. These columns provide significantly
less separation, and so should only be used on a system with very well resolved
peaks (ideally just one peak, or a peak plus elution at the void volume). However,
if your sample is appropriate, the volume requirements and run times are much
lower. With these columns, typical load volumes are ~100 µL and run times
are ~10 minutes.

Note: If you bring your own column, run times will depend on the flow rate and
volume for that column.

Batch mode samples are much faster, typically only 3-30 s of exposure. Throughput
is limited by sample loading. Realistically, expect to do a sample every 3-5 minutes.

Equilibration
^^^^^^^^^^^^^^

You will have to equilibrate the column at the start of your SEC-SAXS or
SEC-MALS-SAXS experiment, and every time thereafter that you want to change
buffers. For SEC-SAXS, we recommend a 2 CV equilibration, which for a
GE Superdex 200 Increase 10/300 GL column will take ~1.25 hours. For SEC-MALS-SAXS,
equilibration requires at least 6 hours, and is ideally done overnight.


What column should I use?
===========================

BioCAT provides a number of columns for users. Typically, users will use one
of these:

*   Superdex 200 Increase, both 10/300 and 5/150 (MW ~10-600 kDa)
*   Superdex 75 Increase 10/300, with a non-Increase 5/150 also available (MW ~3-70 kDa)
*   Superose 6 Increase, 10/300 (MW ~5-5,000 kDa)

Generally speaking, pick the column with the narrowest MW range that can
accommodate your samples. But remember that the MW range is for globular
proteins, extended proteins run as if they are higher MW! BioCAT recommends
running a test separation in your lab, to ensure you can resolve your species.
The default column at BioCAT for all experiments is the Superdex 200 Increase 10/300.

A full list of columns and the corresponding MW ranges is available for both
`SEC-SAXS <{filename}/pages/about_saxs.rst#sec-saxs>`_ and
`SEC-MALS-SAXS <{filename}/pages/about_saxs.rst#sec-mals-saxs>`_.

Users may also provide their own columns if desired. However, due to the dilution
factor, we recommend that you only use analytical grade columns, not the larger
prep columns like the Cytive HiPrep or HiLoad columns.


How much buffer should I bring?
=================================

.. _saxs_buffer_volume:

The following are intended as guidelines for users when planning their experiments.
However, as most buffers do not contain precious components, we recommend bringing
more buffer than you think you'll need, for example taking the below numbers and adding
50%. You never know when you might want to change buffers and do one more run
with a given sample, and have to equilibrate the column again.

If you have precious components in your buffer, there are ways to reduce
your buffer usage. Please contact a beamline scientist to discuss those situations.

Given the large volume of buffer required for experiments, many of BioCAT's
users find it convenient to bring 10x concentrated stocks of buffer and then
dilute on-site.

SEC-SAXS
^^^^^^^^^

For SEC-SAXS experiments, you can calculate the amount of buffer you need as:

Buffer volume = 4*(column volume)*(number of samples + 1) + 100 mL

This accounts for both the per-sample use and the equilibration. Please note
that the system cannot use all the buffer in a bottle, as you cannot
risk drawing air into the system. This is the 100 mL offset in the above formula.

For example, if you are using the GE Superdex 200 Increase 10/300 GL column,
it has a column volume of 24 mL. If you're planning to run 5 samples in a particular
buffer you should bring:

Buffer volume = 4*(24 mL)*(5+1) + 100 mL ~ 0.7 L

For these experiments, you should always bring at least 0.5 L of any buffer you
are using.


SEC-MALS-SAXS
^^^^^^^^^^^^^^

For SEC-MALS-SAXS experiments equilibration needs significantly more buffer than
SEC-SAXS experiments. Additionally, you cannot stop the buffer flow between
experiments. In this case it is more useful to calculate buffer requirements by running
time. Equilibration is done at the same flow rate as experiments. The coflow sheath
also requires buffer. Given that, you can calculate the buffer you need as follows:

Buffer volume = 4*(experiment time)*(flow rate) + (equilibration time)*(flow rate)

For example, if you are using the Wyatt WTC-030S5 which has a flow rate of 0.8 mL/min,
and you plan on 12 hours (720 minutes) of equilibration (overnight) and 8 hours
(480 minutes) of experiments in a given buffer, you should bring:

Buffer volume = 4*(480)*(0.8 mL/min) + (720)*(0.8 mL/min) ~ 2.1 L

For these experiments, you should always bring at least 1.5 L of any buffer you
are using.

Batch Mode
^^^^^^^^^^^

Batch mode experiments require a basic running buffer with ~ 1 L of volume.
For buffers with precious or limited components, a basic running buffer need not
contain that component. The same is true if you have lots of buffer changes (e.g.
titration of a ligand or salt concentration).

Besides the basic running buffer, you need additional aliquots of a perfectly
matched buffer for each sample. You nominally need just 200 µl of
each matched buffer per sample (where each different concentration of the same
system counts as a distinct sample). However, we never recommend bringing less
than ~5 mL of each buffer, just in case. If you are in a situation where this
is too much, please contact a beamline scientist to discuss how much buffer you need.


