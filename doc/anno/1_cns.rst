===========================
T000 Central Nervous System 
===========================

The :abbr:`CNS (Central Nervous System)` tumours in our dataset exhibit three major divides: 
glioma vs. non-gliomas, gliomas with wildtype or mutated IDH1, 
and, in this last group, samples with and without hemizygous 
codeletion of chromosome arms 1p and 19q (Fig. :ref:`CNS1 <fig-cns1>`). 
We believe that the ability of our clustering system to demonstrate 
these genomic differences from purely transcriptional data with high 
confidence is a testament to its effectiveness. Past these major 
divides, differences in histotypes and tumour phenotype, as well 
as the transcriptional signals generated from specific mutations, 
become increasingly important to differentiate sibling classes. 
Indeed, many of these deeper clusters may reflect underlying clinical, 
genomic, and epigenomic differences which we are currently unable to 
determine due to a lack of relevant annotations. Our results express 
the plethora of undiscovered molecular subtypes of gliomas and 
glioblastomas in particular and highlight the need for further 
studies of subtype-specific drivers and their therapeutic 
susceptibilities. 


.. figure:: /img/cns1.png
   :alt: Fig. CNS1
   :name: fig-cns1
   :width: 500px
   
   CNS1: pippo 


Medulloblastoma
===============

