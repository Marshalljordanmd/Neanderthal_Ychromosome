#from STat Quest Python PCA video
#trying to do PCA 
#sample	den8	mez2	I10872_B	I10873_B2b	32_I0231_Russia_4844.0_R1b1a1b1b3	208_I12354_Argentina_450.0_Q1b1a1a	585_I3442_Belize_4998.0_Q1b1a1a	729_I2163_Bulgaria_3639.0_R1a1a1	784_I10873_Cameroon_3097.0_B	787_I10872_Cameroon_7820.0_B	788_I10873_Cameroon_3097.0_B2b	1553_I24882_Croatia_2599.0_J2b2a1a1a1b2~	1597_CAO022026_Cuba_1313.0_Q1b1a1a	1598_CAO023025_Cuba_932.0_Q1b1a1a	1599_CAO024_Cuba_1319.0_Q1b1a1a	1679_I7278_Czech Republic_4333.0_R1b1a1b1a1a2b1c2b1a2	1682_I7286_Czech Republic_4221.0_R1b1a1b1a1a2b1	1719_I14169_Czech Republic_5850.0_R1b	1723_I14173_Czech Republic_5850.0_R1b	1744_I13467_Czech Republic_4289.0_R1b1a1b1b3	1836_I14193_Czech Republic_3850.0_R1a1a1	2023_I14986_Czech Republic_2255.0_R1b1a1b1a1a2b1	2027_I15042_Czech Republic_2225.0_R1b1a1b1a1a2	2090_I13795_Czech Republic_3035.0_R1a1a1	2131_I4893_Czech Republic_6345.0_G2a2a1	2315_I15111_Dominican Republic_607.0_Q1b1a1a	2339_I12344_Dominican Republic_1150.0_Q1b1a1a	2340_I12347_Dominican Republic_1150.0_Q1b1a	2342_I13189_Dominican Republic_753.0_Q1b1a1a	2345_I13195_Dominican Republic_601.0_Q1b1a1a	2420_I14991_Dominican Republic_614.0_Q1b1a1a	2422_I14992_Dominican Republic_543.0_Q1b1a1a	2481_I2447_United Kingdom_3938.0_R1b1a1b1a1a2c1	2538_I6777_United Kingdom_4050.0_R1b1a1b1a1a2c1	2539_I7570_United Kingdom_3569.0_R1b1a1b1a1a2	2566_I5502_United Kingdom_2054.0_R1b1a1b1a1a2	2574_I12413_United Kingdom_2175.0_R1b1a1b1a1a2a	2592_I14327_United Kingdom_2081.0_R1b1a1b1a1a2a	2603_I27380_United Kingdom_4228.0_R1b1a1b1a1a2c1	2636_I27382_United Kingdom_2592.0_R1b1a1b1a1a2c1a1a1a1	2669_I13713_United Kingdom_2912.0_R1b1a1b1a1a2c1	2693_I11144_United Kingdom_1976.0_R1b1a1b1a1a2c1a1i3	2738_I7575_United Kingdom_3107.0_R1b1a1b1a1a2c1	2743_I7640_United Kingdom_3307.0_R1b1a1b1a1a2c1	2763_I11151_United Kingdom_2227.0_R1b1a1b1a1a2c1	2764_I11153_United Kingdom_2285.0_R1b1a1b1a1a2c1a5c2	2779_I13730_United Kingdom_2237.0_R1b1a1b1a1a2c1a2a	2780_I13731_United Kingdom_2246.0_R1b1a1b1a1a2c1	2784_I14380_United Kingdom_2235.0_R1b1a1b1a1a2c1	2800_I16592_United Kingdom_2231.0_R1b1a1b1a1a2c1a6	2808_I17016_United Kingdom_2226.0_R1b1a1b1a1a2c1	2828_I19911_United Kingdom_2250.0_R1b1a1b1a1a2c1	2832_I20586_United Kingdom_2250.0_R1b1a1b1a1a2c1	2842_I21181_United Kingdom_2250.0_R1b1a1b1a1a2c1a1k	2843_I21182_United Kingdom_2250.0_R1b1a1b1a1a2c1	2854_I11991_United Kingdom_2116.0_R1b1a1b1a1a2c1	2855_I11992_United Kingdom_2095.0_R1b1a1b1a1a2c1	2877_I17264_United Kingdom_2225.0_R1b1a1b1a1a2c1	2962_I6750_United Kingdom_5650.0_I2a1b1a1a1b	3244_I5950_Ethiopia_4470.0_E1b1a2b2~	4402_I24528_Guam_475.0_O2a2b2a2b	4426_I24596_Guam_475.0_O2a2b2a2b	4436_I24237_Guam_475.0_O2a2b2a2b	4645_I16759_Hungary_1225.0_R1b1a1b1b3a1a	4681_I2364_Hungary_4220.0_H	4803_SZ2_Hungary_1442.0_R1b1a1b1a1a1c2b	4841_I1495_Hungary_6367.0_I2a1a1b	4912_I1882_Hungary_7050.0_G2a2b2a	5818_I3124_Italy_3824.0_R1b1a1b1a1a2	6296_I11541_Kazakhstan_3684.0_R1a1a1b2a2	6380_I4785_Kazakhstan_2675.0_..	6428_I10112_Kazakhstan_3497.0_R1a1a1b2a2	6719_I4434_Latvia_7441.0_R1b1a1	6968_Ma912_Malaysia_2459.0_O1b1a1a1	7141_SHT001_Mongolia_5009.0_R1b1a1b1a1	7202_I12956_Mongolia_2326.0_..	7266_I13505_Mongolia_3001.0_Q1a	7293_I6363_Mongolia_3095.0_R1a1a1b2a2a3~	7301_I13173_Mongolia_3722.0_N	7403_TAF013_Morocco_14500.0_E1b1b1a	8293_I6537_Poland_4130.0_R1b1a1b1a1	8391_I6601_Portugal_4650.0_I2a1a1a1~	8633_I6714_Russia_4479.0_Q1b2a1a~	8634_I3949_Russia_4569.0_Q1b	8636_I3949_Russia_4569.0_Q1b2a1a~	8860_Kostenki14_Russia_38052.0_C1b	9163_I1526_Russia_4779.0_Q1b1b~	9164_I7335_Russia_4465.0_Q1b1a3	9225_Yana2_Russia_31850.0_P1~	9369_I2631_United Kingdom_4957.0_I2a1a2	9576_I5696_Slovenia_2272.0_R1b1a1b1a1a2b1c2	9958_I2472_Spain_3428.0_R1b1a1b1a1	10978_ART024_Turkey_5384.0_G2a2b1	11076_Bar31_Turkey_8272.0_G2a	11403_I24597_USA_400.0_O2a2b	11412_I24339_USA_400.0_O2a2b	11423_AHUR770c_USA_10988.0_Q1b1a1a	11498_I3921_Vanuatu_1260.0_M	11501_I4106_Vanuatu_140.0_O1a2	11502_I4419_Vanuatu_140.0_S	11506_I4106_Vanuatu_140.0_O1a	12039_KS20_KS25.SG_Nepal_2351.0_O2a2b1a1a1a4a1	12061_S143_S173.SG_Nepal_1275.0_O2a2b1a1a1a4a1	12635_CAO023025_Cuba_932.0_Q1b1a1a	12636_CAO024_Cuba_1319.0_Q1b1a1a	12637_CAO027_Cuba_1299.0_Q1b1a1a

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA

