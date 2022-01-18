.. |br| raw:: html

  <br/>

==========================
N000 Healthy Normal Tissue 
==========================

Version: |version|
|br| 
Last change: |today|


We included in our dataset 1735 RNASeq samples from 31 locations and 52 tissue types within the the `GTEx project <https://gtexportal.org/home/>`_, [GTEx2013]_, [Carithers2015]_. 
Samples from cell cultures (such as fibroblasts and lymphblastoids) were not included in this work. 

The resulting hierarchy of clusters is shown in Fig. :ref:`NORM1 <fig-norm1>`. In a number of cases we observe the merging of tissue types common functional features [Uhlén2015]_. 
To help with the annotation, we looked at histological report shared, which revealed considerable variability of cell types across samples from the same organ.

.. figure:: /img/norm1.png
   :alt: Fig. NORM1
   :name: fig-norm1
   :width: 500px
   
   LEU1: A, 2-dimensional UMAP projection of healthy normal tissue samples by gene expression. Subtypes at the first level of the hierarchy
   are shown with different colours. B, the list of all healthy normal tissue subtypes identified
   and their hierarchical relationship. 


Samples from the digestive tract are found in :abbr:`N010 DIGESTIVE (Digestive system)` (n = 192) and branch out into :abbr:`N043 COLON SIGMOID (Colon sigmoid)` (n = 54), 
:abbr:`N044 ESOPHAGUS MUSCOLARIS (Esophagus muscolaris, esophageal junction and other smooth muscle)` (n = 82), containing both muscolaris and esophageal junction samples), 
:abbr:`N045 COLON TRANSVERSE (Colon transverse)` (n = 27) and :abbr:`N046 SMALL INTESTINE (Small intestine)` (n = 29), although a degree of overlap is observed 
across all these groups. :abbr:`N044 (Esophagus muscolaris, esophageal junction and other smooth muscle)` attracts samples from other organs 
with a majority of smooth muscle tissue.  
|br|
The database contains only 10 bladder samples (the only ones available on 
GTEx at the time of this work), five of which are found within this group. 
The remaining half cluster with prostate tissue :abbr:`N038 PROSTATE+BLADDER (Prostate and bladder)`` (n = 37), 
but could be possibly be further separated if the population were to be increased. 
|br|
This last group is part of a more general supercluster of mostly gland and hormonal 
regulatory tissues (:abbr:`N008 MUCOSA+GLANDS (Mucosa or gland tissue)`, n = 161), esophagus mucosa and submucosa glands 
(:abbr:`N039 ESOPHAGOUS MUCOSA (Esophagous mucosa and glands)`, n = 39, including two salivary gland samples with a majority of mucosa and stroma), 
breast (ducts and glands), fallopian and endocervix tissues (:abbr:`N040 MAMMARY, n = 26), kidney cortex 
(:abbr:`N041 KIDNEY, (Kidney)`, n = 27) vaginal epithelium and mucosa, and ectocervix (:abbr:`N042 VAGINA (Vagina)`, n = 32). As observed before, 
the borders between female reproductive organs tissues also tend to overlap, depending on the ratio between mucosa, 
muscle, or other tissue types within the sample. 
|br|
Cervix and vaginal tissues are also found to a lesser degree in :abbr:`N007 OVARY+UTERUS (Ovaries, uterus and fallopian tubes)` (n = 92), which is then split into
:abbr:`N036 UTERUS (Uterus)` (n = 52), and :abbr:`N037 OVARY (Ovary)` (n = 40) at the next iteration.
|br| |br|
Occasionally, the separation is orthogonal to provided labels. 
:abbr:`N005 SKIN (Skin)` (n = 75) samples are not grouped by sun exposure, but rather by the presence or absence of any dermal fat: 
:abbr:`N034 SKIN DERMAL FAT (Skin with dermal fat)` (n = 51) which also includes a single sample labelled as subcutaneous adipose tissue and 
:abbr:`N035 SKIN NO FAT (Skin without dermal fat)` (n = 24) respectively. 
|br| |br|
Heart tissue samples are found in :abbr:`N013 HEART (Heart)` (n = 74), which then splits by location into 
:abbr:`N047 HEART ATRIAL (Atrial appendage)` (n = 36) and 
:abbr:`N048 HEART VENTRICLE (Left ventricle)` (n = 38). 
Arteries are initially clustered with adipose tissues in :abbr:`N002 ARTERY+ADIPOSE (Artery and adipose tissue)` (n = 203), possibly due to their fat component, 
and are then separated in peripheral :abbr:`N031 ARTERY PERIPHERAL (Artery peripheral (tibial))` (n = 34), and coronary and aorta 
:abbr:`N029 ARTERY TRUNK (Artery coronary and aorta)` (n = 78) which are then split in their specific types, :abbr:`N032 ARTERY CORONARY (Artery coronary)` (n = 42) and 
:abbr:`N033 ARTERY AORTA (Artery aorta)`` (n = 36) respectively. :abbr:`N030 ADIPOSE (Adipose tissue)` (n = 91) is a relatively big group, containing fat tissues from different body parts. 
It includes a majority of visceral and subcutaneous adipose tissue, but also breast and a few gastroesophageal junction samples. 
|br|
:abbr:`N032 (Artery coronary)` also contains a few samples from tibial arteries, and, more interestingly two salivary gland and a vagina sample. 
According to the histological analysis, the salivary gland samples are missing glands and mostly made of fibromuscular tissue, 
while the vagina sample contains almost exclusively fibrovascular stroma, further supporting the importance of proper expression 
profiling for normal samples too. This is particularly important in the context of tumor-normal matching to build a background population. 
|br| |br|
Finally, most central nervous system regions overlap considerably, except for Cerebellum samples, 
which are cleanly grouped together in :abbr:`N009 CEREBELLUM (Cerebellum)` (n = 74), which also includes a single mislabelled cortex sample 
(as confirmed by the histological report). 
|br|
The remaining samples are found in :abbr:`N001 BRAIN (Brain)` (n = 398) and its subclusters: 
:abbr:`N022 CORPUS STRIATUM (Nucleus accumbens, caudate nucleus and putamen)` (n = 96) contains tissues from the nucleus accumbens, 
the caudate nucleus and putamen; hippocampus,
amygdala, and cortex, tend to overlap significantly and are all grouped in the single biggest cluster 
:abbr:`N023 CORTEX+HIPPC+AMYGD (Hippocampus, amygdala, and cortex)` (n = 193), which couldn’t be further separated; 
and finally :abbr:`N024 SPINALC+HYPTM+SNIG (Spinal cord, hypothalamus and substantia nigra)` (n = 109) 
comprises instead spinal cord, hypothalamus and substantia nigra samples. The latter further splits however into 
:abbr:`N026 HYPOTALAMUS (Hypothalamus)` (n = 30), and then again :abbr:`N027 SPINAL CORD (Spinal cord)` (n = 51) and 
:abbr:`N028 SUBSTANTIA NIGRA (Substantia nigra)` (n = 27), although a 
good degree of overlap is observed between the last two. Although :abbr:`N028 (Substantia nigra)` contains the majority of substantia nigra 
samples, this tissue type is observed across most of the other clusters too.
 
Bibliography
============

.. [Carithers2015] Carithers, L.J., Ardlie, K., Barcus, M., et al. 2015. A Novel Approach to High-Quality Postmortem Tissue Procurement: The GTEx Project. Biopreservation and biobanking 13(5), pp. 311–319.
.. [GTEx2013] GTEx Consortium 2013. The Genotype-Tissue Expression (GTEx) project. Nature Genetics 45(6), pp. 580–585.
.. [Uhlén2015] Uhlén, M., Fagerberg, L., Hallström, B.M., et al. 2015. Proteomics. Tissue-based map of the human proteome. Science 347(6220), p. 1260419.

