.. |br| raw:: html

  <br/>

===============================
T002 and T003 Mesodermal Tumour
===============================

Version: |version|
|br| 
Last change: |today|

We find that most sarcomas and other mesenchymal cancers, together with sarcomatoid solid tumours, are divided into two major families. 
Samples in :abbr:`T002 MESODM STEMlow (Mesodermal tumours, low stemness)` (n = 565) have lower stemness and higher immune infiltration, 
while :abbr:`T003 MESODM STEMhigh (Mesodermal tumours, high stemness)` (n = 483) have higher stemness and lower immune infiltration 
(Fig. :ref:`MESD1a, c <fig-mesd1>`)

.. figure:: /img/mesd1.png
   :alt: Fig. MESD1
   :name: fig-mesd1
   :width: 600px
   
   CNS1: A, 2-dimensional UMAP projection of Mesodermal tumors by gene expression. Subtypes at the second level of the hierarchy
   are shown with different shades of green if they belong to the parent class T002 MESODERM STEMlow), of orange
   if they stem from T003 MESODM STEMhigh. B, the list of all Mesodermal subtypes identified
   and their hierarchical relationship. C) 2-dimensional UMAP projection of the same group of tumours, with samples
   coloured according to our in-house stemness score (left), immune score (center) or age (right).

T002 Mesodermal tumour with low stemness
=========================================

:abbr:`T002 (Mesodermal tumours, low stemness)` splits into two clusters at the first level: 
:abbr:`T067 LMS (Leiomyosarcoma)` (n = 78), which contains most leiomyosarcomas (LMS) and 
:abbr:`T066 MESODM STEMlow A (Mesodermal tumours, low stemness, without samples from T067)` 
(n = 487), carrying the remaining malignancies (Fig. :ref:`MESD1b <fig-mesd1>`). 

Leiomyosarcoma
==============

:abbr:`T067 LMS (Leiomyosarcoma)` shows, as expected, overexpression of genes relating to smooth muscle development, including 
*ACTA2* (:abbr:`logFC (log-Fold Change)` = -4.29, :abbr:`FDR (False Discovery Rate)` = 6.853e-133), 
*ACTG2* (:abbr:`logFC (log-Fold Change)` = -7.92, :abbr:`FDR (False Discovery Rate)` = 2.126e-168), 
*DES* (:abbr:`logFC (log-Fold Change)` = -7.62, :abbr:`FDR (False Discovery Rate)` = 4.876e-121), 
and *MYOC* (:abbr:`logFC (log-Fold Change)` = -8.66, :abbr:`FDR (False Discovery Rate)` = 5.518e-154), 
with patients in this group exhibiting significantly better survival than samples in 
:abbr:`T066 MESODM STEMlow A (Mesodermal tumours, low stemness, without samples from T067)` 
(:abbr:`lrt p-val (log-rank test p-value)` = 2.92e-03 at 5840 days). 
It is then divided in three subclasses roughly defined by tumour location. 
:abbr:`T087 ULMS (Uterine leiomyosarcoma)` (n = 18) is composed of uterine :abbr:`LMS (leiomyosarcoma)` 
(n = 14, :abbr:`χ2 p-val (χ2 test p-value)` = 8.96e-11), :abbr:`T088 STLMS ABD (Soft tissue leiomyosarcoma of the abdomen and retroperitoneum)` 
(n = 23) is largely composed of abdominal and retroperitoneal soft tissue :abbr:`LMS (leiomyosarcoma)`  (n= 16, :abbr:`χ2 p-val (χ2 test p-value)` = 7.85e-05), 
while :abbr:`T089 STLMS EXT (Soft tissue leiomyosarcoma of the extremities)` 
(n = 29) contains a significant portion of :abbr:`LMS (Leiomyosarcoma)` of the extremities 
(n = 9, :abbr:`χ2 p-val (χ2 test p-value)` = 3.56e-04). 
Though there is no significant difference in overall survival between the groups 
(:abbr:`lrt p-val (log-rank test p-value)` = 1.32e-01 at 3765 days), :abbr:`T089 STLMS EXT (Soft tissue leiomyosarcoma of the extremities)` 
has a higher incidence of relapsed tumours (:abbr:`χ2 p-val (χ2 test p-value)` = 2.93e-02). 


Mesodermal tumour with low stemness not including Leiomyosarcoma
=================================================================

:abbr:`T066 MESODM STEMlow A (Mesoderm, low stemness, without samples from T067)` splits into three groups: 
osteosarcomas in :abbr:`T068 OSARC (Osteosarcoma)` (n = 131), a class of sarcoma containing mixed diagnoses in 
:abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` (n = 275), and mesotheliomas in 
:abbr:`T070 MPM (Malignant pleural mesothelioma)` (n = 81)  (Fig. :ref:`MESD1a, b <fig-mesd1>`). 
These clusters differ significantly in age (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.67e-33) 
in their proportion of paediatric patients (:abbr:`χ2 p-val (χ2 test p-value)` ≤ 4.49e-56); 
:abbr:`T068 OSARC (Osteosarcoma)` has the youngest patients (median age of 15 :abbr:`y.o. (years old)`) 
and is almost exclusively paediatric (96.18% of samples).
|br| 
At variance, mesotheliomas in :abbr:`T070 MPM (Malignant pleural mesothelioma)` are almost exclusively adult tumours, 
with patients' median age being 63 :abbr:`y.o. (years old)`, and significantly worse overall survival than the other two classes 
(:abbr:`lrt p-val (log-rank test p-value)` = 3.90e-11 at 5840 days). 
Finally, :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)`, the mixed sarcoma class, is in between, with patients’ median age being 60 
:abbr:`y.o. (years old)` and 23.63% pediatric patients.
Of note, within :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` we observe the surprising presence of a number of samples from diseases, 
such as osteosarcoma (n = 26) and :abbr:`LMS (leiomyosarcoma)` (n = 12), for which a type-specific cluster is available 
(See :abbr:`T068 OSARC (Osteosarcoma)` and :abbr:`T067 LMS (Leiomyosarcoma)`)
Samples from said diseases present in :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` 
reflect clinically and/or developmentally distinct groups within these specific tumour types that may exhibit 
different levels of immune activity, genomic lesions, tumour differentiation, and disease progression compared 
to their bona fide clusters, as recently described [Anderson2021]_.

Osteosarcoma
============

The tumours in :abbr:`T068 OSARC (Osteosarcoma)` divide into four distinct subtypes (Fig. :ref:`MESD2a <fig-mesd2>`). All samples for which we have 
clinical data are central osteosarcomas of the long bones or pelvis 
(`TARGET discovery cohort <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000468.v21.p8>`).

.. figure:: /img/mesd2.png
   :alt: Fig. MESD2
   :name: fig-mesd2
   :width: 500px
   
   MESD2: A, 2-dimensional UMAP projection of osteosarcoma tumors by gene expression. 
   The four subtypes are shown with different colours. B, Overall survival time curves for the 
   four osteosarcoma subtypes. C, distribution plots of in-house cartilage development (left),
   bone develompent (center) scores, and SP7 expression (right).

