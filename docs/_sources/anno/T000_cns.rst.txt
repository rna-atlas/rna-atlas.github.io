.. |br| raw:: html

  <br/>

===========================
T000 Central Nervous System 
===========================

Version: |version|
|br| 
Last change: |today|

The :abbr:`CNS (Central Nervous System)` tumors in our dataset exhibit three major divides: 
glioma vs. non-gliomas, gliomas with wildtype or mutated IDH1, 
and, in this last group, samples with and without hemizygous 
codeletion of chromosome arms 1p and 19q (Fig. :ref:`CNS1 <fig-cns1>`). 
We believe that the ability of our clustering system to demonstrate 
these genomic differences from purely transcriptional data with high 
confidence is a testament to its effectiveness. Past these major 
divides, differences in histotypes and tumor phenotype, as well 
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
   :width: 600px
   
   CNS1: On the left, a 2-dimensional UMAP projection of CNS tumors by gene expression, where several subtypes 
   found in the first layers of the hierarchy are highlighted with different colors. On the right, a list of all CNS subtypes identified
   and their hierarchical relationship. 


Medulloblastoma
===============

At the first level, we see the separation of medulloblastomas, 
in :abbr:`T027 MLBLA (Medulloblastoma)` (n = 29), from the rest of :abbr:`CNS (Central nervous system)` 
tumors :abbr:`T026 CNS A (Central nervous system, mix A)` (n = 894) 
(Fig. :ref:`CNS1 <fig-cns1>`) Letters in the naming will be used in this setting to distinguish mixed 
classes that maintain the same composition of their parent class, with the removal of 
specific subtypes singled out into their sibling classes, as in this case. Interestingly, 
we also note the presence of a single pineal parenchymal tumor in :abbr:`T026 (Central nervous system, mix A)`. The recursion 
allows us to observe the emergence of known subtypes from literature at deeper level of 
this branch [Northcott2012]_. This class further splits into :abbr:`T058 MLBLA G3/G4 (Medulloblastoma, G3 or G4)` (n = 37) 
(Fig. :ref:`CNS1 <fig-cns1>`), a cluster of mixed G3 and G4 subtypes, with overexpression of *OTX2* (:abbr:`glmQLFTest (edgeR quasi-likelihood negative binomial generalized log-linear model)` :abbr:`logFC (log-Fold Change)` = 3.48, :abbr:`FDR (False Discovery Rate)` = 6.368e-06) 
and *FOXG1* (:abbr:`logFC (log-Fold Change)` = 8.44, :abbr:`FDR (False Discovery Rate)` = 4.026e-06), while :abbr:`T059 MLBLA WNT/SSH (Medulloblastoma, WNT or SHH)` (n = 5), shows overexpression 
of both *WNT* (:abbr:`ssGSEA (single-sample GSEA from GSVA)` [Hänzelmann2013]_, :abbr:`medNES (median Normalized Enrichment Score)` = 1.15, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 6.74e-05) and *SHH* (:abbr:`medNES (median Normalized Enrichment Score)` = 1.42, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.02e-04) 
pathways [Kanehisa2000]_. While samples of the G3 and G4 subtypes are then separated 
at the next level into :abbr:`T060 MLBLA G4 (Medulloblastoma, G4)` (n = 9) and :abbr:`T061 MLBLA G3 (Medulloblastoma, G3)` 
(n = 15), the population of :abbr:`T059 (Medulloblastoma, WNT or SHH)` is 
well below our set cut-off, preventing RACCOON from dividing *WNT* and *SHH* subtypes. :abbr:`T060 (Medulloblastoma, G4)` overexpresses 
genes of the G4 subtype, including *SNCAIP* (:abbr:`logFC (log-Fold Change)` = 5.68, :abbr:`FDR (False Discovery Rate)` = 1.11e-05), *DIRAS3* (:abbr:`logFC (log-Fold Change)` = 4.35, 
:abbr:`FDR (False Discovery Rate)` = 2.351e-06), *KCNA1* (:abbr:`logFC (log-Fold Change)` = 4.19, :abbr:`FDR (False Discovery Rate)` = 3.684e-04), and *RND1* (:abbr:`logFC (log-Fold Change)` = 3.26, :abbr:`FDR (False Discovery Rate)` = 1.542e-04), 
while :abbr:`T061 (Medulloblastoma, G3)` overexpresses genes upregulated in the G3 subtype, 
such as *PDE6H* (:abbr:`logFC (log-Fold Change)` = -6, :abbr:`FDR (False Discovery Rate)` = 6.038e-04), *GNGT1* (:abbr:`logFC (log-Fold Change)` = -6.1, :abbr:`FDR (False Discovery Rate)` = 2.651e-04), 
and *NPR3* (:abbr:`logFC (log-Fold Change)` = -5.71, :abbr:`FDR (False Discovery Rate)` = 4.824e-04). 

Separation by IDH1 status 
=========================

Following the remainder of CNS tumors after the removal of medulloblastomas, 
we observe the separation of gliomas without IDH1 mutations, which form :abbr:`T028 CNS IDHwt (Central nervous system tumors, IDH wild type)` (n = 406) 
from samples with IDH1 mutations (19/222 vs 417/433, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16), which form :abbr:`T029 CNS IDHmut (Central nervous system tumors, IDH-mutant)` (n = 488) (Fig. :ref:`CNS1 <fig-cns1>`). 
The latter has patients with lower median age (49.00 vs 38.00 y.o., :abbr:`MWU p-val (Mann Whitney U test p-value)` = 2.04e-3), but :abbr:`T028` has a considerably higher proportion 
of pediatric patients (40.06% vs. 27.05%, :abbr:`χ2 p-val (χ2 test p-value)` = 2.40e-05). Furthermore, :abbr:`T028 (Central nervous system tumors, IDH wild type)` displays patients with significantly worse survival 
(:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)``  = 1.57e-50 at 6423 days) in line with literature [Hartmann2010]_ reaching median overall 
survival (OS) at only 448 days compared to :abbr:`T029 (Central nervous system tumors, IDH-mutant)` at 2907 (Fig. :ref:`CNS2 <fig-cns2>`) [Park2016]_, [Steponaitis2016]_, [Cimino2018]_, [Hernández2010]_.

.. figure:: /img/cns2.png
   :alt: Fig. CNS2
   :name: fig-cns2
   :width: 300px

   CNS2: Overall survival time curves of wild-type and mutant IDH tumors. 

BCOR-altered Samples and Ependymoma
===================================

