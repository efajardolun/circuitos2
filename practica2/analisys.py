import PyLTSpice
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

c1=PyLTSpice.RawRead('circuito1.raw')

elements = ['v1', 'rg', 'r1', 'r2', 'r3', 'r4', 'ab']
measurements=[['v'+el+'rms', 'v'+el+'avg' , 'i'+el+'rms' , 'i'+el+'avg', 'p'+el+'avg'] for el in elements]

df1=[[c1.get_trace(meas_name)[0] for meas_name in meas_namelist] for meas_namelist in measurements]
df_medidas_c1 = pd.DataFrame((np.array(df1)),
                             index=[str.upper(x) for x in elements ],
                             columns=pd.MultiIndex.from_tuples([("V", "RMS"),
                                                                ("V", "AVG"),
                                                                ("I","RMS"),
                                                                ("I","AVG"),
                                                                ("P","AVG")]))
df_medidas_c1.insert(1,
                     ("V","RMSAC"),
                     (df_medidas_c1.V.RMS**2-df_medidas_c1.V.AVG**2)**0.5)

df_medidas_c1.insert(4,
                     ("I","RMSAC"),
                     (df_medidas_c1.I.RMS**2-df_medidas_c1.I.AVG**2)**0.5)

df_medidas_c1['I']=df_medidas_c1['I']*1000
df_medidas_c1['P']=df_medidas_c1['P']*1000

df_medidas_c1.style.format('{:.0e}',precision=3)
df_medidas_c1.style.to_latex("tabla_medidas_c1.tex", hrules=True,
                             label="tab:med_c1",
                             caption="Datos simulación del circuito RL")


plt.plot(c1.get_trace('time'), c1.get_trace('vab'))
plt.plot(c1.get_trace('time'), 1000*c1.get_trace('i(l)').data)
plt.plot(c1.get_trace('time'), 1000*c1.get_trace('l:power').data)
plt.savefig("c1.png")
plt.clf()

c1m=PyLTSpice.RawRead('circuito1Mod.raw')

df1=[[c1m.get_trace(meas_name)[0] for meas_name in meas_namelist] for meas_namelist in measurements]
df_medidas_c1m = pd.DataFrame((np.array(df1)),
                             index=[str.upper(x) for x in elements ],
                             columns=pd.MultiIndex.from_tuples([("V", "RMS"),
                                                                ("V", "AVG"),
                                                                ("I","RMS"),
                                                                ("I","AVG"),
                                                                ("P","AVG")]))
df_medidas_c1m.insert(1,
                     ("V","RMSAC"),
                     (df_medidas_c1m.V.RMS**2-df_medidas_c1m.V.AVG**2)**0.5)

df_medidas_c1m.insert(4,
                     ("I","RMSAC"),
                     (df_medidas_c1m.I.RMS**2-df_medidas_c1m.I.AVG**2)**0.5)

df_medidas_c1m['I']=df_medidas_c1m['I']*1000
df_medidas_c1m['P']=df_medidas_c1m['P']*1000

df_medidas_c1m.style.format('{:.0e}',precision=3)
df_medidas_c1m.style.to_latex("tabla_medidas_c1m.tex", hrules=True,
                             label="tab:med_c1m",
                             caption="Datos simulación del circuito RL Modificado")


plt.plot(c1m.get_trace('time'), c1m.get_trace('vab'))
plt.plot(c1m.get_trace('time'), 1000*c1m.get_trace('i(l)').data)
plt.plot(c1m.get_trace('time'), 1000*c1m.get_trace('l:power').data)
plt.savefig("c1m.png")

#plt.show()
