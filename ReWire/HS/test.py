import json, requests
from pprint import pprint

L1000FWD_URL = 'https://maayanlab.cloud/l1000fwd/'

up_genes = ['KIAA0907','KDM5A','CDC25A','EGR1','GADD45B','RELB','TERF2IP','SMNDC1','TICAM1','NFKB2','RGS2','NCOA3','ICAM1','TEX10','CNOT4','ARID4B','CLPX','CHIC2','CXCL2','FBXO11','MTF2','CDK2','DNTTIP2','GADD45A','GOLT1B','POLR2K','NFKBIE','GABPB1','ECD','PHKG2','RAD9A','NET1','KIAA0753','EZH2','NRAS','ATP6V0B','CDK7','CCNH','SENP6','TIPARP','FOS','ARPP19','TFAP2A','KDM5B','NPC1','TP53BP2','NUSAP1']
down_genes = ['SCCPDH','KIF20A','FZD7','USP22','PIP4K2B','CRYZ','GNB5','EIF4EBP1','PHGDH','RRAGA','SLC25A46','RPA1','HADH','DAG1','RPIA','P4HA2','MACF1','TMEM97','MPZL1','PSMG1','PLK1','SLC37A4','GLRX','CBR3','PRSS23','NUDCD3','CDC20','KIAA0528','NIPSNAP1','TRAM2','STUB1','DERA','MTHFD2','BLVRA','IARS2','LIPA','PGM1','CNDP2','BNIP3','CTSL1','CDC25B','HSPA8','EPRS','PAX8','SACM1L','HOXA5','TLE1','PYGL','TUBB6','LOXL1']
payload = {
	'up_genes': up_genes,
	'down_genes': down_genes
}

response = requests.post(L1000FWD_URL + 'sig_search', json=payload)
if response.status_code == 200:
	pprint(response.json())
	json.dump(response.json(), open('api3_result.json', 'wb'), indent=4)