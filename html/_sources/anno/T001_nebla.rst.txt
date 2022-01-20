.. |br| raw:: html

  <br/>


==================
T001 Neuroblastoma 
==================


Version: |version|
|br| 
Last change: |today|

A total of 180 samples were labelled as neuroblastoma in our reference dataset, 
162 of which are from `TARGET <https://ocg.cancer.gov/programs/target>`_  while the rest are from different sources within the `TreeHouse initiative <https://treehousegenomics.ucsc.edu/>`_.  
RACCOON identified four separate subclusters within the neuroblastoma parent class (Fig. :ref:`NEBLA1 <fig-nebla1>`). They exhibit different molecular profiles and clinical outcomes, roughly overlapping with microarray expression clusters described in literature [Abel2011]_.


.. figure:: /img/nebla1.png
   :alt: Fig. NEBLA1
   :name: fig-nebla1
   :width: 500px
   
   NEBLA1: On the left, a 2-dimensional UMAP projection of neuroblastma tumors by gene expression, where the four subtypes identified are shown in different colors.
   Empty circles represent samples that were reported as MYCN amplified by clinical tests.

:abbr:`T062 NEBLA MES ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)`, the smallest cluster, contains a molecular 
signature which corresponds to microarray cluster p43 and comprises Children’s Oncology Group (`COG <https://childrensoncologygroup.org/>`_) samples reported as high-risk (Fig. :ref:`NEBLA2 <fig-nebla2>`). 
It is characterized by underexpression of the neuroblastoma predisposition genes *PHOX2B* (:abbr:`glmQLFTest (edgeR quasi-likelihood negative binomial generalized log-linear model)` :abbr:`medLogFC (median Log-Fold Change)` = -2.58, :abbr:`FDR (False Discovery Rate)` ≤ 2.93e-13), 
*MYCN* (:abbr:`medLogFC (median Log-Fold Change)` = -3.30, :abbr:`FDR (False Discovery Rate)` ≤ 3.11e-09), as well as the cell-cycle genes *BIRC5* 
(:abbr:`medLogFC (median Log-Fold Change)` = -5.92, :abbr:`FDR (False Discovery Rate)` ≤ 2.90e-16) and *CCND1* (:abbr:`medLogFC (median Log-Fold Change)` = -2.13, :abbr:`FDR (False Discovery Rate)` ≤ 4.84e-12), 
compared to its sibling clusters. :abbr:`T062 NEBLA MES ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)`  is also characterized by overexpression of *ERBB2* (*HER2*) (:abbr:`medLogFC (median Log-Fold Change)` = 1.32, :abbr:`FDR (False Discovery Rate)` < 8.16e-08), 
which has been demonstrated to be a favourable prognostic factor [Izycka-Swieszewska2010]_. 


.. figure:: /img/nebla2.png
   :alt: Fig. NEBLA2
   :name: fig-nebla2
   :width: 500px
   
   NEBLA2: Donut plot showing the samples stratification of the four identified neuroblastoma subtypes.
   These include (from top to bottom), COG risk group, Ploidy, Diagnosis and Grade.

Enrichment of *ERBB2* signalling is also seen in this cluster (:abbr:`ssGSEA (single-sample GSEA from GSVA)` :abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.31, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.25e-13, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` > 1.00e-02) [Ashburner2000]_, [TGOC2019]_. 
Neuroblastomas expressing *ERBB2* have increased differentiation, immunoreactivity, and patients show improved overall survival compared to patients with tumors with either low or no *ERBB2* expression [Izycka-Swieszewska2010]_. 
Indeed, we observe statistically significantly higher immune infiltration and lower stemness in this cluster (.38 median score, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`=1.39e-10 and 
.75 median score and :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.75e-12 respectively, see Methods for details on these scores), 
with respect to all the other classes (Fig. :ref:`NEBLA3 <fig-nebla3>`). 
Furthermore, :abbr:`T062 (Neuroblastoma, mesenchymal, ERBB2 overexpression)` contains the majority of nodular ganglioneuroblastomas (7/12, :abbr:`χ2 p-val (χ2 test p-value)` = 3.849e-05) (Fig. :ref:`NEBLA2 <fig-nebla2>`) and shows significant overexpression of 
ganglioneuroblastoma marker *ERRB3* (:abbr:`medLogFC (median Log-Fold Change)` = 5.7, :abbr:`FDR (False Discovery Rate)` ≤ 3.484e-15), as well as enrichment for *ERBB* network gene sets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.27, 
:abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` = 1.95e-09, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Schaefer2009]_. 
It also exhibits enrichment of glial cell developmental pathways (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.31, :abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` = 2.55e-12, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03) and adrenal gland developmental gene sets 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.30, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.14e-12, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02) [Ashburner2000]_, [TGOC2019]_. 

