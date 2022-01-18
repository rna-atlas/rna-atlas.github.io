.. |br| raw:: html

  <br/>

=============
T005 Leukemia
=============

Version: |version|
|br| 
Last change: |today|

We observe a separation between acute lymphoblastic leukemia (ALL), which cluster in 
:abbr:`T119 ALL (Acute lymphoblastic leukemia)` (n = 334), and acute myeloid leukemia (AML), 
which cluster in :abbr:`T120 AML (Acute myeloid leukemia)` (n = 472) at the second hierarchical level. 
A significant difference in age is expected due to the different etiologies 
(median age 7.16 vs 16.76 :abbr:`y.o. (years old)`, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.98e-23) 
and the presence of both adult and pediatric populations in both groups to different degrees. 
No significant difference in :abbr:`OS (overall survival)` is observed.

Acute lymphoblastic leukemia
============================

Within the lymphoblastic branch, we immediately observe the separation of a small group of infant leukemias with *KMT2A* rearrangements, 
found in :abbr:`T121 ALL INF KMT2Ar (Infant acute lymphoblastic leukemia, KMT2A rearrangement)` (n =14), from all other diagnoses, in 
:abbr:`T122 ALL A (Acute lymphoblastic leukemia mix A)` (n = 320) (Fig. :ref:`LEU1 <fig-leu1>`). 

.. figure:: /img/leu1.png
   :alt: Fig. LEU1
   :name: fig-leu1
   :width: 500px
   
   LEU1: A, 2-dimensional UMAP projection of acute lymphoid leukemia tumors by gene expression. Subtypes at the third level of the hierarchy
   are shown with different colours. B, the list of all acute lymphoid leukemia subtypes identified
   and their hierarchical relationship. 

:abbr:`T121 ALL INF KMT2Ar (Infant acute lymphoblastic leukemia, KMT2A rearrangement)` contains most samples marked as infant 
(6 vs 1 :abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16) and mixed-lineage leukemia 
(4 vs 0, :abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16) and has a significantly younger median age 
(0.73 vs 7.20 :abbr:`y.o. (years old)`, MWU p-value = 4.37e-02).
We confirmed this annotation with gene sets, as :abbr:`T121 ALL INF KMT2Ar (Infant acute lymphoblastic leukemia, KMT2A rearrangement)` 
is highly enriched for *KMT2A* downstream targets (:abbr:`medNES (median Normalized Enrichment Score)` = 1.50 , 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.47e-09) [Ross2004]_ (Fig. :ref:`LEU2 <fig-leu2>`).

.. figure:: /img/leu2.png
   :alt: Fig. LEU2
   :name: fig-leu2
   :width: 400px
   
   LEU2: Distribution plots of the expression of genes and gene sets relevant to the definition
   of the KMT2A-rearranged lymphoblastic leukemia class.