Along the IDH1 wild-type branch :abbr:`T028 (Central nervous system tumors, IDH wild type)` we then observe the separation of gliomas and 
glioblastomas in :abbr:`T030 GLI IDHwt (Glioma, IDH wild-type)` from ependymomas in 
:abbr:`T032 EPDY (Ependymoma)` and samples with lesions of the BCL-6 corepressor protein gene, *BCOR*, :abbr:`T031 CNS BCOR/PNET (Central nervous system with BCOR alterations, primitive neuroectodermal tumors)` 
(Fig. :ref:`CNS1 <fig-cns1>`, Fig. :ref:`CNS3a <fig-cns3>`). 
:abbr:`T030 GLI IDHwt (Glioma, IDH wild-type)` (n = 364) includes the vast majority of gliomas and glioblastomas without mutations of IDH1 and is the oldest class 
(median age = 52 y.o. :abbr:`KW p-val (Kruskal–Wallis one-way analysis of variance test p-value)` = 5.72e-10).
:abbr:`T031 CNS BCOR/PNET (Central nervous system with BCOR alterations, primitive neuroectodermal tumors)` is a peculiarly small cluster (n = 12) 
comprised of heterogeneous diagnoses. It includes a variety of brain and 
CNS tumors, including ependymomas, primitive neuroectodermal tumors (PNET), gliomas, an embryonal tumor with multi-layered rosettes, 
and a handful of solid tumors - several possibly misdiagnosed as Ewing sarcoma - and one infantile fibrosarcoma (Fig. 5d). All samples 
are from pediatric patients, with a median age of 4.5 y.o. This cluster is characterized by an overexpression of *BCOR* (:abbr:`medLogFC (median log-fold change)= 4.38, 
:abbr:`FDR (False Discovery Rate)` ≤ 2.94e-41) (Fig. :ref:`CNS3c <fig-cns3>`). 

BCOR participates in a range of chromatin altering activities including binding to histone acetylases and chromatin-altering complexes, 
namely polycomb group complexe [Gearhart2006]_. Alterations of these genes, many of which consist of fusions or internal tandem duplications 
(ITD) (Fig. :ref:`CNS3b <fig-cns3>`), have been well characterized in both soft tissue tumors and a recently defined group of CNS neoplasms:  high-grade 
neuroepithelial tumors of the central nervous system (CNS HGNET-BCOR) [Sturm2016]_. Gene set enrichment analyses revealed significant 
upregulation of both WNT (:abbr:`medNES median Normalized Enrichment Score)` ≥ 1.35, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.83e-09, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Liberzon2015]_ and SHH 
(:abbr:`medNES median Normalized Enrichment Score)` ≥ 1.51, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.16e-09, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) pathways [Nishimura2001]_, as well as basal cell carcinoma pathways 
(:abbr:`medNES median Normalized Enrichment Score)` ≥ 1.70, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.84e-20, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Kanehisa2000]_ in line with what is reported in literature. 
We also observe significant overexpression of *NTRK3* (:abbr:`medLogFC (median log-fold change)` = 2.45, :abbr:`FDR (False Discovery Rate)` ≤ 1.7e-16), but not *NTRK2* (:abbr:`FDR (False Discovery Rate)` ≤ 5.847e-01) and *NTRK1* (:abbr:`FDR (False Discovery Rate)` ≤ 9.063e-01) 
in :abbr:`T031 (Central nervous system with BCOR alterations, primitive neuroectodermal tumors)` vs. :abbr:`T030(Glioma, IDH wild-type)` and :abbr:`T032(Ependymoma)`, as commonly described in BCOR-ITD sarcomas [Kao2018]_, [Kao2020]_. 
Finally, :abbr:`T032 EPDY (Ependymoma)` (n = 30) is comprised almost exclusively of ependymomas. It is the cluster with the youngest patients, with a median age 
of 2.64 y.o. No subtypes are identified, possibly due to the limits in the reference dataset population.

.. figure:: /img/cns3.png
   :alt: Fig. CNS3
   :name: fig-cns3
   :width: 600px

   CNS3: Summary of the findings relating to BCOR-mutated and CIC-mutated tumors. 
   A) 2-dimensional UMAP projection of CNS tumors by gene expression, where a few representative classes are shown with shades of blue and green. 
   The BCOR-mutated class is highlighted in orange (T031). B) Diagram representing the archetypical BCOR-ITD and BCOR-CCNB3 rearrangements. 
   C) BCOR expression distribution across representative CNS classes, showing a clear overexpression in BCOR-mutated samples (T031).  
   D) The idiosyncratic transcriptional profile of BCOR mutations is sufficient to overcome the cell-of-origin attraction during the clustering process. 
   The ratio of tumor types within T031, shows that while it is mostly composed of CNS tumors, sarcomas are also found in this class.  

IDH wild-type glioma
====================

At the next level, we observe the separation between a small pediatric cluster :abbr:`T033 GLI LG PED (Glioma, low-grade, pediatric)` (n = 63) 
and a much larger adult class :abbr:`T034 GLI HG (Glioma high-grade)` (n=301) (Fig. :ref:`CNS1 <fig-cns1>`). Both contain mixed diagnoses but with a 
strong majority of samples labelled as gliomas. There’s a significant difference in age, with :abbr:`T033 (Glioma, low-grade, pediatric)` having a 
population with a median age of only 9.00 y.o. versus :abbr:`T034 (Glioma high-grade)` with 56.00 y.o. (:abbr:`MWU p-val (Mann-Whitney U test p-value)` = 4.00e-20). 
:abbr:`T034 (Glioma high-grade)` is characterized 
by significant upregulation of *HOX* genes (36/39 :abbr:`FDR (False Discovery Rate)` < 0.05), particularly *HOXD9* (:abbr:`logFC (log-Fold Change)` = -5.03, :abbr:`FDR (False Discovery Rate)` = 1.20e-23) and HOXA5 
(:abbr:`logFC (log-Fold Change)` = -6.18, :abbr:`FDR (False Discovery Rate)` = 2.40e-29)  [Tabuse2011]_, [Cimino2018]_ which have been associated with cancer cell survival 
and proliferation in gliomas. Together with overexpression of *VEGFA* [Xu2017]_ (:abbr:`logFC (log-Fold Change)` = -1.04, :abbr:`FDR (False Discovery Rate)` = 2.15e-05), 
a marker of poor survival, and glioma stemness genes *TERT* and *EGFR* (:abbr:`FDR (False Discovery Rate)` ≤ 1.00e-28) [Beck2011]_, this profile suggests :abbr:`T034 (Glioma high-grade)` to be a class of 
high-grade gliomas and glioblastoma multiforme, while :abbr:`T033 (Glioma, low-grade, pediatric)` to be a largely pediatric, low-grade glioma class, though all samples 
from the TCGA are astrocytomas (6/6 vs 50/232, :abbr:`χ2 p-val (χ2 test p-value)` = 6.74e-05). This is supported by :abbr:`T033 (Glioma, low-grade, pediatric)` being enriched for grade II (3/6 vs 10/232, 
:abbr:`χ2 p-val (χ2 test p-value)` = 7.73e-05) samples, with :abbr:`T034 (Glioma high-grade)` being enriched for grade IV samples (0/6 vs 155/232, :abbr:`χ2 p-val (χ2 test p-value)` = 3.11e-03).  However, we are unable 
to confirm differences in survival due to a lack of clinical annotation of samples in :abbr:`T033 (Glioma, low-grade, pediatric)`. 

The glioma subtypes run much deeper along complex hierarchical paths. At the next level, :abbr:`T034 (Glioma high-grade)` splits into :abbr:`T035 GLI HG LOH c7/10 (Glioma, high-grade, Chr7 gain and Chr10 loss)`  (n =236) 
and :abbr:`T036 GLI HG PRON (Glioma, high-grade, proneural subtype)`  (N = 65) (Fig. :ref:`CNS4 <fig-cns4>`). Both are mixed glioma and glioblastoma groups. We also observe a significant difference in age 
(median 58.00 vs 35.00 y.o. :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 8.76e-06) and pediatric composition (13.56% vs 50.77%, :abbr:`χ2 p-val (χ2 test p-value)` = 3.27e-10). 
There is no difference in overall survival between the groups (:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 8.23e-02 at 6423 days) [Ceccarelli2016]_. 
:abbr:`T035 (Glioma, high-grade, Chr7 gain and Chr10 loss)` contains almost all samples of the classical (85/185 vs. 1/29, :abbr:`χ2 p-val (χ2 test p-value)` = 3.527e-05) and mesenchymal (87/185 vs. 3/29, :abbr:`χ2 p-val (χ2 test p-value)` = 4.343e-04)
expression subtypes, while :abbr:`T036 (Glioma, high-grade, proneural subtype)` is almost wholly composed of the proneural subtypes (2/185 vs. 24/29, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16); 
although the majority of neural type samples are also found in :abbr:`T035 (Glioma, high-grade, Chr7 gain and Chr10 loss)`, the difference is not significant (11/185 vs. 1/29, 
:abbr:`χ2 p-val (χ2 test p-value)` = 0.9128) [Ceccarelli2016]_, [Brennan2013]_. :abbr:`T035 (Glioma, high-grade, Chr7 gain and Chr10 loss)` shows significant overexpression of *SAA1* (:abbr:`logFC (log-Fold Change)` = 4.84, 
:abbr:`FDR (False Discovery Rate)` = 2.869e-16), *MEOX2* (:abbr:`logFC (log-Fold Change)` = 4.79, :abbr:`FDR (False Discovery Rate)` = 8.46e-22), *CHI3L1* (:abbr:`logFC (log-Fold Change)` = 3.5, 
:abbr:`FDR (False Discovery Rate)` = 6.93e-20), *S100A4* (:abbr:`logFC (log-Fold Change)` = 2.04, :abbr:`FDR (False Discovery Rate)` = 1.26e-18) 
and *ANXA1* (:abbr:`logFC (log-Fold Change)` = 2.68, :abbr:`FDR (False Discovery Rate)` = 1.18e-37), all associated with poor survival [Tachon2019]_, [Xu2017]_ ,and has a considerably 
higher leukocyte content than :abbr:`T036 (Glioma, high-grade, proneural subtype)` (0.190 vs. 0.059, :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 1.42e-08) [Thorsson2018]_. In turn, :abbr:`T036 (Glioma, high-grade, proneural subtype)` samples overexpress 
*PDGFRA* (:abbr:`logFC (log-Fold Change)` = -2.8, :abbr:`FDR (False Discovery Rate)` = 3.80e-34), a marker of the proneuronal expression type(Brennan2013). :abbr:`T035 (Glioma, high-grade, Chr7 gain and Chr10 loss)` contains more *TP53* 
mutants (:abbr:`χ2 p-val (χ2 test p-value)` =2.11-02), and is also enriched for genesets concerning loss of heterozygosity (LOH) of regions implicated in 
gliomagenesis (:abbr:`medNES (median Normalized Enrichment Score)` = 1.32, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.15e-06) [Roversi2006]_, suggesting it contains samples with gain of 
chromosome 7 and loss of chromosome 10. This is further supported by its overexpression of *EGFR* (:abbr:`logFC (log-Fold Change)` = 3.47, :abbr:`FDR (False Discovery Rate)` = 1.18e-18) 
and is in line with literature, in which classical :abbr:`GBM (Glioblastoma)` samples tend to harbour these lesions. Indeed, :abbr:`T035 (Glioma, high-grade, Chr7 gain and Chr10 loss)` is highly enriched for 
tumors with gain chr7/loss chr10, confirmed by clinical data (139/200 vs. 15/35, :abbr:`χ2 p-val (χ2 test p-value)` = 4.146e-03) [Ceccarelli2016]_. 
:abbr:`T036 (Glioma, high-grade, proneural subtype)` contains a greater proportion of *ATRX*-mutant tumors (9/194 vs. 10/24, :abbr:`χ2 p-val (χ2 test p-value)` = 7.31e-06) [Ceccarelli2016]_.


.. figure:: /img/cns4.png
   :alt: Fig. CNS4
   :name: fig-cns4
   :width: 400px
   
   CNS4: 2-dimensional UMAP projection of subtypes of IDH-mutant gliomas. 
   Samples with reported gain of chromosome 7 and loss of chromosome 10 are shown as empty circles.


Glioblastomas and high-grade gliomas separate at the next level within :abbr:`T036 (Glioma, high-grade, proneural subtype)` (Fig. :ref:`CNS1 <fig-cns1>`). We observe :abbr:`T042 GLI HG/GBM PRON (Glioma, high-grade, or glioblastoma, proneural subtype)`  (n = 48) 
carrying glioblastomas mostly of the proneuronal subtype and :abbr:`T043 GLI HG PED H3.3mut (Glioma, high-grade, pediatric, H3.3 mutant)` (n =19) with the rest of the samples, primarily 
marked as high-grade gliomas from St. Jude’s (:abbr:`χ2 p-val (χ2 test p-value)` = 8.75e-14) (Fig. :ref:`CNS1 <fig-cns1>`). The two classes also differ significantly in age, 
with :abbr:`T042 (Glioma, high-grade, or glioblastoma, proneural subtype)` having patients with a median age of 44.5 y.o. while :abbr:`T043 (Glioma, high-grade, pediatric, H3.3 mutant)` 
has a median age of 5.85 y.o. (:abbr:`MWU p-val (Mann-Whitney U test p-value)` 3.88e-05). In fact, :abbr:`T043 (Glioma, high-grade, pediatric, H3.3 mutant)` 
is the cluster with the youngest group of patients within the entire cohort of both gliomas and gliobastomas and is one of only two 
clusters with >90% pediatric composition, the other being :abbr:`T033 GLI LG PED (Glioma, low-grade, pediatric)`. Given that it’s a majority pediatric cluster whose parent 
cluster demonstrates very poor survival, :abbr:`T043 (Glioma, high-grade, pediatric, H3.3 mutant)` may represent H3.3 (*H3F3A*) mutated tumors. Support for this hypothesis comes from 
enrichment of gene sets involving H3.3 mutation (here nominally K27M) between :abbr:`T043 (Glioma, high-grade, pediatric, H3.3 mutant)` and :abbr:`T042 (Glioma, high-grade, or glioblastoma, proneural subtype)` 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.73, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 3.39e-02) (Fig. :ref:`CNS5 <fig-cns5>`) [Larson2019]_. 
Notch signalling (:abbr:`medNES (median Normalized Enrichment Score)` = 1.05, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.31e-02) and neural differentiation 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.04, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` =6.10e-03) [Schaefer2009]_. 
genesets are also enriched in :abbr:`T043 (Glioma, high-grade, pediatric, H3.3 mutant)` and are a feature of these tumors. [Paugh2011]_, [Chen2020]_ Going back up along the hierarchy, 
:abbr:`T035 GLI HG LOH c7/10 (Glioma, high-grade, Chr7 gain and Chr10 loss)`  also splits in two (Fig. :ref:`CNS1 <fig-cns1>`), with :abbr:`T037 GLI HG NEUR DIFFhigh (Glioma, high-grade, neural differentiation)`  (n = 93) being comprised of gliomas and glioblastomas of 
the classical (49/68 vs. 36/117, :abbr:`χ2 p-val (χ2 test p-value)` = 1.29e-07) and neural subtypes (8/68 vs. 3/117, :abbr:`χ2 p-val (χ2 test p-value)` = 2.58e-02) and :abbr:`T038 GLI HG/GBM MES/CLASS (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)`  (n = 143) 
carrying a mixture of glioblastomas multiforme subtypes. :abbr:`T037 (Glioma, high-grade, neural differentiation)` is composed of a majority of astrocytomas (34/78 vs. 10/118), :abbr:`χ2 p-val (χ2 test p-value)` = 3.13e-08) 
while :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)` contains a majority of glioblastomas (31/78 vs. 100/118, :abbr:`χ2 p-val (χ2 test p-value)` = 9.30e-11). 
Interestingly, while almost all of the gliomas in :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)` 
are marked as IDH1 wild type, a handful of samples are IDH1-mutant (0/84 vs. 10/114, :abbr:`χ2 p-val (χ2 test p-value)` = 1.40e-2), suggesting these may be passenger rather 
than driver mutations. :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)` also has significantly higher leukocyte fraction (0.178 vs. 0.248, :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 1.77e-02). There are no differences in 
proportion of gain chr7/loss chr10 samples (:abbr:`χ2 p-val (χ2 test p-value)` = 3.80e-01).

.. figure:: /img/cns5.png
   :alt: Fig. CNS5
   :name: fig-cns5
   :width: 500px
   
   CNS5: Per sample Normalized Enrichment Score (NES) distributions of gene sets characterizing the H3.3-mutant glioma subtype.

The remaining subtypes are found in the child classes of :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)` (Fig. :ref:`CNS1 <fig-cns1>`): we find the majority of classical samples (31/34 vs 2/27, vs 1/43, 
:abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) in :abbr:`T039 GLI HG/GBM CLASS (Glioma, high-grade, or glioblastoma, classical subtype)`  (n = 37), mesenchymal subtype samples in both :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)` GLI HG/GBM MES (n = 36) and 
:abbr:`T041 GLI HG/GBM NEUR (Glioma, high-grade, or glioblastoma, neural subtype)` (n=57) (3/34 vs. 24/27 vs. 38/43, :abbr:`χ2 p-val (χ2 test p-value)` = 3.28e-14). :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)` contains two concurrent *PIK3CA* and 
*NF1*-mutated samples (:abbr:`χ2 p-val (χ2 test p-value)` = 2.73e-02), *NF1* mutations are typical of mesenchymal :abbr:`GBM (Glioblastoma)` [Fadhlullah2019]_. :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)` inherits all 
*IDH1*-mutants (0/34 vs. 0/26 vs. 10/42, :abbr:`χ2 p-val (χ2 test p-value)`  = 3.64e-04) and is enriched for *TP53* mutants (0/5 vs. 0/5 vs 5/6, :abbr:`χ2 p-val (χ2 test p-value)` = 1.38e-2). 
Patients at :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)` have the best overall survival, reaching median :abbr:`OS (Overall Survival)` at 375 days post diagnosis, while those in :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)` have the worst, 
reaching median :abbr:`OS (Overall Survival)` at 225 days (:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 3.44e-02 at 2549 days). These clusters differ in their share of *TERT* promoter mutations and 
*ATRX* mutations when available, respectively, with :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)` and :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)` comprised of samples with *TERT* promoter mutants (8/8 vs. 9/9 vs. 4/9, :abbr:`χ2 p-val (χ2 test p-value)` = 2.89e-03)
while :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)` contains all *ATRX*-mutants (0/33 vs. 0/25 vs. 7/40, :abbr:`χ2 p-val (χ2 test p-value)` = 4.23e-03). Examination of telomere maintenance pathways reveals samples
with relevant data in :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)` to be driven more by *ATRX* mutations (0/8 vs. 0/8, 4/5, :abbr:`χ2 p-val (χ2 test p-value)` =1.4513-02) while its siblings are wholly driven by 
*TERT* mutations (8/8, 8/8, 4/5, :abbr:`χ2 p-val (χ2 test p-value)` = 3.87e-03). Analysis of gene sets for relevant pathways shows :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)` to be enriched for mesenchymal 
:abbr:`GBM (Glioblastoma)` over its siblings (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.27, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 8.91e-14, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1e-04), 
while :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)` is enriched for neural 
:abbr:`GBM (Glioblastoma)` (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.38, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.59e-14, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1e-04), 
suggesting this subtype has a more neural than mesenchymal identity. 
This is further supported by :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)`’s inheritance of the majority of neural (0/34 vs. 1/27 vs. 2/43, :abbr:`χ2 p-val (χ2 test p-value)` = 4.60e-01) and proneural samples 
(0/34 vs. 0/27 vs. 2/43, :abbr:`χ2 p-val (χ2 test p-value)` = 2.35e-01), though neither reach significance. 