.. figure:: /img/nebla3.png
   :alt: Fig. NEBLA3
   :name: fig-nebla3
   :width: 500px
   
   NEBLA3: 2-dimensional UMAP projection of the neuroblastoma samples coloured according to different scales.
   From left to right: immune activity score (from 0 to 1), identity (from adrenal to mesenchymal) and median Normalized Enrichment Score (from 0 to 1) of a
   set of genes downstream to MYCN amplification. 

:abbr:`T063 NEBLA ADR NTRK1 (Neuroblastoma, mesenchymal, NTRK1 overexpression)`, the most populous subgroup, corresponds to microarray cluster p13, and 
is characterized by overexpression of *NTRK1* with respect to its sibling clusters 
(:abbr:`medLogFC (median Log-Fold Change)` = 1.51, :abbr:`FDR (False Discovery Rate)` < 5.78e-4). Patients with tumors within this class are significantly younger than ones in other NEBLA clusters 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.25e-05). 
It contains all samples classified as low and intermediate `COG <https://childrensoncologygroup.org/>`_ risk by `TARGET <https://ocg.cancer.gov/programs/target>`_ (:abbr:`χ2 p-val (χ2 test p-value)` = 1.04e-08), 
and contains all patients classified as stage 4s (:abbr:`χ2 p-val (χ2 test p-value)` = 2.76e-07) and stage 3 (:abbr:`χ2 p-val (χ2 test p-value)` = 3.58e-2) (Fig. S22b). 
It is significantly enriched in patients with tumors with favourable histology (:abbr:`χ2 p-val (χ2 test p-value)` = 3.30e-08), and also contains the only intermixed ganglioneuroblastoma tumor referenced in the 
`TARGET <https://ocg.cancer.gov/programs/target>`_ cohort (Fig. :ref:`NEBLA2 <fig-nebla2>`). :abbr:`T063 (Neuroblastoma, mesenchymal, NTRK1 overexpression)` shows enrichment of gene sets related to sympathetic nervous system development 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.08, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.97e-17, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02) 
and chromaffin cells (:abbr:`medNES (median Normalized Enrichment Score)` = 1.11, adj. p-val = 4.49e-17, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Ashburner2000]_, [TGOC2019]_, 
suggesting this cluster may be defined by sympathoadrenal differentiation. It carries low immune infiltration (median score 0.29) and high stemness (median score 0.77) Fig. :ref:`NEBLA4 <fig-nebla4>`. 