:abbr:`T122 ALL A (Acute lymphoblastic leukemia mix A)` further splits into two subclasses, 
:abbr:`T123 ALL B (Acute lymphoblastic leukemia mix B)` (n = 127) and :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))` (n = 193) 
(Fig. :ref:`LEU1b <fig-leu1>`), containing most of samples from TARGET. 
Gene sets analysis between all TARGET leukemia samples and the remaining cohort shows enrichment 
(:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` < 1.00e-10) of poly-A RNA binding, 
ribonucleoprotein complex, RNA processing, ribosomal and mitochondrial pathways, and oxidative phosphorylation [Ashburner2000]_, [The2019]_ 
in :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))`. 
Furthermore, :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))` has a lower median age 
(6.41 vs 13.17 :abbr:`y.o. (years old)`, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 5.04e-08). 
We couldn’t identify any biological driver behind the split between :abbr:`T123 ALL B (Acute lymphoblastic leukemia mix B)` 
and :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))` with statistical certainty; stringent low variance genes 
removal or more advanced batch effect removal methods (e.g. COMBaT [Lazar2013]_) weren’t enough to assure complete 
compatibility between the TARGET cohort and the rest of the dataset without the loss of information and damage to the subtyping process. 
We decided to keep the clusters separate as by choice of the algorithm and further investigate their subtypes independently, 
to maintain tumour subtypes that were exclusive of one or the other cohorts and increase the classifier range. 

Acute lymphoblastic leukemia, non-TARGET cohort
===============================================

At the next level within :abbr:`T123 ALL B (Acute lymphoblastic leukemia mix B)`, we observe the separation of 
:abbr:`T126 ALL ETV6-RUNX1 (Acute lymphoblastic leukemia, ETV6-RUNX1 fusion)` (n = 20) a small class of samples marked with 
*ETV6-RUNX1* fusion (:abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16) from the remaining :abbr:`ALL (Acute lymphoblastic leukemia)` 
in :abbr:`T125 ALL C (Acute lymphoblastic leukemia mix C)` (n=107) (Fig. :ref:`LEU1b <fig-leu1>``). 
The t(12;21)(p13;q22) translocation which results from this fusion is often accompanied by copy number gains in *RUNX1*, 
which is overexpressed in :abbr:`T126 ALL ETV6-RUNX1 (Acute lymphoblastic leukemia, ETV6-RUNX1 fusion)` 
(:abbr:`logFC (log-Fold Change)` = 4.17e-01, :abbr:`FDR (False Discovery Rate)` = 3.33e-03). 
Compared to patients in :abbr:`T125 ALL C (Acute lymphoblastic leukemia mix C)`, those in 
:abbr:`T126 ALL ETV6-RUNX1 (Acute lymphoblastic leukemia, ETV6-RUNX1 fusion)` are significantly younger 
(14.5 vs. 4.46 :abbr:`y.o. (years old)`, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 3.29e-08) [Sun2017]_.
|br| |br|
The children of :abbr:`T125 ALL C (Acute lymphoblastic leukemia mix C)` separate into 
:abbr:`T128 ALL ERGdel (Acute lymphoblastic leukemia, ERG deletion)` (n = 36) and 
:abbr:`T127 ALL Ph-like (Acute lymphoblastic leukemia, Philadelphia-like)` (n = 71) (Fig. :ref:`LEU1b <fig-leu1>`). 
|br| |br|
:abbr:`T128 ALL ERGdel (Acute lymphoblastic leukemia, ERG deletion)` is characterized by tumours carrying 
*ERG* deletions (15 vs. 55, :abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16), and exhibits characteristic overexpression of 
*CHST2* (:abbr:`logFC (log-Fold Change)` = -4.48, :abbr:`FDR (False Discovery Rate)` = 5.742e-33), 
*PTPRM* (:abbr:`logFC (log-Fold Change)` = -7.64, :abbr:`FDR (False Discovery Rate)` = 2.987e-32), and 
*GPR49/AGAP1* (:abbr:`logFC (log-Fold Change)` = -6.23, :abbr:`FDR (False Discovery Rate)` = 3.201e-31) [Yeoh2002]_. 
The majority of samples in T127 are composed of Ph-like tumours of various classes (:abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) [Jain2017]_. 
|br| |br|
:abbr:`T127 ALL Ph-like (Acute lymphoblastic leukemia, Philadelphia-like)` then further subdivides in two child nodes, 
:abbr:`T129 ALL Ph-like A (Acute lymphoblastic leukemia, Philadelphia-like mixed alterations A)` (n = 41) and 
:abbr:`T130 ALL Ph-like IKZF1/JAK2 (Acute lymphoblastic leukemia, Philadelphia-like, IKZF1 or JAK2 fusion)` (n = 29) (Fig. :ref:`LEU1b <fig-leu1>`). 
Both contain small populations of *BCR-ABL1* fusion samples (Ph+) (11 and 5, ns) and Philadelphia-like (Ph-like) samples (13 and 14, ns). 
While :abbr:`T129 ALL Ph-like A (Acute lymphoblastic leukemia, Philadelphia-like mixed alterations A)` contains the majority of 
Ph-like non- *CRFL2* tumours (11/28 vs. 14/19, :abbr:`χ2 p-val (χ2 test p-value)` = 4.32e-02), 
there is no corresponding enrichment of this signature via gene sets analysis. 
However, the two differ by some specific lesions known to be present in the Ph-like group: 
:abbr:`T129 ALL Ph-like A (Acute lymphoblastic leukemia, Philadelphia-like mixed alterations A)` contains 6 
*JAK2* fusion samples (0/13 vs 6/14, :abbr:`χ2 p-val (χ2 test p-value)` = 2.69e-02), 
while :abbr:`T130 ALL Ph-like IKZF1/JAK2 (Acute lymphoblastic leukemia, Philadelphia-like, IKZF1 or JAK2 fusion)` contains all 
*EPO* fusion samples (4/13 vs. 0/14, :abbr:`FET p-val (Fisher's exact test p-value)` 4.07e-02). 
Both contain other *JAK/STAT* alterations (4/13 vs. 3/14, ns), and two of other *ABL1/2* fusion samples each. 
:abbr:`T130 ALL Ph-like IKZF1/JAK2 (Acute lymphoblastic leukemia, Philadelphia-like, IKZF1 or JAK2 fusion)` 
is also enriched for tumours with concurrent *IKZF1* alterations (11/28 vs. 14/19, :abbr:`χ2 p-val (χ2 test p-value)` = 4.32e-02).
|br|
:abbr:`T129 ALL Ph-like A (Acute lymphoblastic leukemia, Philadelphia-like mixed alterations A)`  
then divides into two further subtypes, :abbr:`T131 ALL Ph-like JAK/STAT (Acute lymphoblastic leukemia, Philadelphia-like, BCR-ABL or other JAK/STAT)` 
(n=23) and :abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)` (n =12) (Fig. :ref:`LEU3a <fig-leu3>`). 
:abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)` contains the majority of 
*BCR-ABL1* fusion samples (3/23 vs. 8/12, p-val = 4.23e-03). 
Of the Ph-like samples for which we have annotation,  
:abbr:`T131 ALL Ph-like JAK/STAT (Acute lymphoblastic leukemia, Philadelphia-like, BCR-ABL or other JAK/STAT)` 
contains 4 unspecified *JAK/STAT* mutants along with an additional *CRLF2-JAK* mutant, a *CRFL2* rearranged sample with no 
*JAK* rearrangements, and a *RAS* mutant (Fig. :ref:`LEU3a <fig-leu3>`).
:abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)` contains 3 
*EPOR-IGH* fusion samples, while  :abbr:`T131 ALL Ph-like JAK/STAT (Acute lymphoblastic leukemia, Philadelphia-like, BCR-ABL or other JAK/STAT)` 
contains an *EPOR-IGK* fusion (:abbr:`n.s. (not significant)`).
Both groups contain one *ABL* fusion without *CRFL2* rearrangement, while Ph-like non-*CRLF2* samples are evenly 
divided between the clusters (7/20 vs. 4/8, :abbr:`n.s. (not significant)`). 
Another interesting distinction is that  :abbr:`T131 ALL Ph-like JAK/STAT (Acute lymphoblastic leukemia, Philadelphia-like, BCR-ABL or other JAK/STAT)` 
is enriched for tumours with cell-cycle related lesions, either in *TP53*, 
*CDK2NA/B*, or *RB1* (14/20 vs. 1/8, :abbr:`χ2 p-val (χ2 test p-value)` = 1.95e-2). 
:abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)`, 
however, is enriched for samples with concurrent *IKZF1* alterations (5/20 vs. 6/8, :abbr:`χ2 p-val (χ2 test p-value)` = 4.35e-02), 
though these are heterogeneous and have some overlap between the two clusters [Harvey2013]_. 
Gene set enrichment analysis demonstrates :abbr:`T131 ALL Ph-like JAK/STAT (Acute lymphoblastic leukemia, Philadelphia-like, BCR-ABL or other JAK/STAT)` 
to be enriched for non-Ph-like *CRFL2* rearranged samples (:abbr:`medNES (median Normalized Enrichment Score)` = 1.57, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 4.70e-05),
while :abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)` 
is enriched for Ph-like samples with *CRFL2* rearrangments 
(:abbr:`medNES (median Normalized Enrichment Score)` = 2.68, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 1.61e-07) 
[Sadras2017]_ (Fig. :ref:`LEU3b <fig-leu3>`), suggesting that 
:abbr:`T132 ALL Ph+/Ph-like EPOR (Acute lymphoblastic leukemia Philadelphia-like, EPOR fusion)` may contain 
*CRFL2*-rearranged samples which have not been annotated as such.


.. figure:: /img/leu3.png
   :alt: Fig. LEU3
   :name: fig-leu3
   :width: 500px
   
   LEU3: A, 2-dimensional UMAP projection of acute lymphoid leukemia tumors by gene expression. On the left, subtypes
   are shown with different colours, on the right they are coloured by lesions reported by the presenting institution. 
   B, Distribution plots of the expression of genes and gene sets relevant to the definition
   of the identified Ph-like lymphoblastic leukemia subtypes within the non-TARGET cohort (top) and the TARGET cohort (bottom).


Acute lymphoblastic leukemia, TARGET cohort
===========================================

The TARGET :abbr:`ALL (Acute lymphoblastic leukemia)` cluster, :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))`, 
divides into four classes (Fig. :ref:`LEU1b <fig-leu1>`, :ref:`LEU4 <fig-leu4>`)

.. figure:: /img/leu4.png
   :alt: Fig. LEU4
   :name: fig-leu4
   :width: 500px
   
   LEU4: 2-dimensional UMAP projection of acute lymphoid leukemia tumors from the TARGET cohort by gene expression. On the left, subtypes
   are shown with different colours, on the right they are coloured by lesions reported by the presenting institution. 

