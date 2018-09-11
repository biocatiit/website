:title: How to collect SAXS data
:category: users
:slug: how-to-collect-saxs


Protein Preparation Methods
=============================

*   Proteins purified over affinity, heparin, ion exchange, SEC columns etc.

*   Protein purity ensured by a mandatory SEC step at the end of purification and
    subjected to well-known quality control measures (DLS, SDS-PAGE etc).

*   Protein concentration for SAXS "rule of thumb": Concentration (mg/ml) ≥ 100/MW. i.e.
    50 kDa protein, optimal concentration ≥ 100/50=2 mg/ml.

    *   For SEC-SAXS, take dilution ratio (~3X) of SEC columns into consideration.
    *   Typically prepare at least 500 ul of > 5 mg/ml.

*   Post SDS-PAGE gels and chromatograms in your sample data-sheet for sample
    quality check and future reference.


SAXS Collection Method
========================

*   SEC-MALS-SAXS / SEC-SAXS

*   Buffer: 50 mM HEPES or Tris or phosphate buffer, pH ranging from 6-8 (if
    outside this range, consult beamline personnel for potential special
    measures), 150 mM NaCl (typical but up to 1M is permitted, can go higher
    but contrast will be affected), 1-2 % glycerol (higher concentrations can
    be done but column back pressures will increase), up to 5 mM DTT (or 1-2
    mM TCEP)

*   Columns for SEC-MALS-SAXS: Wyatt SEC column for MALS (ask Srinivas if you
    need specific column)

    #.  010S5 100Å (MW range 100-100,000 Da)

    #.  015S5 150Å (MW range 500-150,000 Da)

    #.  030S5 300Å (MW range 5,000-1,250,000 Da)

*   Columns for SEC-SAXS: GE Healthcare SEC columns run at 0.75 ml/min elution rate
    (24 ml - column volume) and discuss with beamline personnel to determine the most
    suitable column for your sample

    #.  Superdex 75 10/300 (MW < 75,000 Da)

    #.  Superdex 200 Increase 10/300 (MW < 400,000 Da)

    #.  Superose 6 10/300 (MW < 5,000,000 Da)

*   Quartz capillary flow-cell is 1.5 mm in diameter with a 10 µm wall

*   0.5-1 s exposure every 2-3 seconds

*   X-ray wavelength is 1.033 Å, 12 keV (this seldom changes)

*   Data recorded on Pilatus3 1M (Dectris) detector at a sample-to-detector
    distance of ~3.5 m. This covers a momentum transfer range of ~ 0.005 Å\ :sup:`-1` <
    q < 0.4 Å\ :sup:`-1` (see \*.dat file for determining this for your specific data)

*   Data usually collected at room temperature (discuss more specific needs
    with beamline personnel).

*   Normalized scattering data to the incident X-ray beam intensity

*   Data are reduced to three column data q, I(q) and σI(q) using
    `BioXTAS RAW <http://bioxtas-raw.readthedocs.io>`_.


Collection Work-flow
=====================

*   Switching buffer/equilibration

    *   SEC-MALS-SAXS setup needs long equilibration (~6 h to overnight), which
        precludes too many buffer exchanges during a single run.

    *   Split buffer in half so both inlet A and B can pump buffer. Be prepared
        for enough buffer and bring them in two bottles in advance. 2L is
        usually sufficient.

    *   Change flow rate by 0.1 ml/min about every minute (after pressure levels
        out) as you stop the flow of one buffer and begin the flow of a new buffer.

    *   Once back up to 0.8-1 ml/min, equilibrate for at least 6 more hours.

    *   If equilibrating overnight, we can equilibrate at a lower speed overnight
        (0.2 ml/min) and ramp up to operational flow-speed 2 hours before the experiment).
        For 6 hr equilibration, ramp up to operational flow speed (0.8-1 ml/min)
        right at the beginning.

    *   Make sure you clean the flow cell for the Optilab - T-rEX in between buffers,
        especially if there's more glycerol etc (anything that could change
        refractive index) - this requires the "purge" button on the LED panel to be switched on.

    *   ALSO: keep glycerol concentrations as low as possible (preferably <5%).

