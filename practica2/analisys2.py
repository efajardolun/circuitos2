import PyLTSpice
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

c=PyLTSpice.RawRead('circuito2.raw')

elements = ['v1', 'rg', 'r1', 'r2', 'r3', 'r4', 'ab']
measurements=[['v'+el+'rms', 'v'+el+'avg' , 'i'+el+'rms' , 'i'+el+'avg', 'p'+el+'avg'] for el in elements]

df1=[[c.get_trace(meas_name)[0] for meas_name in meas_namelist] for meas_namelist in measurements]
df_medidas_c = pd.DataFrame((np.array(df1)),
                             index=[str.upper(x) for x in elements ],
                             columns=pd.MultiIndex.from_tuples([("V", "RMS"),
                                                                ("V", "AVG"),
                                                                ("I","RMS"),
                                                                ("I","AVG"),
                                                                ("P","AVG")]))
df_medidas_c.insert(1,
                     ("V","RMSAC"),
                     (df_medidas_c.V.RMS**2-df_medidas_c.V.AVG**2)**0.5)

df_medidas_c.insert(4,
                     ("I","RMSAC"),
                     (df_medidas_c.I.RMS**2-df_medidas_c.I.AVG**2)**0.5)

df_medidas_c['I']=df_medidas_c['I']*1000
df_medidas_c['P']=df_medidas_c['P']*1000

df_medidas_c.style.format('{:.0e}',precision=3)
df_medidas_c.style.to_latex("tabla_medidas_c2.tex", hrules=True,
                             label="tab:med_c2",
                             caption="Datos simulación del circuito RC")


plt.plot(c.get_trace('time'), c.get_trace('vab'))
plt.plot(c.get_trace('time'), 1000*c.get_trace('i(c)').data)
plt.plot(c.get_trace('time'), 1000*c.get_trace('c:power').data)
plt.savefig("c2.png")
plt.clf()

cm=PyLTSpice.RawRead('circuito2Mod.raw')

df1=[[cm.get_trace(meas_name)[0] for meas_name in meas_namelist] for meas_namelist in measurements]
df_medidas_cm = pd.DataFrame((np.array(df1)),
                             index=[str.upper(x) for x in elements ],
                             columns=pd.MultiIndex.from_tuples([("V", "RMS"),
                                                                ("V", "AVG"),
                                                                ("I","RMS"),
                                                                ("I","AVG"),
                                                                ("P","AVG")]))
df_medidas_cm.insert(1,
                     ("V","RMSAC"),
                     (df_medidas_cm.V.RMS**2-df_medidas_cm.V.AVG**2)**0.5)

df_medidas_cm.insert(4,
                     ("I","RMSAC"),
                     (df_medidas_cm.I.RMS**2-df_medidas_cm.I.AVG**2)**0.5)

df_medidas_cm['I']=df_medidas_cm['I']*1000
df_medidas_cm['P']=df_medidas_cm['P']*1000

df_medidas_cm.style.format('{:.0e}',precision=3)
df_medidas_cm.style.to_latex("tabla_medidas_c2m.tex", hrules=True,
                             label="tab:med_c2m",
                             caption="Datos simulación del circuito RC Modificado")


plt.plot(cm.get_trace('time'), cm.get_trace('vab'))
plt.plot(cm.get_trace('time'), 1000*cm.get_trace('i(c)').data)
plt.plot(cm.get_trace('time'), 1000*cm.get_trace('c:power').data)
plt.savefig("c2m.png")

#plt.show()
