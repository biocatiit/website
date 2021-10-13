How to prepare samples for equilibrium SAXS
###############################################################################

:category: users
:slug: how-to-prepare-saxs

In the following video from the 2019 Everything BioSAXS 5 workshop, Dr. Kushol Gupta
discusses what you need to know about sample preparation for SAXS
(`get slides <{static}/files/eb5_lectures/Gupta_Planning_and_performaing_SAXS_experiments.pdf>`_)

.. row::

    .. column::
        :width: 8

        .. raw:: html

            <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/uWonjUMrKI8' frameborder='0' allowfullscreen></iframe></div>


Checklist for SAXS sample preparation
=======================================

Buffer components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   20-100 mM PBS, Tris,  HEPES, etc. PBS is preferred if possible.
*   Salt concentration < 1M, typically 150-200 mM
*   Avoid radical scavengers (glycerol, DTT, etc) unless needed for the
    stability of your protein. With BioCAT's coflow setup these actually
    increase the likelyhood of seeing radiation damage.

Buffer matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   SEC-SAXS/SEC-MALS-SAXS - Use dialysis buffer or a matched buffer from the
    final SEC purification step.
*   Batch-mode SAXS - use dialysis buffer
*   SEC-SAXS - make enough buffer for both the experiments and equilibration.
    `For SEC-MALS-SAXS > 1.5 L, for SEC-SAXS > 500 mL. <{filename}/pages/users_howto_saxs_design.rst#saxs-buffer-volume>`_
*   If mailing concentrated buffer for SEC-SAXS or SEC-MALS-SAXS (e.g. 10x),
    we recommend you prepare the concentrated solution, create the final
    dilution in your lab, exchange your samples into that, and then mail us
    the remaining concentrated stock for dilution on site. While this doesn't
    perfectly match buffer, it gets close, and the buffer exchange on the
    column will guarantee a perfect match.

Sample (Protein or DNA/RNA) concentration and amount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Concentration:

    *   SEC-MALS-SAXS/SEC-SAXS: 240/(MW in kDa) = concentration mg/ml
    *   Batch mode SAXS: 60/(MW in kDa) = concentration in mg/ml. Use a dilution
        series with a least 2 other concentrations bracketed around this. E.g.
        for a 20 kDa protein, measure at 6, 3, and 1.5 mg/ml.

*   Minimum volume:

    *   SEC-MALS-SAXS / SEC-SAXS - 250 µL
    *   Batch-mode SAXS - 50 µl per concentration

Quality control: Pre-examination before X-ray scattering (Monodispersity)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*   Gel filtration (single and symmetric peak)
*   SDS-PAGE or Native GEL (single band)
*   Centrifugation or filter (> 15,000g * 10 mins)
*   Dynamic light scattering
*   Others

.. image:: {static}/images/gel.jpg
    :class: img-responsive
    :align: center