.. figure:: /img/nebla4.png
   :alt: Fig. NEBLA4
   :name: fig-nebla4
   :width: 500px
   
   NEBLA4: Distribution plots of various scores across the four identified neuroblastoma subtypes.
   From left to right: stemness score (top half), immune activity score (bottom half), identity and median Normalized Enrichment Score of a
   set of genes downstream to MYCN amplification. The last panel also includes at the bottomsamples in :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` while
   split in two groups, according to their MYCN amplification status by clinical tests as reported by the presenting institution.

The two remaining clusters, :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` and :abbr:`T065 NEBLA ADR TERT(Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)`, 
are exclusively comprised of samples marked as `COG <https://childrensoncologygroup.org/>`_ high-risk (Fig. :ref:`NEBLA2 <fig-nebla2>`), and overlap with microarray clusters p3 and p2 [Abel2011]_, respectively. 
Both clusters exhibit overexpression of *BIRC5* compared to :abbr:`T062 NEBLA ERBB2(Neuroblastoma, mesenchymal, ERBB2 overexpression)`  and :abbr:`T063 NEBLA ADR NTRK1 (Neuroblastoma, mesenchymal, NTRK1 overexpression)` (:abbr:`T064 (Neuroblastoma, mesenchymal, MYCN amplification)` :abbr:`logFC (log-Fold Change)`` = 1.74, :abbr:`FDR (False Discovery Rate)` = 3.33e-05; 
:abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` :abbr:`logFC (log-Fold Change)` = 2.05, :abbr:`FDR (False Discovery Rate)` = 9.47e-07). 
:abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)`  is characterized by a statically significant overexpression of *MYCN* (:abbr:`medLogFC (median Log-Fold Change)` = 1.51, :abbr:`FDR (False Discovery Rate)` ≤ 5.78e-04), 
and contains the majority of samples flagged as *MYCN* amplified by `TARGET <https://ocg.cancer.gov/programs/target>`_ 
(:abbr:`χ2 p-val (χ2 test p-value)` = 7.31e-15) (Fig. :ref:`NEBLA1 <fig-nebla1>`). It is also defined by the underexpression of *NTRK1* (:abbr:`logFC (log-Fold Change)` = -3.25, :abbr:`FDR (False Discovery Rate)` = 1.99e-09). 
Though the majority of :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)`  samples are marked by `TARGET <https://ocg.cancer.gov/programs/target>`_ as *MYCN*-amplified, 37.5% of samples (n = 9/34) are annotated as non-amplified. 
However, gene set analysis with downstream *MYCN* targets from literature [Valentijn2012]_ shows continued enrichment of *MYCN* targets in these samples despite the absence of *MYCN* amplification (with all samples, 
:abbr:`medNES (median Normalized Enrichment Score)` = 1.22, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 8.64e-17, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04, 
with only *MYCN*-non amplified tumors in :abbr:`T064 (Neuroblastoma, mesenchymal, MYCN amplification)`, :abbr:`medNES (median Normalized Enrichment Score)` = 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.62e-11) (Fig. :ref:`NEBLA3 <fig-nebla3>`, :ref:`NEBLA4 <fig-nebla4>`). 
In line with previous studies, which identified a correlation between *MYCN*-amplified tumors and mitosis-karryohexis index (MKI) [Teshiba2014]_, 
we observe significantly more samples carrying high MKI (13/33, :abbr:`χ2 p-val (χ2 test p-value)` = 1.03e-02) 
in :abbr:`T064 (Neuroblastoma, mesenchymal, MYCN amplification)` when compared to the other classes.  