data = pd.read_csv('dist_matrix_ancient2',sep='\t',comment='#',header=None)

print(data)
#print(data.shape)  #gives 592 sites by 36 total samples
data = data.set_index(0)
print(data)



scaled_data = preprocessing.scale(data.T)  #passing in the transpose of the dataframe

pca = PCA()
pca.fit(scaled_data)  #this does all the PCA math
pca_data = pca.transform(scaled_data)   #generates coordinates for a PCA graph based on loading scores and scaled data

#make a scree plot to see how much each principal component contributes
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ['PC' + str(x) for x in range(1,len(per_var)+1)]  #labels for scree plot. "PC1","PC2",etc, one label per principal component
#print(labels)
plt.bar(x=range(1,len(per_var)+1),height=per_var,tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

#sample =	[den8	mez2	I10872_B	I10873_B2b	32_I0231_Russia_4844.0_R1b1a1b1b3	208_I12354_Argentina_450.0_Q1b1a1a	585_I3442_Belize_4998.0_Q1b1a1a	729_I2163_Bulgaria_3639.0_R1a1a1	784_I10873_Cameroon_3097.0_B	787_I10872_Cameroon_7820.0_B	788_I10873_Cameroon_3097.0_B2b	1553_I24882_Croatia_2599.0_J2b2a1a1a1b2~	1597_CAO022026_Cuba_1313.0_Q1b1a1a	1598_CAO023025_Cuba_932.0_Q1b1a1a	1599_CAO024_Cuba_1319.0_Q1b1a1a	1679_I7278_Czech Republic_4333.0_R1b1a1b1a1a2b1c2b1a2	1682_I7286_Czech Republic_4221.0_R1b1a1b1a1a2b1	1719_I14169_Czech Republic_5850.0_R1b	1723_I14173_Czech Republic_5850.0_R1b	1744_I13467_Czech Republic_4289.0_R1b1a1b1b3	1836_I14193_Czech Republic_3850.0_R1a1a1	2023_I14986_Czech Republic_2255.0_R1b1a1b1a1a2b1	2027_I15042_Czech Republic_2225.0_R1b1a1b1a1a2	2090_I13795_Czech Republic_3035.0_R1a1a1	2131_I4893_Czech Republic_6345.0_G2a2a1	2315_I15111_Dominican Republic_607.0_Q1b1a1a	2339_I12344_Dominican Republic_1150.0_Q1b1a1a	2340_I12347_Dominican Republic_1150.0_Q1b1a	2342_I13189_Dominican Republic_753.0_Q1b1a1a	2345_I13195_Dominican Republic_601.0_Q1b1a1a	2420_I14991_Dominican Republic_614.0_Q1b1a1a	2422_I14992_Dominican Republic_543.0_Q1b1a1a	2481_I2447_United Kingdom_3938.0_R1b1a1b1a1a2c1	2538_I6777_United Kingdom_4050.0_R1b1a1b1a1a2c1	2539_I7570_United Kingdom_3569.0_R1b1a1b1a1a2	2566_I5502_United Kingdom_2054.0_R1b1a1b1a1a2	2574_I12413_United Kingdom_2175.0_R1b1a1b1a1a2a	2592_I14327_United Kingdom_2081.0_R1b1a1b1a1a2a	2603_I27380_United Kingdom_4228.0_R1b1a1b1a1a2c1	2636_I27382_United Kingdom_2592.0_R1b1a1b1a1a2c1a1a1a1	2669_I13713_United Kingdom_2912.0_R1b1a1b1a1a2c1	2693_I11144_United Kingdom_1976.0_R1b1a1b1a1a2c1a1i3	2738_I7575_United Kingdom_3107.0_R1b1a1b1a1a2c1	2743_I7640_United Kingdom_3307.0_R1b1a1b1a1a2c1	2763_I11151_United Kingdom_2227.0_R1b1a1b1a1a2c1	2764_I11153_United Kingdom_2285.0_R1b1a1b1a1a2c1a5c2	2779_I13730_United Kingdom_2237.0_R1b1a1b1a1a2c1a2a	2780_I13731_United Kingdom_2246.0_R1b1a1b1a1a2c1	2784_I14380_United Kingdom_2235.0_R1b1a1b1a1a2c1	2800_I16592_United Kingdom_2231.0_R1b1a1b1a1a2c1a6	2808_I17016_United Kingdom_2226.0_R1b1a1b1a1a2c1	2828_I19911_United Kingdom_2250.0_R1b1a1b1a1a2c1	2832_I20586_United Kingdom_2250.0_R1b1a1b1a1a2c1	2842_I21181_United Kingdom_2250.0_R1b1a1b1a1a2c1a1k	2843_I21182_United Kingdom_2250.0_R1b1a1b1a1a2c1	2854_I11991_United Kingdom_2116.0_R1b1a1b1a1a2c1	2855_I11992_United Kingdom_2095.0_R1b1a1b1a1a2c1	2877_I17264_United Kingdom_2225.0_R1b1a1b1a1a2c1	2962_I6750_United Kingdom_5650.0_I2a1b1a1a1b	3244_I5950_Ethiopia_4470.0_E1b1a2b2~	4402_I24528_Guam_475.0_O2a2b2a2b	4426_I24596_Guam_475.0_O2a2b2a2b	4436_I24237_Guam_475.0_O2a2b2a2b	4645_I16759_Hungary_1225.0_R1b1a1b1b3a1a	4681_I2364_Hungary_4220.0_H	4803_SZ2_Hungary_1442.0_R1b1a1b1a1a1c2b	4841_I1495_Hungary_6367.0_I2a1a1b	4912_I1882_Hungary_7050.0_G2a2b2a	5818_I3124_Italy_3824.0_R1b1a1b1a1a2	6296_I11541_Kazakhstan_3684.0_R1a1a1b2a2	6380_I4785_Kazakhstan_2675.0_..	6428_I10112_Kazakhstan_3497.0_R1a1a1b2a2	6719_I4434_Latvia_7441.0_R1b1a1	6968_Ma912_Malaysia_2459.0_O1b1a1a1	7141_SHT001_Mongolia_5009.0_R1b1a1b1a1	7202_I12956_Mongolia_2326.0_..	7266_I13505_Mongolia_3001.0_Q1a	7293_I6363_Mongolia_3095.0_R1a1a1b2a2a3~	7301_I13173_Mongolia_3722.0_N	7403_TAF013_Morocco_14500.0_E1b1b1a	8293_I6537_Poland_4130.0_R1b1a1b1a1	8391_I6601_Portugal_4650.0_I2a1a1a1~	8633_I6714_Russia_4479.0_Q1b2a1a~	8634_I3949_Russia_4569.0_Q1b	8636_I3949_Russia_4569.0_Q1b2a1a~	8860_Kostenki14_Russia_38052.0_C1b	9163_I1526_Russia_4779.0_Q1b1b~	9164_I7335_Russia_4465.0_Q1b1a3	9225_Yana2_Russia_31850.0_P1~	9369_I2631_United Kingdom_4957.0_I2a1a2	9576_I5696_Slovenia_2272.0_R1b1a1b1a1a2b1c2	9958_I2472_Spain_3428.0_R1b1a1b1a1	10978_ART024_Turkey_5384.0_G2a2b1	11076_Bar31_Turkey_8272.0_G2a	11403_I24597_USA_400.0_O2a2b	11412_I24339_USA_400.0_O2a2b	11423_AHUR770c_USA_10988.0_Q1b1a1a	11498_I3921_Vanuatu_1260.0_M	11501_I4106_Vanuatu_140.0_O1a2	11502_I4419_Vanuatu_140.0_S	11506_I4106_Vanuatu_140.0_O1a	12039_KS20_KS25.SG_Nepal_2351.0_O2a2b1a1a1a4a1	12061_S143_S173.SG_Nepal_1275.0_O2a2b1a1a1a4a1	12635_CAO023025_Cuba_932.0_Q1b1a1a	12636_CAO024_Cuba_1319.0_Q1b1a1a	12637_CAO027_Cuba_1299.0_Q1b1a1a]
#['den8','mez2','I10872_B','I10873_B2b','32_I0231_Russia_4844.0_R1b1a1b1b3','208_I12354_Argentina_450.0_Q1b1a1a','585_I3442_Belize_4998.0_Q1b1a1a','729_I2163_Bulgaria_3639.0_R1a1a1','784_I10873_Cameroon_3097.0_B','787_I10872_Cameroon_7820.0_B','788_I10873_Cameroon_3097.0_B2b','1553_I24882_Croatia_2599.0_J2b2a1a1a1b2~','1597_CAO022026_Cuba_1313.0_Q1b1a1a','1598_CAO023025_Cuba_932.0_Q1b1a1a','1599_CAO024_Cuba_1319.0_Q1b1a1a','1679_I7278_Czech Republic_4333.0_R1b1a1b1a1a2b1c2b1a2','1682_I7286_Czech Republic_4221.0_R1b1a1b1a1a2b1','1719_I14169_Czech Republic_5850.0_R1b','1723_I14173_Czech Republic_5850.0_R1b','1744_I13467_Czech Republic_4289.0_R1b1a1b1b3','1836_I14193_Czech Republic_3850.0_R1a1a1','2023_I14986_Czech Republic_2255.0_R1b1a1b1a1a2b1','2027_I15042_Czech Republic_2225.0_R1b1a1b1a1a2','2090_I13795_Czech Republic_3035.0_R1a1a1','2131_I4893_Czech Republic_6345.0_G2a2a1','2315_I15111_Dominican Republic_607.0_Q1b1a1a','2339_I12344_Dominican Republic_1150.0_Q1b1a1a','2340_I12347_Dominican Republic_1150.0_Q1b1a','2342_I13189_Dominican Republic_753.0_Q1b1a1a','2345_I13195_Dominican Republic_601.0_Q1b1a1a','2420_I14991_Dominican Republic_614.0_Q1b1a1a','2422_I14992_Dominican Republic_543.0_Q1b1a1a','2481_I2447_United Kingdom_3938.0_R1b1a1b1a1a2c1','2538_I6777_United Kingdom_4050.0_R1b1a1b1a1a2c1','2539_I7570_United Kingdom_3569.0_R1b1a1b1a1a2','2566_I5502_United Kingdom_2054.0_R1b1a1b1a1a2','2574_I12413_United Kingdom_2175.0_R1b1a1b1a1a2a','2592_I14327_United Kingdom_2081.0_R1b1a1b1a1a2a','2603_I27380_United Kingdom_4228.0_R1b1a1b1a1a2c1','2636_I27382_United Kingdom_2592.0_R1b1a1b1a1a2c1a1a1a1','2669_I13713_United Kingdom_2912.0_R1b1a1b1a1a2c1','2693_I11144_United Kingdom_1976.0_R1b1a1b1a1a2c1a1i3','2738_I7575_United Kingdom_3107.0_R1b1a1b1a1a2c1','2743_I7640_United Kingdom_3307.0_R1b1a1b1a1a2c1','2763_I11151_United Kingdom_2227.0_R1b1a1b1a1a2c1','2764_I11153_United Kingdom_2285.0_R1b1a1b1a1a2c1a5c2','2779_I13730_United Kingdom_2237.0_R1b1a1b1a1a2c1a2a','2780_I13731_United Kingdom_2246.0_R1b1a1b1a1a2c1','2784_I14380_United Kingdom_2235.0_R1b1a1b1a1a2c1','2800_I16592_United Kingdom_2231.0_R1b1a1b1a1a2c1a6','2808_I17016_United Kingdom_2226.0_R1b1a1b1a1a2c1','2828_I19911_United Kingdom_2250.0_R1b1a1b1a1a2c1','2832_I20586_United Kingdom_2250.0_R1b1a1b1a1a2c1','2842_I21181_United Kingdom_2250.0_R1b1a1b1a1a2c1a1k','2843_I21182_United Kingdom_2250.0_R1b1a1b1a1a2c1','2854_I11991_United Kingdom_2116.0_R1b1a1b1a1a2c1','2855_I11992_United Kingdom_2095.0_R1b1a1b1a1a2c1','2877_I17264_United Kingdom_2225.0_R1b1a1b1a1a2c1','2962_I6750_United Kingdom_5650.0_I2a1b1a1a1b','3244_I5950_Ethiopia_4470.0_E1b1a2b2~','4402_I24528_Guam_475.0_O2a2b2a2b','4426_I24596_Guam_475.0_O2a2b2a2b','4436_I24237_Guam_475.0_O2a2b2a2b','4645_I16759_Hungary_1225.0_R1b1a1b1b3a1a','4681_I2364_Hungary_4220.0_H','4803_SZ2_Hungary_1442.0_R1b1a1b1a1a1c2b','4841_I1495_Hungary_6367.0_I2a1a1b','4912_I1882_Hungary_7050.0_G2a2b2a','5818_I3124_Italy_3824.0_R1b1a1b1a1a2','6296_I11541_Kazakhstan_3684.0_R1a1a1b2a2','6380_I4785_Kazakhstan_2675.0_..','6428_I10112_Kazakhstan_3497.0_R1a1a1b2a2','6719_I4434_Latvia_7441.0_R1b1a1','6968_Ma912_Malaysia_2459.0_O1b1a1a1','7141_SHT001_Mongolia_5009.0_R1b1a1b1a1','7202_I12956_Mongolia_2326.0_..','7266_I13505_Mongolia_3001.0_Q1a','7293_I6363_Mongolia_3095.0_R1a1a1b2a2a3~','7301_I13173_Mongolia_3722.0_N','7403_TAF013_Morocco_14500.0_E1b1b1a','8293_I6537_Poland_4130.0_R1b1a1b1a1','8391_I6601_Portugal_4650.0_I2a1a1a1~','8633_I6714_Russia_4479.0_Q1b2a1a~','8634_I3949_Russia_4569.0_Q1b','8636_I3949_Russia_4569.0_Q1b2a1a~','8860_Kostenki14_Russia_38052.0_C1b','9163_I1526_Russia_4779.0_Q1b1b~','9164_I7335_Russia_4465.0_Q1b1a3','9225_Yana2_Russia_31850.0_P1~','9369_I2631_United Kingdom_4957.0_I2a1a2','9576_I5696_Slovenia_2272.0_R1b1a1b1a1a2b1c2','9958_I2472_Spain_3428.0_R1b1a1b1a1','10978_ART024_Turkey_5384.0_G2a2b1','11076_Bar31_Turkey_8272.0_G2a','11403_I24597_USA_400.0_O2a2b','11412_I24339_USA_400.0_O2a2b','11423_AHUR770c_USA_10988.0_Q1b1a1a','11498_I3921_Vanuatu_1260.0_M','11501_I4106_Vanuatu_140.0_O1a2','11502_I4419_Vanuatu_140.0_S','11506_I4106_Vanuatu_140.0_O1a','12039_KS20_KS25.SG_Nepal_2351.0_O2a2b1a1a1a4a1','12061_S143_S173.SG_Nepal_1275.0_O2a2b1a1a1a4a1','12635_CAO023025_Cuba_932.0_Q1b1a1a','12636_CAO024_Cuba_1319.0_Q1b1a1a','12637_CAO027_Cuba_1299.0_Q1b1a1a']
samples = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109']
#pca_df = pd.DataFrame(pca_data,index=samples,columns=labels)
#pca_df = pd.DataFrame(pca_data,index=None,columns=labels)
pca_df = pd.DataFrame(pca_data)
print('')
print('')
print(pca_df)
print('')
print('')
#pos	a00_A00	den8	mez2	I5950_E1b1a2b2~	I10871_A00	I10872_B	I10873_B2b	32_I0231_Russia_4844.0_R1b1a1b1b3	208_I12354_Argentina_450.0_Q1b1a1a	585_I3442_Belize_4998.0_Q1b1a1a	729_I2163_Bulgaria_3639.0_R1a1a1	784_I10873_Cameroon_3097.0_B	787_I10872_Cameroon_7820.0_B	788_I10873_Cameroon_3097.0_B2b	1553_I24882_Croatia_2599.0_J2b2a1a1a1b2~	1597_CAO022026_Cuba_1313.0_Q1b1a1a	1598_CAO023025_Cuba_932.0_Q1b1a1a	1599_CAO024_Cuba_1319.0_Q1b1a1a	1679_I7278_Czech Republic_4333.0_R1b1a1b1a1a2b1c2b1a2	1682_I7286_Czech Republic_4221.0_R1b1a1b1a1a2b1	1719_I14169_Czech Republic_5850.0_R1b	1723_I14173_Czech Republic_5850.0_R1b	1744_I13467_Czech Republic_4289.0_R1b1a1b1b3	1836_I14193_Czech Republic_3850.0_R1a1a1	2023_I14986_Czech Republic_2255.0_R1b1a1b1a1a2b1	2027_I15042_Czech Republic_2225.0_R1b1a1b1a1a2	2090_I13795_Czech Republic_3035.0_R1a1a1	2131_I4893_Czech Republic_6345.0_G2a2a1	2315_I15111_Dominican Republic_607.0_Q1b1a1a	2339_I12344_Dominican Republic_1150.0_Q1b1a1a	2340_I12347_Dominican Republic_1150.0_Q1b1a	2342_I13189_Dominican Republic_753.0_Q1b1a1a	2345_I13195_Dominican Republic_601.0_Q1b1a1a	2420_I14991_Dominican Republic_614.0_Q1b1a1a	2422_I14992_Dominican Republic_543.0_Q1b1a1a	2481_I2447_United Kingdom_3938.0_R1b1a1b1a1a2c1	2538_I6777_United Kingdom_4050.0_R1b1a1b1a1a2c1	2539_I7570_United Kingdom_3569.0_R1b1a1b1a1a2	2566_I5502_United Kingdom_2054.0_R1b1a1b1a1a2	2574_I12413_United Kingdom_2175.0_R1b1a1b1a1a2a	2592_I14327_United Kingdom_2081.0_R1b1a1b1a1a2a	2603_I27380_United Kingdom_4228.0_R1b1a1b1a1a2c1	2636_I27382_United Kingdom_2592.0_R1b1a1b1a1a2c1a1a1a1	2669_I13713_United Kingdom_2912.0_R1b1a1b1a1a2c1	2693_I11144_United Kingdom_1976.0_R1b1a1b1a1a2c1a1i3	2738_I7575_United Kingdom_3107.0_R1b1a1b1a1a2c1	2743_I7640_United Kingdom_3307.0_R1b1a1b1a1a2c1	2763_I11151_United Kingdom_2227.0_R1b1a1b1a1a2c1	2764_I11153_United Kingdom_2285.0_R1b1a1b1a1a2c1a5c2	2779_I13730_United Kingdom_2237.0_R1b1a1b1a1a2c1a2a	2780_I13731_United Kingdom_2246.0_R1b1a1b1a1a2c1	2784_I14380_United Kingdom_2235.0_R1b1a1b1a1a2c1	2800_I16592_United Kingdom_2231.0_R1b1a1b1a1a2c1a6	2808_I17016_United Kingdom_2226.0_R1b1a1b1a1a2c1	2828_I19911_United Kingdom_2250.0_R1b1a1b1a1a2c1	2832_I20586_United Kingdom_2250.0_R1b1a1b1a1a2c1	2842_I21181_United Kingdom_2250.0_R1b1a1b1a1a2c1a1k	2843_I21182_United Kingdom_2250.0_R1b1a1b1a1a2c1	2854_I11991_United Kingdom_2116.0_R1b1a1b1a1a2c1	2855_I11992_United Kingdom_2095.0_R1b1a1b1a1a2c1	2877_I17264_United Kingdom_2225.0_R1b1a1b1a1a2c1	2962_I6750_United Kingdom_5650.0_I2a1b1a1a1b	3244_I5950_Ethiopia_4470.0_E1b1a2b2~	4402_I24528_Guam_475.0_O2a2b2a2b	4426_I24596_Guam_475.0_O2a2b2a2b	4436_I24237_Guam_475.0_O2a2b2a2b	4645_I16759_Hungary_1225.0_R1b1a1b1b3a1a	4681_I2364_Hungary_4220.0_H	4803_SZ2_Hungary_1442.0_R1b1a1b1a1a1c2b	4841_I1495_Hungary_6367.0_I2a1a1b	4912_I1882_Hungary_7050.0_G2a2b2a	5818_I3124_Italy_3824.0_R1b1a1b1a1a2	6296_I11541_Kazakhstan_3684.0_R1a1a1b2a2	6380_I4785_Kazakhstan_2675.0_..	6428_I10112_Kazakhstan_3497.0_R1a1a1b2a2	6719_I4434_Latvia_7441.0_R1b1a1	6968_Ma912_Malaysia_2459.0_O1b1a1a1	7141_SHT001_Mongolia_5009.0_R1b1a1b1a1	7202_I12956_Mongolia_2326.0_..	7266_I13505_Mongolia_3001.0_Q1a	7293_I6363_Mongolia_3095.0_R1a1a1b2a2a3~	7301_I13173_Mongolia_3722.0_N	7403_TAF013_Morocco_14500.0_E1b1b1a	8293_I6537_Poland_4130.0_R1b1a1b1a1	8391_I6601_Portugal_4650.0_I2a1a1a1~	8633_I6714_Russia_4479.0_Q1b2a1a~	8634_I3949_Russia_4569.0_Q1b	8636_I3949_Russia_4569.0_Q1b2a1a~	8860_Kostenki14_Russia_38052.0_C1b	9163_I1526_Russia_4779.0_Q1b1b~	9164_I7335_Russia_4465.0_Q1b1a3	9225_Yana2_Russia_31850.0_P1~	9369_I2631_United Kingdom_4957.0_I2a1a2	9576_I5696_Slovenia_2272.0_R1b1a1b1a1a2b1c2	9958_I2472_Spain_3428.0_R1b1a1b1a1	10978_ART024_Turkey_5384.0_G2a2b1	11076_Bar31_Turkey_8272.0_G2a	11403_I24597_USA_400.0_O2a2b	11412_I24339_USA_400.0_O2a2b	11423_AHUR770c_USA_10988.0_Q1b1a1a	11498_I3921_Vanuatu_1260.0_M	11501_I4106_Vanuatu_140.0_O1a2	11502_I4419_Vanuatu_140.0_S	11506_I4106_Vanuatu_140.0_O1a	12039_KS20_KS25.SG_Nepal_2351.0_O2a2b1a1a1a4a1	12061_S143_S173.SG_Nepal_1275.0_O2a2b1a1a1a4a1	12635_CAO023025_Cuba_932.0_Q1b1a1a	12636_CAO024_Cuba_1319.0_Q1b1a1a	12637_CAO027_Cuba_1299.0_Q1b1a1a
plt.scatter(pca_df[0],pca_df[1],c=['b', 'r', 'r', 'blueviolet', 'b', 'c', 'c', 'g', 'g', 'g', 'g', 'c', 'c', 'c', 'darkorange', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'blueviolet', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'blueviolet', 'g', 'darkorange', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'g', 'g', 'black', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],alpha=1)
plt.title('aDNA Haplogroups PCA graph')

plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))

