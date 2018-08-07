:title: The BioCAT Beamline 18ID
:category: about
:slug: beamline


The BioCAT undulator beamline 18ID at the Advanced Photon Source, although
now over 20 years old, remains a state-of-the-art instrument for biological small
and wide angle fiber diffraction and macromolecular solution scattering
(Fischetti, et al., 2004 J. Synchrotron Rad. (2004). 11, 399-405). It is
capable of delivering well over 10\ :sup:`13` photons/s into focal spots as small
as 30 x 150 µm\ :sup:`2` with the conventional beamline optics. The BioCAT beamline
was designed by Dr. Rosenbaum (Argonne National Laboratory) and shares the
same overall mechanical design of the SBC undulator 19-ID (Rosenbaum et al.
J Synchrotron. 2006 Jan;13(Pt 1):30-45). Undulator "A" provides very intense
monochromatic radiation in the 3.2 - 14 keV range (first harmonic) with low
angular divergence (<8.3 micro-radian vertical and <29.3 micro-radian
horizontal FWHM) with a small source size (typically ~ 680 micrometers
horizontal by ~22 micrometers vertical FWHM, specifications as of fall 2010).
While it is possible to change the beam energy, in practice all experiments are done at 12 keV.
A differential pump separates the vacuum structure from the storage ring
eliminating the need for any windows between the beamline and the storage ring.

.. class:: table-hover

    ===================================================== =============================================================================
    Source                                                APS Undulator A
    Monochromators                                        Si <111> and <400>
    Energy Range (Si <111>)                               3.5-13 keV (fundamental), 10.5-39 keV (third harmonic)
    Energy Resolution (dE/E)                              2 x 10\ :sup:`-4` (Si <111>)
    Minimum Spot Size (µm\ :sup:`2` FWHM)                 < 1500 x 3500 (unfocused), ~30 x 150 (focused at detector 3.5 m from sample)
    Angular Resolution (µrad\ :sup:`2` FWHM)              160 x 190
    ===================================================== =============================================================================

The first optical element is a set of white beam slits located just downstream
of the differential pump that can be used to define the incoming beam size as well
as mitigate heat loading. There are two independent double-crystal monochromator
assemblies. The upstream monochromator #1 has fixed Si(111) crystals to
facilitate energy changes for the microfocus setup while the downstream
monochromator #2 has a sagittal focusing second crystal assemblies that can
provide horizontal focusing of the beam for the main SAXS camera. We have
observed a FWHM of 150 µm in intensity profiles of the sagittally
focused 12.0 keV X-ray beam at the focal point for a 2 meter SAXS camera
(about 64 m from the source) which corresponds to a demagnification ratio
of 4.4:1. The maximum horizontal demagnification ratios are 6.2:1 and 7.3:1
for monochromator #1 and monochromator #2, respectively. (The increased
divergence due to the relatively high demagnification ratios is not generally
a problem for the systems we are studying). The beamline mirror is used for
harmonic rejection and vertical focusing but it easily can be withdrawn from
the beam path when desired.

The current vertical focusing mirror is a dynamically bent flat mirror. Typical
vertical beam profiles when focused for 1.5-3.5 m SAXS camera configurations are
less than 30 µm FWHM. Downstream of the mirror are horizontal and vertical
beam-defining slits for the monochromatic beam. These can be set to pass the
entire beam or define a beam as small as 25 µm x 25 µm. A monochromatic photon
shutter allows the monochromator optics to stay warm while allowing the user
to enter the experimental enclosure.

.. image:: {filename}/images/beamlineoptics.jpg
    :class: img-responsive
    :align: center

The experimental enclosure is 14 m long x 5 m wide x 3.3 m tall. The first
2 m are taken up by the vertical collimation slits and the downstream
support, which incorporates filter/shutter assemblies, and an ion chamber
for the primary beam (I0) monitor. Following the vertical collimation slits
is a beryllium window. All components upstream of this window are under high
vacuum (10\ :sup:`-7` – 10\ :sup:`-8` torr); thereafter, all components are in rough vacuum
(10\ :sup:`-3` – 10\ :sup:`-4` torr). The downstream support moves all these components under
computer control to follow the beam as reflected off of the mirror. Downstream
of this table is 6.4 x 1.5 m vibration-isolation table that is used for most
small-angle diffraction and scattering experiments.

The beamline control software is based on the `Experimental Physics and
Industrial Control System (EPICS) <http://www.aps.anl.gov/epics>`_ which
is a distributed system using VME-based electronics with crate controllers
running the proprietary real-time UNIX-like operating system VxWorks (Wind
River Systems). User interface software communicates with the VME crates
over Ethernet via the EPICS Channel Access (CA) protocol. The hardware is
interfaced by reading and writing the fields in the EPICS databases using
CA calls from a wide variety of programming languages. The beamline Graphical
User Interface (GUI) is implemented using Tcl/Tk and Java menus as well as
using the EPICS graphical control displays (MEDM). These controls are all
portable between different operating systems. The portable beamline control
software package MX (Lavender, 2000) is also supported.

The beamline motors and data acquisition systems are controlled by four VME
crates with Motorola MVME162FX controllers. The beamline motors were chosen
to be DC servos because of their advantages in high torque, speed, and power
consumption over stepper motors. Nine 8-channel Delta Tau PMAC-1 servo motor
controllers control the beamline optics and XY positioning stages. These 15
year-old motor controllers are in the process of being replaced by new Delta
Tau Power PMAC motor controllers. For most of the experimental hutch equipment,
stepper motors are used controlled by five 8-channel Oregon Microsystems OMS-58
stepper motor controllers.

For time resolved data acquisition there is a Struck 3820 multichannel
histogramming scaler with 32 inputs. For conventional scans there is also a
Joerger VCS16 scaler with 16 inputs and a voltage to frequency converter
(Hytec VFC 2504, Hytec Electronics Ltd). External equipment (area detectors,
shutters) can be interfaced to the control system using a digital I/O board
(Acromag-9440) with 16 input and 16 output channels. To implement PID feedback
control loops there is also an Acromag IP330 ADC with 16 inputs Systran DAC
with 8 outputs. There are 8 current amplifiers (Keithley, model 42) which
are interfaced through the RS232 ports on the beamline workstations. We have
designed simulated EPICS servers for these devices so that they can be accessed
from other computers in exactly the same way as the VME modules.

Two XIA model PF2S2 filter assemblies contain a series of aluminum filters
that allow at least 3 decades of beam attenuation (at 12 keV) as well as
two pneumatically activated shutters. By using these in series, exposure
times of less than 500 ms can be achieved. We have recently implemented a
shutter capable of <500 µs minimum exposure time consisting of
two electrically-activated, inclined blade-type shutters in series (Model
LS500, NM laser products Inc) with ca. 1 ms latency.
