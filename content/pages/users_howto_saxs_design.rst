How to design an equilibrium SAXS experiment
###############################################################################

:category: users
:slug: how-to-design-saxs-exp


SAXS has emerged as a standard biophysical tool deployed routinely for
characterizing macromolecules of biomedical interest. The relative logistical
simplicity embodied in a technique that provides easy access to the size and
low-resolution shape of macromolecules makes it an essential part of the
biophysicists' tool kit. With the range of separation coupled SAXS experiments,
such as SEC-SAXS, at BioCAT, SAXS data can be collected from even the most
challenging systems.

There are four equilibrium data acquisition strategies available at BioCAT:
`SEC-SAXS <{filename}/pages/about_saxs.rst#sec-saxs>`_,
`SEC-MALS-SAXS <{filename}/pages/about_saxs.rst#sec-mals-saxs>`_,
`IEC-SAXS <{filename}/pages/about_saxs.rst#iec-saxs>`_,
`AF4-MALS-SAXS <{filename}/pages/about_saxs.rst#af4-mals-saxs>`_ and
`batch mode SAXS <{filename}/pages/about_saxs.rst#batch-saxs>`_.

Below we give some general guidelines for designing your SAXS experiment. If you
have questions, or are a new user, please `contact a beamline scientist <{filename}/pages/contact.rst>`_.