# handles = ['Neander','A','B','Ham','Shem','Japheth']
# labels = ['r','b','c','blueviolet','g','gold']
# plt.legend(handles,labels)


# for s in pca_df.index:
# 	plt.annotate(s,(pca_df[0].loc[s],pca_df[1].loc[s]))

#plt.annotate('Ancients',color='r',xy=(.2,-1.3),fontweight='bold')
plt.annotate('A',color='b',xy=(38,-4),fontweight='bold')
plt.annotate('B',color='c',xy=(12,-5),fontweight='bold')
plt.annotate('E',color='blueviolet',xy=(10,-2),fontweight='bold')
plt.annotate('G',color='black',xy=(0,-2.5),fontweight='bold')
plt.annotate('N,O,Q,R,S',color='g',xy=(-7,3),fontweight='bold')
plt.annotate('I,J',color='darkorange',xy=(6,1),fontweight='bold')

plt.annotate('mez/den',color='r',xy=(28,-4),fontweight='bold')	
plt.show()



########Below are to make graph of PC2 and PC3
#samples = ['a00_A00','den8','mez2','I5950_E1b1a2b2~','I10871_A00','I10872_B','I10873_B2b','32_I0231_Russia_4844.0_R1b1a1b1b3','208_I12354_Argentina_450.0_Q1b1a1a','585_I3442_Belize_4998.0_Q1b1a1a','729_I2163_Bulgaria_3639.0_R1a1a1','784_I10873_Cameroon_3097.0_B','787_I10872_Cameroon_7820.0_B','788_I10873_Cameroon_3097.0_B2b','1553_I24882_Croatia_2599.0_J2b2a1a1a1b2~','1597_CAO022026_Cuba_1313.0_Q1b1a1a','1598_CAO023025_Cuba_932.0_Q1b1a1a','1599_CAO024_Cuba_1319.0_Q1b1a1a','1679_I7278_Czech Republic_4333.0_R1b1a1b1a1a2b1c2b1a2','1682_I7286_Czech Republic_4221.0_R1b1a1b1a1a2b1','1719_I14169_Czech Republic_5850.0_R1b','1723_I14173_Czech Republic_5850.0_R1b','1744_I13467_Czech Republic_4289.0_R1b1a1b1b3','1836_I14193_Czech Republic_3850.0_R1a1a1','2023_I14986_Czech Republic_2255.0_R1b1a1b1a1a2b1','2027_I15042_Czech Republic_2225.0_R1b1a1b1a1a2','2090_I13795_Czech Republic_3035.0_R1a1a1','2131_I4893_Czech Republic_6345.0_G2a2a1','2315_I15111_Dominican Republic_607.0_Q1b1a1a','2339_I12344_Dominican Republic_1150.0_Q1b1a1a','2340_I12347_Dominican Republic_1150.0_Q1b1a','2342_I13189_Dominican Republic_753.0_Q1b1a1a','2345_I13195_Dominican Republic_601.0_Q1b1a1a','2420_I14991_Dominican Republic_614.0_Q1b1a1a','2422_I14992_Dominican Republic_543.0_Q1b1a1a','2481_I2447_United Kingdom_3938.0_R1b1a1b1a1a2c1','2538_I6777_United Kingdom_4050.0_R1b1a1b1a1a2c1','2539_I7570_United Kingdom_3569.0_R1b1a1b1a1a2','2566_I5502_United Kingdom_2054.0_R1b1a1b1a1a2','2574_I12413_United Kingdom_2175.0_R1b1a1b1a1a2a','2592_I14327_United Kingdom_2081.0_R1b1a1b1a1a2a','2603_I27380_United Kingdom_4228.0_R1b1a1b1a1a2c1','2636_I27382_United Kingdom_2592.0_R1b1a1b1a1a2c1a1a1a1','2669_I13713_United Kingdom_2912.0_R1b1a1b1a1a2c1','2693_I11144_United Kingdom_1976.0_R1b1a1b1a1a2c1a1i3','2738_I7575_United Kingdom_3107.0_R1b1a1b1a1a2c1','2743_I7640_United Kingdom_3307.0_R1b1a1b1a1a2c1','2763_I11151_United Kingdom_2227.0_R1b1a1b1a1a2c1','2764_I11153_United Kingdom_2285.0_R1b1a1b1a1a2c1a5c2','2779_I13730_United Kingdom_2237.0_R1b1a1b1a1a2c1a2a','2780_I13731_United Kingdom_2246.0_R1b1a1b1a1a2c1','2784_I14380_United Kingdom_2235.0_R1b1a1b1a1a2c1','2800_I16592_United Kingdom_2231.0_R1b1a1b1a1a2c1a6','2808_I17016_United Kingdom_2226.0_R1b1a1b1a1a2c1','2828_I19911_United Kingdom_2250.0_R1b1a1b1a1a2c1','2832_I20586_United Kingdom_2250.0_R1b1a1b1a1a2c1','2842_I21181_United Kingdom_2250.0_R1b1a1b1a1a2c1a1k','2843_I21182_United Kingdom_2250.0_R1b1a1b1a1a2c1','2854_I11991_United Kingdom_2116.0_R1b1a1b1a1a2c1','2855_I11992_United Kingdom_2095.0_R1b1a1b1a1a2c1','2877_I17264_United Kingdom_2225.0_R1b1a1b1a1a2c1','2962_I6750_United Kingdom_5650.0_I2a1b1a1a1b','3244_I5950_Ethiopia_4470.0_E1b1a2b2~','4402_I24528_Guam_475.0_O2a2b2a2b','4426_I24596_Guam_475.0_O2a2b2a2b','4436_I24237_Guam_475.0_O2a2b2a2b','4645_I16759_Hungary_1225.0_R1b1a1b1b3a1a','4681_I2364_Hungary_4220.0_H','4803_SZ2_Hungary_1442.0_R1b1a1b1a1a1c2b','4841_I1495_Hungary_6367.0_I2a1a1b','4912_I1882_Hungary_7050.0_G2a2b2a','5818_I3124_Italy_3824.0_R1b1a1b1a1a2','6296_I11541_Kazakhstan_3684.0_R1a1a1b2a2','6380_I4785_Kazakhstan_2675.0_..','6428_I10112_Kazakhstan_3497.0_R1a1a1b2a2','6719_I4434_Latvia_7441.0_R1b1a1','6968_Ma912_Malaysia_2459.0_O1b1a1a1','7141_SHT001_Mongolia_5009.0_R1b1a1b1a1','7202_I12956_Mongolia_2326.0_..','7266_I13505_Mongolia_3001.0_Q1a','7293_I6363_Mongolia_3095.0_R1a1a1b2a2a3~','7301_I13173_Mongolia_3722.0_N','7403_TAF013_Morocco_14500.0_E1b1b1a','8293_I6537_Poland_4130.0_R1b1a1b1a1','8391_I6601_Portugal_4650.0_I2a1a1a1~','8633_I6714_Russia_4479.0_Q1b2a1a~','8634_I3949_Russia_4569.0_Q1b','8636_I3949_Russia_4569.0_Q1b2a1a~','8860_Kostenki14_Russia_38052.0_C1b','9163_I1526_Russia_4779.0_Q1b1b~','9164_I7335_Russia_4465.0_Q1b1a3','9225_Yana2_Russia_31850.0_P1~','9369_I2631_United Kingdom_4957.0_I2a1a2','9576_I5696_Slovenia_2272.0_R1b1a1b1a1a2b1c2','9958_I2472_Spain_3428.0_R1b1a1b1a1','10978_ART024_Turkey_5384.0_G2a2b1','11076_Bar31_Turkey_8272.0_G2a','11403_I24597_USA_400.0_O2a2b','11412_I24339_USA_400.0_O2a2b','11423_AHUR770c_USA_10988.0_Q1b1a1a','11498_I3921_Vanuatu_1260.0_M','11501_I4106_Vanuatu_140.0_O1a2','11502_I4419_Vanuatu_140.0_S','11506_I4106_Vanuatu_140.0_O1a','12039_KS20_KS25.SG_Nepal_2351.0_O2a2b1a1a1a4a1','12061_S143_S173.SG_Nepal_1275.0_O2a2b1a1a1a4a1','12635_CAO023025_Cuba_932.0_Q1b1a1a','12636_CAO024_Cuba_1319.0_Q1b1a1a','12637_CAO027_Cuba_1299.0_Q1b1a1a']

