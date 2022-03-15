.. |br| raw:: html

  <br/>

.. _home:

Welcome to the Annotation of the Transcriptional Cancer Atlas!
==============================================================

Version: |version|
|br| 
Last change: |today|

This website contains a detailed description of the classes available in the transcriptional cancer atlas, a curated resource of 
gene expression data clustering from the Hospital for Sick Children. The atlas was produced with `RACCOON <https://github.com/fcomitani/raccoon>`_, 
a scale-adaptive clustering algorithm, and serves as a target to the `OTTER <insert link to OTTER web page here when available>`_ classifier. 

The data was gathered from different sources, including the `TreeHouse Childhood Cancer Initiative <https://treehousegenomics.ucsc.edu/>`_, 
`TCGA <https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga>`_,
`TARGET <https://ocg.cancer.gov/programs/target>`_ ,
`GTEx <https://gtexportal.org/home/>`_, and
`St. Jude Children's Research Hospital <https://pecan.stjude.cloud/>`_.

The classes have been manually annotated. Each one has been characterized based on its most relevant transcriptional properties and,
where available, clinical and genomics information. 

This website is still a work in progress. We are striving to cover all subtypes currently available in the atlas, please check back in the future
if what you are looking for is still not available.
For questions, comments or suggestions, please :ref:`contacts`. See also our :ref:`faq` section.

**IMPORTANT NOTE**: The annotation is updated periodically, make sure you are looking at a version
that is matching the classifier used in your project.

.. image:: /img/full_atlas.png
   :alt: UMAP of the full atlas
   :width: 500px
   :align: center

|br|
If you are using this annotation data or related software, please cite:
|br|
|br|
*F. Comitani, J. O. Nash, S. Cohen-Gogo, A. Chen Schwertschkow, T. T. Wen, A. Maheshwari, B. Goyal, E. S. L. Tio, K. Tabataei, K. Brunga, J. E. G. Lawrence, P. Balogh, A. Flanagan, S. Teichmann, V. Ramaswamy, J. Hitzler, J. Wasserman, R. A. Gladdy, B. C. Dickson, U. Tabori, M. J. Cowley, S. Behjati, D. Malkin, A. Villani, M. S. Irwin and A. Shlien, "Multi-scale transcriptional clustering and heterogeneity analysis reveal diagnostic classes of childhood cancer" (under review).*

..
   Citation of the paper, 
   https://doi.org/10.5281/zenodo.5788411
   Possibly add maybe the version should be published too with Zenodo.
   
Copyright ©2022 Federico Comitani, Josh O. Nash and Adam Shlien.

RESEARCH USE ONLY: This website is intended for research purposes only. These analyses were not performed for the purposes of diagnosis, prophylaxis, or treatment.



.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Annotation

   anno/N000_normal.rst
   anno/T000_cns.rst
   anno/T001_nebla.rst
   anno/T002_T003_mesoderm.rst
   anno/T005_leuk.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Dashboard
   
   dash.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: F.A.Q.
   
   faq.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Contact us
   
   contacts.rst