:abbr:`T071 OSARC OSSIF (Osteosarcoma, ossification)` (n = 32)
contains predominantly male patients (75.00% of samples) with a median age of 15.65 :abbr:`y.o. (years old)`. 
It exhibits overexpression (:abbr:`FDR (False Discovery Rate)` < 0.05) 
of cancer testis antigen (*CTA*) genes, most notably the *SSX* (8/9 genes), *MAGEA* (10/12), *MAGEB* (6/10), *CSAG* (2/2) and *XAGE* (4/5) 
families, several of which are known to be upregulated in osteosarcoma [Zou2012]_. 
|br|
Though :abbr:`CTA (Cancer testis antigen)` expression has been associated with poor prognosis in osteosarcoma [Zou2012]_, 
this cluster exhibits favourable prognosis when compared to its sibling clusters (:abbr:`lrt p-val (log-rank test p-value)` = 5.56e-05 at 5840 days, 
median :abbr:`OS (overall survival)` not reached) (Fig. :ref:`MESD2b <fig-mesd2>`). 
As this cluster is also associated with direct ossification (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.69e-10) 
and positive regulation of osteoblast differentiation (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.05, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.18e-02) 
and highly expresses *ALPL* (median :abbr:`logFC (log-Fold Change)` = 0.998, :abbr:`FDR (False Discovery Rate)` ≤ 9.069e-03 vs. 
:abbr:`T072 OSARC CHOND (Osteosarcoma, chondroblastic differentiation)` and :abbr:`T074 OSARC OSCL (Osteosarcoma, osteoclastic infiltrate)`) 
it may represent a subtype of osteoblastic or non-specific Osteosarcoma, good prognosis. 
|br| |br|
:abbr:`T072 OSARC CHOND (Osteosarcoma, chondroblastic differentiation)` (n = 38) also contains predominantly male patients (57.89%), 
with a median age of 15 :abbr:`y.o. (years old)`. It is enriched for chondrocyte marker genes, such as *COL9A1* 
(median :abbr:`logFC (log-Fold Change)` = 7.73, :abbr:`FDR (False Discovery Rate)` ≤ 7.08e-08), *SOX9* 
(median :abbr:`logFC (log-Fold Change)` = 2.20, :abbr:`FDR (False Discovery Rate)` ≤ 3.34e-05), and 
*OGN* (median :abbr:`logFC (log-Fold Change)` = 3.98, :abbr:`FDR (False Discovery Rate)` ≤ 1.16e-03), 
as well as genesets for collagen synthesis (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.97, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.20e-12,
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03), 
chondrocyte differentiation (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.13, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.77e-09, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03), 
and cartilage development involved in endochondral morphogenesis (:abbr:`medNES (median Normalized Enrichment Score)` = 1.13, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.21e-09) 
[Ashburner2000]_, [TGOC2019]_ (Fig. :ref:`MESD3 <fig-mesd3>`). 
These data suggest these tumours have significant chondroid components and may represent chondroblastic osteosarcoma. 
Furthermore, :abbr:`T072 OSARC CHOND (Osteosarcoma, chondroblastic differentiation)` 
contains all osteosarcomas of the pelvis, including the ilium and sacrum, in our dataset 
(0/22 vs. 4/16 vs. 0/17 vs. 0/3, :abbr:`χ2 p-val (χ2 test p-value)` = 1.03e-02), a location 
associated with chondroblastic osteosarcomas [Saab2005]_, [Kawai1998]_. 
:abbr:`T072 OSARC CHOND (Osteosarcoma, chondroblastic differentiation)` also overexpresses 
*MYC* (median :abbr:`logFC (log-Fold Change)` = 1.2, :abbr:`FDR (False Discovery Rate)` ≤ 4.67e-04), 
and has the lowest expression of *RB1* (median :abbr:`logFC (log-Fold Change)` = -1.11, 
:abbr:`FDR (False Discovery Rate)` ≤ 1.63e-03). Patients in this cluster exhibit poor overall survival, 
reaching median :abbr:`OS (overall survival)` at 1906 days post diagnosis (Fig. :ref:`MESD2b <fig-mesd2>`).
|br| |br|
:abbr:`T073 OSARC OSBLA (Osteosarcoma, osteoblastic differentiation)` (n = 37) has the youngest 
group of patients with a median age of 13.66 :abbr:`y.o. (years old)` and is composed predominantly 
of female patients (57.89% of the samples). 
It significantly overexpresses the master bone regulator *SP7* (median :abbr:`logFC (log-Fold Change)` = 0.939, 
:abbr:`FDR (False Discovery Rate)` ≤ 1.712e-02) (Fig. :ref:`MESD2c <fig-mesd2>`), 
and osteoblast markers *SOST* (median :abbr:`logFC (log-Fold Change)` = 5.66, 
:abbr:`FDR (False Discovery Rate)` ≤ 1.437e-04)
and *SATB2* (median :abbr:`logFC (log-Fold Change)` = 1.52, :abbr:`FDR (False Discovery Rate)` ≤ 1.142e-03) [Conner2013]_. 
Furthermore, it is enriched for genesets for bone mineralization (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.02, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.26e-05), 
and replacement ossification of existing non-cartilagenous tissues (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.23e-03, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) 
[Ashburner2000]_, [TGOC2019]_ (Fig. :ref:`MESD3 <fig-mesd3>`). 
It also displays enrichment of mTORC1 signalling (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.03,
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.41e-06, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02), 
associated with poor prognosis in osteosarcoma [Hu2016]_, as well as cell cycle progression 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.76e-05, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02).
Samples within this cluster exhibit the worst overall survival of all osteosarcoma clusters, 
reaching median :abbr:`OS (overall survival)` at 679 days post diagnosis (Fig. :ref:`MESD2b <fig-mesd2>`). 
As this cluster is composed of ossifying tumours with very poor prognosis, it may represent an aggressive 
subtype of osteoblastic osteosarcoma.
|br| |br|
Finally, :abbr:`T074 OSARC OSCL (Osteosarcoma, osteoclastic infiltrate)` (n = 11) 
is the smallest cluster, with the oldest median age (22.57 :abbr:`y.o. (years old)`), 
and predominantly female composition (75.00% of the samples). 
It also exhibits the best overall survival among all its siblings, with no deaths recorded in our dataset at 5840 days 
(Fig. :ref:`MESD2b <fig-mesd2>`).
Gene sets analysis revealed significant enrichment of sets related to osteoclast differentiation 
(:abbr:`medNES (median Normalized Enrichment Score)`≥ 1.16, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.80e-11, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02), 
bone remodelling (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.14, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.14e-06, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02), 
and fibrinolysis (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 9.43, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 8.83e-06, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) 
[Ashburner2000]_, [TGOC2019]_ (Fig. :ref:`MESD3 <fig-mesd3>`). 
This profile suggests this cluster contains osteoclast-rich and highly lytic or unstable tumours, 
likely representing telangiectatic osteosarcoma, though we lack the clinical annotation 
to confirm histotypes for any of the osteosarcoma samples present.

.. figure:: /img/mesd3.png
   :alt: Fig. MESD3
   :name: fig-mesd3
   :width: 500px
   
   MESD3: Distribution plots of the expression of genes (top) and gene sets (bottom) relevant to the definition
   of the four identified osteosarcoma transcriptional subtypes.

Mesothelioma
============

Similarly, the chidren of :abbr:`T070 MPM (Malignant pleural mesothelioma)` 
follow a simple path in their subtyping hierarchy (Fig. :ref:`MESD1b <fig-mesd1>`). 
It first splits into two clusters: :abbr:`T083 MPM BP1 LOH (Malignant pleural mesothelioma, loss of heterozygosity of BP1)` 
(n = 59), a mixed biphasic and epithelial class, 
and :abbr:`T084 MPM EPITH (Malignant pleural mesothelioma, epithelial morphology without loss of BP1)` 
(n = 23) which is composed almost exclusively of epithelial tumours (17/21). 
:abbr:`T083 MPM BP1 LOH (Malignant pleural mesothelioma, loss of heterozygosity of BP1)` 
shows higher *BP1* loss of heterozygosity (p-val = 3.96e-2) [Pulford2017]_, [Alakus2015]_ 
has significantly worse prognosis than :abbr:`T084 MPM EPITH (Malignant pleural mesothelioma, epithelial morphology without loss of BP1)` 
(:abbr:`lrt p-val (log-rank test p-value)` = 1.20e-3 at 2800 days post diagnosis), 
and shows higher EMT (epithelial mesenchymal transition) scores 
(:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 4.24e-05) [Hmeljak2018]_ 
due to its biphasic component, as well as lower ploidy (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 1.55e-3). 
:abbr:`T083 MPM BP1 LOH (Malignant pleural mesothelioma, loss of heterozygosity of BP1)` 
further splits by histology, with :abbr:`T085 MPM BP1 LOH (Malignant pleural mesothelioma, loss of heterozygosity of BP1 with biphasic and epithelial morphology)` 
(n = 23) containing both biphasic and epithelial samples and 
:abbr:`T086 MPM BP1 LOH EPITH (Malignant pleural mesothelioma, loss of heterozygosity of BP1 and epithelial morphology)` (n = 23) 
being almost exclusively composed of epithelial tumours. 
As before, :abbr:`T086 MPM BP1 LOH EPITH (Malignant pleural mesothelioma, loss of heterozygosity of BP1 and epithelial morphology)`, 
with a majority component of biphasic samples exhibit a significantly higher 
:abbr:`EMT (epithelilal mesenchymal transition)` score (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 1.73e-2).


Mixed low-stemness sarcoma
==========================

The hierarchy of :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` is deeper and more complex than the bona fide sarcoma groups (Fig. :ref:`MESD1b <fig-mesd1>`, :ref:`MESD4 <fig-mesd4>`). 
At the first level, we see the separation of :abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` (n = 218) 
and :abbr:`T076 SARC CIN (Sarcoma, chromosomal instability)` (n = 57). 

.. figure:: /img/mesd4.png
   :alt: Fig. MESD4
   :name: fig-mesd4
   :width: 400px
   
   MESD4: 2-dimensional UMAP projection of mixed sarcoma tumours with low stemness by gene expression. 
   The subtypes identified are shown with different colours. Samples labelled as carcinoma by their presenting institution are shown
   as empty circles.

Both are mixed clusters, though :abbr:`T076 SARC CIN (Sarcoma, chromosomal instability)` 
contains mostly soft tissue sarcoma, including dedifferentiated liposarcoma (DDLPS), undifferentiated pleomorphic sarcoma (UPS), and myxofibrosarcoma (MFS). 
:abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` 
contains significantly younger patients, likely due to the presence of a high number of osteosarcoma, 
(58.00 vs. 65.00, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 9.16e-04) 
but we observed no difference in survival between the two classes (:abbr:`lrt p-val (log-rank test p-value)` = 5.10e-01 at 5204 days).
:abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` overexpresses 
(:abbr:`FDR (False Discovery Rate)` < 0.05 & median :abbr:`logFC (log-Fold Change)`  > 0) :abbr:`CTA (cancer testis antigens)` genes, 
which show considerable promise for immunotherapeutics [Gjerstorff2015]_. These include *GAGE* (9/13), *PAGE* (4/6), *MAGEA* (11/12), *MAGEC* (3/3), and *XAGE* (3/5) [Carregaro2013]_. 
We then investigated immune checkpoint ligands and receptors expression, revealing overexpression of 
*PD1* (median :abbr:`logFC (log-Fold Change)` = -3.37, :abbr:`FDR (False Discovery Rate)` ≤ 2.044e-03), 
*PDL1* (median :abbr:`logFC (log-Fold Change)` = -0.87, :abbr:`FDR (False Discovery Rate)` ≤ 1.078e-02), 
and *CTLA4* in :abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` 
(median :abbr:`logFC (log-Fold Change)` = -2.75, :abbr:`FDR (False Discovery Rate)` ≤ 8.047e-06). 
Consistent with this, :abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` 
displays the lowest leukocyte fraction of its siblings (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`  = 5.11e-10, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` ≤ 3.69e-04) [Thorsson2018]_.
More interestingly, samples in :abbr:`T076 SARC CIN (Sarcoma, chromosomal instability)` show significantly 
higher chromosomal instability (CIN) (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 1.15e-05) 
(:ref:`MESD5 <fig-mesd5>`) without a corresponding difference in mutation load (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 4.75e-01); 
this holds true for both :abbr:`DDLPS (dedifferentiated liposarcoma)`  
(:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 3.70e-03) and 
:abbr:`UPS (undifferentiated pleomorphic sarcoma)` (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 1.43e-02) 
subpopulations when taken independently [TCGA2017]_ .