:abbr:`T133 ALL TRG A (Acute lymphoblastic leukemia (TARGET) mix A)` (n = 109) is the largest cluster and contains a 
mixture of genomic alterations: :abbr:`ALL (Acute lymphoblastic leukemia)` with hyperdiploidy without trisomy of 
chr4 and ch10 (:abbr:`χ2 p-val (χ2 test p-value)` = 3.31e-4), :abbr:`ALL (Acute lymphoblastic leukemia)` with 
hyperdiploidy with trisomy chr4 and ch10, samples with iAMP21, plus a number of unspecified samples 
(Fig. :ref:`LEU4 <fig-leu4>`). 
The cluster is characterized by significant overexpression of *CRLF2* (:abbr:`logFC (log-Fold Change)`= 4.96, :abbr:`FDR (False Discovery Rate)` ≤ 7.749e-04). 
Indeed, gene set enrichment analysis confirmed this cluster contains a sizeable population of 
Ph+ and Ph-like samples (:abbr:`medNES (median Normalized Enrichment Score)` = 79.08, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 7.03e-14, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03). 
|br| |br|
:abbr:`T134 ALL TRG ZNF384 (Acute lymphoblastic leukemia (TARGET) ZNF384 rearrangement)` (n = 13) 
is the smallest cluster and contains the oldest group of patients (median age 13.23 
:abbr:`y.o. (years old)`, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.13e-03). 
Patients with :abbr:`ALL (Acute lymphoblastic leukemia)` in this cluster display the best overall survival 
(:abbr:`lrt p-val (log-rank test p-value)` < 1e-04). 
Gene set enrichment analysis of genes upregulated and downregulated in *ZNF384*-rearanged 
:abbr:`ALL (Acute lymphoblastic leukemia)` demonstrates a characteristic gene expression pattern of 
*ZNF384*-fusion downstream targets, in both upregulated (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.51, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 5.56e-16 , 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) and 
donwregulated targets (:abbr:`medNES (median Normalized Enrichment Score)` ≤ 4.81e-01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 2.59e-16, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04), respectively [Qian2017]_, [Hirabayashi2017]_ 
(Fig. :ref:`LEU5 <fig-leu5>`). 

.. figure:: /img/leu5.png
   :alt: Fig. LEU5
   :name: fig-leu5
   :width: 200px

   LEU5: Distribution plots of the expression of genes and gene sets relevant to the definition
   of the ZNF384A-rearranged lymphoblastic leukemia class.

:abbr:`T135 ALL TRG TCF3 (Acute lymphoblastic leukemia (TARGET) TCF3 rearrangment)` (n = 30) is comprised of samples harbouring both 
*TCF3-PBX1* (n = 19, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) and *TCF3-HLF* (n = 3, :abbr:`χ2 p-val (χ2 test p-value)` = 1.60e-02) 
fusions. 
Out of all TARGET :abbr:`ALL (Acute lymphoblastic leukemia)` subgroups, 
:abbr:`T135 ALL TRG TCF3 (Acute lymphoblastic leukemia (TARGET) TCF3 rearrangment)` contains the patient group with the worst overall survival, 
reaching median :abbr:`OS (overall survival)` at 483 days (:abbr:`lrt p-val (log-rank test p-value)` = 6.30e-22 at 4383 days, 
post-hoc pairwise :abbr:`lrt p-val (log-rank test p-value)` ≤ 1.5e-06).
When comparing patients with each fusion within this class, those with *TCF3-HLF* 
fusions exhibit significantly worse :abbr:`OS (overall survival)` (:abbr:`lrt p-val (log-rank test p-value)` = 4.89e-02), 
consistent with literature [Inukai2007]_. 
Though identifying *TCG3-HLF* outright is important for determining clinical course due to 
its negative prognostic indication [Inukai2007]_, due to a paucity of these samples we are unable to separate them further.
|br| |br|
The final subclass of :abbr:`T124 ALL TRG (Acute lymphoblastic leukemia (TARGET))`, 
:abbr:`T136 ALL TRG ETV6-RUNX1 (Acute lymphoblastic leukemia (TARGET) ETV6-RUNX1 fusion)` (n = 27), 
contains samples with *ETV6-RUNX1* fusions (n = 20, :abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16) (Fig. :ref:`LEU4 <fig-leu4>`) 
and comprises the youngest patients (median 3.1 :abbr:`y.o. (years old)`, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.13e-03).

|br| |br| 


