:title: Capabilities for X-ray Fluorescence Microcopy
:category: about
:slug: fluorescence


The BioCAT X-ray microprobe instrument has been developed to the point where
it is now a robust, high performance instrument for micron scale x-ray
fluorescence microscopy (Barrea, et al. 2010). It is available on a
collaborative basis with BioCAT staff (not available through APS General
User Program). The basic beamline and microprobe instrument parameters are
given in Table 1. The heart of the instrument is a Kirkpatrick-Baez mirror
bender system of the University of Chicago design (Eng, et al., 1998) with
two Rh-coated silicon mirrors each 200 mm long.

The shortest focal lengths of the horizontal and vertical KB mirrors are
220 mm and 420 mm respectively, which deliver a minimum beam size of 3
mm (V) x 5 µm (H) FWHM with a flux of 1.3 x 1012 photons/s. The mirrors
can be dynamically bent under remote control via EPICS to focus at longer
distances for different applications such as micro-diffraction or micro-SAXS.
Total delivered flux can be increased ~4-fold by pre-focussing the beam with
the main beamline optics at the expense of minimal focal spot size (Huang
et al., 2010, Table 2). The incoming beam is defined by a set of slits
located immediately upstream of the mirror box while a set of apertures
(50-100-200 microns diameter each) downstream of the mirrors are available
and can be selected to act as a guard aperture. Two ion chambers are located
upstream and downstream of the KB mirror box, used for monitoring the flux
of the incoming and delivered microbeam, respectively. The whole system is
mounted on a remotely controllable table that is located at the end of the
experimental hutch D, 70 m downstream from the undulator source, allowing
for maximum demagnification of the source (the table is proposed to be
upgraded in the upcoming grant cycle).

Three silicon drift detectors (SDD's) are available for fluorescence signal
measurement. The first is a four-element Vortex SDD, with each element
having 50 mm2 active area. The other two are single element SDDs one with
a 10 mm2 and the other with a 80 mm2 active area, both with energy resolution
of 170 eV at the Mn Ka line. The small area detector has a thin Moxtek Ap3.3
polymer window that allows low-energy X-ray photons from light elements to
be measured. The 80 mm2 area detector with a 25 mm-thick Be window is now
used as a backup to the Vortex. The fluorescence signal from the single
element is collected and analyzed by two digital Saturn DXP spectrometers
(XIA) that can handle up to 700,000 counts/s with very good stability,
although showing a large deviation from linearity at these very high count
rates due to a very high detector dead time. The Vortex detector uses the
XIA DXP-XMAP electronics for collection and analysis of fluorescent signals.
These electronics support sophisticated mapping modes, allowing for full
spectrum or multi-SCA acquisition at sub-millisecond dwell times. The DXP-XMAP
system consists of four Digital X-ray Processor (DXP) channels, a Digital
Signal Processor (DSP), a System FPGA, SRAM memory and a PCI interface.
Each of the four DXP channels accepts a preamplified signal input and
produces a 16-bit pipelined output stream of x-ray energies. Each channel
has up to 1,000,000 counts/sec throughput with peaking time range of 0.1
to 100 microseconds. Multi-channel analysis for each channel allows optimal
use of data. Data is collected in HDF5 file format and processed using
custom MatLAB program and program the MAPS (Vogt, 2003).

BioCAT's scanning software allows fast continuous scans to be performed
while acquiring and storing full multichannel analyzer spectra per pixel
on-the-fly with minimal overhead time (<20 ms per pixel). Together, the
high-flux X-ray microbeam and the rapid-scanning capabilities of the BioCAT
beamline allow the collection of XFM measurements from as many as 48 tissue
sections per day.