*   Injecting sample and starting HPLC run

    *   Each run will take 18-23 minutes. Have samples ready (concentrate
        or dilute to appropriate concentration and spin down 10-15 minutes) so
        that near the end of one run you can

        #.  Clean the capillary

        #.  Have the auto-sampler inject your sample just as the next run is
            about to start

    *   Each run should be about done after ~15 min (may vary based on sample elution
        profile and flow rate and usually signified by the integrated scattering
        intensity coming back to baseline levels) - stop collecting SAXS data
        then and you will have 5 min to clean the capillary and put the new sample
        in the sample tray

        *   If the integrated scattering intensity fails to come back to the baseline,
            it is important to clean the SAXS cell more thoroughly, which involves
            soaking the capillary for 5-10 min in 2% Hellmanex

        *   If you think you will be running late, time can be extended

        *   To change time, right click in Quat. pump, select Method, change time

    *   Preparing your sample

        *   Samples are injected from vials. 250 - 350 µl will be injected, but
            fill vials to ~50 µl more than the injection volume (900 µl is the upper
            limit).

    *   Washing the system

        *   Wash the capillary

            *   Do not have the HPLC and wash pump connected to the capillary at
                the same time

            *   Connect capillary to Hamilton syringe pump (on desktop) and press wash

            *   When done, capillary can be reconnected to the HPLC

                *   Make sure tube connection is secure and check all unions for leaks before exiting the hutch.


                *   **BE CAREFUL MANOUVERING THE PEEK TUBES CONNECTED TO THE
                    CAPILLARY AS THE CAPILLARY WALLS ARE 10 MICRON QUARTZ AND
                    THEREFORE EXTREMELY FRAGILE.**

    *   Loading your sample

        *   At the beginning of each new sample set, set a program for that sample set

            *   In ASTRA (Wyatt's MALS software):

                *   Create new sequence file, type number of samples and name them

                *   Set the sample property 1) name, 2) choose method (MALS-dRI-SAXS),
                    3) set time (18-23 mins depending on flow rate) for each sample

            *   In Chemstation (Agilent's HPLC software):

                *   Use the sample entry window to select positions in sample tray and name them

                *   Set the method SEC_constflow for each sample

                *   Make sure the sample volume is appropriate and make necessary changes before starting the program.

        *   For each sample, put the vial in the proper position in the tray
            for that sample.

        *   Watch the autosampler pick up the vial, aspirate the sample, and
            replace the vial

        *   Once the vial has been replaced and the robot moves out of the way,
            remove the vial and check that a reasonable amount of sample has been
            aspirated to ensure proper functioning of the autosampler. Begin
            station search (make sure capillary has been cleaned and is hooked
            back up to HPLC)

    *   Data from HPLC runs are saved in pre-determined folder (usually date followed by PI last name).


Computer Workflow: SAXS
=========================

*   On the data collection and analysis computer, in the remote desktop to the
    computer called Rodin, set up the labview program that records the
    intensity of the incident and transmitted x-ray beams. Beamline personnel
    will give you detailed instructions for how to do this before the start
    of the experiment.

*   On the data collection and analysis computer, in medm interface that
    controls the detector, update file name and change the file counter field
    (next file) to 1. Make sure the name you type here matches the one entered
    in the labview program above.

    *   **For the medm interface you have to click in box and leave cursor in box
        while typing. Must press enter before moving mouse. Make sure these
        fields are updated before you proceed with data acquisition!!!**

    *   Once these things are updated, start data collection. This will
        open and close the shutter exposing the sample to x-rays for 0.5 to 1 s
        periods every 2-3 seconds. Do make sure the shutter allowing beam into
        hutch D is open before commencing data acquisition.