:abbr:`T133 ALL TRG A (Acute lymphoblastic leukemia (TARGET) mix A)` separates in further components (Fig. :ref:`LEU4 <fig-leu4>`).  
|br|
:abbr:`T137 ALL TRG Ph+/Ph-like CRLF2 (Acute lymphoblastic leukemia (TARGET), Philadelphia-like CRLF2 rearrangement or BCR-ABL)` (n=29) 
contains all samples labelled as harbouring *BCR*-*ABL1* fusions (n = 3), *MLL*-rearranged :abbr:`ALL (acute lymphoblastic leukemia)` samples (n=3), 
and the highest proportion of otherwise unspecified :abbr:`ALL (acute lymphoblastic leukemia)` samples (n = 23, :abbr:`χ2 p-val (χ2 test p-value)` = 2.95e-05). 
It shows overexpression of CRLF2 (:abbr:`logFC (log-Fold Change)` = 2.99, :abbr:`FDR (False Discovery Rate)` = 1.48e-02) 
nd enrichment of *CRLF2*-rearrangment signatures in Ph-like :abbr:`ALL (acute lymphoblastic leukemia)` (Ph+ CRFL2 positive, 
:abbr:`medNES (median Normalized Enrichment Score)` = 2.21, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.05e-03) 
[Sadras2017]_ (Fig. :ref:`LEU3b <fig-leu3>`). 
It also exhibits overexpression of *IDH1* (:abbr:`logFC (log-Fold Change)` = 1.28, :abbr:`FDR (False Discovery Rate)` = 3.66e-05), 
*JAK1* (:abbr:`FDR (False Discovery Rate)`  = 0.641, :abbr:`FDR (False Discovery Rate)` = 4.15e-02) 
and is enriched for Ph-like gene signatures (:abbr:`medNES (median Normalized Enrichment Score)` = 2.88, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 9.79e-06, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-03) [Harvey2010]_, [Harvey2013]_ 
when compared to its siblings (Fig. :ref:`LEU3b <fig-leu3>`). 
|br| |br|
:abbr:`T138 ALL TRG HYPERDIP (Acute lymphoblastic leukemia (TARGET), hyperdiploid)` (n=21) 
is enriched for tumours with hyperdiploidy without trisomy of both chromosomes 4 and 10 
(1/29 vs. 11/20 vs. 7/22, :abbr:`χ2 p-val (χ2 test p-value)` = 2.66e-04). Patients in 
:abbr:`T138 (Acute lymphoblastic leukemia (TARGET), hyperdiploid)` are also significantly younger than its siblings (3.59 :abbr:`y.o. (years old)`, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.14e-02). 
Furthermore, :abbr:`T138 (Acute lymphoblastic leukemia (TARGET), hyperdiploid)` exhibits the highest DNA index of its siblings, an indicator of hyperdiploidy 
(median = 1.17, :abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 3.97e-07, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` ≤ 4.18e-03) [Rachieru-Sourisseau2010]_. 
|br| |br|
:abbr:`T139 ALL TRG Ph-like EPOR (Acute lymphoblastic leukemia (TARGET), Philadelphia-like, EPOR fusion)` (n = 22) 
is characterized by overexpression of *EPOR* (median :abbr:`logFC (log-Fold Change)` = 2.06, :abbr:`FDR (False Discovery Rate)` ≤ 1.20e-04), 
as well as enrichment of erythrocyte developmental gene sets (:abbr:`medNES (median Normalized Enrichment Score)` = 1.22, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 2.06-06, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 5.00e-02) [Ashburner2000]_, [TGOC2019]_.
It also exhibits overexpression of *IDH2* (median :abbr:`logFC (log-Fold Change)` = 1.65, :abbr:`FDR (False Discovery Rate)` ≤ 3.40e-11). 

|br| |br| |br|

Acute Myeloid Leukemia 
======================

Myeloid malignancies in :abbr:`T120 AML (Acute myeloid leukemia)` immediately separate into 9 different 
classes at the following heirarchical level (Fig. :ref:`LEU6 <fig-leu6>`). 
Similar to :abbr:`ALL (Acute lymphoblastic leukemia)`, we observe two classes made up exclusively of 
TARGET samples: :abbr:`T144 AML TRG (Acute myeloid leukemia (TARGET))` and 
:abbr:`T146 AML TRG IDH2low (Acute myeloid leukemia (TARGET), IDH2 underexpression)`, which are discussed at the end of this section.

.. figure:: /img/leu6.png
   :alt: Fig. LEU6
   :name: fig-leu6
   :width: 500px
   
   LEU6: A, 2-dimensional UMAP projection of acute myeloid leukemia tumors by gene expression. Subtypes at the third level of the hierarchy
   are shown with different colours. B, the list of all acute myeloid leukemia subtypes identified
   and their hierarchical relationship. 


Acute Myeloid Leukemia, non-TARGET cohort
=========================================

:abbr:`T140 AML KMT2Ar (Acute myeloid leukemia, KMT2A rearrangement)` (n = 52) has a median age of 60.00 y.o (KW p-val =1.54e-48) due to the presence of 46/52 adult patients. 
It contains a number of samples marked for *KMT2A* fusions (most of them high risk, :abbr:`χ2 p-val (χ2 test p-value)` = 4.45e-08), 
and is highly enriched (:abbr:`medNES (median Normalized Enrichment Score)` > 1.08, KW adj. p-val < 1.00e-40, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) 
for their matching pathways ([Ross2004]_; [Mullighan2007]_) (Fig. :ref:`LEU7 <fig-leu7>`). 
It is also enriched for *NPM1* mutated pathways (:abbr:`medNES (median Normalized Enrichment Score)` = 1.07, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 1.97e-38, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) [Mullighan2007]_ 
suggesting a large cohort within this class may be *NPM1* mutated. Indeed, all samples in this cluster for which we have 
*NPM1* and *FLT3* mutation data are mutated for either *NPM1* (n=23) or *FLT3* (n=16). 
This class displays poor :abbr:`OS (overall survival)` (:abbr:`lrt p-val (log-rank test p-value)` = 6.31e-11at 4022 days), 
reaching median :abbr:`OS (overall survival)` at 327days.  

.. figure:: /img/leu7.png
   :alt: Fig. LEU7
   :name: fig-leu7
   :width: 300px
   
   LEU7: Distribution plots of the normalized enrichment score of gene sets relevant to the definition
   of the KMT2A-rearranged myeloid leukemia class.
 

:abbr:`T140 AML KMT2Ar (Acute myeloid leukemia, KMT2A rearrangement)` splits into two subclasses 
(Fig. :ref:`LEU6b <fig-leu6>`). :abbr:`T149 AML KMT2Ar 11q23 (Infant acute lymphoblastic leukemia, KMT2A rearrangement chr11q23)` 
(n = 8) is a very small cluster and is considerably younger (45.00 vs 62.00 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 7.24e-03) than 
:abbr:`T150 AML KMT2A NPM1/FLT3 (Infant acute lymphoblastic leukemia, KMT2A rearrangement, NPM1 or FLT3 mutant)` (n = 44); 
this is also reflected in the percentage of samples marked as paediatric (50.00% vs. 4.55%, :abbr:`χ2 p-val (χ2 test p-value)` = 7.25e-03). 
While 5 samples are marked as :abbr:`AML (Acute myeloid leukemia)`, 
:abbr:`T149 AML KMT2Ar 11q23 (Infant acute lymphoblastic leukemia, KMT2A rearrangement chr11q23)` also contains 
3 samples marked as mixed lineage leukemias (:abbr:`χ2 p-val (χ2 test p-value)` = 7.79e-04). 
It contains 4 samples from :abbr:`TCGA (The Cancer Genome Atlas)`, all of which are annotated with 
*KMT2A* fusions (two *MLL10-KMT2A* and one *KMT2A-MLLT3* and one *KMT2A-MLLT4*), while 
:abbr:`T150 AML KMT2A NPM1/FLT3 (Infant acute lymphoblastic leukemia, KMT2A rearrangement, NPM1 or FLT3 mutant)` 
contains 40 samples from TGCA, 10 of which have reported gene fusions, with seven involving *KMT2A* genes. 
When compared to :abbr:`T150 AML KMT2A NPM1/FLT3 (Infant acute lymphoblastic leukemia, KMT2A rearrangement, NPM1 or FLT3 mutant)` , 
:abbr:`T149 AML KMT2Ar 11q23 (Infant acute lymphoblastic leukemia, KMT2A rearrangement chr11q23)` is significantly 
enriched for genes sets involving chr11q23 rearrangement (:abbr:`medNES (median Normalized Enrichment Score)` = 8.46, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.06e-08) [Yagi2003]_ 
and AML cluster 16 from Valk et al. 2004 (:abbr:`medNES (median Normalized Enrichment Score)` = 4.03, adj. p-val = 2.66e-09), 
which is composed of samples with 11q23 rearrangements [Valk2004]_. 
:abbr:`T150 AML KMT2A NPM1/FLT3 (Infant acute lymphoblastic leukemia, KMT2A rearrangement, NPM1 or FLT3 mutant)` 
inherits all of the *NPM1* and *FLT3* mutants found in its parent   
:abbr:`T140 AML KMT2Ar (Acute myeloid leukemia, KMT2A rearrangement)` [Braoudaki2010]_, 
and is enriched for their corresponding gene sets (:abbr:`medNES (median Normalized Enrichment Score)` =2.34, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` =7.97e-08, 
:abbr:`medNES (median Normalized Enrichment Score)` = 1.85, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 1.25e-04, respectively) [Valk2004]_, [Verhaak2009]_.
|br| |br|
:abbr:`T141 AML BM (Acute myeloid leukemia, bone marrow contamination)` (n = 30) is a mixed-lineage cluster. 
It comprises myeloid, megakaryoblastic, non-specific, and lymphoblastic leukemias along with a few lymphomas and osteosarcomas. 
It is not enriched for any leukemia associated gene sets, suggesting this class may contain samples contaminated by normal blood or bone marrow tissue. 
|br| |br|
:abbr:`T142 AML MATlow (Acute myeloid leukemia, low maturation)` (n = 105) is largely composed of FAB subtypes M1 
(n = 33, :abbr:`χ2 p-val (χ2 test p-value)` = 7.44e-04), :abbr:`AML (Acute myeloid leukemia)` with minimal maturation, 
and M2 (n = 34, :abbr:`χ2 p-val (χ2 test p-value)` = 1.60e-06), :abbr:`AML (Acute myeloid leukemia)` with maturation, 
and a smaller subpopulation of undifferentiated M0 (n = 15, :abbr:`χ2 p-val (χ2 test p-value)` = 1.15e-04). 
It is composed of older patients, with a median age of 57 y.o, and is enriched for samples classified as intermediate 
(n = 54, :abbr:`χ2 p-val (χ2 test p-value)` = 1.43e-07) and high-risk (n = 37, :abbr:`χ2 p-val (χ2 test p-value)` 1.61e-09). 
It contains two *BCR-ABL1* fusion samples, 24 *FLT3* mutants - all of which are from the :abbr:`TCGA (The Cancer Genome Atlas)`, 
though the mutations themselves are heterogenous – 24 *NMP1* mutants, 21 of which are W288F (:abbr:`χ2 p-val (χ2 test p-value)` < 2.2e-16), 
along with 9 *WT1* mutants (:abbr:`χ2 p-val (χ2 test p-value)` = 1.56 e-4). 
All samples in this cluster for which we have *NPM1* and *FLT3* mutation data have mutations in either gene. 
This cluster displays intermediate low prognosis, reaching median :abbr:`OS (overall survival)` at 417 days 
(:abbr:`lrt p-val (log-rank test p-value)` = 6.31e-11 at 4022 days). 
|br| |br|
:abbr:`T142 AML MATlow (Acute myeloid leukemia, low maturation)` splits into two two subclasses, 
:abbr:`T151 AML MATlow NPM1mut (Acute myeloid leukemia, low maturation, NPM1 mutant)` and 
:abbr:`T152 AML MATlow noNPM1 (Acute myeloid leukemia, low maturation, no NPM1 mutation)` (Fig. S26b), 
which are separated by the presence or absence of *NPM1* mutations, as well as karyotypic complexity. 
:abbr:`T151 AML MATlow NPM1mut (Acute myeloid leukemia, low maturation, NPM1 mutant)` (n = 34) has a 
higher ratio of FAB M1 samples, :abbr:`AML (Acute myeloid leukemia)` with minimal maturation, 
(16/32 vs 17/62, :abbr:`FET p-val (Fisher's exact test p-value)` = 4.04e-02) and inherits all *NPM1*-mutant 
samples except for one, a p.K263R (:abbr:`χ2 p-val (χ2 test p-value)` = 6.67e-13); all samples for which we have 
*NPM1* data within this cluster (n=25) are *NPM1* mutated. 
As expected, we confirmed this annotation through significance (:abbr:`medNES (median Normalized Enrichment Score)` = 1.25, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 7.83e-16) in *NPM1* mutation pathways [Mullighan2007]_. 
Its sibling, :abbr:`T152 AML MATlow noNPM1 (Acute myeloid leukemia, low maturation, no NPM1 mutation)` (n = 71), 
has a higher proportion of FAB M0 samples, undifferentiated :abbr:`AML (Acute myeloid leukemia)` 
(1 vs. 14, :abbr:`FET p-val (Fisher's exact test p-value)` = 3.21e-02), and possibly contains equivalent samples 
without *NPM1* mutation.
M2 samples are evenly split between the clusters (:abbr:`χ2 p-val (χ2 test p-value)` = 6.51e-01), suggesting 
maturation is not a critical determinant of this split. Samples with *FLT3* and *WT1* mutations are more common in 
:abbr:`T151 AML MATlow NPM1mut (Acute myeloid leukemia, low maturation, NPM1 mutant)` than in 
:abbr:`T152 AML MATlow noNPM1 (Acute myeloid leukemia, low maturation, no NPM1 mutation)`, confirmed by gene 
sets for *FLT3* mutation (:abbr:`medNES (median Normalized Enrichment Score)` = 1.90, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.29e-13) [Valk2004]_.
We observe no significant separation in survival between the two clusters. 
|br| |br|
:abbr:`T152 AML MATlow noNPM1 (Acute myeloid leukemia, low maturation, no NPM1 mutation)` further splits into 
:abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` (n = 58) and 
:abbr:`T154 AML CEBPA (Acute myeloid leukemia CEBPA mutated)` (n = 13) (Fig. S26b). There is a significantly age 
desparity between patients in these clusters (63 vs 32 :abbr:`y.o. (years old)` 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 7.80e-05). 
:abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` contains all M0 samples 
(n = 14 vs 0) while :abbr:`T154 AML CEBPA (Acute myeloid leukemia CEBPA mutated)` is enriched for FAB M2 samples 
(n = 12 vs 9, :abbr:`χ2 p-val (χ2 test p-value)` = 3.81e-03). 
:abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` also contains five acute 
megakaryoblastic leukemias and two mixed lineage leukemias, and carries more samples with complex cytogenetics 
(:abbr:`χ2 p-val (χ2 test p-value)` < 1.00-03) and has significantly reduced 
:abbr:`OS (overall survival)` (:abbr:`lrt p-val (log-rank test p-value)` = 2.00e-02). 
In line with findings described in literature, 
:abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` exhibits a 
higher mutation burden (median = 17.00 vs. 8.50, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.06e-03), 
which is largely related to age in :abbr:`AML (Acute myeloid leukemia)` [Shaver2015]_. 
T153 contains six FLT3 mutant samples (three of which have in frame insertions), while :abbr:`T154 AML CEBPA (Acute myeloid leukemia CEBPA mutated)` 
contains only one. :abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` overexpresses 
a myriad of genes (21/39, :abbr:`FDR (False Discovery Rate)` < 0.05), which are known to be upregulated in samples 
harbouring *FLT3* internal tandem duplications (FLT3-ITD), as well as enrichment of 
:abbr:`FLT3-ITD (FLT3 internal tandem duplication)` gene sets 
(:abbr:`medNES (median Normalized Enrichment Score)` = 3.11, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 5.99e-08) [Valk2004]_. 
On the other hand, :abbr:`T153 AML FLT3-ITD (Acute myeloid leukemia, FLT3 internal tandem duplication)` contains 
only three *CEBPA* mutated samples, while :abbr:`T154 AML CEBPA (Acute myeloid leukemia CEBPA mutated)` contains 
eight (:abbr:`χ2 p-val (χ2 test p-value)` = 3.28e-06)

|br| |br|
The direct subclusters of :abbr:`T120 AML (Acute myeloid leukemia)` continue here. 
|br|
:abbr:`T143 AMKL (Acute megakarioblastic leukemia)` (n = 49) is exclusively composed of 
megakaryoblastic samples (n = 41, :abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16) while eight samples 
are unlabelled, and as expected is enriched for :abbr:`AMKL (Acute megakaryoblastic leukemia)` 
pathways (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.70 , 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 1.01e-38)(Ross2004).
Note that all cases are non-trisomy 21. This cluster displays the worst prognosis of all its 
siblings, reaching median :abbr:`OS (overall survival)` at 313 days (:abbr:`lrt p-val (log-rank test p-value)` = 6.31e-11). 
:abbr:`T143 AMKL (Acute megakarioblastic leukemia)` then splits into :abbr:`T155 AMKL CBFA2T3-GLIS2 (Megakaryoblastic leukemia, CBFA2T3-GLIS2 fusion)` 
(n = 12) and :abbr:`T156 AMKL HOX (Acute megakarioblastic leukemia with HOX expression program)` (n = 37). 
Though both are entirely paediatric, the former cluster contains significantly younger patients (median age of 0.97 vs 2.17 
:abbr:`y.o. (years old)` ,:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.08e-02).
All samples in :abbr:`T155 AMKL CBFA2T3-GLIS2 (Megakaryoblastic leukemia, CBFA2T3-GLIS2 fusion)` for which genomic 
data are available are characterized by a *CBFA2T3-GLIS2* fusion (9/9 vs. 0/25, :abbr:`χ2 p-val (χ2 test p-value)` = 7.03e-08) [deRooij2017]_. 
Patients in :abbr:`T155 AMKL CBFA2T3-GLIS2 (Megakaryoblastic leukemia, CBFA2T3-GLIS2 fusion)` have poorer prognsosis, 
reaching median :abbr:`OS (overall survival)` at just 313 days post diagnosis. :abbr:`T156 AMKL HOX (Acute megakarioblastic leukemia with HOX expression program)` is composed of other driver events: two *GATA1* mutants , four HOXr (*HOX* fusion) samples, eight *KMT2A-MLLT3/10* fusions, four *NUP98-KDM5A* fusions, two *RBM15-MKL1* fusions, and four samples with other driver mutations. 
With a greater sample size its possible these mutations would form their own clusters as well. When comparing these 
two classes, :abbr:`T156 AMKL HOX (Acute megakarioblastic leukemia with HOX expression program)` exhibits overexpression of 
*HOXA* (11/11 genes upregulated, median :abbr:`logFC (log-Fold Change)` ≤ -5.67, :abbr:`FDR (False Discovery Rate)` ≤ 8.47e-03 )
and *HOXB* genes (8/10 upregulated, median :abbr:`logFC (log-Fold Change)` = -5.65, :abbr:`FDR (False Discovery Rate)` ≤ 7.31e-03) [deRooij2017]_. 
|br| |br|
The remaining subclasses of :abbr:`T120 AML (Acute myeloid leukemia)` are defined by clear fusion events. All samples 
within :abbr:`T145 AML CBFB-MYH11 (Acute myeloid leukemia CBFB-MYH11 fusion)` (n = 14) are marked as core binding factor positive, *CBFB-MYH11*. 
As expected, it is enriched (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.35 , 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)`= 3.65e-27) 
for *CBFB-MYH11* associated gene sets [Ross2004]_, [Valk2004]_. 
All samples in :abbr:`T147 APML (Acute promyelocytic leukemia)` (n = 15), except for one, are positive for 
*PML-RARA* fusions (:abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16) and marked as FAB M3 
(:abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16), acute promyelocytic leukemia. 
This class also contains 5 samples with *FLT3* mutations, four of which are p600 in frame insertions 
(from :abbr:`TCGA (The Cancer Genome Atlas)`); these seem to be exclusive to this cluster. 
This class has the best prognosis of the cohort, with >60% of patients surviving at 4022 days post diagnosis. 
The final child of :abbr:`T120 AML (Acute myeloid leukemia)`, 
:abbr:`T148 AML RUNX1-RUNX1T1 (Acute myeloid leukemia, RUNX1-RUNX1T1 fusion)` (n = 13), exclusively contains 
*RUNX1-RUNX1T1* fusion :abbr:`AML (Acute myeloid leukemia)` (:abbr:`χ2 p-val (χ2 test p-value)` < 2.20e-16). 
It has moderate-good prognosis, reaching median :abbr:`OS (overall survival)` 2910 days. 