More details about the specifics of BioCAT's experimental setup can be `found
elsewhere on our website. <{filename}/pages/about_saxs.rst>`_

.. contents:: Topics:


What technique should I use?
=============================

BioCAT strongly encourages users to use either SEC-SAXS or SEC-MALS-SAXS if possible.
If multiple components in solution cannot be separated by size, IEC-SAXS may
be the appropriate choice. If components need to be separated by size but are
not amenable to size exclusion (such as having strong column interactions or
falling apart due to shear or hydrostatic pressure) then AF4-MALS-SAXS is a good
choice. This is of particular use for samples like lipid nanoparticles (LNPs).

There are also some cases where sample concentration and volume are inadequate
for SEC-SAXS, in which case you will use batch mode. Batch mode is also useful
if you need to measure a large number of buffer conditions, such as in
a titration experiment, or where your have a precious component in the buffer
and cannot provide enough buffer for one of the other methods.

SEC-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Your system has a single well defined peak or several well resolved peaks
    (not including large aggregates that show up in the void)
*   You have a complicated elution with several overlapping or poorly resolved
    peaks
*   You will need to make several buffer changes during your experiment

SEC-MALS-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Your system has a single well defined peak or several well resolved peaks
    (not including large aggregates that show up in the void)
*   You are measuring a complex or oligomer with unknown stoichiometry or
    molecular weight
*   You need a minimal number of buffer changes
*   There is little or no elution in the void

IEC-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have multiple components in solution that cannot be well separated by size
*   You can design an IEC gradient that separates your components

AF4-MALS-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Your system is not monodisperse, but cannot be separated well on a
    size exclusion column due to column interactions or other factors
*   Your system is larger than the maximum size that can be separated on
    a size exclusion column

Batch mode SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You can't meet the concentration and volume requirements for SEC-SAXS
    (see below)
*   You can't provide enough buffer for SEC-SAXS due to having a precious
    component (e.g. expensive ligand) in the buffer
*   You need a large number (>~5) buffer changes due to the nature of your
    experiment (e.g. a titration experiment)
*   Your system does not survive the a column, for example some weakly associating
    complexes


What sample concentration and volume do I need?
================================================

SEC-SAXS and SEC-MALS-SAXS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a rule of thumb, you will get good SAXS data if you prepare a protein concentration
in mg/ml that is:

*   240/MW in kDa for SEC-SAXS or SEC-MALS-SAXS

For example, for a 20 kDa protein you would want a concentration of ~240/20 = 12 mg/ml
whereas for a 150 kDa protein you would want a concentration of ~240/150 = 1.6 mg/ml.
RNA and DNA samples scatter ~2.5 times more strongly than protein, so you can use a
concentration of ~96/MW.

Note that the MW calculation is done for the expected oligomeric MW. So if a
protein is a 50 kDa monomer, but you expect it to be dimeric, you would prepare
a concentration of ~240/100 = 2.4 mg/ml.

In SEC-SAXS and SEC-MALS-SAXS experiments the sample may elute in several peaks.
This should be accounted for. If a significant amount of your sample elutes in
other peaks, further increase your concentration to compensate. Also note that
the recommendation above already takes into account the column dilution factor.

Typical SEC-SAXS and SEC-MALS-SAXS injection volumes are ~300 µl.
We recommend that you bring enough sample volume for two measurements at each
condition, that way if something happens during a measurement (such as the
beam going down) we can repeat and obtain the desired data.

Less sample can be used, either as lower concentrations or volumes, either with
lower but still decent signal on the same columns or by using the smaller 5/150
columns with less resolution but similar signal. Talk to your beamline scientist
about options if you cannot product enough sample.


Batch SAXS
^^^^^^^^^^^^^

As a rule of thumb, you will get good SAXS data if you target a protein concentration
in mg/ml that is:

*   60/MW in kDa

For example, for a 20 kDa protein you would want a concentration of ~60/20 = 3 mg/ml
whereas for a 150 kDa protein you would want a concentration of ~60/150 = 0.4 mg/ml.
RNA and DNA samples scatter ~2.5 times more strongly than protein, so you can use a
concentration of ~24/MW.

Note that the MW calculation is done for the expected oligomeric MW. So if a
protein is a 50 kDa monomer, but you expect it to be dimeric, you would prepare
a concentration of ~60/100 = 0.6 mg/ml.

For these experiments you need to prepare at least 3 concentrations, ideally
bracketing the target concentration in factors of 2 or more. For example, for a 100 kDa
protein you might prepare concentrations of 0.6 mg/ml (target), 0.3 mg/ml and
1.2 mg/ml.

Batch mode experiments can be done routinely with ~10 µl per measurement.
We recommend that you bring enough sample volume for two measurements at each
condition, that way if something happens during a measurement (such as the
beam going down) we can repeat and obtain the desired data.

IEC-SAXS and AF4-MALS-SAXS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Concentrations for IEC-SAXS will depending on the loading volume, but you should
be aiming for a concentration on elution similar to that of a batch mode experiment.
AF4-MALS-SAXS has concentration requirements similar to SEC-SAXS.

IEC-SAXS experiments can have significantly larger loading volumes if desired,
and concentration can be done on the column. The Capto HiRes 5/50 have a maximum
loading capacity of 50 mg. AF4-MALS-SAXS experiments use sample volumes similar
to SEC-SAXS.

In either case, talk to your beamline scientist for more details.


How many samples should I bring?
=================================

When considering how many samples to bring, you need to think both about the
experiment time and the equilibration.

Experiment time
^^^^^^^^^^^^^^^^^^

At BioCAT, users typically use the Superdex 200 Increase 10/300 GL column.
This has a column volume of 24 and a flow rates of ~0.6 ml. That means that
a 1.25 column volume (CV) experiment for SEC-SAXS or SEC-MALS-SAXS takes ~50
minutes. If you know that nothing elutes after 1 CV (including small molecules)
you can further reduce this to ~40 minutes. So you should expect to run ~1-1.5
samples an hour.

With the coflow cell, BioCAT users now have the ability to run samples on the
Cytiva 5/150 columns without radiation damage. These columns provide significantly
less separation, and so should only be used on a system with well resolved
peaks (ideally just one peak, or a peak plus elution at the void volume). However,
if your sample is appropriate, the volume requirements and run times are much
lower. With these columns, typical load volumes are ~50 µL and run times
are ~15 minutes.

Note: If you bring your own column, run times will depend on the flow rate and
volume for that column.

The batch mode autosampler can run a sample every ~3 minutes.

IEC-SAXS experiments can take significantly longer, hours to run a single elution
depending on the gradient, plus needing an equilibration step after each elution
to restore the starting conditions, and so are much lower throughput than
SEC-SAXS.

AF4-MALS-SAXS experiments take roughly the same amount of time as a SEC-SAXS
experiment.

Equilibration
^^^^^^^^^^^^^^

You will have to equilibrate the column at the start of your SEC-SAXS or
SEC-MALS-SAXS experiment, and every time thereafter that you want to change
buffers. We recommend a 2 CV equilibration, which for a Superdex 200 Increase
10/300 GL column will take ~1.5 hours.


What column should I use?
===========================

BioCAT provides a number of columns for users. Typically, users will use one
of these:

*   Superdex 75 Increase, both 10/300 and 5/150 (MW ~3-70 kDa)
*   Superdex 200 Increase, both 10/300 and 5/150 (MW ~10-600 kDa)
*   Superose 6 Increase, both 10/300 and 5/150 (MW ~5-5,000 kDa)

Generally speaking, pick the column with the narrowest MW range that can
accommodate your samples. But remember that the MW range is for globular
proteins, extended proteins run as if they are higher MW! BioCAT recommends
running a test separation in your lab, to ensure you can resolve your species.
The default column at BioCAT for all experiments is the Superdex 200 Increase 10/300.

A full list of columns and the corresponding MW ranges is available for both
`SEC-SAXS and SEC-MALS-SAXS. <{filename}/pages/about_saxs.rst#sec-saxs>`_

