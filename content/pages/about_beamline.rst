:title: The BioCAT Beamline 18ID
:category: about
:slug: beamline


The BioCAT undulator beamline 18ID at the Advanced Photon Source, although
now 15 years old, remains a state-of-the-art instrument for biological small
and wide angle fiber diffraction and macromolecular solution scattering
(Fischetti, et al., 2004 J. Synchrotron Rad. (2004). 11, 399-405). It is
capable of delivering well over 1013 photons/s into focal spots as small
as 60 x 150 µm2 with the conventional beamline optics. The BioCAT beamline
was designed by Dr. Rosenbaum (Argonne National Laboratory) and shares the
same overall mechanical design of the SBC undulator 19-ID (Rosenbaum et al.
J Synchrotron. 2006 Jan;13(Pt 1):30-45). Undulator "A" provides very intense
monochromatic radiation in the 3.2 - 14 keV range (first harmonic) with low
angular divergence (<8.3 micro-radian vertical and <29.3 micro-radian
horizontal FWHM) with a small source size (typically ~ 680 micrometers
horizontal by ~22 micrometers vertical FWHM, specifications as of fall 2010).
A differential pump separates the vacuum structure from the storage ring
eliminating the need for any windows between the and the storage ring.

.. class:: table-hover

    ===================================================== =====================================================================
    Source                                                APS Undulator A
    Monochromators                                        Si <111> and <400>
    Energy Range (Si <111>)                               3.5-13 keV (fundamental), 10.5-39 keV (third harmonic)
    Energy Resolution (dE/E)                              2 x 10\ :sup:`-4`\  (Si <111>)
    Minimum Spot Size (um\ :sup:`2`\  FWHM)               < 1500 x 3500 (unfocused), < 60 x 160 (at detector 3.5 m from sample)
    Angular Resolution (urad\ :sup:`2`\  FWHM)            160 x 190
    ===================================================== =====================================================================

The first optical element is a moveable fixed mask with an aperture of 4.2 mm
x 2.1 mm just upstream of two independent double-crystal monochromator
assemblies. The upstream monochromator #1 has fixed Si(111) crystals to
facilitate energy changes for the microfocus setup while he downstream
monochromator #2 has a sagittal focusing second crystal assemblies that can
provide horizontal focusing of the beam for the main SAXS camera. We have
observed a FWHM of 150 &micor;m in intensity profiles of the sagittally
focused 12.0 KeV X-ray beam at the focal point for a 2 meter SAXS camera
(about 64 m from the source) which corresponds to a demagnification ratio
of 4.4:1. The maximum horizontal demagnification ratios are 6.2:1 and 7.3:1
for monochromator #1 and monochromator #2, respectively. (The increased
divergence due to the relatively high demagnification ratios is not generally
a problem for the systems we are studying). The beamline mirror is used for
harmonic rejection and vertical focusing but it easily can be withdrawn from
the beam path when desired.

The current vertical focusing mirror is an adaptive, so-called bi-morph
design from SESO. Typical vertical beam profiles when focused for 1.5-3.5
m SAXS camera configurations are about 65 µm FWHM. Downstream of the mirror
are horizontal and vertical beam-defining slits for the monochromatic beam.
These can be set to pass the entire beam or define a beam as small as 25 µm
x 25 µm. A monochromatic photon shutter allows the monochromator optics to
stay warm while allowing the user to enter the experimental enclosure.

.. image:: {filename}/images/beamlineoptics.jpg
    :class: img-responsive
    :align: center

The experimental enclosure is 14m long x 5m wide x 3.3m tall. The first
2 m are taken up by the vertical collimation slits and the downstream
support, which incorporates filter/shutter assemblies, and an ion chamber
for the primary beam (I0) monitor. Following the vertical collimation slits
is a beryllium window. All components upstream of this window are under high
vacuum (10-7 – 10-8 torr); thereafter, all components are in rough vacuum
(10-3 – 10-4torr). The downstream support moves all these components under
computer control to follow the beam as reflected off of the mirror. Downstream
of this table is 6.4 x 1.5 m vibration-isolation table that is used for most
small-angle diffraction and scattering experiments.

The beamline control software is based on the Experimental Physics and
Industrial Control System (EPICS) [http://www.aps.anl.gov/epics] which
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
Tau Power PMAC motor controllers). For most of the experimental hutch equipment,
stepper motors are used controlled by five 8-channel Oregon Microsystems OMS-58
stepper motor controllers.

For time resolved data acquisition there is a Struck 7201 multichannel scaler
with 32 inputs and 4K memory arrays per each input. For conventional scans there
is also a Joerger VCS16 scaler with 16 inputs and a voltage to frequency converter
(Hytec VFC 2504, Hytec Electronics Ltd). External equipment (CCD detectors,
shutters) can be interfaced to the control sytem using a digital I/O board
(Acromag-9440) with 16 input and 16 output channels. To implement PID feedback
control loops there is also an Acromag IP330 ADC with 16 inputs Systran DAC
with 8 outputs. There are 8 current amplifiers (Keithley, model 42) which
are interfaced through the RS232 ports on the beamline workstations. We have
designed simulated EPICS servers for these devices so that they can be accessed
from other computers in exactly the same way as the VME modules. CAMAC modules
can also be accommodated via Kinetic Systems KS-2917 VME to CAMAC interface
board and a Kinetic Systems CAMAC crate and model 3922 controller interfaced
with EPICS.

To take full advantage of the high x-ray flux at the Advanced Photon Source
and to reduce radiation damage to labile biological samples, considerable
effort has been devoted to implementing fast on-the-fly scans and thus
reducing the exposure times and, consequently, dose delivered to the sample.
This was a challenging task since the distributed control system imposes
network latencies on the communication between different VME crates and
the control workstations. Currently two types of scans have been implemented
– a "generic" fast scan and an "energy" fast scan. With the generic scan we
can scan any servo or stepper motor at the beamline while recording the output
into any of 16 inputs of the Joerger scaler. The scan may use one of three
different algorithms but all of them have the same lower limit to the time
resolution of ~150 ms/point imposed by the network latencies. As a result,
the typical generic scan time is ~15-60 seconds.

These scanning protocols have been very useful in beamline diagnosis and
alignment and have found use in various experimental protocols. The fast
energy scan, as implemented for both the beamline monochromators is simplified
by the fact that the synchronization of three different motions in the double
crystal monochromator is handled by the PMAC controllers (which were designed
for simultaneous multi-axis motions), so that the scan software program
need only deal with one combined pseudo-motor called "energy." This scan
makes use of the 32 memory arrays in the Struck scaler, which simultaneously
records the monochromator encoder outputs and the x-ray intensities. The
minimum time per point for this scan is ~1 ms and the total scan time is
typically 1-10 s. We have also incorporated synchronous motion of
monochromator and the beamline undulator into the energy scans so that the
energy of the two devices can be changed simultaneously. Finally, all the
energy and generic scans provide for two or three dimensional scans with
step-wise motion of the second and the third motors respectively retaining
continuous scanning in the first dimension.

Two XIA model PF2S2 filter assemblies contain a series of aluminum filters
that allow at least 3 decades of beam attenuation (at 12 kev) as well as
two pneumatically activated shutters. By using these in series, exposure
times of less than 500 ms can be achieved. We have recently implemented a
shutter capable of <500 micro-second minimum exposure time consisting of
two electrically-activated, inclined blade-type shutters in series (Model
LS500, NM laser products Inc) with ca. 1ms latency. A Kinetic Systems model
3655-LIA timing-pulse generator is used to control these fast shutter systems.
Accurate exposure times are user-selectable via a simple GUI interface.