samples = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35']
#pca_df = pd.DataFrame(pca_data,index=samples,columns=labels)
#pca_df = pd.DataFrame(pca_data,index=None,columns=labels)
pca_df = pd.DataFrame(pca_data)
print(pca_df)
plt.scatter(pca_df[1],pca_df[2],c=['b', 'r', 'r', 'blueviolet', 'b', 'c', 'c', 'g', 'g', 'g', 'g', 'c', 'c', 'c', 'darkorange', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'blueviolet', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'blueviolet', 'g', 'darkorange', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'darkorange', 'g', 'g', 'black', 'black', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],alpha=1)
plt.title('aDNA Haplogroups PCA graph')

plt.xlabel('PC2 - {0}%'.format(per_var[1]))
plt.ylabel('PC3 - {0}%'.format(per_var[2]))

#plt.annotate('Ancients',color='r',xy=(-1.5,-1.3),fontweight='bold')
plt.annotate('A',color='b',xy=(-4,7.5),fontweight='bold')
plt.annotate('B',color='c',xy=(-5,-2.5),fontweight='bold')
plt.annotate('E',color='blueviolet',xy=(-2.6,-3.5),fontweight='bold')
plt.annotate('G',color='black',xy=(-2,-7.5),fontweight='bold')
plt.annotate('N,O,Q,R,S',color='g',xy=(2,1),fontweight='bold')
plt.annotate('I,J',color='darkorange',xy=(1.3,-2.8),fontweight='bold')

plt.annotate('mez/den',color='r',xy=(-5,2.5),fontweight='bold')	
plt.show()






