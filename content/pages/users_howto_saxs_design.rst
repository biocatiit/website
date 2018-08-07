:title: How to design an equilibrium SAXS experiment
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

There are three equilibrium data acquisition strategies available at BioCAT:
`SEC-SAXS <{filename}/pages/about_saxs.rst#sec-saxs>`_,
`SEC-MALS-SAXS <{filename}/pages/about_saxs.rst#sec-mals-saxs>`_, and
`batch mode SAXS <{filename}/pages/about_saxs.rst#batch-saxs>`_.

Below we give some general guidelines for designing your SAXS experiment. If you
have questions, or are a new user, please `contact a beamline scientist <{filename}/pages/contact.rst>`_.

What technique should I use?
=============================

BioCAT strongly encourages all users to use either SEC-SAXS or SEC-MALS-SAXS.
There are some rare cases where sample concentration and volume are inadequate
for SEC-SAXS, in which case you will use batch mode.

SEC-MALS-SAXS allows highly accurate quantification of molecular weight,
making it generally superior to SEC-SAXS. However, the equilibration times
for the SEC-MALS system are quite long (at least 6 hours), which limits the
number of buffer changes. Additionally, the SEC-MALS columns have a limited
pH range (3-8). Finally, because of the sensitivity of the system,
the requirements on the sample quality are much higher than for SEC-SAXS.

SEC-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Your system has a single well defined peak or several well resolved peaks
    (not including large aggregates that show up in the void)
*   You will need to make several buffer changes during your experiment
*   You need to use a wide range of pH in your buffers (3-12)

SEC-MALS-SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have a complicated elution with several overlapping or poorly resolved
    peaks
*   You need at most one buffer change
*   You can use a narrower range of pH in your buffer (3-8)

Batch mode SAXS is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You can't meet the concentration and volume requirements for SEC-SAXS
    (see below)


What sample concentration and volume do I need?
================================================

Concentration
^^^^^^^^^^^^^^

As a rule of thumb, you will get good SAXS data if your protein concentration
in mg/ml in the SAXS cell is ~60/MW in kDa. For example, for a 20 kDa protein
you would want a concentration of ~60/20 = 3 mg/ml whereas for a 150 kDa
protein you would want a concentration of ~60/150 = 0.4 mg/ml. RNA and DNA
samples scatter ~2.5 times more strongly than protein, so you can use a
concentration of ~24/MW.

The above rule of thumb applies to the concentration in the SAXS cell. In
the SEC-SAXS and SEC-MALS-SAXS experiments the sample is diluted by the column,
and may elute in several peaks. This should be accounted for. We recommend
adding a column dilution factor of ~4x for your SEC-SAXS sample preps. This
would give ~240/MW as the target concentration. If a significant amount of your
sample elutes in other peaks, further increase your concentration to compensate.

Note: In SEC-SAXS, if your sample has concentration dependent aggregation
that prevents you from achieving the high concentrations needed, you may be
able to compensate by increasing your load volume.

Volume
^^^^^^^

Typical SEC-SAXS and SEC-MALS-SAXS injection volumes are ~250-350 µl.

Batch mode experiments can be done routinely with 100 µl per measurement. Note
that typical batch mode experiments require measuring several concentrations, and
so can actually end up requiring more volume than a SEC-SAXS experiment.


How many samples should I bring?
=================================

When considering how many samples to bring, you need to think both about the
experiment time and the equilibration.

Experiment time
^^^^^^^^^^^^^^^^^^

At BioCAT, users typically use the GE Superdex 200 Increase 10/300 GL column
\(SEC-SAXS) or the Wyatt WTC-030S5 (SEC-MALS-SAXS). These have column volumes
of 24 and 18 ml respectively. Flow rates are ~0.9 ml and 1.0 ml respectively.
That means that a 1.5 column volume (CV) experiment for SEC-SAXS takes ~40 minutes,
and a 1.5 CV experiment for SEC-MALS-SAXS takes ~27 minutes. If you know that
nothing elutes after 1 CV (including small molecules) you can further reduce
this to ~27 and 18 minutes respectively. So you should expect to run ~1.5-3 samples an
hour, depending on the technique.

Note: If you bring your own column, run times will depend on the flow rate and
volume for that column.

Batch mode samples are much faster, typically only 3-30 s of exposure. Throughput
is limited by sample loading and cell cleaning. Realistically, expect to do a sample
every 3-5 minutes.

Equilibration
^^^^^^^^^^^^^^

You will have to equilibrate the column at the start of your SEC-SAXS or
SEC-MALS-SAXS experiment, and every time thereafter that you want to change
buffers. For SEC-SAXS, we recommend a 2 CV equilibration, which for a
GE Superdex 200 Increase 10/300 GL column will take ~1 h. For SEC-MALS-SAXS,
equilibration requires at least 6 hours, and is ideally done overnight.


What column should I use?
===========================

A list of columns and the corresponding MW sizes is available for both
`SEC-SAXS <{filename}/pages/about_saxs.rst#sec-saxs>`_ and
`SEC-MALS-SAXS <{filename}/pages/about_saxs.rst#sec-mals-saxs>`_.
Generally speaking, pick the column with the narrowest MW range that can
accommodate your samples. But remember that the MW range is for globular
proteins, extended proteins run as if they are higher MW! BioCAT recommends
running a test separation in your lab, to ensure you can resolve your species.

