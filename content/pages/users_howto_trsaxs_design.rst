How to design a time-resolved SAXS experiment
###############################################################################

:category: users
:slug: how-to-prepare-trsaxs


SAXS has emerged as a standard biophysical tool deployed routinely for
characterizing macromolecules of biomedical interest. The relative logistical
simplicity embodied in a technique that provides easy access to the size and
low-resolution shape of macromolecules makes it an essential part of the
biophysicists' tool kit. BioCAT has a world-leading time-resolved SAXS
(TR-SAXS) program that allows users to initiate a reaction through mixing
and then measure the changes in the sample as soon as ~45 µs after mixing.

BioCAT provides three different time resolved instruments, which have different
accessible time ranges and sample and buffer requirements. These are:

*   `Chaotic flow mixing, ~45 µs to 60 ms time range <{filename}/pages/about_saxs.rst#cf-tr-saxs>`_
*   `Laminar flow mixing, ~5 ms to 1.5 s time range <{filename}/pages/about_saxs.rst#cf-tr-saxs>`_
*   `Stopped flow mixing, >~1 ms time range  <{filename}/pages/about_saxs.rst#sf-tr-saxs>`_

Note that longer time points can also easily be accessed via on-plate mixing
capabilities of the equilibrium batch mode setup, so talk to a beamline
scientist about that possibility if interested.

More details about the specifics of BioCAT's experimental setup can be `found
elsewhere on our website. <{filename}/pages/about_saxs.rst#tr-saxs>`_

.. contents:: Topics:


What technique should I use?
=============================

BioCAT strongly encourages users to use either of our continuous flow mixers,
the chaotic flow or laminar flow mixing approaches. These will provide the best
quality data for your experiments. However, some experiments, particularly if
you have a highly viscous buffer or need an extended time range, may be more
appropriate for the stopped flow instrument.

Note that both the chaotic flow and laminar flow mixers can be used as part
of the same beamtime, and the measured time points can be merged between the
two mixers to provide information spanning almost five orders of magnitude in
time, from  ~45 µs to 1.5 s.

Stopped flow experiments are generally not recommended as they are highly
sample and time intensive and are prone to radiation damage.


Chaotic flow mixing is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You need ultra-fast time points (<1 ms)
*   You can provide plenty of sample and buffer

Laminar flow mixing is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have minimal sample available
*   You want to measure slower time points (>1 ms) or aren't sure what the
    time range of interest is

Stopped flow is the right choice if . . .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   You have a very viscous buffer that isn't compatible with the continuous
    flow mixers
*   You need time points longer than 1.5 s


What sample concentration and volume do I need?
================================================

Chaotic flow mixing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For chaotic flow experiments, we typically recommend a final concentration
in mg/ml after dilution that is:

*   ~60/(MW in kDa) for protein
*   ~24/(MW in kDa) for nucleic acids (due to the higher contrast)

Note that in chaotic mixing experiments the sample undergoes typically
between 4-10x dilution.

For example, to measure a 100 kDa protein we would recommend a concentration
after dilution of 0.6 mg/ml. For example, to measure a 100 kDa protein we would
recommend a concentration after dilution of 0.6 mg/ml. At a typical dilution
factor of 5x, this would be a starting concentration of 3.0 mg/ml.
Whereas for a 100 kDa nucleic acid, we would recommend a diluted
concentration of 0.24 mg/ml, and so a starting concentration (for 5x dilution)
of 1.2 mg/ml.

With this mixer we typically measure the time series using a 1 mL injection,
and make 3 repeated measurements to improve signal to noise, for a total
loaded volume of 3 mL.

Note that with these concentrations and volumes, a chaotic flow experiment with
a 100 kDa protein would take less than 10 mg for the entire time series

Laminar flow mixing
^^^^^^^^^^^^^^^^^^^^^^^^

For laminar flow experiments, we typically recommend a concentration in mg/ml of:

*   ~120/(MW in kDa) for proteins
*   ~48/(MW in kDa) for nucleic acids (due to the higher contrast)

For example, a 100 kDa protein would be injected at a concentration
of ~1.2 mg/ml and a 100 kDa RNA would be injected at a concentration
of ~0.48 mg/ml.

With this mixer, we typically measure the time series using a 100 µL injection,
and make 3 repeated measurements to improve signal to noise, for a total loaded
volume of 300 µL.