While it is surprising to see two unrelated clusters of glioblastomas containing large populations of classical expression subtype glioblastomas, 
:abbr:`T037 (Glioma, high-grade, neural differentiation)` and :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)`, closer examination reveals :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)` to represent a bona fide classical :abbr:`GBM (Glioblastoma)` subtype, supported by significant enrichment of classical 
glioblastoma gene signatures (:abbr:`medNES (median Normalized Enrichment Score)`  1.15, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 1.61e-08), and by its higher proportion of classical samples 
(31/34 vs. 49/68, :abbr:`FET p-val (Fisher Exact Test p-value)` = 3.94e-02) (Fig. :ref:`CNS6 <fig-cns6>`). :abbr:`T037 (Glioma, high-grade, neural differentiation)` is instead enriched for neural (:abbr:`medNES (median Normalized Enrichment Score)` = 1.79, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 1.87e-13) 
and proneural signatures (:abbr:`medNES (median Normalized Enrichment Score)` = 1.15, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 8.81e-05) over :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)` (Fig. :ref:`CNS6 <fig-cns6>`). Furthermore, the presence of a sizeable 
astrocytoma/glioma component in :abbr:`T037 (Glioma, high-grade, neural differentiation)` suggests it may represent a more “mixed” phenotype of glioma than its sibling :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)`, whose 
children separate into histotype-specific component clusters of :abbr:`GBM (Glioblastoma)`. Indeed, :abbr:`T037 (Glioma, high-grade, neural differentiation)` is enriched for neural and proneural signatures against 
all children of :abbr:`T038 (Glioma, high-grade, or glioblastoma, mesenchymal or classical subtype)` (:abbr:`medNES (median Normalized Enrichment Score)` ≤ 1.04, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 4.07e-16) (Fig. :ref:`CNS6 <fig-cns6>`). 
We hypothesize :abbr:`T037 (Glioma, high-grade, neural differentiation)` represents a more neurally differentiated 
class, transcending canonical subtyping. This is further supported by enrichment of genes pertaining to neural development (:abbr:`medNES (median Normalized Enrichment Score)` = 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.01e-14, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05) and differentiation (:abbr:`medNES (median Normalized Enrichment Score)` = 1.11, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.24e-12, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.001) [TGOC2019]_, [Ashburner2000]_ 
in :abbr:`T037 (Glioma, high-grade, neural differentiation)` with respect to :abbr:`T039 (Glioma, high-grade, or glioblastoma, classical subtype)`, :abbr:`T040 (Glioma, high-grade, or glioblastoma, mesenchymal subtype)`, and :abbr:`T041 (Glioma, high-grade, or glioblastoma, neural subtype)` (Fig. :ref:`CNS6 <fig-cns6>`). 