.. figure:: /img/mesd5.png
   :alt: Fig. MESD5
   :name: fig-mesd5
   :width: 300px
   
   MESD5: Distribution plots of chromosomal instability in sarcomas.

:abbr:`T076 SARC CIN (Sarcoma, chromosomal instability)` then splits by diagnosis into 
:abbr:`T081 UPS/MFS CIN (Undifferentiated pleomorphic sarcoma and myxofibrosarcoma with chromosomal instability)` (n = 33), 
containing mostly :abbr:`UPS (undifferentiated pleomorphic sarcoma)` and :abbr:`MFS (myxofibrosarcoma)`, 
and :abbr:`T082 DDLPS CIN (Dedifferentiated liposarcoma with chromosomal instability)` (n = 24) (Fig. S23b), 
which is largely composed of :abbr:`DDLPS (Dedifferentiated liposarcoma)`. 
This is reflected in the higher amplification of chr12q15, common to :abbr:`DDLPS (dedifferentiated liposarcoma)`, 
in :abbr:`T095 MYOGEN FUS- A (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative without Wilms tumours)` 
(median amp. 23.00 vs 2.00, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 8.335e-07) [TCGA2017]_ . 
Furthermore, :abbr:`T082 DDLPS CIN (Dedifferentiated liposarcoma with chromosomal instability)` has both significantly higher genomic 
amplification and gene expression of *MDM2* (2.40e-2 vs. 3.66, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 4.37e-06; 
:abbr:`logFC (log-Fold Change)` = -4.55, :abbr:`FDR (False Discovery Rate)` = 5.39e-18) 
and *CDK4* (0.00 vs. 3.66 :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 7.48e-06; 
:abbr:`logFC (log-Fold Change)` = -4.27, :abbr:`FDR (False Discovery Rate)` = 5.39e-18) [TCGA2017]_ . 
|br| |br|
Finally, :abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` separates into four terminal 
classes, with varying disease composition, immunogenicity, and patient age (:ref:`MESD6 <fig-mesd6>`). 
Nevertheless, there are no significant differences in survival between these clusters. 
:abbr:`T077 SARC HYPOX (Sarcoma, hypoxic gene expression)` (n = 58) contains a high variability of diagnoses but is mostly composed of osteosarcoma, 
:abbr:`UPS (undifferentiated pleomorphic sarcoma)`, and :abbr:`LMS (Leiomyosarcoma)`. Only 31.03% of these samples are paediatric, 
the median age is 60 :abbr:`y.o. (years old)` Sarcoma,in this cluster display the highest mitotic rate compared to those in sibling clusters 
(:abbr:`(Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`  = 4.75e-05), 
as also reflected in gene set enrichment analysis (:abbr:`logFC (log-Fold Change)` = 0.871, adj. p-val = 7.76e-01). 
This cluster also has the lowest expression of *TP53* (:abbr:`logFC (log-Fold Change)`= -1.66, :abbr:`FDR (False Discovery Rate)` ≤ 1.78e-11). 
Tumours in :abbr:`T077 SARC HYPOX (Sarcoma, hypoxic gene expression)` display the lowest leukocyte fraction 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.11e-10, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` ≤ 1.70e-07) 
among this family, and also exhibit the lowest expression of the immune checkpoint genes *PD1* (median :abbr:`logFC (log-Fold Change)` = -3.37, 
:abbr:`FDR (False Discovery Rate)` ≤ 2.044e-03), *PDL1* (median :abbr:`logFC (log-Fold Change)` = -0.87, :abbr:`FDR (False Discovery Rate)` ≤ 1.078e-02), and *CTLA4* (median :abbr:`logFC (log-Fold Change)` = -2.75, :abbr:`FDR (False Discovery Rate)` ≤ 8.047e-06). 
It is enriched for genes associated with hypoxia in soft tissue sarcomas (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.08, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 1.44e-05, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05) [Yang2018]_ (Fig. :ref:`MESD6 <fig-mesd6>`). 
|br| |br|
:abbr:`T078 SARC EPITH/KIT (Sarcoma, epithelial differentiation and/or c-KIT overexpression)` (n = 77) is the largest cluster, 
and is mostly composed of osteosarcoma and :abbr:`DDLPS (dedifferentiated liposarcoma)`, but importantly also contains five gastrointestinal 
stromal tumours (GIST). It is the cluster with the youngest median age (24 :abbr:`y.o. (years old)` 
:abbr:`(Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`  = 2.50e-06, 
57.14% paediatric, :abbr:`χ2 p-val (χ2 test p-value)` = 4.66e-11). 
:abbr:`T078 SARC EPITH/KIT (Sarcoma, epithelial differentiation and/or c-KIT overexpression)` has the highest expression of the 
*KIT* proto-oncogene (median :abbr:`logFC (log-Fold Change)` = 1.33, :abbr:`FDR (False Discovery Rate)` ≤ 3.88e-02) (Fig. :ref:`MESD6 <fig-mesd6>`). 
Mutations in *KIT* are a major driver of :abbr:`GIST (gastrointestinal stromal tumour)` [Hirota1998]_ and may explain their affinity to this class. 
Nevertheless, *KIT* mutations are not exclusive of this tumour type [Smithey2002]_, and, indeed, the significance in overexpression is maintained 
after the removal of :abbr:`GISTs (gastrointestinal stromal tumours)` 
(median :abbr:`logFC (log-Fold Change)`  = 1.52, :abbr:`FDR (False Discovery Rate)` ≤ 4.11e-02). 
We confirmed enrichment of *KIT* downstream genes with gene sets analysis 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.02, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.82e-08) 
[Schaefer2009]_ (Fig. :ref:`MESD6 <fig-mesd6>`). 
:abbr:`T078 SARC EPITH/KIT (Sarcoma, epithelial differentiation and/or c-KIT overexpression)` also displays the highest 
chr12q13-15 amplification among its siblings (:abbr:`(Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.77e-04), 
likely a consequence of its high population of :abbr:`DDLPS (dedifferentiated liposarcoma)` . 
Furthermore, :abbr:`T078 SARC EPITH/KIT (Sarcoma, epithelial differentiation and/or c-KIT overexpression)` 
has the highest expression of epithelial markers *EPCAM* (median :abbr:`logFC (log-Fold Change)` = 1.41, :abbr:`FDR (False Discovery Rate)` ≤ 1.280e-02), 
*CLDN1* (median :abbr:`logFC (log-Fold Change)` = 1.86, :abbr:`FDR (False Discovery Rate)` ≤ 2.941e-04), 
and *CDH1* (median :abbr:`logFC (log-Fold Change)` = 2.02, :abbr:`FDR (False Discovery Rate)` ≤ 7.437e-03) 
among its siblings and shows enrichment of epithelial development gene sets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.12, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.43e-16, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) 
[Ashburner2000]_, [TGOC2019]_ (Fig. :ref:`MESD6 <fig-mesd6>`). 
It is also enriched for gene sets involving angiogenesis (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.10, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.12e-08, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 0.05) [Liberzon2015]_, 
which has been implicated in the pathogenesis of sarcoma with epithelial features [Quesada2012]_.
As such, we hypothesize that this class comprises Sarcoma, epithelial differentiation and related tumours, 
possibly including epitheloid subtypes of :abbr:`DDLPS (dedifferentiated liposarcoma)` , osteosarcoma, and others [Deyrup2007]_, [Thway2016]_, [Makise2017]_. 
|br| |br|
The majority of samples present in :abbr:`T079 SARC CARCN (Sarcomas and carcinomas with sarcomatoid components)` (n = 41) 
are not labelled by their source institutions as malignancies of mesenchymal origin, but rather as carcinomas or related 
ecto- or endodermal tumours (Fig. :ref:`MESD4 <fig-mesd4>`). In fact, 23/41 tumours are carcinomas or skin cutaneous melanoma compared to 15/41 being sarcomas; 
however, sarcomatoid components were noted in many of these samples’ clinical data when available [TCGA2017]_. 
:abbr:`T079 SARC CARCN (Sarcomas and carcinomas with sarcomatoid components)` is enriched for
*E2F* targets (:abbr:`medNES (median Normalized Enrichment Score)` = 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.17e-28) , 
*MYC* targets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.02, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 3.59e-25, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03), 
and DNA synthesis (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.04e-24, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) 
and G2M checkpoint (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.16e-28) pathways 
[Ashburner2000]_, [TGOC2019]_, suggesting its constituents share a pool of mutations whose pathways converge upon increased translation, 
protein processing, and cell cycle progression. 
It is also highly enriched for gene sets involving translation (:abbr:`medNES (median Normalized Enrichment Score)` ≤ 1.02, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.07e-19, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) and protein processing 
(:abbr:`medNES (median Normalized Enrichment Score)` ≤ 1.10, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.31e-18, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) ([Ashburner2000]_; [TGOC2019]_). Intereatingly, Sarcoma,in this class have a significantly higher mutation load than those in sibling clusters (median 96.00, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.60e-03) [TCGA2017]_. 
This cluster also has a high leukocyte fraction, with the highest lymphocyte content of its siblings 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.325e-4), 
specifically CD8+ T cells (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.14e-06) [Newman2015]_. 
|br| |br|
:abbr:`T080 SARC DIFFlow IMMhigh (Sarcoma, high immune activity)` (n = 30) is the smallest child cluster of 
:abbr:`T075 SARC STEMlow A (Sarcoma, low stemness without chromosomal instability)` and contains the oldest patient cohort 
(median age of 62 :abbr:`y.o. (years old)`, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.50e-06) 
with no paediatric samples. It is mainly composed of :abbr:`DDLPS (dedifferentiated liposarcoma`) and :abbr:`UPS (undifferentiated pleomorphic sarcoma)`, 
similar to :abbr:`T082 DDLPS CIN (Dedifferentiated liposarcoma with chromosomal instability)`, but significantly lower in chromosomal instability. 
It is possible a similar subdivision by diagnosis would have been observed with a more sizeable cohort. It has the highest leukocyte 
fraction of its sibling classes (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.11e-10) 
and is significantly enriched (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 8.90e-11) 
for a myriad of gene sets relating to the immune response, proinflammatory signalling, and complement activation [Liberzon2015]_. 
We hypothesize that :abbr:`T080 SARC DIFFlow IMMhigh (Sarcoma, high immune activity)` represents a group of soft tissue sarcoma with high immune infiltration. 

.. figure:: /img/mesd6.png
   :alt: Fig. MESD6
   :name: fig-mesd6
   :width: 500px
   
   MESD6: Distribution plots of the expression of genes and gene sets relevant to the definition
   of low-stemness sarcomas transcriptional subtypes without chromosomal instability.

|br| |br|

T003 Mesodermal tumour with high stemness
=========================================

Following the hierarchy along the high stemness sarcomas branch, :abbr:`T003 MESODM STEMhigh (Mesodermal tumours, low stemness)`, 
we first observe a separation by diagnosis (Fig. :ref:`MESD1a <fig-mesd1>`). 
:abbr:`T090 MYOGEN (Myogenic sarcomas)` is composed of myogenic sarcoma, and the median pateint age is 7.00 :abbr:`y.o. (years old)`, 
:abbr:`T091 MESODM STEMhigh A (Mesodermal tumour with high stemness, non-myogenic)` (n = 212) is the largest and most diverse cluster; 
it is composed of Testicular Germ Cell Tumours (TGCT) synovial sarcomas (SYSARC), and uterine carcinosarcomas (UCS), among other tumour types. 
It is the cluster with the oldest patients, with a median age of 33.00  :abbr:`y.o. (years old)`. 
Finally, we observe a homogeneous Wilms tumours class, :abbr:`T092 WILMS (Wilms tumour)` (n = 119),
which contains patients with youngest median age (4.38 :abbr:`y.o. (years old)`). 

.. _Myogenic:

Myogenic tumour
===============

Myogenic tumours in :abbr:`T090 MYOGEN (Myogenic sarcomas)` further split into 
:abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` (n = 108) containing the majority of embryonal rhabdomyosarcomas 
(ERMS) and other myogenic malignancies, and :abbr:`T094 RMSARC ALV FUS+ (Alveolar rhabdomyosarcoma FOX1-PAX3/7 fusion-positive)` 
(n = 47), which contains the majority of alveolar rhabdomyosarcomas (ARMS)  (Fig. :ref:`MESD1b <fig-mesd1>`). 
Indeed, :abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` exhibits significantly higher expression of the 
*FOXO1-PAX3/7* fusion-negative markers *HMGA2* (:abbr:`logFC (log-Fold Change)` = 4.76, :abbr:`FDR (False Discovery Rate)` = 3.82e-17), 
*EGFR* (:abbr:`logFC (log-Fold Change)` = 2.73, :abbr:`FDR (False Discovery Rate)` = 2.72e-19), and *FBN2* 
(:abbr:`logFC (log-Fold Change)` = 5.35, :abbr:`FDR (False Discovery Rate)` = 9.920e-35), while 
:abbr:`T094 RMSARC ALV FUS+ (Alveolar rhabdomyosarcoma FOX1-PAX3/7 fusion-positive)` shows marked overexpression 
(:abbr:`logFC (log-Fold Change)` ≤ -3.17, :abbr:`FDR (False Discovery Rate)` ≤ 9.73e-22) of FOX1-PAX3/7 fusion-positive markers 
*TFAP2B* (:abbr:`logFC (log-Fold Change)` = -9.14, :abbr:`FDR (False Discovery Rate)` = 5.078e-45) and 
*CDH3* (:abbr:`logFC (log-Fold Change)` = -3.17, :abbr:`FDR (False Discovery Rate)` = 9.728e-22) [Davicioni2009]_, [Parham2013]_, 
and significant enrichment (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.12, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value ≤ 3.79e-18`) of 
*FOXO1-PAX3/7* fusion-associated pathways [Gryder2017]_, [Davicioni2009]_ (Fig. :ref:`MESD7 <fig-mesd7>`). 
Though :abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` contains a handful of samples labelled as 
:abbr:`ARMS (alveolar rhabdomyosarcoma)`, it is sensible to speculate these may be fusion-negative; 
this occurrence is common and the fusion is not a necessary feature of this histotype [Barr2002]_.
In fact, the molecular profile and clinical course of fusion negative :abbr:`ARMS (alveolar rhabdomyosarcoma)` is indistinguishable from 
:abbr:`ERMS (embryonal rhabdomyosarcoma)`, supporting a common transcriptional identity as observed here [Williamson2010]_. 
However, though :abbr:`ARMS (alveolar rhabdomyosarcoma)` is associated with worse prognosis than 
:abbr:`ERMS (embryonal rhabdomyosarcoma)`, due to a lack of clinical annotatioon we are unable to confirm any 
differences in survival between  :abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` and 
:abbr:`T094 RMSARC ALV FUS+ (Alveolar rhabdomyosarcoma FOX1-PAX3/7 fusion-positive)`.  
|br| |br|
:abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` then divides into two clusters. 
We observe the separation of a small group of samples labelled as Wilms tumours, 
:abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` (n = 12) from the rest of fusion-negative myogenic tumours in 
:abbr:`T095 MYOGEN FUS- A (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative without Wilms tumours)` (n = 95) (Fig. :ref:`MESD7 <fig-mesd7>`).
When compared to :abbr:`T092 WILMS (Wilms tumour)` (see below for details), the major Wilms tumour class, 
:abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` has high expression of striated muscle genes such as 
*MYL1* (:abbr:`logFC (log-Fold Change)` = 11.9, :abbr:`FDR (False Discovery Rate)` = 4.61e-51), *MYOG* (:abbr:`logFC (log-Fold Change)` = 9.45, 
:abbr:`FDR (False Discovery Rate)` = 3.93e-55), and *MYOD1* (:abbr:`logFC (log-Fold Change)` = 8.93, :abbr:`FDR (False Discovery Rate)` = 1.12e-51). 
Furthermore, :abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` is enriched for gene sets related to skeletal muscle development 
(:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value` = 3.56e-09, :abbr:`medNES (median Normalized Enrichment Score)` = 1.85) 
[Ashburner2000]_, [TGOC2019]_ (Fig. :ref:`MESD7 <fig-mesd7>`), 
suggesting this specific subtype of Wilms tumours to have significant areas with skeletal muscle differentiation. 
As an alternative hypothesis, we also advance the possibility this may be a class of misdiagnosed rhabdomyosarcoma of the kidney 
, [Mehrain2013]_, [Samkari2018]_ or a striated-muscle-like Wilms tumour phenotype.  
Furthermore, :abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` is enriched for gene sets of rhabdomyosarcomas both with and without 
*FOXO1-PAX3/7* fusions (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value` = 7.17e-04) [Davicioni2009]_, 
and :abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` also has significantly higher expression of 
NOGGIN (*NOG*) (:abbr:`logFC (log-Fold Change)` = 1.77, :abbr:`FDR (False Discovery Rate)` = 4.31e-07), 
when compared to :abbr:`T092 WILMS (Wilms tumour)` [Gerhart2019]_. 
A common classification of Wilms tumours separates them between those with favourable histology 
(FHWT) and those with diffuse anaplasia (DAWT); :abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` 
is the only Wilms tumour class within our cohort which contains a majority of diffuse anaplasia samples.
|br|
The tumours found in :abbr:`T095 MYOGEN FUS- A (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative without Wilms tumours)` 
separate into three subclasses (Fig :ref:`MESD1b <fig-mesd1>`). Two have are comprised almost exlusively of embryonal 
rhabdomyosarcoma (ERMS): :abbr:`T097 RMSARC EMB MYO (Embryonal rhabdomyosarcoma, well-differentiated)` 
(n = 30) which also contains a few presumably fusion-negative :abbr:`ARMS (alveolar rhabdomyosarcoma)`, 
and :abbr:`T098 RMSARC EMB MYOD1mut (Embryonal rhabdomyosarcoma, MYOD1 mutant)` (n = 35) which also includes two spindle cell/sclerotizing rhabdomyosarcoma. 
The third cluster is :abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)` (n = 19), 
a small class of :abbr:`UCS (uterine carcinosarcoma)`. 
These classes split by age; as expected :abbr:`T097 RMSARC EMB MYO (Embryonal rhabdomyosarcoma, well-differentiated)` 
and :abbr:`T098 RMSARC EMB MYOD1mut (Embryonal rhabdomyosarcoma, MYOD1 mutant)`  are almost entirely paediatric 
(median age 5 :abbr:`y.o. (years old)` for both), while patients in :abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)`  
are mostly adults (median age 63 :abbr:`y.o. (years old)`, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.30e-05 with 21.06% of paediatric samples, 
:abbr:`χ2 p-val (χ2 test p-value)` = 3.76e-13).
|br| |br|
Comparing the two :abbr:`ERMS (embryonal rhabdomyosarcoma)` classes, :abbr:`T097 RMSARC EMB MYO (Embryonal rhabdomyosarcoma, well-differentiated)`, 
and :abbr:`T098 RMSARC EMB MYOD1mut (Embryonal rhabdomyosarcoma, MYOD1 mutant)`, :abbr:`T097 RMSARC EMB MYO (Embryonal rhabdomyosarcoma, well-differentiated)` 
has a significantly elevated expression of skeletal muscle developmental gene sets 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.15, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.61e-07) 
and a high expression of muscle genes (Fig. :ref:`MESD7 <fig-mesd7>`), 
suggesting these tumours comprise a well-differentiated subtype of :abbr:`ERMS (embryonal rhabdomyosarcoma)` [Davicioni2009]_.
:abbr:`T098 RMSARC EMB MYOD1mut (Embryonal rhabdomyosarcoma, MYOD1 mutant)` 
is characterized instead by high expression of gene sets related to immune activation [Ashburner2000]_, [TGOC2019]_, 
low expression of skeletal muscle genes - including *MYH8* (:abbr:`logFC (log-Fold Change)`= - 4.54, 
:abbr:`FDR (False Discovery Rate)` = 1.13e-06), *ACTA1* (:abbr:`logFC (log-Fold Change)` = -4.9, :abbr:`FDR (False Discovery Rate)` = 9.23e-09), 
and *MYOG* (:abbr:`logFC (log-Fold Change)` = -1.74, :abbr:`FDR (False Discovery Rate)` = 2.31e-04) - and enrichment of 
*PI3K* signalling (:abbr:`medNES (median Normalized Enrichment Score)` = 1.11, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value` = 4.58e-05) [Schaefer2009]_, 
a gene expression pattern characteristic of RMS with *MYOD1* L122R mutations [Kohsaka2014]_ . 
Further gene set enrichment analysis of targets downregulated by *MYOD1* LI22R compared to wild type 
*MYOD1* shows significant underexpression in :abbr:`T098 RMSARC EMB MYOD1mut (Embryonal rhabdomyosarcoma, MYOD1 mutant)` 
compared to both its sibling clusters (:abbr:`medNES (median Normalized Enrichment Score)` ≤ 4.04e-02, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.44e-11, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) (Fig. :ref:`MESD7 <fig-mesd7>`); 
however, we lack any genomic information to confirm this. 
|br| |br|
When compared to the major uterine carcinosarcoma class :abbr:`T111 UCS (Uterine carcinosarcoma)` (see below for details), 
:abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)` is significantly higher in sarcomatous components 
(median 100.00% vs. 70.00, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 8.462e-04) 
and heterologous rhabdomyosarcomatous components (mean 23.5% vs. 0.00%, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 6.13e-04), 
while T111 exhibits a higher carcinomatous component (median 1.00% vs. 30.00%, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 1.03e-02) [Cherniack2017]_. 
:abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)`  
also exhibits significantly higher expression of skeletal muscle genes 
*MYOD1* (:abbr:`logFC (log-Fold Change)` = 6.88, :abbr:`FDR (False Discovery Rate)` = 7.27e-16) and 
*MYOG* (:abbr:`logFC (log-Fold Change)` = 9.55, :abbr:`FDR (False Discovery Rate)` = 9.30e-17), 
conforming with a recently described myogenic subtype of :abbr:`UCS (uterine carcinosarcoma)` (subtype II) [An2017]_.

