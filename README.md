# Cheat Sheet
slicing: nums[a,b]左闭右开，对应index: a到(b-1)，对应1-based position: (a+1)到b

range: range(a,b)左闭右开，表示a到b-1（所以nums[a,b]相当于用range(a,b)生成index a到(b-1), 然后调用index对应的position (a+1)到b）

pandas.DataFrame: df[a:b] and df.iloc[a:b, :]都是左闭右开，取index: a到b-1的行

所以，只用记得code中的范围左闭右开后就是index范围，不要老想实际位置，只要记得位置等于index+1就行了

特例： 
df.loc在slice时包含start和end
df.loc[2:5, :]表示index为2到5的行，所以左右都是闭区间  
而要回到iloc的范围的话就得使用df.loc[df.index[2:5], :]，即先利用普通slice的左闭右开性质，取df.index中的2到4，强行去掉5 (df.index是一个RangeIndex data type)
note: 若非特殊说明，以上都是在讲index (start from 0)
