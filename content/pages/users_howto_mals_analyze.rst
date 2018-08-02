:title: How to analyze MALS data
:category: users
:slug: how-to-analyze-mals


All analysis uses ASTRA (Wyatt's software for SEC in-line MALS). At the beamline,
we use ASTRA 7.

*   Open an experiment (your file)

*   Open Experiments tab on the bottom left

*   Configuration -> generic pump (on left side panel)

    *   Set flow rate, (default is 0.8 but you should remember to change this to
        the real flow rate for any given experiment).

*   Procedures -> baselines (on left)

    *   First click autofind baselines

    *   Click through baselines and make sure all baselines are defined (if
        they are not good you have to define them; click once at start point
        and, hold and drag it to right side to define the baseline and range)

    *   Click Apply

*   In the top toolbar, Experiment -> configuration -> band broadening

    *   Define an area

    *   Click Perform fit

    *   Manually define peaks if needed

    *   Click Apply

*   Click Peaks on left side panel

    *   Choose what peaks (UV curve) you will be working with (better to choose
        range above baseline)

    *   Click Apply

*   Click Molecular Mass & Radius from LS on left side panel

    *   De-select detectors that had bad baselines

    *   Click Apply

    *   Can scroll through peaks to see MW for each peak from MALS

*   Click Rh from QELS on left side panel

    *   Can scroll through peak and see Rh from QELS (DLS)