Both :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` and :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)`  are characterized by significant *TERT* overexpression compared to 
:abbr:`T062 NEBLA ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)` and :abbr:`T063 NEBLA ADR NTRK1 (Neuroblastoma, mesenchymal, NTRK1 overexpression)`. 
Previous studies have explored the associations between telomere maintenance and prognosis in neuroblastoma, identifying three mutually exclusive pathways which are enriched in high risk tumors: 
*ATRX* upregulation, *MYCN* amplification, and *TERT* rearrangements, each of which result in the overexpression of *TERT* [Valentijn2015]_, [Duan2018]_. 
Indeed, both :abbr:`T064 (Neuroblastoma, mesenchymal, MYCN amplification)` and :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
have enrichment of alternative telomere lengthening pathways (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` < 2.06e-14) [Nabetani2011]_, [Jassal2020]_ (Fig. :ref:`NEBLA5 <fig-nebla5>`). 
*TERT* rearrangements are associated with the upregulation of *SLC6A18* and *SLC6A19*, genes neighbouring *TERT* on the distal side of its breakpoint. 
Both these genes were significantly upregulated in :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)`  
(*SLC6A18*, :abbr:`medLogFC (median Log-Fold Change)` = 3.77, :abbr:`FDR (False Discovery Rate)` ≤ 3.78e-06; 
*SLC6A19*, :abbr:`medLogFC (median Log-Fold Change)` = 3.88, :abbr:`FDR (False Discovery Rate)` < 2.96e-03), 
but not in :abbr:`T064 NEBLA MYCN(Neuroblastoma, mesenchymal, MYCN amplification)` , suggesting :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` may be comprised of *TERT*-rearranged neuroblastomas. 
*CCND1* amplification has been observed concurrently with *TERT* rearrangements in neuroblastomas [Fransson2020]_ and is highly upregulated in :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
(:abbr:`medLogFC (median Log-Fold Change)` = 1.09, :abbr:`FDR (False Discovery Rate)` ≤ 5.67e-06). 
We find no significant differences in expression of *ATRX* between clusters. :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
exhibits the lowest expression of gene sets related to adrenal development (:abbr:`medNES (median Normalized Enrichment Score)` = 0.39, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.14e-12, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [TGOC2019]_, [Ashburner2000]_, 
as well as low expression of mature chromaffin markers such as *EPAS1* (:abbr:`medLogFC (median Log-Fold Change)` = -1.09, :abbr:`FDR (False Discovery Rate)` ≤ 4.412e-02) [Westerlund2019]_, 
suggesting this cluster is formed of poorly differentiated neuroblastomas. To further support this hypothesis, we observe here the highest median stemness score (0.81) among all classes, while a non-negligible immune infiltration score is also observed (.45) (Fig. :ref:`NEBLA3 <fig-nebla3>`, :ref:`NEBLA4 <fig-nebla4>`). 
Hypermethylation of the *TERT* locus in high-risk neuroblastomas has been reported in literature [Olsson2016]_. 
In line with this observation, :abbr:`T065 NEBLA ADR TERT(Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)`  
shows enrichment for DNA methylation pathways (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.79e-14), 
and numerous histone modification gene sets: notably methylation of *H3K4*, a transcriptional inducer 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.02, :abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` = 2.97e-13), 
and methylation of *H3K9*, a known silencer of tumor suppressors (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.15, 
:abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` = 1.78e-12) [Ashburner2000]_, [TGOC2019]_, [Ke2014]_, [Durinck2018]_. 
Furthermore, :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` is highly enriched for *PRC2* complex activity (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.15e-14, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03) [Nishimura2001]_. 
Though *PRC2* activity is usually examined in the context of *MYCN* amplification [Corvetta2013]_, [Tsubota2017]_, [Chen2018]_, 
this data supports recent evidence of a *PRC2* signature independent of *MYCN* amplification in high-risk neuroblastoma [Yang2017]_.

Both :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` and :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
show a characteristic enrichment of COSMIC signature 18 gene set (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 4.87e-12) [Brady2020]_, 
associated with reactive oxygen species, when compared to T061 and :abbr:`T062 (Neuroblastoma, mesenchymal, ERBB2 overexpression)` (Fig. :ref:`NEBLA5 <fig-nebla5>`). 
This signature has been suggested to be causative of point mutations in neuroblastoma and has been associated with *MYCN* amplification, and increased expression of electron-transport, ribosomal, and mitochondrial genes. 
The latter, in particular, follows from a 17q gain, a prognostic marker for poor outcome [Brady2020]_, [Kucab2019]_. 
We observe significant enrichment of chromosome 17q gene sets in :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.20, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 5.86e-04) [Yates2020]_. 
Partial loss of 11q (q21-25), associated with *TERT* rearrangements in literature [Roderwieser2019]_, is also present in 
:abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` 
(:abbr:`medNES (median Normalized Enrichment Score)` ≤ 6.56e-01, :abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` ≤ 1.03e-05). 
Our data support the existence of two major phenotypes with very poor outcome in canonically high-risk neuroblastoma, one driven by *MYCN* activation, 
the other by *TERT* activation independent of *MYCN*. While genomic rearrangements 
for samples in :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` were not reported, 
neuroblastomas lacking genomic rearrangements at the *TERT* locus, but expressing a high *TERT* phenotype, have been reported in literature [Roderwieser2019]_, [Ackermann2018]_. 
We speculate :abbr:`T065 (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` may also include samples with non-lesional *TERT* activation, 
potentially involving gain of 17q and loss of 11q.

.. figure:: /img/nebla5.png
   :alt: Fig. NEBLA5
   :name: fig-nebla5
   :width: 500px
   
   NEBLA5: Distribution plots of various gene sets enrichment scores relevant to the lineage definition across the four identified neuroblastoma subtypes.


The four neuroblastoma classes also show a significant segregation of samples by ploidy level. :abbr:`T063 (Neuroblastoma, mesenchymal, NTRK1 overexpression)` contains most hyperdiploid tumors 
(34/46, :abbr:`χ2 p-val (χ2 test p-value)` = 4.01e-03) and consequently has the highest median ploidy value (1.285, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.56e-03) (Fig. :ref:`NEBLA2 <fig-nebla2>`). 
:abbr:`T062 NEBLA ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)`  and :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)`  have the lowest median value (1.00 both), 
with the former having a majority of diploid members (9/12, :abbr:`χ2 p-val (χ2 test p-value)` = 4.01e-03) (Fig. :ref:`NEBLA2 <fig-nebla2>`). 

Furthermore, we observe a significant separation between the Kaplan-Meier fitted curves of overall survival rates (OS, available only for `TARGET <https://ocg.cancer.gov/programs/target>`_ data, :abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 1.36e-02 at 4948 days) (Fig.  :ref:`NEBLA6 <fig-nebla6>`). 
As expected, patients with tumors in :abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` have the poorest outcome, 
followed by :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)`,
:abbr:`T062 NEBLA ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)`  and finally :abbr:`T062 NEBLA ADR NTRK1 (Neuroblastoma, mesenchymal, ERBB2 overexpression)`. 
This is consistent with literature: improved survival was documented for *ERBB2*-overexpressing neuroblastomas [Izycka-Swieszewska2010]_, 
although here observed only against other `COG <https://childrensoncologygroup.org/>`_ high-risk samples.


.. figure:: /img/nebla6.png
   :alt: Fig. NEBLA6
   :name: fig-nebla6
   :width: 250px
   
   NEBLA5: Overall survival time curves of the four identified neuroblastoma subtypes. 

Recent work investigated linage and developmental differences across neuroblastomas and identified two major groups defined by distinct expression modules driven: 
a sympathoadrenal identity and neural-crest cell-like (NCC-like)/mesenchymal identity. 
These developmental states are mediated epigenetically through the action of of super-enhancer and super-enhancer related transcriptional factor networks.  
Neuroblastomas can move from one to the other identity under selective pressure, induced by therapy or epigenetic alterations and often contain intermixed 
populations [Boeva2017]_, [vanGroningen2017]_. We thus decided to search for overlaps between these developmental identities and our clusters. 
Interestingly, we observe the characteristic signature of both lineages in all clusters although expressed to different degrees. 
:abbr:`T062 NEBLA ERBB2 (Neuroblastoma, mesenchymal, ERBB2 overexpression)` in particular is committed to an NCC-like linage as shown by high expression of 
NCC-like and mesenchymal markers (:abbr:`medNES (median Normalized Enrichment Score)` = 1.57, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.69e-07, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03) against all other classes (Fig. :ref:`NEBLA3 <fig-nebla3>`, :ref:`NEBLA4 <fig-nebla4>`). 
These in turn show enrichment noradrenergic and sympathoadrenal gene sets (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 1.19e-09) [Boeva2017]_, [vanGroningen2017]_, [Tomolonis2018]_ (Fig.  :ref:`NEBLA5 <fig-nebla5>`).  
Samples belonging to :abbr:`T065 NEBLA ADR TERT (Neuroblastoma, mesenchymal, TERT overexpression without MYCN amplification)` seem to be the most committed to the sympathoadrenal specification (:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05 
against :abbr:`T062 (Neuroblastoma, mesenchymal, ERBB2 overexpression)` and :abbr:`T064 (Neuroblastoma, mesenchymal, MYCN amplification)`) (Fig. :ref:`NEBLA4 <fig-nebla4>`). 
:abbr:`T064 NEBLA MYCN (Neuroblastoma, mesenchymal, MYCN amplification)` shows high variation in the values of its enrichment scores for both linages (Fig. :ref:`NEBLA4 <fig-nebla4>`). 
The expression profile downstream of *MYCN* amplification may have overridden the original identity signal, 
or alternatively mixed-lineage populations are common in *MYCN*-amplified samples.


Bibliography
============

.. [Abel2011] Abel, F., Dalevi, D., Nethander, M.,2011. A 6-gene signature identifies four molecular subgroups of neuroblastoma. Cancer cell international 11, p. 9.
.. [Ackermann2018] Ackermann, S., Cartolano, M., Hero, B.,2018. A mechanistic classification of clinical phenotypes in neuroblastoma. Science 362(6419), pp. 1165–1170.
.. [Ashburner2000] Ashburner, M., Ball, C.A., Blake, J.A.,2000. Gene Ontology: tool for the unification of biology. Nature Genetics 25(1), pp. 25–29.
.. [Boeva2017] Boeva, V., Louis-Brennetot, C., Peltier, A.,2017. Heterogeneity of neuroblastoma cell identity defined by transcriptional circuitries. Nature Genetics 49(9), pp. 1408–1413.
.. [Brady2020] Brady, S.W., Liu, Y., Ma, X.,2020. Pan-neuroblastoma analysis reveals age- and signature-associated driver alterations. Nature Communications 11(1), p. 5183.
.. [Chen2018] Chen, L., Alexe, G., Dharia, N.V.,2018. CRISPR-Cas9 screen reveals a MYCN-amplified neuroblastoma dependency on EZH2. The Journal of Clinical Investigation.
.. [Corvetta2013] Corvetta, D., Chayka, O., Gherardi, S.,2013. Physical interaction between MYCN oncogene and polycomb repressive complex 2 (PRC2) in neuroblastoma: functional and therapeutic implications. The Journal of Biological Chemistry 288(12), pp. 8332–8341.
.. [Duan2018] Duan, X.-F. and Zhao, Q. 2018. TERT-mediated and ATRX-mediated Telomere Maintenance and Neuroblastoma. Journal of Pediatric Hematology/Oncology 40(1), pp. 1–6.
.. [Durinck2018] Durinck, K. and Speleman, F. 2018. Epigenetic regulation of neuroblastoma development. Cell and Tissue Research 372(2), pp. 309–324.
.. [Fransson2020] Fransson, S., Martinez-Monleon, A., Johansson, M.,2020. Whole-genome sequencing of recurrent neuroblastoma reveals somatic mutations that affect key players in cancer progression and telomere maintenance. Scientific Reports 10(1), p. 22432.
.. [vanGroningen2017] van Groningen, T., Koster, J., Valentijn, L.J.,2017. Neuroblastoma is composed of two super-enhancer-associated differentiation states. Nature Genetics 49(8), pp. 1261–1266.
.. [Izycka-Swieszewska2010] Izycka-Swieszewska, E., Wozniak, A., Kot, J.,2010. Prognostic significance of HER2 expression in neuroblastic tumors. Modern Pathology 23(9), pp. 1261–1268.
.. [Jassal2020] Jassal, B., Matthews, L., Viteri, G.,2020. The Reactome Pathway Knowledgebase. Nucleic Acids Research 48(D1), pp. D498–D503.
.. [Ke2014] Ke, X.-X., Zhang, D., Zhu, S., Xia, Q., Xiang, Z. and Cui, H. 2014. Inhibition of H3K9 methyltransferase G9a repressed cell proliferation and induced autophagy in neuroblastoma cells. Plos One 9(9), p. e106962.
.. [Kucab2019] Kucab, J.E., Zou, X., Morganella, S.,2019. A compendium of mutational signatures of environmental agents. Cell 177(4), p. 821–836.e16.
.. [Nabetani2011] Nabetani, A. and Ishikawa, F. 2011. Alternative lengthening of telomeres pathway: recombination-mediated telomere maintenance mechanism in human cells. Journal of Biochemistry 149(1), pp. 5–14.
.. [Nishimura2001] Nishimura, D. 2001. BioCarta. Biotech Software & Internet Report 2(3), pp. 117–120.
.. [Olsson2016] Olsson, M., Beck, S., Kogner, P., Martinsson, T. and Carén, H. 2016. Genome-wide methylation profiling identifies novel methylated genes in neuroblastoma tumors. Epigenetics 11(1), pp. 74–84.
.. [Roderwieser2019] Roderwieser, A., Sand, F., Walter, E.,2019. Telomerase is a prognostic marker of poor outcome and a therapeutic target in neuroblastoma. JCO precision oncology (3), pp. 1–20.
.. [Schaefer2009] Schaefer, C.F., Anthony, K., Krupa, S.,2009. PID: the pathway interaction database. Nucleic Acids Research 37(Database issue), pp. D674-9.
.. [Teshiba2014] Teshiba, R., Kawano, S., Wang, L.L.,2014. Age-dependent prognostic effect by Mitosis-Karyorrhexis Index in neuroblastoma: a report from the Children’s Oncology Group. Pediatric and developmental pathology : the official journal of the Society for Pediatric Pathology and the Paediatric Pathology Society 17(6), pp. 441–449.
.. [TGOC2019] The Gene Ontology Consortium 2019. The Gene Ontology Resource: 20 years and still GOing strong. Nucleic Acids Research 47(D1), pp. D330–D338.
.. [Tomolonis2018] Tomolonis, J.A., Agarwal, S. and Shohet, J.M. 2018. Neuroblastoma pathogenesis: deregulation of embryonic neural crest development. Cell and Tissue Research 372(2), pp. 245–262.
.. [Tsubota2017] Tsubota, S., Kishida, S., Shimamura, T.,2017. PRC2-Mediated Transcriptomic Alterations at the Embryonic Stage Govern Tumorigenesis and Clinical Outcome in MYCN-Driven Neuroblastoma. Cancer Research 77(19), pp. 5259–5271.
.. [Valentijn2012] Valentijn, L.J., Koster, J., Haneveld, F.,2012. Functional MYCN signature predicts outcome of neuroblastoma irrespective of MYCN amplification. Proceedings of the National Academy of Sciences of the United States of America 109(47), pp. 19190–19195.
.. [Valentijn2015] Valentijn, L.J., Koster, J., Zwijnenburg, D.A.,2015. TERT rearrangements are frequent in neuroblastoma and identify aggressive tumors. Nature Genetics 47(12), pp. 1411–1414.
.. [Westerlund2019] Westerlund, I., Shi, Y. and Holmberg, J. 2019. EPAS1/HIF2α correlates with features of low-risk neuroblastoma and with adrenal chromaffin cell differentiation during sympathoadrenal development. Biochemical and Biophysical Research Communications 508(4), pp. 1233–1239.
.. [Yang2017] Yang, X.H., Tang, F., Shin, J. and Cunningham, J.M. 2017. Incorporating genomic, transcriptomic and clinical data: a prognostic and stem cell-like MYC and PRC imbalance in high-risk neuroblastoma. BMC Systems Biology 11(Suppl 5), p. 92.
.. [Yates2020] Yates, A.D., Achuthan, P., Akanni, W.,2020. Ensembl 2020. Nucleic Acids Research 48(D1), pp. D682–D688.