Note that these recommended concentrations are 2x lower and the loading volume
is equivalent to what we recommend for SEC-SAXS experiments, so a lamianr flow
time series can be measured with less material than a single SEC-SAXS injection.
For many proteins and nucleic acids these experiments require significantly
less than 1 mg of material, making them feasible for essentially every
system that can be measured by equilibrium SAXS.

How many samples should I bring?
=================================

Below we give recommendations for how many samples to bring in your beamtime.
However, time-resolved SAXS experiments are often more exploratory than
equilibrium measurements, as the exact time range over which the behavior occurs
may not be known, and so often more time is spent analyzing and iterating
on conditions and measured time ranges than is spent measuring data.

Chaotic flow mixing
^^^^^^^^^^^^^^^^^^^^^

A typical chaotic flow experiment will run for ~10 minutes in order to
collect pre and post buffer measurements as well as the sample measurement.
It takes ~5 minutes to load a sample and start data collection. A final time
series usually consists three repeated measurements of the same sample,
so you can plan on measuring roughly one time series per hour.

If you need to change buffers between that takes roughly 30 minutes.

Laminar flow mixing
^^^^^^^^^^^^^^^^^^^^^^

A typical laminar flow experiment will run for ~30 minutes in order to collect
pre and post buffer measurements as well as the sample measurement. It
takes ~5 minutes to load a sample and start data collection. A final time
series usually consists three repeated measurements of the same sample,
so you can plan on measuring roughly one time series per two hour.

If you need to change buffers between that takes roughly 60 minutes.


What buffers should I use?
=================================

Sample and buffer preparation is done in the standard way for SAXS experiments.
Because there is no in-line purification (such as for SEC-SAXS), the samples
must be of sufficient monodispersity and homogeneity that you could make batch
mode SAXS measurements with them.

Note that we have two distinct buffers for mixing experiments. The first is the
"sample buffer", which is the initial state the sample is in. The second is the
"mixing buffer", which is the buffer that will be mixed into the sample buffer
to create the final buffer. The excess sample buffer is used to inject the sample
and to make the necessary buffer measurements for the experiment, so it must
be perfectly matched to the actual buffer the sample is in (e.g. by dialysis).

For these experiments we recommend including a radical scavenger to protect
against radiation damage. Typically we recommend 1-2% glycerol, but in
some cases reductant (e.g. DTT or EDTA) or other radioprotectants may be used.


Chaotic flow mixing
^^^^^^^^^^^^^^^^^^^^^^

Buffers should be prepared taking into account final dilution ratios of the mixing.
The chaotic flow mixer is usually run at sample high dilution, typically between 4-10x.
For example, at the 5x dilution, any components in the sample buffer that are
not in the mixing buffer will be diluted 5x, and any components in the mixing
buffer that are not in the sample buffer will be diluted by 4/5th.

You can use the following formula (where IC standards for initial concentration,
DR for dilution ratio, SB sample buffer, and MB mixing buffer) to calculate any
parameter if you fix the others. For example, you could calculate the mixing
buffer concentration given a target final value, initial value, and dilution ratio:

*   Final concentration = (1 - 1/(DR))*(IC in MB) + (1/DR)*(IC in SB)

Note that if you have zero of the component in either buffer this formula
simplifies.

Suppose you want to do a salt dilution experiment, where the sample goes from
high to low salt. If you know the sample needs to start in 1 M start for the
initial state of interest and you want a mixed state with 150 mM salt, you
would then pick a dilution ratio of 1000 mM/150 mM = 6.67, using a zero salt
mixing buffer. On the other hand, if you wanted a final state of  150 mM salt
but didn't care what the  starting concentration was as long as it was above
500 mM, you could stick with the standard dilution ratio of 5x and use a
starting concentration of (150 mM)*5 = 750 mM, again with a zero salt
mixing buffer.

Equivalently, a salt jump experiment mixing from a zero salt sample buffer into
a high salt mixing buffer is easy to calculate. If you want a final
salt condition of 500 mM, and you are using a dilution ratio of 5x, the necessary
starting concentration of the mixing buffer is (500 mM)/(1-1/5)) = 625 mM.

For the more complicated case, consider a salt jump experiment where you start
with low but non-zero salt and do a 5x dilution into a high salt buffer. If you
start with the sample in a 50 mM salt in the sample buffer, and you wanted to
end with 500 mM salt, you would need to have a mixing buffer with a salt
concentration of:

*   (Final concentration - (IC in SB)/DR)/(DR-1/DR) = (IC in MB)
*   (500 mM - (50 mM)/5)/(4/5) = 612.5 mM

Note that any component can be changed via mixing, salt is just a sample example.
If you are changing pH, note that the above formulas will not apply.

Components for which you do not want to change the concentration should be
at the same concentration in both sample and mixing buffers.


Laminar flow mixing
^^^^^^^^^^^^^^^^^^^^^

In the laminar flow mixer the dilution is fixed by the ratios of the flow rate of
the sample buffer and mixing buffer. Components in the sample buffer will
get diluted to 8.7% (11.5x) of their initial value and components in the mixing buffer
will get diluted to 91.3% (1.1x) of their initial value. You can calculate the
final mixed concentration as (where IC is initial concentration, SB is sample
buffer and MB is mixing buffer)

* Final concentration = 0.087*(IC in SB) + 0.913*(IC in MB)

Consider the example of mixing from high salt in the sample buffer to
low salt in the final buffer. If the salt in the mixing buffer is zero,
then the final concentration = 0.087*(initial concentration in sample buffer).
So if you want a final concentration of 150 mM, you'd need an initial concentration
of (150 mM)/0.087 = 1.724 M. Alternatively, if you wanted to start with a 500 mM
solution, you would achieve a final concentration of (500 mM)*0.087 = 43.5 mM.

Equivalently, consider a salt jump experiment mixing from a zero salt sample buffer
to a high salt final buffer. If you want a final salt concentration of 500 mM,
you would use a mixing buffer with (500 mM)/0.913 = 548 mM salt.

For a more complicated sample, consider a case where you want to start with
50 mM salt in the sample buffer and end with 500 mM salt final buffer. The necessary
mixing buffer salt concentration would be:

*   (Final concentration - (0.087*(IC in SB)))/0.913 = IC in MB
*   (500 mM - (0.087*(50 mM)))/0.913 = 543 mM

Note that any component can be changed via mixing, salt is just a sample example.
If you are changing pH, note that the above formulas will not apply.

Components for which you do not want to change the concentration should be
at the same concentration in both sample and mixing buffers.


How much buffer should I bring?
=================================

The following are intended as guidelines for users when planning their experiments.
However, as most buffers do not contain precious components, we recommend bringing
more buffer than you think you'll need, for example taking the below numbers and adding
50%. You never know when you might want to do a couple more measurements with
a given sample.

Given the large volume of buffer required for experiments, many of BioCAT's
users find it convenient to bring 10x concentrated stocks of buffer and then
dilute on-site. This can only be done for the buffer the sample is mixing into,
the sample running buffer must be perfectly matched to the buffer the sample
is in, such as with dialysis.

Chaotic flow mixing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chaotic flow experiments involve dilution of the sample into the mixing buffer.
Dilution factors can be whatever the user desires, but typically are between
~4-10x, and 5x is considered standard. Flow rates can also be varied to adjust
the time range measured and are typically between 4.5-8 mL/min, with 6 mL/min being
standard.

You can calculate the necessary buffer as:

*   Sample buffer = (10 min)*(flow rate)*(number of measurements+1)*(1/(dilution ratio)) + 50 mL
*   Mixing buffer = (10 min)*(flow rate)*(number of measurements+1)*(1 - 1/(dilution ratio)) + 50 mL

So, for example, for the standard flow rate of 6 mL/min and the standard dilution
factor of 5x, to measure a time series consisting of 3 repeated measurements on
the same sample, you would prepare:

*   Sample buffer = (10 min)*(6 mL/min)*(4)*(1/5) + 50 mL = 98 mL
*   Mixing buffer = (10 min)*(6 mL/min)*(4)*(4/5) + 50 mL = 242 mL

Talk to your beamline scientist for recommendations on flow rate and dilution
factor.

Laminar flow mixing
^^^^^^^^^^^^^^^^^^^^^^^

Laminar flow experiments are typically run at fixed ratios between the mixing buffer
and sample buffer and at standard flow rates. You can calculate the necessary buffer as:

*   Sample buffer = (0.4 mL)*(number of measurements) + 10 mL
*   Mixing buffer = (4.1 mL)*(number of measurements) + 20 mL

So, for example, to measure a time series consisting of 3 repeated measurements on
the same sample, you would prepare:

*   Sample buffer = (0.4 mL)*3 + 10 mL = 11.2 mL
*   Mixing buffer = (4.1 mL)*3 + 20 mL = 32.3 mL


