# Cheat Sheet
slicing: nums[a,b]左闭右开，对应index: a到(b-1)，对应1-based position: (a+1)到b

range: range(a,b)左闭右开，表示a到b-1（所以nums[a,b]相当于用range(a,b)生成index a到(b-1), 然后调用index对应的position (a+1)到b）

pandas.DataFrame: df[a:b] and df.loc[a:b,:]都是用