At the first level, we see the separation of medulloblastomas, 
in :abbr:`T027 MLBLA (Medulloblastoma)` (n = 29), from the rest of :abbr:`CNS (Central nervous system)` 
tumours :abbr:`T026 CNS A (Central nervous system, mix A)` (n = 894) 
(Fig. :ref:`CNS1 <fig-cns1>`) Letters in the naming will be used in this setting to distinguish mixed 
classes that maintain the same composition of their parent class, with the removal of 
specific subtypes singled out into their sibling classes, as in this case. Interestingly, 
we also note the presence of a single pineal parenchymal tumour in :abbr:`T026 (Central nervous system, mix A)`. The recursion 
allows us to observe the emergence of known subtypes from literature at deeper level of 
this branch [Northcott2012]_. This class further splits into :abbr:`T058 MLBLA G3/G4 (Medulloblastoma, G3 or G4)` (n = 37) 
(Fig. :ref:`CNS1 <fig-cns1>`), a cluster of mixed G3 and G4 subtypes, with overexpression (:abbr:`glmQLFTest (edgeR quasi-likelihood negative binomial generalized log-linear model)` of *OTX2* (logFC = 3.48, FDR = 6.368e-06) 
and *FOXG1* (logFC = 8.44, FDR = 4.026e-06), while :abbr:`T059 MLBLA WNT/SSH (Medulloblastoma, WNT or SHH)` (n = 5), shows overexpression 
of both *WNT* (:abbr:`ssGSEA (single-sample GSEA from GSVA)` [Hänzelmann2013]_, :abbr:`medNES (median Normalized Enrichment Score)` = 1.15, 
 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`` = 6.74e-05) and *SHH* (medNES = 1.42, MWU adj. p-val = 2.02e-04) 
pathways [Kanehisa2000]_. While samples of the G3 and G4 subtypes are then separated 
at the next level into :abbr:`T060 MLBLA G4 (Medulloblastoma, G4)` (n = 9) and :abbr:`T061 MLBLA G3 (Medulloblastoma, G3)` 
(n = 15), the population of :abbr:`T059 (Medulloblastoma, WNT or SHH)` is 
well below our set cut-off, preventing RACCOON from dividing *WNT* and *SHH* subtypes. :abbr:`T060 (Medulloblastoma, G4)` overexpresses 
genes of the G4 subtype, including *SNCAIP* (logFC = 5.68, FDR = 1.11e-05), *DIRAS3* (logFC = 4.35, 
FDR = 2.351e-06), *KCNA1* (logFC = 4.19, FDR = 3.684e-04), and *RND1* (logFC = 3.26, FDR = 1.542e-04), 
while :abbr:`T061 (Medulloblastoma, G3)` overexpresses genes upregulated in the G3 subtype, 
such as *PDE6H* (logFC = -6, FDR = 6.038e-04), *GNGT1* (logFC = -6.1, FDR = 2.651e-04), 
and *NPR3* (logFC = -5.71, FDR = 4.824e-04). 

Separation by IDH1 status 
=========================

Following the remainder of CNS tumours after the removal of medulloblastomas, 
we observe the separation of gliomas without IDH1 mutations, which form :abbr:`T028 CNS IDHwt (Central nervous system tumours, IDH wild type)` (n = 406) 
from samples with IDH1 mutations (19/222 vs 417/433, χ2 p-val < 2.2e-16), which form :abbr:`T029 CNS IDHmut (Central nervous system tumours, IDH mutant)` (n = 488) (Fig. :ref:`CNS1 <fig-cns1>`). 
The latter has patients with lower median age (49.00 vs 38.00 y.o., :abbr:`MWU p-val (Mann Whitney U test p-value)` = 2.04e-3), but :abbr:`T028` has a considerably higher proportion 
of paediatric patients (40.06% vs. 27.05%, χ2 p-val = 2.40e-05). Furthermore, :abbr:`T028 (Central nervous system tumours, IDH wild type)` displays patients with significantly worse survival 
(:abbr:`lrt (Kaplan Meier log rank test)`` p-val = 1.57e-50 at 6423 days) in line with literature [Hartmann2010]_ reaching median overall 
survival (OS) at only 448 days compared to :abbr:`T029 (Central nervous system tumours, IDH mutant)` at 2907 (Fig. :ref:`CNS2 <fig-cns2>`) [Park2016]_, [Steponaitis2016]_, [Cimino2018]_, [Hernández2010]_.

.. figure:: /img/cns2.png
   :alt: Fig. CNS2
   :name: fig-cns2
   :width: 200px

   
   CNS2: pippo 


Bibliography
============

.. [Northcott2012] Northcott, P.A., Dubuc, A.M., Pfister, S. and Taylor, M.D. 2012. Molecular subgroups of medulloblastoma. Expert Review of Neurotherapeutics 12(7), pp. 871–884.
.. [Hänzelmann2013] Hänzelmann, S., Castelo, R. and Guinney, J. 2013. GSVA: gene set variation analysis for microarray and RNA-seq data. BMC Bioinformatics 14, p. 7.
.. [Kanehisa2000] Kanehisa, M. and Goto, S. 2000. KEGG: Kyoto encyclopedia of genes and genomes. Nucleic Acids Research 28(1), pp. 27–30.
.. [Hartmann2010] Hartmann, C., Hentschel, B., Wick, W., et al. 2010. Patients with IDH1 wild type anaplastic astrocytomas exhibit worse prognosis than IDH1-mutated glioblastomas, and IDH1 mutation status accounts for the unfavorable prognostic effect of higher age: implications for classification of gliomas. Acta Neuropathologica 120(6), pp. 707–718.
.. [Park2016] Park, S.Y., Piao, Y., Jeong, K.J., Dong, J. and de Groot, J.F. 2016. Periostin (POSTN) regulates tumor resistance to antiangiogenic therapy in glioma models. Molecular Cancer Therapeutics 15(9), pp. 2187–2197.
.. [Steponaitis2016] Steponaitis, G., Skiriutė, D., Kazlauskas, A., et al. 2016. High CHI3L1 expression is associated with glioma patient survival. Diagnostic Pathology 11, p. 42.
.. [Cimino2018] Cimino, P.J., Kim, Y., Wu, H.-J., et al. 2018. Increased HOXA5 expression provides a selective advantage for gain of whole chromosome 7 in IDH wild-type glioblastoma. Genes & Development 32(7–8), pp. 512–523.
.. [Hernández2010] Hernández, M., Martín, R., García-Cubillas, M.D., Maeso-Hernández, P. and Nieto, M.L. 2010. Secreted PLA2 induces proliferation in astrocytoma through the EGF receptor: another inflammation-cancer link. Neuro-oncology 12(10), pp. 1014–1023.