Acute Myeloid Leukemia, TARGET cohort
=========================================

We observe two classes within the :abbr:`AML (Acute myeloid leukemia)` branch with an exclusive TARGET composition (Fig. :ref:`LEU6 <fig-leu6>`).
:abbr:`T146 AML TRG IDH2low (Acute myeloid leukemia (TARGET), IDH2 underexpression)` (n = 23) is composed by samples with various diagnostic 
categories: three *KMT2A* fusions (n =3), eight normal karyotypes, and 10 other lesions, including two t(X;10)(p11.2;p11.2), 
add(17)(p11.2) and two inv(17)(p13.1q11.2), both exclusive to this group. 
However, it contains the highest proportion of *WT1* mutations (7/23, :abbr:`χ2 p-val (χ2 test p-value)` = 1.39e-3) 
and *FLT3*-ITDs (8/23, :abbr:`χ2 p-val (χ2 test p-value)` = 2.427e-05) amongst the TARGET cohort. 
It also exhibits the lowest expression of *IDH2* (:abbr:`logFC (log-Fold Change)` = -0.836, p-val = 2.58e-2 
against T155-T159 and :abbr:`T161 AML TRG RUNX-RUNX1T1  (Acute myeloid leukemia (TARGET), RUNX1-RUNX1T1 fusion)`). 
This group displays intermediate prognosis, reaching median :abbr:`OS (overall survival)` at 1394 days post diagnosis. 