We also have standard columns available for IEC-SAXS:

*   Capto HiRes Q 5/50
*   Capto HiRes S 5/50

Users may also provide their own columns if desired. However, due to the dilution
factor, we recommend that you only use analytical grade columns, not the larger
prep columns like the Cytiva HiPrep or HiLoad columns.


How much buffer should I bring?
=================================

.. _saxs_buffer_volume:

The following are intended as guidelines for users when planning their experiments.
However, as most buffers do not contain precious components, we recommend bringing
more buffer than you think you'll need, for example taking the below numbers and adding
50%. You never know when you might want to change buffers and do one more run
with a given sample, and have to equilibrate the column again.

If you have precious components in your buffer, there are ways to reduce
your buffer usage. We have been able to run SEC-SAXS experiments with as
little as ~40 mL of buffer. Please contact a beamline scientist to discuss
these situations.

Given the large volume of buffer required for experiments, many of BioCAT's
users find it convenient to bring 10x concentrated stocks of buffer and then
dilute on-site.

SEC-SAXS and SEC-MALS-SAXS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For SEC-SAXS experiments, you can calculate the amount of buffer you need as:

Buffer volume = 4*(column volume)*(number of samples + 1) + 250 mL

This accounts for both the per-sample use and the equilibration. Please note
that the system cannot use all the buffer in a bottle, as you cannot
risk drawing air into the system. There is also a fixed volume used for pump
washing. This is the 250 mL offset in the above formula.

For example, if you are using the Superdex 200 Increase 10/300 GL column,
it has a column volume of 24 mL. If you're planning to run 5 samples in a particular
buffer you should bring at minimum:

Buffer volume = 4*(24 mL)*(5+1) + 250 mL = 826 mL

As mentioned above, we recommend bringing in excess of this, so for example
bring 1.5*826 mL = ~1.2 L of buffer for 5 SEC-SAXS samples with the recommended
50% excess rule.

For these experiments, you should always bring at least 0.5 L of any buffer you
are using.


Batch Mode
^^^^^^^^^^^

Batch mode experiments require a basic running buffer that is used for
the coflow sheath. This volume should be at least:

Buffer volume = 0.6*(number of samples) + 50 mL

This accounts for both the per-sample use and the equilibration. If you have
a standard buffer we recommend bringing significantly more, just for ease of use,
~200 mL should be more than enough for most experiments.

For buffers with precious or limited components, coflow sheath buffer need not
contain that component. The same is true if you have lots of buffer changes (e.g.
titration of a ligand or salt concentration).

Besides the coflow sheath buffer, you need additional aliquots of a perfectly
matched buffer for each sample. If you do not have precious components in the
buffer and are not doing lots of buffer changes, we recommend having the
coflow sheath buffer be perfectly matched (e.g. via dialysis), as that makes
the measurement simple. Note that in this case you should ship the buffer
stock at 1x (unlike SEC-SAXS experiments where it's okay to ship a concentrated
buffer for dilution on site).

If you will have mis-matched coflow sheath and sample buffers, you should
provide at least:

Buffer volume = 3*(sample volume)

As you typically will bracket the concentration series with buffer measurements.
If you wish to make more buffer measurements, e.g. between each sample, then
you will need more buffer.

IEC-SAXS and AF4-MALS-SAXS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The required buffer volumes for these experiments depend heavily on the methods
used. However, typically these experiments require more buffer than SEC-SAXS
experiments. Please consult your beamline scientist for recommendations.

