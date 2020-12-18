import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


binstep=0.1


dfr=pd.read_csv('shortGRBsDetectedByIRT.txt',header=None)
dfx=pd.read_csv('shortGRBsDetectedBySXIXGIS.txt',header=None)
zr=dfr[0]
zx=dfx[0]

zmax=20

l=int((zmax-0)/binstep)

bins=[]
for i in range(0,l):
    bins.append(round(binstep*i,1))
    #bins.append(round(binstep*i,2))

#hist_x_density=plt.hist(zx,bins=bins,density=True,color='blue',linewidth=5,histtype='step',alpha=0)
hist_x_density=plt.hist(zx,bins=bins,density=True,color='blue',linewidth=5,alpha=0)

#hist_x_density=plt.hist(zx,bins=bins,density=True,alpha=0)
hist_x_number=plt.hist(zx,bins=bins,alpha=0)
# distribuzione delle simulazioni (400)
#Fx=hist_x_density[0]
zbinx=hist_x_density[1]
Nx=hist_x_number[0]
Fx=Nx/sum(Nx)     # Fx con stepbin =1 riproduce le percentuali del MOS quindi ok

# con plt.hist credo si deve moltiplicare per stebin ogni bin (con 1 viene automatico ma con 0.3 no)

# percentuale di casi per ciascun zbin fino a z=3

#PGRBinz_x=Fx[0:10]

hist_r_density=plt.hist(zr,bins=bins,density=True,alpha=0)
hist_r_number=plt.hist(zr,bins=bins,alpha=0)
# distribuzione delle simulazioni (400)
# percentuale di casi per ciascun zbin
#Fr=hist_r_density[0]
zbin_r=hist_r_density[1]
Nr=hist_r_number[0]
Fr=Nr/sum(Nr)

frac=len(zr)/len(zx)

#PGRBinz_r=Fr[0:10]
#PGRBinz_xr=PGRBinz_x*PGRBinz_r

# original redshift grid  by Stefan
#x1=np.asarray([0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7])
#x2=np.asarray([0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3.0])
#Pbns_ETCE=(np.asarray([0.115,0.125,0.118,0.08,0.055,0.04,0.03,0.02,0.01,0.01])/0.125)
#Pbns_ET=(np.asarray([0.115,0.12,0.07,0.025,0.021,0.005,0.01,0.0,0.0,0.0])/0.125)
# efficienza di detection in bin di ampiezza 0.1 (ogni valore della prob. è ripetuto 3 volte)
#Pbns_ETCE=(np.asarray([0.115,0.115,0.115,0.125,0.125,0.125,0.118,0.118,0.118,0.08,0.08,0.08,0.055,0.055,0.055,0.04,0.04,0.04,0.03,0.03,0.03,0.02,0.02,0.02,0.01,0.01,0.01,0.01,0.01,0.01])/0.125)
#Pbns_ET=(np.asarray([0.115,0.115,0.115,0.12,0.12,0.12,0.07,0.07,0.07,0.025,0.025,0.025,0.021,0.021,0.021,0.005,0.005,0.005,0.01,0.01,0.01,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])/0.125)

# efficienza di detection in bin di ampiezza 0.3 per gli on-axis (5deg)
#Pbns_ETCE_03=(np.asarray([0.115,0.125,0.118,0.08,0.055,0.04,0.03,0.02,0.01,0.01])/0.125)
#Pbns_ET_03=(np.asarray([0.115,0.12,0.07,0.025,0.021,0.005,0.01,0.0,0.0,0.0])/0.125)
Pbns_ET2CE_03=(np.asarray([1,1,1,1,0.9,0.6,0.3,0.1,0.0,0.0]))
Pbns_ETCE_03=(np.asarray([1,1,1,0.8,0.6,0.4,0.05,0.01,0.0,0.0]))
Pbns_ET_03=(np.asarray([1,1,0.7,0.4,0.4,0.05,0.01,0.0,0.0,0.0]))

# efficienza di detection in bin di ampiezza 0.02
#Pbns_ET2CE=np.repeat(Pbns_ET2CE_03,15)
#Pbns_ETCE=np.repeat(Pbns_ETCE_03,15)
#Pbns_ET=np.repeat(Pbns_ET_03,15)

# efficienza di detection in bin di ampiezza 0.1
Pbns_ET2CE=np.repeat(Pbns_ET2CE_03,3)
Pbns_ETCE=np.repeat(Pbns_ETCE_03,3)
Pbns_ET=np.repeat(Pbns_ET_03,3)


#x1=x1[0:6]
#x2=x2[0:6]

