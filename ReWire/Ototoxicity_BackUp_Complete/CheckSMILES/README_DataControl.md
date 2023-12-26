# Checking SMILES in the original dataset



Goals
 - Make sure that the SMILES used for prediction represents the chemical structure we needed correctly and uniquely


About the files
 - **Class_0_original_dataset** and **Class_1_original_dataset** are the original datasets.

 - Each is processed as shown in CheckSMILEv2.ipynb and generated **processed_class0.csv** and **processed_class1.csv**.

 - Because some of the names (like NSC number) in the original dataset are not supported for searching in PubChem, I searched manually and got **augmented_class0.csv** and **augmented_class1.csv**.

 - Compounds that have no matching SMILES record in PubChem are filtered out in **nomatch_class0.csv** and **nomatch_class1.csv**. (294/906 for class1, 598/1607 for class0)

Methods
  1. Each compound name was searched in PubChem and relevant chemicals were retrieved in the format of PubChem ID.

  2. The original SMILES was compared against the most relevant SMILES in PubChem and results indicated in Match_MostRelevant column.

  3. If not matched with the most Relevant SMILES, the original SMILES would be compared against all relevant SMILES retrieved in step 1. 

  4. If a compound finds a match in step 2 or step 3, the corresponding SMILES(in PubChem format), PubChemID and InChIKeys will be stored.

Comparison of two SMILES
 - To check if two SMILES represent the same chemical structure, it is not reasonbale to simply compare two strings because different SMILES format could potentially represent the same structure. 

 - The current method is to create the molecule based on the two SMILES using RDkit and then regenerate the SMILES from the molecules and check if the two regenerated SMILES are the same. 

 - It is originally believed that the SMILES generated with the same toolkit would be the same for the same molecule. Further testification may be needed for this idea.

Note
 - The PubChem CIDs and InChIKeys for the matched SMILES are also included because they are unique identifiers for chemical structures while a drug name could be related to multiple chemical structures. Using these IDs/keys could reduce potential mistakes.