.. figure:: /img/mesd7.png
   :alt: Fig. MESD7
   :name: fig-mesd7
   :width: 400px
   
   MESD7: Distribution plots of normalized enrichment score of gene sets relevant to the definition
   of myogenic tumours.

Other sarcoma with high stemness
================================

Following the children of :abbr:`T091 MESODM STEMhigh A (Mesodermal tumours with high stemness, non-myogenic)`, 
we find 6 different subclasses with a wide variety of diagnoses (Fig. :ref:`MESD8 <fig-mesd8>`). 

.. figure:: /img/mesd8.png
   :alt: Fig. MESD8
   :name: fig-mesd8
   :width: 400px
   
   MESD8: a 2-dimensional UMAP projection of mixed sarcoma tumours with high stemness by gene expression. 
   The subtypes identified are shown with different colours. 

Some, like :abbr:`T100 SYSARC (Synovial sarcoma)` (n = 37) and :abbr:`T102 CPC (Choroid plexus carcinoma)` (n = 6) are clearly defined by a single tumour type, 
in this case, synovial sarcoma and choroid plexus carcinoma, respectively.
Others, like :abbr:`T104 SARC CICr (Sarcoma, CIC rearrangement)` (n = 21), 
are composed of samples of disparate origins brought together by specific lesions. 
This is an exemplary case and is similar to that of *BCOR* altered samples within the CNS branch, here both CNS malignancies and sarcomas carrying 
*CIC-DUX4* fusions (Fig. :ref:`MESD9 <fig-mesd9>`). 

