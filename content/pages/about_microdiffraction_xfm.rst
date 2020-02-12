:title: Microbeam Imaging
:category: about
:slug: about-microbeam-imaging

.. page-header::

    .. alert::
        :type: info

        Please note that at this time microbeam imaging is not available
        through the  GU system and is only available to collaborators.


.. image:: {static}/images/microdiffraction.jpg
    :class: img-responsive
    :align: center

.. lead::
    When excited by High-energy X-rays, metals will fluoresce. The spectrum of X-rays
    emitted from the metal depends on both the metal and its environment. By illuminating
    a sample with tightly-focused X-rays, we can determine the content and distribution
    of the metals present in the sample. By doing this in combination with Small- and
    Wide-angle Diffraction, it is possible to correlate metal distribution with the
    distribution of ordered regions in the sample. This technique is used to help us
    understand how the distribution of metals (such as iron and zinc) in tissues
    affects such things as neurological diseases, normal human development, heart
    disease, and cancer.


The BioCAT micro-Diffraction and X-ray Florescent Microscopy(XFM)
instruments are designed  for X-ray elemental mapping and micro-X-ray Diffraction
studies of biological samples. The microbeams are produced by one of two
Compound Refractive Lenses (CRL's). The first of these has a focal length of
1.8 m and a spot size at the focus of 23 x 4 µm\ :sup:`2` with a flux of
~2 x 10\ :sup:`12` photons/s. The second CRL has a focal length of 50 cm with a
focal spot of ~ 1 x 5 µm\ :sup:`2` containing ~2 x 10\ :sup:`11` photons/s. When
configured as a micro-diffraction instrument, the useful d-space range  is
1/200 - 1/3.4 Å\ :sup:`-1` at 12 keV and 1/900-1/20 Å\ :sup:`-1` at 8 keV with
the modified Mar 165 detector with 40 mm pixels (60 mm psf function for phosphor)
for very high-resolution data when the microbeam is focused at the detector.

X-ray fluorescence experiments are done with  a four-element Vortex silicon drift
detector (SDD), with each element having 50 mm\ :sup:`2` active area. The Vortex detector uses the
XIA DXP-XMAP electronics for collection and analysis of fluorescent signals.
These electronics support sophisticated mapping modes, allowing for full
spectrum or multi-SCA acquisition at sub-millisecond dwell times. The DXP-XMAP
system consists of four Digital X-ray Processor (DXP) channels, a Digital
Signal Processor (DSP), a System FPGA, SRAM memory and a PCI interface.
Each of the four DXP channels accepts a pre-amplified signal input and
produces a 16-bit pipelined output stream of x-ray energies. Each channel
has up to 1,000,000 counts/sec throughput with peaking time range of 0.1
to 100 µs. Multi-channel analysis for each channel allows optimal
use of data. Data is collected in HDF5 file format and processed using
custom MatLAB program and program the MAPS (Vogt, 2003).

Areas of interest up to a few mm\ :sup:`2` in tissue sections can be scanned to
determine metal distributions with 1-5 µm resolution in XFM configuration.
Several metals (10 or more) can be probed simultaneously with a minimum of
sample preparation. Low-resolution maps may be performed initially over
larger areas to determine smaller areas of interest that will subsequently
be scanned at higher resolutions. This approach maximizes the efficiency
of the microprobe, spending beam time selectively where it is most needed.
BioCAT's scanning software allows fast continuous scans to be performed
while acquiring and storing full multichannel analyzer spectra per pixel
on-the-fly with minimal overhead time (<20 ms per pixel).

Samples may be freeze- or air-dried and our Linkam cryostage can maintain
frozen hydrated samples at liquid nitrogen temperatures. The Linkham stage
can be useful for XFM but is less useful for microdiffraction


*   Useful References

    X-ray Fluorescence Microscopy

    *   R.A. Barrea, D. Gore, N. Kujala, C. Karanfil, S. Kozyrenko, R.
        Heurich, M. Vukonich, R. Huang, T. Paunesku, G. Woloschak, T.C.
        Irving, "Fast-scanning high-flux microprobe for biological X-ray
        fluorescence microscopy and microXAS," J. Synchrotron Rad. 17 (4),
        522-529 (2010). DOI: 10.1107/S0909049510016869
    *   Andreana C. Leskovjan, Ariane Kretlow, Antonio Lanzirotti, Raul
        Barrea, Stefan Vogt, Lisa M. Miller, "Increased brain iron coincides
        with early plaque formation in a mouse model of Alzheimer's disease,"
        Neuroimage 55 (1), 32-38 (2011). DOI: 10.1016/j.neuroimage.2010.11.073
    *   Gregory Robison, Taisiya Zakharova, Sherleen Fu, Wendy Jiang, Rachael
        Fulper, Raul Barrea, Matthew A. Marcus, Wei Zheng, Yulia Pushkar, "X-Ray
        Fluorescence Imaging: A New Tool for Studying Manganese Neurotoxicity,"
        PLoS One 7 (11), e48899-1-e48899-12 (2012). DOI: 10.1371/journal.pone.0048899

    Microdiffraction

    *   Yoshiharu Nishiyama, Masahisa Wada, B. Leif Hanson, Paul Langan,
        "Time-resolved X-ray diffraction microprobe studies of the conversion
        of cellulose I to ethylenediamine-cellulose I," Cellulose 17 (4),
        735-745 (2010). DOI: 10.1007/s10570-010-9415-9
    *   Eric C. Landahl, Olga Antipova, Angela Bongaarts, Raul Barrea, Robert
        Berry, Lester I. Binder, Thomas Irving, Joseph Orgel, Laurel Vana,
        Sarah E. Rice, "X-ray diffraction from intact tau aggregates in human
        brain tissue," Nucl. Instrum. Methods A 649 (1), 184-187 (2011).
        DOI: 10.1016/j.nima.2011.01.059
    *   R.A. Barrea, O. Antipova, D. Gore, R. Heurich, M. Vukonich, N.G.
        Kujala, T.C. Irving, J.P.R.O. Orgel, "X-ray micro-diffraction studies
        on biological samples at the BioCAT Beamline 18-ID at the Advanced
        Photon Source," J. Synchrotron Rad. 21 (5), 1200-1205 (2014).
        DOI: 10.1107/S1600577514012259
