How to prepare samples for equilibrium SAXS
###############################################################################

:category: users
:slug: how-to-prepare-saxs

.. contents::

SAXS sample shreadsheets
============================

BioCAT requests that for each beamtime you send us a spreadsheet of your samples
and buffers at least a week before the beamtime starts or you ship your samples
(whichever is earlier). Please note that there are two tabs, one for sample and
one for buffer. You may also find it useful for tracking/planning your experiments.
If you're not sure what the final concentrations are a week out, send us the
spreadsheet with target concentrations, then send us an update once you've
finalized the preparation. This helps us make sure the appropriate equipment
is available for your beamtime, and also lets us recommend any changes that
might be needed to sample or buffer volumes/quantities/concentrations ahead
of time, ensuring a more successful beamtime.

*   `Download blank sample spreadsheet <{static}/files/saxs_samples.xlsx>`_
*   `Download example sample spreadsheet <{static}/files/20210730_Hopkins_saxs_samples_example.xlsx>`_

Checklist for SAXS sample preparation
=======================================

Below are the recommendations for buffer and sample preparation for SAXS. Note
that at the end of the day, these are guidelines and the goal is always the
happiness and stability of the sample. We can accommodate most buffers, so ask
your beamline scientist if you have an unusual buffer composition.

Also, if possible we recommend combining similar buffers, particularly for
separation-coupled measurements like SEC-SAXS. Fewer buffers will save you a
significant amount of time during your experiment, so consider whether you can
combine similar conditions.

Buffer component recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   20-100 mM PBS, Tris,  HEPES, etc. PBS is preferred if possible.
*   Salt concentration < 1M, typically 50-200 mM
*   Avoid radical scavengers (glycerol, DTT, etc) unless needed for the
    stability of your protein. With BioCAT's coflow setup these actually
    increase the likelihood of seeing radiation damage.
*   If you need a reductant, use longer lived ones like TCEP
    rather than DTT (especially with higher pH buffers)

Buffer matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   SEC-SAXS/SEC-MALS-SAXS - Best if buffer is perfectly matched, but can
    tolerate nominally matched buffers that are not matched through exchange.
*   Batch SAXS - Must be a perfect match. Use dialysis buffer, the buffer
    from the final SEC purification step, or the flow through from the final
    concentration step.

If mailing concentrated buffer for separation coupled measurements (e.g. a
10x stock for use with SEC-SAXS), we recommend you prepare the concentrated
solution, create the final dilution in your lab, exchange your samples into
that, and then mail us the remaining concentrated stock for dilution on site.
While this doesn't perfectly match buffer, it gets close, and the buffer exchange
on the column will provide the necessary perfect match.

Buffer volume
^^^^^^^^^^^^^^^^^
*   SEC-SAXS/SEC-MALS-SAXS - `Buffer volume = 4*(column volume)*(number of samples + 1) + 250 mL. <{filename}/pages/users_howto_saxs_design.rst#saxs-buffer-volume>`_
*   Batch SAXS - Requires a `basic running buffer for the sheath and a perfectly
    matched buffer for the sample (can be the sample) <{filename}/pages/users_howto_saxs_design.rst#saxs-buffer-volume>`_.

    *   Sheath buffer: Buffer volume = 0.6*(number of samples) + 50 mL
    *   Perfectly matched buffer (if not sheath): Buffer volume = 3*(sample volume)

Sample (Protein or DNA/RNA) concentration and volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Concentration:

    *   SEC-MALS-SAXS/SEC-SAXS: 240/(MW in kDa) = concentration mg/ml
    *   Batch mode SAXS: 60/(MW in kDa) = concentration in mg/ml. Use a dilution
        series with a least 2 other concentrations bracketed around this. E.g.
        for a 20 kDa protein, measure at 6, 3, and 1.5 mg/ml.

For nucleic acid samples, you can divide the above concentrations by 2.5.

*   Minimum volume:

    *   SEC-SAXS/SEC-MALS-SAXS - 250 µL
    *   Batch-mode SAXS - 10 µL per concentration

Note: If mail-in samples are shipped frozen, they will be fast thawed
(e.g. in hand/water bath) unless you specify that the samples should
be thawed on ice.

Quality control: Pre-examination before X-ray scattering (Monodispersity)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Gel filtration (single and symmetric peak)
*   SDS-PAGE or Native GEL (single band)
*   Centrifugation or filter (> 15,000 x g * 5-10 mins)
*   Dynamic light scattering
*   SEC-MALS
*   Others

.. image:: {static}/images/gel.jpg
    :class: img-responsive
    :align: center

More details
=============

In the following video from the 2019 Everything BioSAXS 5 workshop, Dr. Kushol Gupta
discusses what you need to know about sample preparation for SAXS
(`get slides <{static}/files/eb5_lectures/Gupta_Planning_and_performaing_SAXS_experiments.pdf>`_)

.. row::

    .. column::
        :width: 8

        .. raw:: html

            <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/uWonjUMrKI8' frameborder='0' allowfullscreen></iframe></div>

