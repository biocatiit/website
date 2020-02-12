How to analyze SAXS data
###############################################################################

:category: users
:slug: how-to-analyze-saxs


SAXS Processing At The Beamline
=================================

*   On the SAXS data analysis computer you will use BioXTAS RAW to reduce the
    detector images (.tif) to one dimensional scattering profiles (.dats) and
    do preliminary processing.

    *   RAW is a full-featured GUI-based SAXS analysis program that can do data
        reduction and has specialized tools for processing SEC-SAXS data. It can
        do analysis all the way from basic background subtraction to Guinier fits,
        molecular weight calculation, IFT calculation (P(r) function) using GNOM,
        envelope calculation using DAMMIF/N, electron density calculation using DENSS,
        and deconvolution of SEC-SAXS data using EFA.

    *   Full written tutorials, video tutorials, a manual, and instructions for how
        to install RAW on your own computer can be obtained from the
        `RAW website <https://bioxtas-raw.readthedocs.io/>`_.

    *   BioCAT users may find the section on Basic SEC-SAXS processing particularly useful.

    *   Beamline scientists will provide hands-on training with RAW at the beamline

    *   RAW is developed and maintained by Jesse Hopkins, a beamline scientist at BioCAT.
        Bugs reports, feature requests, and other RAW questions should be sent to him.

*   In addition to RAW we also provide the ATSAS package (latest version), pyMOL
    and Chimera on the primary data analysis computer.

*   There is an additional identically configured computer available for data
    analysis at the beamline.


SAXS Data Processing At Home
==============================

*   Users will take home all unprocessed data: .tif files and log files, as well as a
    RAW .cfg file. In addition, they will take home any data processed at the beamline.

*   In order to carry out basic processing (images into one dimensional scattering
    profiles) users will need to `install RAW <https://bioxtas-raw.readthedocs.io/en/latest/install.html>`_.

    *   **IMPORTANT:** You need version 1.5.2 or greater to process (image) data collected
        at BioCAT.

*   Once you've installed RAW, make sure to load in your config file ("SAXS.cfg")
    BEFORE loading any images.

    *   This part of the RAW tutorial covers loading config files and how to process
        batch-mode samples: https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_basic.html

    *   This part of the RAW tutorial covers basic SEC-SAXS data processing:
        https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_sec.html

*   Please check the `RAW tutorial <https://bioxtas-raw.readthedocs.io/en/latest/tutorial.html>`_
    and the `RAW tutorial videos <https://bioxtas-raw.readthedocs.io/en/latest/videos.html>`_
    for more processing help, and reach out to use if you have any questions.

*   If you'd rather use another data processing program (like Primus or ScAtter),
    simply load your .cfg file into RAW, select all of your images in the 'File'
    Control Panel and click 'Quick Reduce'. This will generate .dat files from the
    images without loading them into RAW. These .dats are compatible with most popular
    SAXS software packages.


SAXS Processing Method
============================

*   A standard batch-mode data set for a well behaved globular protein might be
    processed using RAW as:

    *   `Buffer subtraction, scaling, and averaging
        data <http://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_basic.html>`_

    *   `Guinier fit <https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_guinier.html>`_

    *   `MW calculation to verify data quality and oligomeric state
        <https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_mw.html>`_

    *   `P(r) calculation using GNOM and datGNOM
        <https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s2_gnom.html>`_

    *   Evaluating the potential ambiguity of a 3D reconstruction using
        `AMBIMETER <https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s2_ambimeter.html>`_
        to verify that a reconstruction is worth doing

    *   3D reconstruction with ab initio bead models using `DAMMIF/N and average
        these models using DAMAVER <http://bioxtas-raw.readthedocs.io/en/latest/tutorial/s2_dammif.html>`_
        or cluster these models using DAMCLUST

    *   3D reconstruction with ab initio electron density models using `DENSS and
        EMAN2 <http://bioxtas-raw.readthedocs.io/en/latest/tutorial/s2_denss.html>`_

*   For more on what RAW can do, see the full tutorial:
    `tutorial <https://bioxtas-raw.readthedocs.io/en/latest/tutorial.html>`_
    and `tutorial videos <https://bioxtas-raw.readthedocs.io/en/latest/videos.html>`_

*   Alternatively, you can use Primus or Scatter for the processing described above,
    except for the electron density reconstruction.

*   A standard SEC-SAXS data set for a well behaved globular protein might be
    processed using RAW as:

    *   `Load the SEC curve <https://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_sec.html>`_
        in RAW, and use plots of the Rg and MW across the peak to determine what
        regions to process

    *   Testing buffer regions before and after the peak, `create a subtracted
        scattering profile <http://bioxtas-raw.readthedocs.io/en/latest/tutorial/s1_sec.html>`_

    *   Carry out the steps for batch-mode processing above starting with
        Guinier analysis.

*   P(r) can be used to calculate ab initio models using GASBOR, part of the ATSAS
    package, which is more reliable with higher quality high-q data (meaning > q =
    0.25-0.3) and for non-globular proteins

*   I-TASSER (or Phyre2 or Swiss-model) is used to build a homology model (if you
    don't have any structural information for your protein, which is then fit to
    the model using SUPCOMB)

*   SymmDock can be used to generate models with P2 and P4 symmetry (based on
    Phyre2 and I-TASSER model) *This symmetry stuff is necessary if you are
    trying to figure out what oligomeric state the protein is in. This may not
    be necessary for everyone*

*   CRYSOL used to calculate theoretical scattering curves of P1 (starting model),
    P2, and P4 homology models and compare to experimental data (*do this before
    you dock your model to ab initio envelope*)

    *   This will generate a .fit file containing a theoretical scattering curve
        of the pdb file fit to the experimental data (dat file) (the first three
        columns are q, Iexp(q) and Ifit(q)), and used for plotting). These .fit
        files can be loaded directly into RAW.

*   SUPCOMB will superimpose envelopes to homology models

    *   supcomb \*\*.pdb \*\*\*.pdb

    *   Output file will be \*\*\*r.pdb

    *   \*\*reference (homology) model

    *   \*\*\*moving (envelopes) model