.. figure:: /img/leu8.png
   :alt: Fig. LEU8
   :name: fig-leu8
   :width: 400px
   
   LEU8: 2-dimensional UMAP projection of acute myeloid leukemia tumors from the TARGET cohort by gene expression. Subtypes at the third level of the hierarchy
   are shown with different colours. 

:abbr:`T144 AML TRG (Acute myeloid leukemia (TARGET))` (n = 163) is the largest subcluster of :abbr:`T120 AML (Acute myeloid leukemia)` and is composed 
largely of unspecified :abbr:`AML (Acute myeloid leukemia)` (n=154), and surprisingly contains 5 
:abbr:`ALL (Acute lymphoblastic leukemia)`. It is an entirely paediatric cluster 
(median age 9.36 :abbr:`y.o. (years old)`) and has excellent prognosis, with >50% of patients surviving at 4022 days post diagnosis. 
Diving deeper into this class (Fig. S26b, c), we observe first the singling out of :abbr:`AML (Acute myeloid leukemia)`
with *KMT2A* translocations (23/33 vs 12/120, :abbr:`χ2 p-val (χ2 test p-value)` = 2.623e-12) in 
:abbr:`T158 AML TRG KMT2Ar (Acute myeloid leukemia (TARGET), KMT2A rearrangement)` (n = 33) from all 
other samples in :abbr:`T157 AML TRG A (Acute myeloid leukemia (TARGET) mixture A)` (n = 130). 
As expected, :abbr:`T158 AML TRG KMT2Ar (Acute myeloid leukemia (TARGET), KMT2A rearrangement)` shows 
enrichment (:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` ≤ 1.00e-03) 
of *KMT2A*-associated gene sets [Ross2004]_, [Mullighan2007]_. There is no difference in :abbr:`OS (overall survival)` between the two subclasses.
|br| |br|
We then observe :abbr:`T157 AML TRG A (Acute myeloid leukemia (TARGET) mixture A)` splitting into three small 
subclasses characterized by unique molecular aberrations: 
:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)` (n = 65), 
:abbr:`T160 AML TRG CFB-MYH11 (Acute myeloid leukemia (TARGET), CFB-MYH11 fusion)` (n = 36), 
and :abbr:`T161 AML TRG RUNX-RUNX1T1  (Acute myeloid leukemia (TARGET), RUNX1-RUNX1T1 fusion)` (n = 29).
Aside from myeloid malignancies, 
:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)` 
contains 4 :abbr:`ALL (Acute lymphoblastic leukemia)` samples, one unspecified leukemia and one lymphoma. 
It has the highest proportion of intermediate risk samples (n = 36, :abbr:`χ2 p-val (χ2 test p-value)` = 1.581e-06) 
and patients within it exhibit a significantly worse :abbr:`OS (overall survival)` than either of its siblings 
(:abbr:`lrt p-val (log-rank test p-value)` = 2.20e-04). This cluster also inherits all *NPM1* mutant samples, while 
*FLT3*-ITD and *WT1* mutants are spread across all three clusters. 
This class also contains samples labelled as *KMT2A*-rearranged (n = 11/56, :abbr:`χ2 p-val (χ2 test p-value)` = 4.103e-03). 
It shows overexpression of a wide variety of *HOX* genes (24/39 *HOX* genes with median 
:abbr:`logFC (log-Fold Change)` > 0 & :abbr:`FDR (False Discovery Rate)` < 0.05, 22/39 :abbr:`FDR (False Discovery Rate)` < 1e-04, median 
:abbr:`logFC (log-Fold Change)` = 4.62), a phenotype previously described in AMLs with *KMT2A* partial internal tandem duplication (*KMT2A*-PTD) [Dorrance2006]_. 
The characteristic expression patterns of *KMT2A*-:abbr:`PTD (partial tandem duplication)` 
could explain the inclusion of a handful of :abbr:`ALL (Acute lymphoblastic leukemia)` samples, which may also 
harbour non-canonical *KMT2A* aberrations. 
Indeed, manual inspection of a subsample of eight mRNA sequences (five labelled as :abbr:`AML (Acute myeloid leukemia)`, 
three as :abbr:`ALL (Acute lymphoblastic leukemia)`) from TARGET revealed the majority of these samples (4/8) harbour 
complex lesions in KMT2A or (2/8) with rearrangments to exon 7 and 8 associated with *KMT2A*-:abbr:`PTD (partial tandem duplication)`.
The transcriptional profile of *KMT2A* lesions in this class departs from that most commonly described by literature, 
as most gene sets involving *KMT2A* mutated leukemias agree an impoverishment in this class when compared to the 
bona-fide *KMT2A*-rearranged :abbr:`AML (Acute myeloid leukemia)` class 
:abbr:`T158 AML TRG KMT2Ar (Acute myeloid leukemia (TARGET), KMT2A rearrangement)` 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.27 for positive signatures in :abbr:`T158 AML TRG KMT2Ar (Acute myeloid leukemia (TARGET), KMT2A rearrangement)`, 
≥ 1.61 for negative signatures in :abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)`, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` ≤ 3.32e-15) ([Ross2004]_; [Mullighan2007]_;).
A single sample harbours a *BSG-CDC34* fusion. While no *KMT2A* mutation was reported, *CDC34* is known to mediate stability and degradation of 
*KMT2A* ([Meyer2018]_; [Sugeedha2021]_), supporting the idea that 
:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)` 
is composed of tumours with various lesions which converge upon *KMT2A* pathway pertubation. 
|br| |br|
KMT2A rearrangements are also common in mixed phenotype acute leukemias (MPAL) [Winters2017]_, [Yang2017]_; 
to assess whether some of these samples are :abbr:`MPAL (Mixed phenotype acute leukemia)`, we interrogated a number of gene sets (Fig. :ref:`LEU9 <fig-leu9>`). 
Indeed, :abbr:`MPAL (Mixed phenotype acute leukemia)` expression sets were significantly upregulated in 
:abbr:`AML (Acute myeloid leukemia)` within  
:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)` 
when compared to all other :abbr:`AML (Acute myeloid leukemia)` in :abbr:`T120 AML (Acute myeloid leukemia)` 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.20, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 2.94-12), 
which in turn have higher markers of :abbr:`AML (Acute myeloid leukemia)` vs :abbr:`MPAL (Mixed phenotype acute leukemia)` 
(:abbr:`medNES (median Normalized Enrichment Score)` = 1.04, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 5.55e-05) [Bian2018]_. 
Furthermore, these samples carry higher lymphocyte differentiation expression than :abbr:`AML (Acute myeloid leukemia)` 
from their family class (:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)` 
vs :abbr:`T120 AML (Acute myeloid leukemia)`, :abbr:`medNES (median Normalized Enrichment Score)` = 2.63, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 1.36e-03) [The2019]_, [Ashburner2000]_. 
In turn, the four :abbr:`ALL (Acute lymphoblastic leukemia)` samples within this same class have significant enrichment 
for myeloid differentiation when compared to all other :abbr:`ALL (Acute lymphoblastic leukemia)` in 
:abbr:`T119 ALL (Acute lymphoblastic leukemia)` (:abbr:`medNES (median Normalized Enrichment Score)` = 1.25, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` = 9.01e-04) [The2019]_, [Ashburner2000]_.
|br|
Furthermore, we report enrichment of T-cell development and differentiation gene sets when comparing 
samples of matching reported lineage to either :abbr:`T120 AML (Acute myeloid leukemia)` 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.10, :abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` ≤ 9.82e-08) 
and :abbr:`T119 ALL (Acute lymphoblastic leukemia)` (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.27, 
:abbr:`MWU adj. p-val (Mann Whitney U test Benjamin-Hochberg adjusted p-value)` ≤ 2.77e-02) [The2019]_, [Ashburner2000]_, 
composed exclusively of B-cell :abbr:`ALL (Acute lymphoblastic leukemia)` (Fig. :ref:`LEU9 <fig-leu9>`). 
These results support the hypothetical presence of T-cell :abbr:`MPAL (Mixed phenotype acute leukemia)` within 
:abbr:`T159 AML TRG KMT2Ar/MPAL (Acute myeloid leukemia (TARGET), KMT2A rearrangement or mixed-phenotype acute leukemia)`. 
While limited information is given by the labelling of these samples, we can confidently speculate this class includes 
*KMT2A*-rearranged B-cell and/or T-cell :abbr:`MPAL (Mixed phenotype acute leukemia)`, or at the very least samples of either 
linage expressing both myeloid and lymphoid markers.

