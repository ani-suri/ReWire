Class_0_original_dataset and Class_1_original_dataset are the original datasets.

Each is processed as shown in CheckSMILEv2.ipynb and generated processed_class0.csv and processed_class0.csv.

Because some of the names (like NSC number) in the original dataset are not supported for searching in PubChem, I searched manually and got augmented_class0.csv and augmented_class1.csv.

In the augmented CSVs, I also included the PubChem CIDs and InChIKeys for the matched SMILES because they are unique identifiers for chemical structures while a drug name could be related to multiple chemical structures.

Compounds that have no matching SMILES record in PubChem are filtered out in nomatch_class0.csv and nomatch_class1.csv.




