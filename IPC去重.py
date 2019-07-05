# -*- coding: utf-8 -*-
import pandas as pd 

df=pd.read_excel("data.xls",encoding="utf-8")

ipc_list=[]
for i in range(len(df)):
	ipcs=df['IPC分类号'][i].split(' | ')
	for ipc in ipcs:
		if ipc[0:4] not in ipc_list:
			ipc_list.append(ipc[0:4])
	print(ipc_list)
	ipc_list=[]