.. figure:: /img/leu9.png
   :alt: Fig. LEU9
   :name: fig-leu9
   :width: 300px
   
   LEU9: Distribution plots of the normalized enrichment score of gene sets relevant to the definition
   of the KMT2A-rearranged myeloid leukemia classes from the TARGET cohort.

Finally, a more straightforward annotation allows us to determine :abbr:`T160 AML TRG CFB-MYH11 (Acute myeloid leukemia (TARGET), CFB-MYH11 fusion)` 
harbours core binding factor-mutated samples, as the majority of its samples are labelled as *CFB-MYH11* 
fusion positive (n = 26/35, :abbr:`χ2 p-val (χ2 test p-value)` = 9.70e-15), and furthermore shows enrichment 
(:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.84, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 9.376e-16, 
:abbr:`Dunn adj. p-val (Dunn’s test of multiple comparisons Benjamin-Hochberg adjusted p-value)` < 1.00e-04) of its associated gene sets [Ross2004]_. 
Similarly, :abbr:`T161 AML TRG RUNX-RUNX1T1  (Acute myeloid leukemia (TARGET), RUNX1-RUNX1T1 fusion)` is largely 
composed of samples labelled as harbouring *RUNX1-RUNX1T1* fusions (n = 18/29, :abbr:`χ2 p-val (χ2 test p-value)` = 1.77e-11) 
and is enriched for respective gene sets (:abbr:`medNES (median Normalized Enrichment Score)` ≥ 1.01, 
:abbr:`KW adj. p-val (Kruskal–Wallis one-way analysis of variance test Benjamin-Hochberg adjusted p-value)` = 5.83e-04) [Tonks2007]_. 
It also contains 6 *CEBPA* mutants (:abbr:`χ2 p-val (χ2 test p-value)` = 8.21e-3).


Bibliography
=================