.. figure:: /img/cns6.png
   :alt: Fig. CNS6
   :name: fig-cns6
   :width: 800px
   
   CNS6: Per sample Normalized Enrichment Score (NES) distributions of gene sets characterizing gliomas with high neural differentiation.

IDH-mutant glioma
=================

Along the alternative branch hosting IDH-mutant gliomas (:abbr:`T029 (Central nervous system tumors, IDH-mutant)`) we find that the hemizygous codeletion of chromosome arms 
1p and 19q is a major driver in the separation of classes: we find samples with codeletion in :abbr:`T044 GLI IHDmut CODEL Glioblastoma, IDH-mutant 1p19q codeletion)` (n = 270) 
and samples without codeletion in :abbr:`T045 GLI IDHmut noCODEL (Glioblastoma, IDH-mutant without 1p19q codeletion)` (n = 218) (168/ 221 vs. 1/213, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) (Fig. :ref:`CNS1 <fig-cns1>`, c). 
Though :abbr:`T044 (Glioblastoma, IDH-mutant 1p19q codeletion)` has significantly older patients (median age 40 vs. 36 y.o. :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 2.56e-03), it has a slightly larger pediatric 
population (28.14% vs. 25.69%). According to the clinical information from TGCA, :abbr:`T044 (Glioblastoma, IDH-mutant 1p19q codeletion)` contains significantly more tumors with *TERT* 
promoter mutations (89/125 vs. 6/124, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16), while :abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)` is enriched for *ATRX* mutants (23/ 221 vs. 155/211, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16). 
:abbr:`T044 (Glioblastoma, IDH-mutant 1p19q codeletion)` contains a majority of oligodendrogliomas (134/198 vs. 28/183, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) while :abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)` contains a majority of astrocytomas 
(17/198 vs. 97/183, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16). However, despite differences in codeletion status, we find no difference in overall survival 
between the two groups (:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 3.78e-01 at 5546 days).
Following along :abbr:`T044 (Glioblastoma, IDH-mutant 1p19q codeletion)`, we observe the singling out of a small set of low-grade gliomas (n = 12/30 vs 4/240, :abbr:`χ2 p-val (χ2 test p-value)` = 1.54e-15) and 
dysembryoplastic neuroepithelial tumors (DNET) (10/30 vs. 2/240, :abbr:`χ2 p-val (χ2 test p-value)` = 1.67e-14) in :abbr:`T046 GLI LG IDHmut CODEL/DNET (Glioma, IDH-mutant, 1p19q codeletion or dysembryoplastic neuroepithelial tumors)`  (n = 30) 
from the rest of the gliomas in :abbr:`T047 GLI IHDmut CODEL A (Glioblastoma, IDH-mutant 1p19q codeletion mix A)`  (n = 240). There is a significant age disparity between the two clusters 
(14.11 vs. 41 y.o., :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 9.61e-11) as the former class is made up entirely of pediatric samples.
:abbr:`T047 (Glioblastoma, IDH-mutant 1p19q codeletion mix A)` further split by age and histotype. :abbr:`T048  GLI IHDmut MULTICELL NET (Glioma, IDH-mutant, multicellular network)` (n = 67) has significantly younger patients than :abbr:`T049 GLI IHDmut CODEL B (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` (n = 173) 
(median 35.00 vs 44.00 y.o. :abbr:`MWU p-val (Mann-Whitney U test p-value)` = 2.26e-03) due to its larger pediatric component (38.80% vs. 11.56%, :abbr:`χ2 p-val (χ2 test p-value)` = 3.70e-06). There is no 
difference in overall survial (:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 6.23e-02 at 5546 days). While :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` contains more astrocytomas (13/48 vs 4/150, :abbr:`χ2 p-val (χ2 test p-value)` = 7.06e-07), 
:abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` has a considerably higher oligodendroglioma population (20/48 vs 114/150, :abbr:`χ2 p-val (χ2 test p-value)` = 2.14e-05). According to TCGA data, :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` is enriched for 
*EGFR* (3/33 vs. 0/87, :abbr:`χ2 p-val (χ2 test p-value)`  = 2.83e-02), *ATRX* (12/33 vs. 6/87, :abbr:`χ2 p-val (χ2 test p-value)` = 1.77e-04) and *TP53*-mutant tumors (13/33 vs. 7/87, :abbr:`χ2 p-val (χ2 test p-value)` = 1.23e-04), 
while :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` contains more *CIC* (:abbr:`χ2 p-val (χ2 test p-value)` = 1/33 vs. 48/87, 6.33e-07), *FUBP1* (1/33 vs. 22/87, :abbr:`χ2 p-val (χ2 test p-value)` = 1.22e-02) and *NOTCH1* (0/33 vs. 19/87, :abbr:`χ2 p-val (χ2 test p-value)` = 8.14e-03) 
mutants (Fig. :ref:`CNS7 <fig-cns7>`). Most tumors in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` are neural (46/49 vs. 38/144, :abbr:`χ2 p-val (χ2 test p-value)` = 7.39e-16), while the majority of those in :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` are proneural 
(2/49 vs. 105/144, :abbr:`χ2 p-val (χ2 test p-value)` = 2.26e-16). Most importantly, and quite unexpectedly, :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` is mostly composed of IDH1 wild-type (16/53) and non-codeleted 
samples (45/53). It is not clear why this class is found within the IDH1-codeleted branch. 

.. figure:: /img/cns7.png
   :alt: Fig. CNS7
   :name: fig-cns7
   :width: 800px
   
   CNS7: Top and center, per sample Normalized Enrichment Score (NES) distributions of gene sets characterizing the gliomas subtype with multicellular network overexpression.
   Bottom, per sample expression distributions of *NOTCH1* and *GAP43* genes in gliomas subtypes with or without multicellular network overexpression. 

Gene set enrichment analysis reveals that every locus available for chr1p, with the expectation of chr1p11, (:abbr:`MWU p-val (Mann-Whitney U test p-value)` ≤ 8.35e-04) and chr19q 
(:abbr:`MWU p-val (Mann-Whitney U test p-value)` ≤ 5.18e-23) are significantly downregulated in :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` compared to :abbr:`T048 (Glioma, IDH-mutant, multicellular network)`, confirming more severe population-wide loss of these loci in 
:abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` vs. :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` and supporting that, true to their annotation, the majority of samples in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` have normal expression of these loci, in spite of 
their transcriptional similarities with the codeleted branch. The overall expression profile of both IDH wild type and non-codeleted tumors within 
:abbr:`T048 (Glioma, IDH-mutant, multicellular network)` have a high correlation with true chr1p/19q co-deleted IDHmut gliomas within :abbr:`T044 (Glioblastoma, IDH-mutant 1p19q codeletion)` (R ≥ 0.802, Pearson correlation p-val < 2.20e-16). 
Further examination of gene sets upregulated in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` compared to its sibling class :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)`, its uncle class :abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)` GLI IDHmut noCODEL, and its cousin 
class :abbr:`T030 GLI IDHwt (Glioma, IDH wild-type)` revealed significant upregulation of genesets related to neuron-neuron synaptic transmission (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.35e-89, 
:abbr:`medNES (median Normalized Enrichment Score)` = 1.13, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)`-val < 1.00e-04), synaptic plasticity (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.23e-85, :abbr:`medNES (median Normalized Enrichment Score)` = 1.30, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)`-val < 1.00e-04), 
neurite formation (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.45e-51, :abbr:`medNES (median Normalized Enrichment Score)` = 1.15, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Jassal2020]_, and microtubule polymerization 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.59e-63, :abbr:`medNES (median Normalized Enrichment Score)` = 1.10, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)`-val < 1.00e-04) (Fig. :ref:`CNS7 <fig-cns7>`). We also observe upregulation of glutaminergic signalling (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.06e-102, 
:abbr:`medNES (median Normalized Enrichment Score)` = 1.31, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)`< 1.00e-04), particularly of AMPA cationic channel activity (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 9.08e-59, :abbr:`medNES (median Normalized Enrichment Score)` = 1.43, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04), 
including AMPA-dependent synaptic plasticity (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.36-84, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04), and of extracellular calcium export (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.61e-93, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04, :abbr:`medNES (median Normalized Enrichment Score)` = 1.14) [Venkataramani2019]_, [Venkatesh2019]_, [Jassal2020]_ (Fig. :ref:`CNS7 <fig-cns7>`). 
We also observe increases in gap junction formation (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.81e-35, :abbr:`medNES (median Normalized Enrichment Score)` = 2.39, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) and connexin binding 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.61e-28, :abbr:`medNES (median Normalized Enrichment Score)` = 1.26, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) (Fig. :ref:`CNS7 <fig-cns7>`). 
Taken together, these results suggest :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` to be composed of gliomas of a recently described multicellular network phenotype, a pro-invasive and 
radioresistant resistant mode of glioma growth [Osswald2015]_. Gene expression analysis reveals significant upregulation of *GAP34* in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` 
vs. other IDH1-mutant tumor groups (:abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)` and :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)`) (:abbr:`medLogFC (median Log-fold Change)` = 1.33, :abbr:`FDR (False Discovery Rate)` ≤ 1.80e-13), the principal gap-junction protein mediating this 
phenotype [Osswald2015]_, as well as *NOTCH1* underexpression (:abbr:`medLogFC (median Log-fold Change)`= -1.16, :abbr:`FDR (False Discovery Rate)` ≤ 1.950e-06) and downregulation of *NOTCH1* signalling 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.65e-45, :abbr:`medNES (median Normalized Enrichment Score)` = 0.92, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)`-val < 0.05) [Jassal2020]_ over all other glioma types, the crucial determinant of this phenotype [Jung2021]_ (Fig. :ref:`CNS7 <fig-cns7>`). 
This is despite the lack of *NOTCH1*-mutant samples in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)`; :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` contains the majority NOTCH1 mutants of the glioma cohort (vs. :abbr:`T048 (Glioma, IDH-mutant, multicellular network)`, :abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)`, and T030, 0/33 vs. 19/87 vs. 4/113 vs. 0/52, :abbr:`χ2 p-val (χ2 test p-value)` = 2.29e-07) 
and exhibits the highest *NOTCH1* expression (:abbr:`medLogFC (median Log-fold Change)`= 0.83, :abbr:`FDR (False Discovery Rate)` ≤ 2.961e-02), so we speculate these NOTCH1 mutations to be gain-of-function. However, despite this phenotype displaying radioresistance, samples in :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` show no significant differences in overall survival compared to other IDH-mutated glioma groups (:abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)` and :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)`) at 6423 days.
We speculate this novel phenotype may have good transcriptional affinity with chr1p/19q codeletion, in spite of the lack of apparent lesions 
in the region.
Though this phenotype is mostly associated with astrocytomas [Osswald2015]_,  :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` is a mixed cluster – containing large amounts of both 
astrocytomas and oligodendrogliomas. :abbr:`T048 (Glioma, IDH-mutant, multicellular network)` then splits in two classes (Fig. :ref:`CNS1 <fig-cns1>`), with different histological populations; 
:abbr:`T050 GLI IDHmut MULTICELL NET OLIGOD (Glioma, IDH-mutant, multicellular network, oligodendroglioma)`  (n = 31) contains more oligodendrogliomas (15/22 vs. 5/26, :abbr:`χ2 p-val (χ2 test p-value)` = 1.73-3) than :abbr:`T051 GLI IDHmut MULTICELL NET ASTROC (Glioma, IDH-mutant, multicellular network, astrocytoma)`  (n = 36), 
which instead is populated by astrocytomas (0/22 vs. 13/26, :abbr:`χ2 p-val (χ2 test p-value)` = 3.74e-04) [Davare2018]_, [Zhang2017]_. 
:abbr:`T050 (Glioma, IDH-mutant, multicellular network, oligodendroglioma)` also inherits the 
majority of chr1p/19q codelted samples (7/16 vs. 1/29, :abbr:`χ2 p-val (χ2 test p-value)` = 1.91e-02).
Similarly, :abbr:`T049 (Glioblastoma, IDH-mutant 1p19q codeletion mix B)` splits by histological composition (Fig. :ref:`CNS1 <fig-cns1>`) with :abbr:`T052 GLI IHDmut CODEL NOTCH1 (Glioblastoma, IDH-mutant 1p19q codeletion NOTCH1 mutant)` (n = 89) being enriched (68/81 vs. 46/69, 
:abbr:`χ2 p-val (χ2 test p-value)` = 2.27e-02) for oligodendrogliomas and :abbr:`T053 GLI IHDmut CODEL OLIGOAST (Glioblastoma, IDH-mutant 1p19q codeletion oligoastrocytomat)` (n = 84) for oligoastrocytomas (11/81 vs. 21/69, :abbr:`χ2 p-val (χ2 test p-value)` = 2.08e-02). 
:abbr:`T052 (Glioblastoma, IDH-mutant 1p19q codeletion NOTCH1 mutant)` also has a significantly higher population of *NOTCH1* mutant samples (17/56 vs. 2/39, :abbr:`χ2 p-val (χ2 test p-value)` = 2.07e-02). :abbr:`T051 (Glioma, IDH-mutant, multicellular network, astrocytoma)` contains a larger share of 
neural gliomas (30/78 vs. 8/66, :abbr:`χ2 p-val (χ2 test p-value)` = 7.154e-04), while :abbr:`T052 (Glioblastoma, IDH-mutant 1p19q codeletion NOTCH1 mutant)` contains more proneural gliomas (48/78 vs. 57/66, :abbr:`χ2 p-val (χ2 test p-value)` = 1.623-03).
Finally, following along the non-codeleted branch defined by :abbr:`T045 (Glioblastoma, IDH-mutant without 1p19q codeletion)`, we observe four children classes, characterized by significant differences in 
the sex ratios (Fig. :ref:`CNS1 <fig-cns1>`): :abbr:`T054 GLI IDHmut noCODEL OLIGOC (Glioblastoma, IDH-mutant without 1p19q codeletion oligodendrocytes)`  (n = 99) is composed by 63.64% of males, 
:abbr:`T055 GLI IDHmut noCODEL NEUR DIFFhigh (Glioma, IDH-mutant, no codeletion, neural development)`  (n = 30) 
is entirely female (:abbr:`χ2 p-val (χ2 test p-value)` = 2.65e-17), :abbr:`T056 GLI IDHmut noCODEL MES (Glioma, IDH-mutant, no codeletion, mesenchymal)`  (n = 24) is 75.00% male and :abbr:`T057 GLI IDHmut noCODEL H3demet (Glioma, IDH-mutant, no codeletion, H3 demethylation)` (n = 47) is almost 
exclusively male (97.87% :abbr:`χ2 p-val (χ2 test p-value)` = 2.65e-17). Although sex differences have previously been reported to be associated with differences in survival 
in glioma and :abbr:`GBM (Glioblastoma)` [Yang2019]_, patients in these clusters have no significant differences in overall survival (:abbr:`lrt p-val (Kaplan-Meier log rank test p-value)` = 1.44e-01 at 4752 days). 