# percentuale vista anche con GW
#P_TH_ETCE=PGRBinz_x*Pbns_ETCE
#P_TH_ET=PGRBinz_x*Pbns_ET
P_TH_ET2CE=Fx[0:30]*Pbns_ET2CE
P_TH_ETCE=Fx[0:30]*Pbns_ETCE
P_TH_ET=Fx[0:30]*Pbns_ET
#P_TH_ETCE=Fx[0:150]*Pbns_ETCE
#P_TH_ET=Fx[0:150]*Pbns_ET
#P_TH_ETCE=Pbns_ETCE
#P_TH_ET=Pbns_ET

# plot histogram
#plt.bar((x1+x2)/2,Pbns_ETCE,align='center',width=(x2-x1),label='THESEUS+ET+CE') # A bar chart
#plt.hist(zr,bins=bins,density=True,color='red',linewidth=8,histtype='step',alpha=0.7,label='THESEUS short GRB with IRT detection')

#plt.bar(zbinx[0:10],100*PGRBinz_x,width=binstep,align='edge',log=False,linewidth=4,color="None",edgecolor='blue',alpha=0.9,label='THESEUS short GRB')
#plt.bar(zbin_r[0:10],100*PGRBinz_xr,width=binstep,align='edge',log=False,linewidth=4,color="None",edgecolor='red',alpha=0.9,label='THESEUS short GRB with IRT')
plt.bar(zbinx[0:-1],100*Fx,width=binstep,align='edge',log=False,linewidth=2,color="None",edgecolor='cornflowerblue',alpha=0.9,label='THESEUS short GRB')


#plt.bar((x1+x2)/2.,100*P_TH_ETCE,width=(x2-x1),log=False,align='center',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE short GRB')
#plt.bar((x1+x2)/2.,100*P_TH_ET,width=(x2-x1),log=False,align='center',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET short GRB')
#plt.bar(zbinx[0:10],100*P_TH_ETCE,width=(x2-x1),log=False,align='edge',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE short GRB')
#plt.bar(zbinx[0:10],100*P_TH_ET,width=(x2-x1),log=False,align='edge',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET short GRB')
plt.bar(zbinx[0:30],100*P_TH_ET2CE,width=binstep,log=False,align='edge',hatch='-',color='violet',alpha=0.5,label='THESEUS+ET+2CE short GRB')
plt.bar(zbinx[0:30],100*P_TH_ETCE,width=binstep,log=False,align='edge',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE short GRB')
plt.bar(zbinx[0:30],100*P_TH_ET,width=binstep,log=False,align='edge',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET short GRB')
#plt.bar(zbinx[0:150],100*P_TH_ETCE,width=binstep,log=False,align='edge',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE short GRB')
#plt.bar(zbinx[0:150],100*P_TH_ET,width=binstep,log=False,align='edge',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET short GRB')
plt.bar(zbin_r[0:-1],100*Fr*frac,width=binstep,align='edge',log=False,linewidth=2,color="None",edgecolor='indigo',alpha=0.9,label='THESEUS short GRB with IRT')

#plt.xlim(0.,13)
plt.xlim(0.,6)
plt.ylim(0,7.5)
plt.xlabel('redshift')
plt.ylabel(' short GRB [% in each redshift bin]')

#plt.legend(fontsize='small')
plt.legend()
plt.show()

#plt.savefig('SGRB_hist_ET_CE_onaxis_bin01.pdf')
#plt.savefig('SGRB_hist_ET_CE_onaxis_bin01.png',dpi=500)
plt.savefig('SGRB_hist_ET_2CE_onaxis_bin01.png',dpi=500)

onaxisGRBperyear=Fx*12

print('')
print('THESEUS+ET',100*sum(P_TH_ET),'%')
print('THESEUS+ET+CE',100*sum(P_TH_ETCE),'%')
print('THESEUS+ET+2CE',100*sum(P_TH_ET2CE),'%')
print('')

print('Total GRB THESEUS (on axis) in 1(3.45)yr:', 12,'(',12*3.45,')')
print('Total GRB THESEUS+ET (on axis) in 1(3.45)yr:', 12*sum(P_TH_ET),'(',12*3.45*sum(P_TH_ET),')')
print('Total GRB THESEUS+ET+CE (on axis) in 1(3.45)yr:', 12*sum(P_TH_ETCE),'(',12*3.45*sum(P_TH_ETCE),')')
print('Total GRB THESEUS+ET+2CE (on axis) in 1(3.45)yr:', 12*sum(P_TH_ET2CE),'(',12*3.45*sum(P_TH_ET2CE),')')

# only if bin <=0.1
print('')
#print('Total GRB THESEUS+2G (at z<0.1) in 3.45 yr: ',sum(40*Fx[0]))
#print('Total GRB THESEUS+2G (at z<0.08) in 3.45 yr: ',sum(40*Fx[0]))
#print('Total GRB THESEUS+2G (at z<0.06) in 3.45 yr: ',sum(40*Fx[0]))