.. [Ashburner2000] Ashburner, M., Ball, C.A., Blake, J.A., et al. 2000. Gene Ontology: tool for the unification of biology. Nature Genetics 25(1), pp. 25–29.
.. [Bian2018] Bian, S., Hou, Y., Zhou, X., et al. 2018. Single-cell multiomics sequencing and analyses of human colorectal cancer. Science 362(6418), pp. 1060–1063.
.. [Braoudaki2010] Braoudaki, M., Papathanassiou, C., Katsibardi, K., Tourkadoni, N., Karamolegou, K. and Tzortzatou-Stathopoulou, F. 2010. The frequency of NPM1 mutations in childhood acute myeloid leukemia. Journal of hematology & oncology 3, p. 41.
.. [Dorrance2006] Dorrance, A.M., Liu, S., Yuan, W., et al. 2006. Mll partial tandem duplication induces aberrant Hox expression in vivo via specific epigenetic alterations. The Journal of Clinical Investigation 116(10), pp. 2707–2716.
.. [Harvey2010] Harvey, R.C., Mullighan, C.G., Wang, X., et al. 2010. Identification of novel cluster groups in pediatric high-risk B-precursor acute lymphoblastic leukemia with gene expression profiling: correlation with genome-wide DNA copy number alterations, clinical characteristics, and outcome. Blood 116(23), pp. 4874–4884.
.. [Harvey2013] Harvey, R.C., Kang, H., Roberts, K.G., et al. 2013. Development and Validation Of a Highly Sensitive and Specific Gene Expression Classifier To Prospectively Screen and Identify B-Precursor Acute Lymphoblastic Leukemia (ALL) Patients With a Philadelphia Chromosome-Like (“Ph-like” or “BCR-ABL1-Like”) Signature For Therapeutic Targeting and Clinical Intervention. Blood 122(21), pp. 826–826.
.. [Hirabayashi2017] Hirabayashi, S., Ohki, K., Nakabayashi, K., et al. 2017. ZNF384-related fusion genes define a subgroup of childhood B-cell precursor acute lymphoblastic leukemia with a characteristic immunotype. Haematologica 102(1), pp. 118–129.
.. [Inukai2007] Inukai, T., Hirose, K., Inaba, T., et al. 2007. Hypercalcemia in childhood acute lymphoblastic leukemia: frequent implication of parathyroid hormone-related peptide and E2A-HLF from translocation 17;19. Leukemia 21(2), pp. 288–296.
.. [Jain2017] Jain, N., Roberts, K.G., Jabbour, E., et al. 2017. Ph-like acute lymphoblastic leukemia: a high-risk subtype in adults. Blood 129(5), pp. 572–581.
.. [Lazar2013] Lazar, C., Meganck, S., Taminau, J., et al. 2013. Batch effect removal methods for microarray gene expression data integration: a survey. Briefings in Bioinformatics 14(4), pp. 469–490.
.. [Meyer2018] Meyer, C., Burmeister, T., Gröger, D., et al. 2018. The MLL recombinome of acute leukemias in 2017. Leukemia 32(2), pp. 273–284.
.. [Mullighan2007] Mullighan, C.G., Kennedy, A., Zhou, X., et al. 2007. Pediatric acute myeloid leukemia with NPM1 mutations is characterized by a gene expression profile with dysregulated HOX gene expression distinct from MLL-rearranged leukemias. Leukemia 21(9), pp. 2000–2009.
.. [Rachieru-Sourisseau2010] Rachieru-Sourisseau, P., Baranger, L., Dastugue, N., et al. 2010. DNA Index in childhood acute lymphoblastic leukaemia: a karyotypic method to validate the flow cytometric measurement. International Journal of Laboratory Hematology 32(3), pp. 288–298.
.. [deRooij2017] de Rooij, J.D.E., Branstetter, C., Ma, J., et al. 2017. Pediatric non-Down syndrome acute megakaryoblastic leukemia is characterized by distinct genomic subsets with varying outcomes. Nature Genetics 49(3), pp. 451–456.
.. [Qian2017] Qian, M., Zhang, H., Kham, S.K.-Y., et al. 2017. Whole-transcriptome sequencing identifies a distinct subtype of acute lymphoblastic leukemia with predominant genomic abnormalities of EP300 and CREBBP. Genome Research 27(2), pp. 185–195.
.. [Ross2004] Ross, M.E., Mahfouz, R., Onciu, M., et al. 2004. Gene expression profiling of pediatric acute myelogenous leukemia. Blood 104(12), pp. 3679–3687.
.. [Sadras2017] Sadras, T., Heatley, S.L., Kok, C.H., et al. 2017. Differential expression of MUC4, GPR110 and IL2RA defines two groups of CRLF2-rearranged acute lymphoblastic leukemia patients with distinct secondary lesions. Cancer Letters 408, pp. 92–101.
.. [Shaver2015] Shaver, A.C., Seegmiller, A.C., Strickland, S.A., et al. 2015. Mutational burden in acute myeloid leukemia is largely age dependent. Blood 126(23), pp. 2605–2605.
.. [Sugeedha2021] Sugeedha, J., Gautam, J. and Tyagi, S. 2021. SET1/MLL family of proteins: functions beyond histone methylation. Epigenetics 16(5), pp. 469–487.
.. [Sun2017] Sun, C., Chang, L. and Zhu, X. 2017. Pathogenesis of ETV6/RUNX1-positive childhood acute lymphoblastic leukemia and mechanisms underlying its relapse. Oncotarget 8(21), pp. 35445–35459.
.. [The2019] The Gene Ontology Consortium 2019. The Gene Ontology Resource: 20 years and still GOing strong. Nucleic Acids Research 47(D1), pp. D330–D338.
.. [Tonks2007] Tonks, A., Pearn, L., Musson, M., et al. 2007. Transcriptional dysregulation mediated by RUNX1-RUNX1T1 in normal human progenitor cells and in acute myeloid leukaemia. Leukemia 21(12), pp. 2495–2505.
.. [Valk2004] Valk, P.J.M., Verhaak, R.G.W., Beijen, M.A., et al. 2004. Prognostically useful gene-expression profiles in acute myeloid leukemia. The New England Journal of Medicine 350(16), pp. 1617–1628.
.. [Verhaak2009] Verhaak, R.G.W., Wouters, B.J., Erpelinck, C.A.J., et al. 2009. Prediction of molecular subtypes in acute myeloid leukemia based on gene expression profiling. Haematologica 94(1), pp. 131–134.
.. [Winters2017] Winters, A.C. and Bernt, K.M. 2017. MLL-Rearranged Leukemias-An Update on Science and Clinical Approaches. Frontiers in pediatrics 5, p. 4.
.. [Yagi2003] Yagi, T., Morimoto, A., Eguchi, M., et al. 2003. Identification of a gene expression signature associated with pediatric AML prognosis. Blood 102(5), pp. 1849–1856.
.. [Yang2017] Yang, W., Tran, P., Khan, Z., Rezk, S. and O’Brien, S. 2017. MLL-rearranged mixed phenotype acute leukemia masquerading as B-cell ALL. Leukemia & Lymphoma 58(6), pp. 1498–1501.
.. [Yeoh2002] Yeoh, E.-J., Ross, M.E., Shurtleff, S.A., et al. 2002. Classification, subtype discovery, and prediction of outcome in pediatric acute lymphoblastic leukemia by gene expression profiling. Cancer Cell 1(2), pp. 133–143.