.. figure:: /img/mesd9.png
   :alt: Fig. MESD9
   :name: fig-mesd9
   :width: 500px

   MESD9: A, 2-dimensional UMAP projection of mixed sarcoma tumours with high stemness by gene expression. The subtypes identified are shown with different colours, 
   CIC-mutant tumours are shown in red. B, schematic representation of a typical CIC-DUX4 fusion event. C, distribution plots
   of MYCN expression high-stemness sarcoma subtypes. D, tumour type composition of the T104 SARC CICr class.

Gene set enrichment analysis of this cluster revealed both significant enrichment of upregulated targets 
(:abbr:`medNES (median Normalized Enrichment Score)` ≤ 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.36e-18) 
and significant paucity of downregulated targets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 8.34e-01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.29e-11) 
in *CIC-DUX4* fusion-positive round cell tumours [Specht2014]_, [Yoshimoto2017]_ ((Fig. :ref:`MESD10 <fig-mesd10>`).
:abbr:`T104 SARC CICr (Sarcoma, CIC rearrangement)` also exhibits overexpression of 
*MYC* (median :abbr:`logFC (log-Fold Change)` = 2.47, :abbr:`FDR (False Discovery Rate)` ≤ 1.39e-06) (Fig. :ref:`MESD9d <fig-mesd9>`), 
frequently amplified in *CIC* rearranged tumours [Smith2015]_, as well as its canonical downstream effector *CDKN1A* 
(median :abbr:`logFC (log-Fold Change)` = 2.69, :abbr:`FDR (False Discovery Rate)` ≤ 5.70e-09). 
The class includes a few samples labelled as Ewing sarcoma, which are likely misdiagnosed.

.. figure:: /img/mesd10.png
   :alt: Fig. MESD10
   :name: fig-mesd10
   :width: 300px
   
   MESD10: Distribution plots of normalized enrichment score of gene sets relevant to the definition
   of CIC-mutated tumours.

:abbr:`T103 SARC NF1low (Sarcoma, NF1 underexpression)` (n = 47) contains the majority of :abbr:`UCS (uterine carcinosarcoma)` in our dataset, 
along with a few retroperitoneal :abbr:`DDLPS (dedifferentiated liposarcoma)`, 
MPNST (malignant peripheral nerve sheath tumour), two ovarian serous cystadenocarcinomas, and uterine corpus endometrial carcinomas, 
among other tumour types. This then divides roughly by diagnosis: :abbr:`UCS (uterine carcinosarcoma)` 
samples are clustered into :abbr:`T111 UCS (Uterine carcinosarcoma)` (n = 37) at the next level (Fig. :ref:`MESD1b <fig-mesd1>`), 
separating them from all other malignancies, which are found in :abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` (n=25). 
When compared to the myogenic :abbr:`UCS (uterine carcinosarcoma)`  
cluster :abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)`, 
we observe higher expression of cell adhesion and apoptotic genes, *SIPA1L1* 
(:abbr:`logFC (log-Fold Change)` = 1.33, :abbr:`FDR (False Discovery Rate)` = 7.290e-08), 
*STAT6* (:abbr:`logFC (log-Fold Change)` = 0.846, :abbr:`FDR (False Discovery Rate)` = 4.461e-02), 
*CASP6* (:abbr:`logFC (log-Fold Change)` = 1.01, :abbr:`FDR (False Discovery Rate)` = 2.585e-05), 
and *CASP8* (:abbr:`logFC (log-Fold Change)` = 0.702, :abbr:`FDR (False Discovery Rate)` = 4.084e-02) in :abbr:`T111 UCS (Uterine carcinosarcoma)`, 
associated with a recently described UCS group (subtype I)[An2017]_.
|br| |br|
:abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` contains a majority of 
:abbr:`MPNST (malignant peripheral nerve sheath tumour)`  and :abbr:`DDLPS (dedifferentiated liposarcoma)` 
(n = 4 each), which seem to be characterized by a loss of *NF1*. This explains the marked separation of this group 
from the majority of these diagnoses, which are found in :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` in the entirely different mesodermal tumour family. 
We observe highly significant enrichment of genes upregulated in *NF1* mutants and impoverishment of genes 
downregulated by the same lesions between all diagnoses included within :abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` 
and their counterparts in all other clusters (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.26, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value`` ≤ 6.53e-07) (Fig. :ref:`MESD11 <fig-mesd11>`), 
and more specifically between :abbr:`MPNST (malignant peripheral nerve sheath tumour)`  and :abbr:`DDLPS (dedifferentiated liposarcoma)`  
in :abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` vs. :abbr:`T069 SARC STEMlow (Sarcoma, low stemness)` 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.33, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value`` ≤ 6.25e-04) [Pemov2020]_. 
As :abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` contains tumours from markedly different lineages, 
including two glioblastoma multiformes and three melanomas, it is likely this class contains 
*NF1* mutant tumours regardless of their tissue of origin, similarly to what observed for 
*BCOR* altered samples in CNS and *CIC*-fusion samples ([Kiuru2017]_; [Costa2019]_; [Kim2020]_).
We observe no significant difference in these downstream *NF1* gene sets, between :abbr:`T110 SARC NF1mut (Sarcoma, NF1 mutation)` 
and :abbr:`T111 UCS (Uterine carcinosarcoma)` (p-val ≥ 3.80e-01), suggesting this expression pattern 
is characteristic of their whole parent class :abbr:`T103 SARC NF1low (Sarcoma, NF1 underexpression)`. 
Within :abbr:`T111 UCS (Uterine carcinosarcoma)`, only one sample is reported as *NF1* mutated - the only case in the 
:abbr:`TCGA (The Cancer Genome Atlas)` :abbr:`UCS (uterine carcinosarcoma)`  cohort [Cherniack2017]_ - possibly suggesting a role of 
*NF1* in :abbr:`UCS (uterine carcinosarcoma)`  regardless of its mutation status. 
Interestingly, when comparing :abbr:`T111 UCS (Uterine carcinosarcoma)` with :abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)` 
and its parent cluster :abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)`, only the downregulated targets of 
*NF1* mutations are significantly lower (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.40e-05 
and 6.30e-01 vs. :abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)`, 6.22e-03 and 6.97e-01 vs. 
:abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)`). 
This is possibly due to the reported role of *NF1* in myogenesis [Kossler2011]_, 
and suggests that only the loss of expression in downstream target may be the specific marker of *NF1* alterations in these malignancies. 

.. figure:: /img/mesd11.png
   :alt: Fig. MESD11
   :name: fig-mesd11
   :width: 300px

   MESD11: Distribution plots of normalized enrichment score of gene sets relevant to the definition
   of NF1-mutated tumours.


Testicular tumour 
=================

Within the child classes of :abbr:`T093 MYOGEN FUS- (Myogenic sarcoma, FOX1-PAX3/7 fusion-negative)` we find two separate groups of 
:abbr:` TGCT NON-SEM (testicular germ cell tumour non-seminomas)` (Fig. :ref:`MESD1b <fig-mesd1>`). 
:abbr:`T101  (Testicular germ cell tumour non-seminoma, mature teratoma or yolk sac tumour)` (n = 45) is composed of 
both mature teratoma and yolk sac tumours, as evident both from clinical annotation (:abbr:`χ2 p-val (χ2 test p-value)` ≤ 3.67e-02) 
and tissue type percentage information (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value ≤ 8.35e-03) [Shen2018]_. 
Conversely, :abbr:`T105 TGCT nonSEM EMB (Testicular germ cell tumour non-seminoma embryonal carcinoma rich)` 
contains embryonal carcinoma-rich tumours, gleaned from both from clinical annotation (0 vs. 27/39, :abbr:`χ2 p-val (χ2 test p-value)` = 1.21e-07) 
and tissue composition (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value =1.48e-8) [Shen2018]_. 
:abbr:`T101  (Testicular germ cell tumour non-seminoma, mature teratoma or yolk sac tumour)` exhibits elevated 
*AFP* expression (:abbr:`logFC (log-Fold Change)` = 2.23, :abbr:`FDR (False Discovery Rate)` = 8.421e-03), while 
:abbr:`T105 TGCT nonSEM EMB (Testicular germ cell tumour non-seminoma embryonal carcinoma rich)` overexpresses 
lactate dehydrogenase genes (4/6, :abbr:`FDR (False Discovery Rate)` < 1.00e-6) and *CGB* (β-HCG) genes (4/5, :abbr:`FDR (False Discovery Rate)` < 1.00e-04). 
:abbr:`T105 TGCT nonSEM EMB (Testicular germ cell tumour non-seminoma embryonal carcinoma rich)` 
is highly enriched for an embryonal carcinoma gene sets (:abbr:`medNES (median Normalized Enrichment Score)` = 216.80, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value = 3.27e-06)`, while 
:abbr:`T101 (Testicular germ cell tumour non-seminoma, mature teratoma or yolk sac tumour)` is enriched for yolk sac gene sets 
(:abbr:`medNES (median Normalized Enrichment Score)` = 2.06, :abbr:`MWU adj. p-val 
(Mann Whitney U test Benjamin-Hochberg adjusted p-value = 3.27e-06) [Korkola2005]_. 
|br| |br|
:abbr:`T101  (Testicular germ cell tumour non-seminoma, mature teratoma or yolk sac tumour)` then divides into four separate 
subtypes which fall along on a spectrum of differentiation from yolk sac to mature tumours 
(:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` < 1.00e-04) 
(Fig. :ref:`MESD12 <fig-mesd12>`). Indeed, we observe :abbr:`T108 TGCT nonSEM YOLK H (Testicular germ cell tumour non-seminoma yolk sac high)` 
(n  = 13) carrying yolk sac and yolk sac dominant samples with the highest percentage of yolk sac tissue (median 95.00%) and lowest of mature tissue (0.00%), 
:abbr:`T107 TGCT nonSEM YOLK I (Testicular germ cell tumour non-seminoma yolk sac intermediate)` (n = 9), being just below 
(yolk sac 42.50%, mature 25.00%), :abbr:`T109 TGCT nonSEM MAT I (Testicular germ cell tumour non-seminoma mature interemediate)` (n = 10) 
containing mature teratoma dominant samples with low yolk sac content (10.0%) and a considerably higher mature tissue component (65.00%), 
and finally :abbr:`T106 TGCT nonSEM MAT H (Testicular germ cell tumour non-seminoma mature high)` (n = 13) containing samples showing the 
lowest yolk sac (2.00%) and highest maturate tissue (95.00%) content [Shen2018]_.
This separation is further confirmed in the case of :abbr:`T108 TGCT nonSEM YOLK H (Testicular germ cell tumour non-seminoma yolk sac high)` by gene sets, 
where we see an enrichment of yolk sac tumours genes 
(:abbr:`medNES (median Normalized Enrichment Score)` = 2.26, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.21e-05) [Korkola2006]_.
|br| |br|
:abbr:`T105 TGCT nonSEM EMB (Testicular germ cell tumour non-seminoma embryonal carcinoma rich)`, containing :abbr:`TGCT (testicular germ cell tumour)`  
of the embryonal subtype, splits into two subclasses. :abbr:`T112 TGCT nonSEM EMB I (Testicular germ cell tumour non-seminoma embryonal carcionma intermediate)` 
(n = 20) contains samples with mixed clinical annotation, while :abbr:`T113 TGCT nonSEM EMB H (Testicular germ cell tumour non-seminoma embryonal carcinoma high)` 
(n = 25) is composed almost entirely of samples marked as embryonal. 
The embryonal carcinoma percentages (median 40.00% vs. 100.00%, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)`  = 5.11e-05) 
further the idea of a continuous spectrum of tissue type between these clusters, analogous to what we observed in the subtypes of 
:abbr:`T101  (Testicular germ cell tumour non-seminoma, mature teratoma or yolk sac tumour)`. Here, 
:abbr:`T113 TGCT nonSEM EMB H (Testicular germ cell tumour non-seminoma embryonal carcinoma high)` 
contains samples almost exclusively composed of embryonal tissue, while 
:abbr:`T112 TGCT nonSEM EMB I (Testicular germ cell tumour non-seminoma embryonal carcionma intermediate)` contains samples with a more intermediate component. 
This is confirmed by gene set enrichment, where :abbr:`T112 TGCT nonSEM EMB I (Testicular germ cell tumour non-seminoma embryonal carcionma intermediate)` 
is enriched for yolk sac and teratoma gene sets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.24 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value ≤ 1.00e-5)` 
while :abbr:`T113 TGCT nonSEM EMB H (Testicular germ cell tumour non-seminoma embryonal carcinoma high)` 
is enriched for an established embryonal carcinoma gene sets (:abbr:`medNES (median Normalized Enrichment Score)` = 1.04, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value = 1.15e-03)` [Korkola2005]_. 

.. figure:: /img/mesd12.png
   :alt: Fig. MESD12
   :name: fig-mesd12
   :width: 400px
   
   MESD12: 2-dimensional UMAP projection of TGCT by gene expression. 
   On the left, the subtypes identified are shown with different colours. 
   On the right, samples are coloured by their relative proprtion of cell populations by type and level of maturation.
   

Wilms Tumour
============

When comparing the major Wilms tumour cluster :abbr:`T092 WILMS (Wilms tumour)` to 
:abbr:`T099 UCS MYO (Uterine carcinosarcoma, myogenic differentiation)`, we observe significantly higher expression 
of metanephrogenic genes *PAX2* (:abbr:`logFC (log-Fold Change)` = 1.81, :abbr:`FDR (False Discovery Rate)` = 1.03e-07), 
*OSR1* (:abbr:`logFC (log-Fold Change)` = 1.77, :abbr:`FDR (False Discovery Rate)` = 9.07e-04), *EYA1* (:abbr:`logFC (log-Fold Change)` = 1.44, 
:abbr:`FDR (False Discovery Rate)` = 1.17e-06), *MEOX1* (:abbr:`logFC (log-Fold Change)` = 1.13, :abbr:`FDR (False Discovery Rate)` = 2.269e-03), 
and *SALL2* (:abbr:`logFC (log-Fold Change)` = 0.96, :abbr:`FDR (False Discovery Rate)` = 3.962e-04) [Li2002]_, 
suggesting these tumours to have an expression profile closer to the kidney. 
:abbr:`T092 WILMS (Wilms tumour)` then divides into 5 different subtypes with characteristic transcriptional profiles (Fig. :ref:`MESD1b <fig-mesd1>`), 
in line with :abbr:`FHWT (favourable histology)`  transcriptional clusters recently described by a joint COG-TARGET initiative [Gadd2017]_. 
|br|
Importantly, we observe a mixture of both :abbr:`FHWT (favourable histology)` 
and :abbr:`DAWT (diffuse analplasia)`  categories across all classes; however, all our bona 
fide Wilms subtypes (children of :abbr:`T092 WILMS (Wilms tumour)` ) have significantly higher proportion of :abbr:`FHWT (favourable histology)`, 
apart from :abbr:`T117 WILMS KDEV (Wilms tumour high kidney development by estrogen and NOTCH)` which is evenly divided. 
:abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` is the only Wilms tumour group to have a higher :abbr:`DAWT (diffuse analplasia)` 
component (see section on the :ref:`Myogenic` group) and is the only one composed exclusively of histologically mixed tumours [Gadd2017]_. 
|br| |br|
:abbr:`T114 WILMS PI3K/MTOR (Wilms tumour high PI3K/MTOR and vasculogenesis)` (n=11) is the smallest cluster and is 
exclusively composed of COG-TARGET :abbr:`FHWT (favourable histology)` 
expression cluster 2 samples (:abbr:`χ2 p-val (χ2 test p-value)` = 5.587e-07) [Gadd2017]_ 
and is defined by significant enrichment of gene sets related to *PI3K-mTOR* signalling 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.14e-04) 
and the interferon response (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.32e-04) 
(Fig. :ref:`MESD13 <fig-mesd13>`). It also exclusively contains *SIX1/2* mutants (n = 5 and 4, respectively). 
Furthermore, it has the greatest proportion of blastemal samples (6/7, :abbr:`χ2 p-val (χ2 test p-value)` = 5.74e-04) [Gadd2017]_.
|br| |br|
:abbr:`T115 WILMS OXYPHO (Wilms tumour high oxidative phosphorilation)`(n = 27), the largest cluster, is defined by 
enrichment of gene sets related to oxidative phosphorylation (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.06, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.13e-08, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02) 
and low expression of mitotic spindle related sets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 0.90, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.03e-10, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03) [Liberzon2015]_ 
(Fig. :ref:`MESD13 <fig-mesd13>`), which is similar to COG-TARGET cluster 5 [Gadd2017]_. 
That :abbr:`T115 WILMS OXYPHO (Wilms tumour high oxidative phosphorilation)` is the only cluster to contain expression class 5 
:abbr:`FHWT (favourable histology)`  samples (:abbr:`χ2 p-val (χ2 test p-value)` = 2.03e-3) 
confirms this identity, though it also contains an equal number of expression class 1 and class 2 samples. 
Like :abbr:`T114 WILMS PI3K/MTOR (Wilms tumour high PI3K/MTOR and vasculogenesis)`, 
:abbr:`T115 WILMS OXYPHO (Wilms tumour high oxidative phosphorilation)` is also composed of a majority of blastemal samples (11/17) [Gadd2017]_. 
|br| |br|
:abbr:`T116 WILMS EMT (Wilms tumour high EMT)` (n = 26) is defined by enrichment of gene sets related to 
:abbr:`EMT (epithelilal mesenchymal transition)` (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.41e-08, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) and 
angiogenesis (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.30e-06) [Liberzon2015]_ 
(Fig. :ref:`MESD13 <fig-mesd13>`). 
It also exhibits the lowest expression of WT1 amongst its siblings (median :abbr:`logFC (log-Fold Change)` = -1.24, 
:abbr:`FDR (False Discovery Rate)` ≤ 1.30e-02). It should be noted that this expression profile also corresponds to 
:abbr:`T096 WILMS MYO (Wilms striated-muscle-like)`, with these two classes corresponding to the profile of COG-TARGET cluster 4. 
However, while :abbr:`T116 WILMS EMT (Wilms tumour high EMT)` is composed of a majority of expression class 3 samples 
(13/23, :abbr:`χ2 p-val (χ2 test p-value)` = 6.806e-05), it and :abbr:`T096 WILMS MYO (Wilms striated-muscle-like)` 
contain the largest expression class 4 components (n = 3 each). 
:abbr:`T116 WILMS EMT (Wilms tumour high EMT)` is composed mainly of mixed tumours (15/23), 
and also contains the majority of :abbr:`FHWT (favourable histology)`  samples marked as having WT1 loss 
(:abbr:`χ2 p-val (χ2 test p-value)` = 3.04e-02) [Gadd2017]_. 
|br| |br|
:abbr:`T117 WILMS KDEV (Wilms tumour high kidney development by estrogen and NOTCH)` (n = 23) is defined by enrichment 
of the estrogen (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.07, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` ≤ 1.67e-06) and androgen responses (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.05, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.38e-04, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) and notch signalling (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.04, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.97e-08) [Liberzon2015]_; consequently, gene sets for kidney development relating to the ureteric metanephric mesenchyme (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.54, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 4.68e-04, :abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-02) and loop of Henle (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 8.11, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.25e-08) ([Ashburner2000]_; [TGOC2019]_) are also upregulated (Fig. :ref:`S24e <INSERT_FIGURE>`). 
It is the only cluster to contain COG-TARGET expression class 6 samples (n = 3, :abbr:`χ2 p-val (χ2 test p-value)` = 2.61e-04) 
but contains a higher amount of class 3 samples (n = 6). It contains the highest number of *TP53* mutants, and is 
composed entirely of mixed and epithelial tumours (5/9 and 4/9, respectively) [Gadd2017]_. 
|br| |br|
Finally, :abbr:`T118 WILMS E2F (Wilms tumour high E2F proliferation)` (n = 26) is defined by enrichment cell proliferation sets, 
including the G2M checkpoint (:abbr:`medNES (median Normalized Enrichment Score)` = 1.01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.39e-03) 
and mitotic spindle (:abbr:`medNES (median Normalized Enrichment Score)` = 1.03 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 6.03e-10) [Liberzon2015]_, 
as well as genesets for E2F (E2F6 :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.86e-03, 
and E2F1 activity (:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.82e-06) 
[ENCODE2012]_, and histone modifications (Fig. :ref:`S24e <INSERT_FIGURE>`). 
Given its enrichment for E2F signalling and proliferative gene sets, :abbr:`T118 WILMS E2F (Wilms tumour high E2F proliferation)` 
corresponds to COG-TARGET cluster 1. Indeed, it is the only cluster to be composed of a majority of expression class 1 samples 
(14/17, :abbr:`χ2 p-val (χ2 test p-value)` = 1.927e-05). Its samples exhibit variable histology, with a majority of samples being blastemal 
(8/17), with smaller mixed (5/7) and epithelial (4/17) components.
Although no differences in survival reached significance between any of the clusters (:abbr:`lrt p-val (log-rank test p-value)` = 7.40e-02 at 4795 days), 
:abbr:`T118 WILMS E2F (Wilms tumour high E2F proliferation)` exhibits the worst overall survival and is the only cluster to 
reach median :abbr:`OS (overall survival)` (1229 days post-diagnosis). 
|br|
Our clusters of Wilms tumours seem to represent a spectrum of differentiation from blastemal 
through mixed to epithelial tumours, similar to the :abbr:`TGCT NO-SEM (testicular germ cell tumour non-seminomas)` described previously.

.. figure:: /img/mesd13.png
   :alt: Fig. MESD13
   :name: fig-mesd13
   :width: 300px
   
   MESD13: Distribution plots of normalized enrichment score of gene sets relevant to the definition
   of Wilms tumour subtypes.

Bibliography
===========================
.. [Alakus2015] Alakus, H., Yost, S.E., Woo, B., et al. 2015. BAP1 mutation is a frequent somatic event in peritoneal malignant mesothelioma. Journal of Translational Medicine 13, p. 122.
.. [An2017] An, Y., Wang, H., Jie, J., et al. 2017. Identification of distinct molecular subtypes of uterine carcinosarcoma. Oncotarget 8(9), pp. 15878–15886.
.. [Anderson2021] Anderson, N.D., Babichev, Y., Fuligni, F., et al. 2021. Lineage-defined leiomyosarcoma subtypes emerge years before diagnosis and determine patient survival. Nature Communications 12(1), p. 4496.
.. [Ashburner2000] Ashburner, M., Ball, C.A., Blake, J.A., et al. 2000. Gene Ontology: tool for the unification of biology. Nature Genetics 25(1), pp. 25–29.
.. [Barr2002] Barr, F.G., Qualman, S.J., Macris, M.H., et al. 2002. Genetic heterogeneity in the alveolar rhabdomyosarcoma subset without typical gene fusions. Cancer Research 62(16), pp. 4704–4710.
.. [Carregaro2013] Carregaro, F., Stefanini, A.C.B., Henrique, T. and Tajara, E.H. 2013. Study of small proline-rich proteins (SPRRs) in health and disease: a review of the literature. Archives of Dermatological Research 305(10), pp. 857–866.
.. [Conner2013] Conner, J.R. and Hornick, J.L. 2013. SATB2 is a novel marker of osteoblastic differentiation in bone and soft tissue tumours. Histopathology 63(1), pp. 36–49.
.. [Costa2019] Costa, A.D.A. and Gutmann, D.H. 2019. Brain tumors in Neurofibromatosis type 1. Neuro-Oncology Advances 1(1), p. vdz040.
.. [Cherniack2017] Cherniack AD, Shen H, Walter V, Stewart C, Murray BA, Bowlby R, et al. Integrated molecular characterization of uterine carcinosarcoma. Cancer Cell. 2017 Mar 13;31(3):411–23.
.. [Davicioni2009] Davicioni, E., Anderson, M.J., Finckenstein, F.G., et al. 2009. Molecular classification of rhabdomyosarcoma--genotypic and phenotypic determinants of diagnosis: a report from the Children’s Oncology Group. The American Journal of Pathology 174(2), pp. 550–564.
.. [Deyrup2007] Deyrup, A.T. and Montag, A.G. 2007. Epithelioid and Epithelial Neoplasms of Bone. Archives of Pathology & Laboratory Medicine.
.. [ENCODE2012] ENCODE Project Consortium 2012. An integrated encyclopedia of DNA elements in the human genome. Nature 489(7414), pp. 57–74.
.. [Gadd2017] Gadd, S., Huff, V., Walz, A.L., et al. 2017. A Children’s Oncology Group and TARGET initiative exploring the genetic landscape of Wilms tumor. Nature Genetics 49(10), pp. 1487–1494.
.. [Gerhart2019] Gerhart, J., Behling, K., Paessler, M., et al. 2019. Rhabdomyosarcoma and Wilms tumors contain a subpopulation of noggin producing, myogenic cells immunoreactive for lens beaded filament proteins. Plos One 14(4), p. e0214758.
.. [Gjerstorff2015] Gjerstorff, M.F., Andersen, M.H. and Ditzel, H.J. 2015. Oncogenic cancer/testis antigens: prime candidates for immunotherapy. Oncotarget 6(18), pp. 15772–15787.
.. [Gryder2017] Gryder, B.E., Yohe, M.E., Chou, H.-C., et al. 2017. PAX3-FOXO1 Establishes Myogenic Super Enhancers and Confers BET Bromodomain Vulnerability. Cancer discovery 7(8), pp. 884–899.
.. [Hirota1998] Hirota, S., Isozaki, K., Moriyama, Y., et al. 1998. Gain-of-function mutations of c-kit in human gastrointestinal stromal tumors. Science 279(5350), pp. 577–580.
.. [Hmeljak2018] Hmeljak, J., Sanchez-Vega, F., Hoadley, K.A., et al. 2018. Integrative molecular characterization of malignant pleural mesothelioma. Cancer discovery 8(12), pp. 1548–1565.
.. [Hu2016] Hu, K., Dai, H.-B. and Qiu, Z.-L. 2016. mTOR signaling in osteosarcoma: Oncogenesis and therapeutic aspects (Review). Oncology Reports 36(3), pp. 1219–1225.
.. [Kawai1998] Kawai, A., Huvos, A.G., Meyers, P.A. and Healey, J.H. 1998. Osteosarcoma of the pelvis. Oncologic results of 40 patients. Clinical Orthopaedics and Related Research (348), pp. 196–207.
.. [Kim2020] Kim, Y.-S., Shin, S., Jung, S.-H. and Chung, Y.-J. 2020. Pathogenic NF1 truncating mutation and copy number alterations in a dedifferentiated liposarcoma with multiple lung metastasis: a case report. BMC Medical Genetics 21(1), p. 200.
.. [Kiuru2017] Kiuru, M. and Busam, K.J. 2017. The NF1 gene in tumor syndromes and melanoma. Laboratory Investigation 97(2), pp. 146–157.
.. [Kohsaka2014] Kohsaka, S., Shukla, N., Ameur, N., et al. 2014. A recurrent neomorphic mutation in MYOD1 defines a clinically aggressive subset of embryonal rhabdomyosarcoma associated with PI3K-AKT pathway mutations. Nature Genetics 46(6), pp. 595–600.
.. [Korkola2006] Korkola, J.E., Houldsworth, J., Chadalavada, R.S.V., et al. 2006. Down-regulation of stem cell genes, including those in a 200-kb gene cluster at 12p13.31, is associated with in vivo differentiation of human male germ cell tumors. Cancer Research 66(2), pp. 820–827.
.. [Korkola2005] Korkola, J.E., Houldsworth, J., Dobrzynski, D., et al. 2005. Gene expression-based classification of nonseminomatous male germ cell tumors. Oncogene 24(32), pp. 5101–5107.
.. [Kossler2011] Kossler, N., Stricker, S., Rödelsperger, C., et al. 2011. Neurofibromin (Nf1) is required for skeletal muscle development. Human Molecular Genetics 20(14), pp. 2697–2709.
.. [Li2002] Li, C.-M., Guo, M., Borczuk, A., et al. 2002. Gene expression in Wilms’ tumor mimics the earliest committed stage in the metanephric mesenchymal-epithelial transition. The American Journal of Pathology 160(6), pp. 2181–2190.
.. [Liberzon2015] Liberzon, A., Birger, C., Thorvaldsdóttir, H., Ghandi, M., Mesirov, J.P. and Tamayo, P. 2015. The Molecular Signatures Database (MSigDB) hallmark gene set collection. Cell Systems 1(6), pp. 417–425.
.. [Makise2017] Makise, N., Yoshida, A., Komiyama, M., et al. 2017. Dedifferentiated liposarcoma with epithelioid/epithelial features. The American Journal of Surgical Pathology 41(11), pp. 1523–1531.
.. [Mehrain2013] Mehrain, R. and Nabahati, M. 2013. A case of rhabdomyosarcoma of kidney mimicking nephroblastoma. Caspian journal of internal medicine 4(1), pp. 621–623.
.. [Newman2015] Newman, A.M., Liu, C.L., Green, M.R., et al. 2015. Robust enumeration of cell subsets from tissue expression profiles. Nature Methods 12(5), pp. 453–457.
.. [Parham2013] Parham, D.M. and Barr, F.G. 2013. Classification of rhabdomyosarcoma and its molecular basis. Advances in Anatomic Pathology 20(6), pp. 387–397.
.. [Pemov2020] Pemov, A., Li, H., Presley, W., Wallace, M.R. and Miller, D.T. 2020. Genetics of human malignant peripheral nerve sheath tumors. Neuro-Oncology Advances 2(Suppl 1), pp. i50–i61.
.. [Pulford2017] Pulford, E., Huilgol, K., Moffat, D., Henderson, D.W. and Klebe, S. 2017. Malignant mesothelioma, BAP1 immunohistochemistry, and VEGFA: does BAP1 have potential for early diagnosis and assessment of prognosis? Disease markers 2017, p. 1310478.
.. [Quesada2012] Quesada, J. and Amato, R. 2012. The molecular biology of soft-tissue sarcomas and current trends in therapy. Sarcoma 2012, p. 849456.
.. [Saab2005] Saab, R., Rao, B.N., Rodriguez-Galindo, C., Billups, C.A., Fortenberry, T.N. and Daw, N.C. 2005. Osteosarcoma of the pelvis in children and young adults: the St. Jude Children’s Research Hospital experience. Cancer 103(7), pp. 1468–1474.
.. [Samkari2018] Samkari, A. and Al-Maghrabi, H. 2018. Rhabdomyosarcoma of the kidney. Journal of Pediatric Surgery Case Reports 32, pp. 62–67.
.. [Schaefer2009] Schaefer, C.F., Anthony, K., Krupa, S., et al. 2009. PID: the pathway interaction database. Nucleic Acids Research 37(Database issue), pp. D674-9.
.. [Shen2018] Shen, H., Shih, J., Hollern, D.P., et al. 2018. Integrated molecular characterization of testicular germ cell tumors. Cell reports 23(11), pp. 3392–3406.
.. [Smith2015] Smith, S.C., Buehler, D., Choi, E.-Y.K., et al. 2015. CIC-DUX sarcomas demonstrate frequent MYC amplification and ETS-family transcription factor expression. Modern Pathology 28(1), pp. 57–68.
.. [Smithey2002] Smithey, B.E., Pappo, A.S. and Hill, D.A. 2002. C-kit expression in pediatric solid tumors: a comparative immunohistochemical study. The American Journal of Surgical Pathology 26(4), pp. 486–492.
.. [Specht2014] Specht, K., Sung, Y.-S., Zhang, L., Richter, G.H.S., Fletcher, C.D. and Antonescu, C.R. 2014. Distinct transcriptional signature and immunoprofile of CIC-DUX4 fusion-positive round cell tumors compared to EWSR1-rearranged Ewing sarcomas: further evidence toward distinct pathologic entities. Genes, Chromosomes & Cancer 53(7), pp. 622–633.
.. [TCGA2017] The Cancer Genome Atlas Research Network 2017. Comprehensive and integrated genomic characterization of adult soft tissue sarcomas. Cell 171(4), p. 950–965.e28.
.. [TGOC2019] The Gene Ontology Consortium 2019. The Gene Ontology Resource: 20 years and still GOing strong. Nucleic Acids Research 47(D1), pp. D330–D338.
.. [Thorsson2018] Thorsson, V., Gibbs, D.L., Brown, S.D., et al. 2018. The immune landscape of cancer. Immunity 48(4), p. 812–830.e14.
.. [Thway2016] Thway, K., Jones, R.L., Noujaim, J. and Fisher, C. 2016. Epithelioid sarcoma: diagnostic features and genetics. Advances in Anatomic Pathology 23(1), pp. 41–49.
.. [Williamson2010] Williamson, D., Missiaglia, E., de Reyniès, A., et al. 2010. Fusion gene-negative alveolar rhabdomyosarcoma is clinically and molecularly indistinguishable from embryonal rhabdomyosarcoma. Journal of Clinical Oncology 28(13), pp. 2151–2158.
.. [Yang2018] Yang, L., Forker, L., Irlam, J.J., Pillay, N., Choudhury, A. and West, C.M.L. 2018. Validation of a hypoxia related gene signature in multiple soft tissue sarcoma cohorts. Oncotarget 9(3), pp. 3946–3955.
.. [Yoshimoto2017] Yoshimoto, T., Tanaka, M., Homme, M., et al. 2017. CIC-DUX4 Induces Small Round Cell Sarcomas Distinct from Ewing Sarcoma. Cancer Research 77(11), pp. 2927–2937.
.. [Zou2012] Zou, C., Shen, J., Tang, Q., et al. 2012. Cancer-testis antigens expressed in osteosarcoma identified by gene microarray correlate with a poor patient prognosis. Cancer 118(7), pp. 1845–1855.
