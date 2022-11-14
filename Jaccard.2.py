#to compute the Jaccard index for samples in a vcf file
#J = intersection/union = |A ^ B|/|A U B| = |A^B|/(|A|+|B|-|A^B|)

import pandas as pd
import os



if os.path.exists('Jaccard_table'):
	os.remove('Jaccard_table')



def jaccard(s1,s2):
#to get the JC for the pair of columns
	intersect = 0
	total_gtpos = 0

	for i in range(rws):

		geno1 = df.iloc[i,s1]
		geno2 = df.iloc[i,s2]
	
		if geno1 !='.' and geno2 !='.':
			if geno1 == '1' and geno2 == '1':
				intersect += 1
			if geno1 == '1' or geno2 == '1':
				total_gtpos += 1

	JC = intersect/total_gtpos
	JC = round(JC,3)
	return(JC)





#file = 'Petr_Noah_root_annotated.vcf'
#file = 'ancient_y_annotated.vcf'
file = 'Petr_karmin_ABhaplogroups_37_annotated_culled.vcf'
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	den4	den8	mez2	spy1	elsidron2	GRC13292545_A00	GRC13292546_A00	GS000016204-ASM_A3	GS000035247-ASM_A2	GS000001577-ASM_B5	GS000001807-ASM_B4	GS000003125-ASM_B5	GS000003124-ASM_B4	GS00319-DNA_A01_1100_37-ASM_B4	GS00319-DNA_C01_1100_37-ASM_B4	GS00319-DNA_G01_1100_37-ASM_B4	GS00319-DNA_G02_1100_37-ASM_B4	GS000035246-ASM_B2	a00_A00	S_BedouinB-1_J1b2b	S_Burmese-1_O3a1c2	S_Dai-2_O21a	S_Dinka-1_E2a	S_Finnish-2_I1a1b5	S_French-1_J2a1b1	S_Gambian-1_E1b1a1a1f	S_Han-2_O1a1	S_Ju_hoan_North-1_B2b1b	S_Karitiana-1_Q1a2a1a1	S_Mandenka-1_E1b1a1a1g1	S_Mbuti-1_E1b1a1a1g1	S_Papuan-2_S	S_Punjabi-1_J2a1	S_Saami-2_N1c1a1a2a	S_Sardinian-1_J1b2b	S_Thai-1_O3a2c	S_Turkish-1_R1b1a2a1a2c1g	S_Yoruba-2_E1b1a1a1f1b1


df = pd.read_csv(file,sep='\t',comment='#',header=None,low_memory=False)
print(df)
rws = df.shape[0]
ref = df.iloc[:,3]
alt = df.iloc[:,4]
noah = df.iloc[:,5]

f2 = 'correct.txt'
df2 = pd.read_csv(f2,sep='\t',header=None)
print(df2)
cid = df2.iloc[0,:]



s1 = [9,10,11,12,13]  #ancient samples
s2 = [27,16,17,26,31]  #modern samples

print('ancients = ',cid[9],',',cid[10],',',cid[11],',',cid[12],',',cid[13])
print('')
print('moderns = ',cid[27],',',cid[16],',',cid[17],',',cid[26],',',cid[31])


intersect = 0
total_gtpos = 0


with open('Jaccard_table','a') as jc:
	jc.write('Jaccard coefficients')
	jc.write('\n')
	jc.write('\t')
	jc.write('\t')
	jc.write('A00')
	jc.write('\t')
	jc.write('\t')
	jc.write('A3')
	jc.write('\t')
	jc.write('\t')
	jc.write('A2')
	jc.write('\t')
	jc.write('\t')
	jc.write('B2')
	jc.write('\t')
	jc.write('\t')
	jc.write('E2a')
	jc.write('\n')
	
	for ancient in s1:
		jc.write(cid[ancient])
		print(cid[ancient])
		
		for modern in s2:
			jc.write('\t')			
			jc_coef = jaccard(ancient,modern)
			jc.write(str(jc_coef))
			
		jc.write('\n')
		
print('Done')
			


















