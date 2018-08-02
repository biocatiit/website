:title: How to design a fiber-diffraction experiment
:category: users
:slug: how-to-design-fiber-exp

You need to know the first order resolution needed and the highest resolution
needed in order to have interpretable data for your system. Then the task is to
select a camera length and a size that allows both of these to be achieved. To
make this simple, please use our X-Ray Tools Q Calculator.

Enter the X-ray energy in KeV (all experiments are usually done at 12 keV) and a
trial camera length in mm. Knowing the dimensions of the backstop and the detector
active area, one can find the optimal camera length for your application by adjusting
it in the application by trial and error.

The following area detectors are available at the beamline:

*   The Pilatus3 X 1M detector has 981 x 1043 172 µm pixels (168.7 x 179.4
    mm\ :sup:`2` active area) and can be read out at 500 fps.
*   The Pilatus 100K detector has 497 x 195 172 µm pixels (83.8 x 33.5 mm\ :sup:`2`
    active area) and can be read out at 200 fps
*   The MAR165 CCD detector has a circular active area 165 mm in diameter with
    pixels just under 80 µm square (2x2 binned). It can also be used unbinned
    for 4k x 4k 40 µm pixels.
*   There are two Merlin pixel array detectors.The first one has 256 x 1024 55
    µm pixels for an active area of 14 x 56 mm\ :sup:`2` and the second one is 512 x
    512 55 µm pixels for an active area 28.2 x 28.2 mm\ :sup:`2`. Both detectors,
    based on the Medipix3 chip are direct detecting photon counting detectors
    capable of running continuously at 200 HZ or for ~ 1 s burst at 1000 Hz.
    Their very small packaging allows them to be used in combination with other
    detectors to provide high resolution in selected parts of a pattern.
*   The EIGER X 500K pixel array detector. This photon counting, direct detection
    detector has  1030 x 514 75 µm pixels (active area 77.2 x 38.6 mm\ :sup:`2`) and
    can run continuously at 3 kHz. *This detector should be available by early 2019.*

For small angle fiber diffraction experiments, the available range of camera
lengths go from approximately 1 to 9 m with 2-3 m being the most commonly used
length. The minimum beamstop size that is practical to use with the standard
small-angle camera is 4 mm. We are capable of accommodating a very wide variety of
sample chambers, laser setups, etc.

Please contact `Weikang Ma <{filename}/pages/contact.rst>`_ to discuss your
needs for fiber and muscle diffraction experiments.

A short introduction to the basis of the equatorial
X-ray diffraction pattern from muscle can be found here:
`Equatorial Diffraction Intro <https://musclex.readthedocs.io/en/latest/AppSuite/Equator/The-Equatorial-Diffraction-Pattern-from-Striated-Muscle.html>`_.

BioCAT Microdiffraction capabilities are described in Barrea, et al.
`X-ray micro-diffraction studies on biological samples at the BioCAT Beamline
18-ID at the Advanced Photon Source <https://www.ncbi.nlm.nih.gov/pubmed/25178013>`_.
J. Synchrotron Radiat. 2014 Sept;21:1200-5. doi: 10.1107/S1600577514012259.

