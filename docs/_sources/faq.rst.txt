.. _faq:

==========================
Frequently Asked Questions
==========================

**What is this site?**

This is a database containing manually curated annotations of the RNA-Seq gene expression-based clusters which are part of the Transcriptional Cancer Atlas. It contains details on their expression profiles, lesions or other relevant clinical information that may be helpful in deciphering the biology behind this stratification.  For more information, please see our publications in the home page.

**What is RACCOON?**

RACCOON is a scale-adaptive clustering framework. It has been used on our reference gene expression dataset to build the hierarchy of tumor types described in this website. To know more about it and to check out the code, see its `repository <https://github.com/fcomitani/raccoon>`_.

**Why are only a few tumour types available in the annotation?**

The manual curation is very time consuming, for the moment we focused our efforts on the most commont tumor families in pediatric patients. We hope to add more classes in the future.


**Is this dataset exclusively pediatric?**

No, while our focus is mostly on characterizing pediatric tumors, the dataset contains also adult samples.


**Can I browse clinical data such as age for each class more in detail?**

Yes, :ref:`dash` allows you to explore interactively all the shareable clinical information of our reference dataset.


**What is OTTER?**

OTTER is an ensamble of convolutional neural networks for tumor subtype prediction from RNA-Seq expression data.
We are currently working on a web platform that will host this classifier and allow people to submit their samples for prediction.
Stay tuned!

**The dashboard is not working.**

If you can't visualize the OTTER dashboard try refreshing the page or switch to a different browser. If you are still having issues please contact us.


**I downloaded your data, but there are discrepancies in the anmes of the clusters in this annotation.**

Make sure you are looking at a version of this database that matches the version of the data you are using. We are striving to keep this resource up to date by periodically refining both the clusters hierarchy and its annotation. 


**Can I use this data in my work?**

This data is free to access and to use. We only ask you to cite the following publications.