Differential expression and gene sets analyses on these classes revelated that :abbr:`T054 (Glioblastoma, IDH-mutant without 1p19q codeletion oligodendrocytes)` is enriched for oligodendrocyte development 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.03, adj p-val = 4.85e-15) and myelination (:abbr:`medNES (median Normalized Enrichment Score)` = 1.23, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.97e-09, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.01) [TGOC2019]_, [Ashburner2000]_, 
and overexpresses *MBP* and *MOBP* (:abbr:`FDR (False Discovery Rate)` ≤ 2.461e-04), predictors of improved survival [Wang2019]_, [Kong2013]_. :abbr:`T055 (Glioma, IDH-mutant, no codeletion, neural development)` is enriched for gene sets related 
to neuronal development (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.01, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 9.36e-17). :abbr:`T056 (Glioma, IDH-mutant, no codeletion, mesenchymal)` is enriched for genesets involving *MYC* signalling (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 6.76e-03, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05), the G2M checkpoint,(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.16, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.46e-03, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.01), and the 
immune response (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.510, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 1.05e-05, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.01) [Liberzon2015]_; it also exhibits the highest immune infiltration 
score out of its siblings (median = 990 vs. 648 vs. 2185 vs. 977, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` ≤ 4.81e-05). It overexpresses MMP9 (:abbr:`medLogFC (median Log-fold Change)` = 1.41, :abbr:`FDR (False Discovery Rate)` ≤ 3.515e-02), 
*CHI3L1* (:abbr:`medLogFC (median Log-fold Change)` = 1.79, :abbr:`FDR (False Discovery Rate)` 8.332e-03), S100A4 (:abbr:`medLogFC (median Log-fold Change)`= 2.12, :abbr:`FDR (False Discovery Rate)` ≤ 4.281e-09), EN1 (:abbr:`medLogFC (median Log-fold Change)`= 5.01, :abbr:`FDR (False Discovery Rate)` ≤ 8.643e-14), and *ANXA1* 
(:abbr:`medLogFC (median Log-fold Change)`= 2.56, :abbr:`FDR (False Discovery Rate)` ≤ 7.266e-14), markers of poor prognosis, and *IGF2BP3* (:abbr:`medLogFC (median Log-fold Change)`= 4.06, :abbr:`FDR (False Discovery Rate)` ≤ 8.147e-13), a glioblastoma-specific proliferative and 
invasive marker. :abbr:`T056 (Glioma, IDH-mutant, no codeletion, mesenchymal)` is also the only cluster to contain a significant population of mesenchymal samples (0/58 vs. 0/21 vs. 5/11 vs. 2/ 35, :abbr:`χ2 p-val (χ2 test p-value)` = 3.211e-08) 
and is enriched for epithelial mesenchymal transition genesets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.15, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.46e-07, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05) [Liberzon2015]_.
:abbr:`T057 (Glioma, IDH-mutant, no codeletion, H3 demethylation)` is enriched for genesets involving *H3K4* demethylation (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.07, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 6.91e-11, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05) and *H3K27* demethylation 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.08, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 6.00e-03) [TGOC2019]_, [Ashburner2000]_. It also overexpresses *LDHC* (median LogFC= 3.44, 
:abbr:`FDR (False Discovery Rate)` ≤ 7.16e-06), which was found to be elevated in mesenchymal glioma stem cells and negatively correlates with survival [Mao2013]_, [Beckner2016]_.


Bibliography
============

.. [Ashburner2000] Ashburner, M., Ball, C.A., Blake, J.A.,2000. Gene Ontology: tool for the unification of biology. Nature Genetics 25(1), pp. 25–29.
.. [Beck2011] Beck, S., Jin, X., Sohn, Y.-W.,2011. Telomerase activity-independent function of TERT allows glioma cells to attain cancer stem cell characteristics by inducing EGFR expression. Molecules and Cells 31(1), pp. 9–15.
.. [Beckner2016] Beckner, M.E., Pollack, I.F., Nordberg, M.L. and Hamilton, R.L. 2016. Glioblastomas with copy number gains in EGFR and RNF139 show increased expressions of carbonic anhydrase genes transformed by ENO1. BBA clinical 5, pp. 1–15.
.. [Brennan2013] Brennan, C.W., Verhaak, R.G.W., McKenna, A.,2013. The somatic genomic landscape of glioblastoma. Cell 155(2), pp. 462–477.
.. [Ceccarelli2016] Ceccarelli, M., Barthel, F.P., Malta, T.M.,2016. Molecular profiling reveals biologically discrete subsets and pathways of progression in diffuse glioma. Cell 164(3), pp. 550–563.
.. [Chen2020] Chen, K.-Y., Bush, K., Klein, R.H.,2020. Reciprocal H3.3 gene editing identifies K27M and G34R mechanisms in pediatric glioma including NOTCH signaling. Communications Biology 3(1), p. 363.
.. [Cimino2018] Cimino, P.J., Kim, Y., Wu, H.-J.,2018. Increased HOXA5 expression provides a selective advantage for gain of whole chromosome 7 in IDH wild-type glioblastoma. Genes & Development 32(7–8), pp. 512–523.
.. [Davare2018] Davare, M.A., Henderson, J.J., Agarwal, A.,2018. Rare but recurrent ROS1 fusions resulting from chromosome 6q22 microdeletions are targetable oncogenes in glioma. Clinical Cancer Research 24(24), pp. 6471–6482.
.. [Fadhlullah2019] Fadhlullah, S.F.B., Halim, N.B.A., Yeo, J.Y.T.,2019. Pathogenic mutations in neurofibromin identifies a leucine-rich domain regulating glioma cell invasiveness. Oncogene 38(27), pp. 5367–5380.
.. [Gearhart2006] Gearhart, M.D., Corcoran, C.M., Wamstad, J.A. and Bardwell, V.J. 2006. Polycomb group and SCF ubiquitin ligases are found in a novel BCOR complex that is recruited to BCL6 targets. Molecular and Cellular Biology 26(18), pp. 6880–6889.
.. [Hänzelmann2013] Hänzelmann, S., Castelo, R. and Guinney, J. 2013. GSVA: gene set variation analysis for microarray and RNA-seq data. BMC Bioinformatics 14, p. 7.
.. [Hartmann2010] Hartmann, C., Hentschel, B., Wick, W.,2010. Patients with IDH1 wild type anaplastic astrocytomas exhibit worse prognosis than IDH1-mutated glioblastomas, and IDH1 mutation status accounts for the unfavorable prognostic effect of higher age: implications for classification of gliomas. Acta Neuropathologica 120(6), pp. 707–718.
.. [Hernández2010] Hernández, M., Martín, R., García-Cubillas, M.D., Maeso-Hernández, P. and Nieto, M.L. 2010. Secreted PLA2 induces proliferation in astrocytoma through the EGF receptor: another inflammation-cancer link. Neuro-oncology 12(10), pp. 1014–1023.
.. [Jassal2020] Jassal, B., Matthews, L., Viteri, G.,2020. The Reactome Pathway Knowledgebase. Nucleic Acids Research 48(D1), pp. D498–D503.
.. [Jung2021] Jung, E., Osswald, M., Ratliff, M.,2021. Tumor cell plasticity, heterogeneity, and resistance in crucial microenvironmental niches in glioma. Nature Communications 12(1), p. 1014.
.. [Kanehisa2000] Kanehisa, M. and Goto, S. 2000. KEGG: Kyoto encyclopedia of genes and genomes. Nucleic Acids Research 28(1), pp. 27–30.
.. [Kao2018] Kao, Y.-C., Owosho, A.A., Sung, Y.-S.,2018. BCOR-CCNB3 Fusion Positive Sarcomas: A Clinicopathologic and Molecular Analysis of 36 Cases With Comparison to Morphologic Spectrum and Clinical Behavior of Other Round Cell Sarcomas. The American Journal of Surgical Pathology 42(5), pp. 604–615.
.. [Kao2020] Kao, Y.-C., Sung, Y.-S., Argani, P.,2020. NTRK3 overexpression in undifferentiated sarcomas with YWHAE and BCOR genetic alterations. Modern Pathology 33(7), pp. 1341–1349.
.. [Kong2013] Kong, J., Cooper, L.A.D., Wang, F.,2013. Machine-based morphologic analysis of glioblastoma using whole-slide pathology images uncovers clinically relevant molecular correlates. Plos One 8(11), p. e81049.
.. [Larson2019] Larson, J.D., Kasper, L.H., Paugh, B.S.,2019. Histone H3.3 K27M accelerates spontaneous brainstem glioma and drives restricted changes in bivalent gene expression. Cancer Cell 35(1), p. 140–155.e7.
.. [Liberzon2015] Liberzon, A., Birger, C., Thorvaldsdóttir, H., Ghandi, M., Mesirov, J.P. and Tamayo, P. 2015. The Molecular Signatures Database (MSigDB) hallmark gene set collection. Cell Systems 1(6), pp. 417–425.
.. [Mao2013] Mao, P., Joshi, K., Li, J.,2013. Mesenchymal glioma stem cells are maintained by activated glycolytic metabolism involving aldehyde dehydrogenase 1A3. Proceedings of the National Academy of Sciences of the United States of America 110(21), pp. 8644–8649.
.. [Nishimura2001] Nishimura, D. 2001. BioCarta. Biotech Software & Internet Report 2(3), pp. 117–120.
.. [Northcott2012] Northcott, P.A., Dubuc, A.M., Pfister, S. and Taylor, M.D. 2012. Molecular subgroups of medulloblastoma. Expert Review of Neurotherapeutics 12(7), pp. 871–884.
.. [Osswald2015] Osswald, M., Jung, E., Sahm, F.,2015. Brain tumor cells interconnect to a functional and resistant network. Nature 528(7580), pp. 93–98.
.. [Park2016] Park, S.Y., Piao, Y., Jeong, K.J., Dong, J. and de Groot, J.F. 2016. Periostin (POSTN) regulates tumor resistance to antiangiogenic therapy in glioma models. Molecular Cancer Therapeutics 15(9), pp. 2187–2197.
.. [Paugh2011] Paugh, B.S., Broniscer, A., Qu, C.,2011. Genome-wide analyses identify recurrent amplifications of receptor tyrosine kinases and cell-cycle regulatory genes in diffuse intrinsic pontine glioma. Journal of Clinical Oncology 29(30), pp. 3999–4006.
.. [Roversi2006] Roversi, G., Pfundt, R., Moroni, R.F.,2006. Identification of novel genomic markers related to progression to glioblastoma through genomic profiling of 25 primary glioma cell lines. Oncogene 25(10), pp. 1571–1583.
.. [Schaefer2009] Schaefer, C.F., Anthony, K., Krupa, S.,2009. PID: the pathway interaction database. Nucleic Acids Research 37(Database issue), pp. D674-9.
.. [Steponaitis2016] Steponaitis, G., Skiriutė, D., Kazlauskas, A.,2016. High CHI3L1 expression is associated with glioma patient survival. Diagnostic Pathology 11, p. 42.
.. [Sturm2016] Sturm, D., Orr, B.A., Toprak, U.H.,2016. New Brain Tumor Entities Emerge from Molecular Classification of CNS-PNETs. Cell 164(5), pp. 1060–1072.
.. [Tabuse2011] Tabuse, M., Ohta, S., Ohashi, Y.,2011. Functional analysis of HOXD9 in human gliomas and glioma cancer stem cells. Molecular Cancer 10, p. 60.
.. [Tachon2019] Tachon, G., Masliantsev, K., Rivet, P.,2019. Prognostic significance of MEOX2 in gliomas. Modern Pathology 32(6), pp. 774–786.
.. [TGOC2019] The Gene Ontology Consortium 2019. The Gene Ontology Resource: 20 years and still GOing strong. Nucleic Acids Research 47(D1), pp. D330–D338.
.. [Thorsson2018] Thorsson, V., Gibbs, D.L., Brown, S.D.,2018. The immune landscape of cancer. Immunity 48(4), p. 812–830.e14.
.. [Venkataramani2019] Venkataramani, V., Tanev, D.I., Strahle, C.,2019. Glutamatergic synaptic input to glioma cells drives brain tumor progression. Nature 573(7775), pp. 532–538.
.. [Venkatesh2019] Venkatesh, H.S., Morishita, W., Geraghty, A.C.,2019. Electrical and synaptic integration of glioma into neural circuits. Nature 573(7775), pp. 539–545.
.. [Wang2019] Wang, S., Liu, F., Wang, Y.,2019. Integrated analysis of 34 microarray datasets reveals CBX3 as a diagnostic and prognostic biomarker in glioblastoma. Journal of Translational Medicine 17(1), p. 179.
.. [Xu2017] Xu, Yonggang, Wang, J., Xu, Yanbin, Xiao, H., Li, J. and Wang, Z. 2017. Screening critical genes associated with malignant glioma using bioinformatics analysis. Molecular medicine reports 16(5), pp. 6580–6589.
.. [Yang2019] Yang, W., Warrington, N.M., Taylor, S.J.,2019. Sex differences in GBM revealed by analysis of patient imaging, transcriptome, and survival data. Science Translational Medicine 11(473).
.. [Zhang2017] Zhang, X., Lv, Q.-L., Huang, Y.-T., Zhang, L.-H. and Zhou, H.-H. 2017. Akt/FoxM1 signaling pathway-mediated upregulation of MYBL2 promotes p