import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

binstep=0.1

# read output from read_zlim_vs_theta.py
#dbtheta=pd.read_csv('thetabin_zbin01.log')
dbtheta=pd.read_csv('thetabin_zbin01.log')
#dbtheta=pd.read_csv('thetabin_zbin002.log')


thetaview=dbtheta['theta']
zview=dbtheta['z']

# read output from MOS
dfx=pd.read_csv('shortGRBsDetectedBySXIXGIS.txt',header=None)
zx=dfx[0]

zmax=20

l=int((zmax-0)/binstep)

bins=[]
for i in range(0,l):
    bins.append(round(binstep*i,1))
    #bins.append(round(binstep*i,2))

hist_x_density=plt.hist(zx,bins=bins,density=True,color='blue',linewidth=5,histtype='step',alpha=0)

#hist_x_density=plt.hist(zx,bins=bins,density=True,alpha=0)
hist_x_number=plt.hist(zx,bins=bins,alpha=0)
# distribuzione delle simulazioni (400)
#Fx=hist_x_density[0]
Nx0=hist_x_number[0]
zbinx=hist_x_density[1]

# deg up to which a grb at zbin can be detected offaxis
thetajet=4
theta=np.asarray(Nx0)*0+thetajet

#theta[0]=12
#theta[1]=8.1
#theta[2]=6.5

#theta[0]=16
#theta[1]=10.0
#theta[2]=6.5
#theta[3]=5
#theta[4]=5
#theta[5]=5
#theta[6]=5

#theta[0]=12.4
#theta[1]=8.2
#theta[2]=6.4
#theta[3]=5.3
#theta[4]=4.6

#for i in range(0,32):
for i in range(0,16):
#for i in range(0,90):
    theta[i]=thetaview[i]


thetaoffaxisvsz=theta*np.pi/180
thetonaxis=thetajet*np.pi/180
increasefact=(1-np.cos(thetaoffaxisvsz))/(1-np.cos(thetonaxis))

Fx0=Nx0/sum(Nx0)
Nx=Nx0*increasefact
Fx=Nx/sum(Nx)

# percentuale di casi per ciascun zbin fino a z=3
#PGRBinz_x=Fx[0:10]
#PGRBinz_x_bin0=Fx[0:30]

# original redshift grid  by Stefan
#x1=np.asarray([0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7])
#x2=np.asarray([0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3.0])


# efficienza di detection in bin larghi 0.3
#Pbns_ETCE=(np.asarray([0.115,0.125,0.118,0.08,0.055,0.04,0.03,0.02,0.01,0.01])/0.125)
#Pbns_ET=(np.asarray([0.115,0.12,0.07,0.025,0.021,0.005,0.01,0.0,0.0,0.0])/0.125)

# efficienza di detection in bin di ampiezza 0.1 (ogni valore della prob. è ripetuto 3 volte)
#Pbns_ETCE=(np.asarray([0.115,0.115,0.115,0.125,0.125,0.125,0.118,0.118,0.118,0.08,0.08,0.08,0.055,0.055,0.055,0.04,0.04,0.04,0.03,0.03,0.03,0.02,0.02,0.02,0.01,0.01,0.01,0.01,0.01,0.01])/0.125)
#Pbns_ET=(np.asarray([0.115,0.115,0.115,0.12,0.12,0.12,0.07,0.07,0.07,0.025,0.025,0.025,0.021,0.021,0.021,0.005,0.005,0.005,0.01,0.01,0.01,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])/0.125)

# efficienza di detection in bin di ampiezza 0.3 per gli on- e off-axis (10deg)
#Pbns_ETCE_03=(np.asarray([0.115,0.125,0.118,0.08,0.055,0.04,0.03,0.02,0.01,0.01])/0.125)
#Pbns_ET_03=(np.asarray([0.115,0.12,0.07,0.025,0.021,0.005,0.01,0.0,0.0,0.0])/0.125)
Pbns_ET2CE_03=(np.asarray([1,1,1,1,0.9,0.6,0.3,0.1,0.0,0.0]))
Pbns_ETCE_03=(np.asarray([1,1,1,0.8,0.6,0.4,0.05,0.01,0.0,0.0]))
Pbns_ET_03=(np.asarray([1,1,0.7,0.4,0.4,0.05,0.01,0.0,0.0,0.0]))

# efficienza di detection in bin di ampiezza 0.02
#Pbns_ETCE=np.repeat(Pbns_ETCE_03,15)
#Pbns_ET=np.repeat(Pbns_ET_03,15)
# efficienza di detection in bin di ampiezza 0.1
Pbns_ET2CE=np.repeat(Pbns_ET2CE_03,3)
Pbns_ETCE=np.repeat(Pbns_ETCE_03,3)
Pbns_ET=np.repeat(Pbns_ET_03,3)

# efficienza di detection in bin di ampiezza 0.05 (ogni valore della prob. è ripetuto 3 volte)
#Pbns_ETCE=(np.asarray([0.115,0.115,0.115,0.115,0.115,0.115,0.125,0.125,0.125,0.125,0.125,0.125,0.118,0.118,0.118,0.118,0.118,0.118,0.08,0.08,0.08,0.08,0.08,0.08,0.055,0.055,0.055,0.055,0.055,0.055,0.04,0.04,0.04,0.04,0.04,0.04,0.03,0.03,0.03,0.03,0.03,0.03,0.02,0.02,0.02,0.02,0.02,0.02,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])/0.125)
#Pbns_ET=(np.asarray([0.115,0.115,0.115,0.115,0.115,0.115,0.12,0.12,0.12,0.12,0.12,0.12,0.07,0.07,0.07,0.07,0.07,0.07,0.025,0.025,0.025,0.025,0.025,0.025,0.021,0.021,0.021,0.021,0.021,0.021,0.005,0.005,0.005,0.005,0.005,0.005,0.01,0.01,0.01,0.01,0.01,0.01,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])/0.125)



# percentuale vista anche con GW
#P_TH_ETCE=PGRBinz_x*Pbns_ETCE
#P_TH_ET=PGRBinz_x*Pbns_ET
P_TH_ET2CE=Fx[0:30]*Pbns_ET2CE
P_TH_ETCE=Fx[0:30]*Pbns_ETCE
P_TH_ET=Fx[0:30]*Pbns_ET
#P_TH_ETCE=Fx[0:150]*Pbns_ETCE
#P_TH_ET=Fx[0:150]*Pbns_ET


plt.bar(zbinx[0:-1],100*Fx,width=binstep,align='edge',log=False,linewidth=2,color="None",edgecolor='cornflowerblue',alpha=0.9,label='THESEUS on+off axis short GRB')

plt.bar(zbinx[0:30],100*P_TH_ET2CE,width=binstep,log=False,align='edge',hatch='-',color='violet',alpha=0.5,label='THESEUS+ET+CE on+off axis short GRB')
plt.bar(zbinx[0:30],100*P_TH_ETCE,width=binstep,log=False,align='edge',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE on+off axis short GRB')
plt.bar(zbinx[0:30],100*P_TH_ET,width=binstep,log=False,align='edge',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET on+offaxis short GRB')
#plt.bar(zbinx[0:150],100*P_TH_ETCE,width=binstep,log=False,align='edge',hatch='\\',color='magenta',alpha=0.5,label='THESEUS+ET+CE on+off axis short GRB')
#plt.bar(zbinx[0:150],100*P_TH_ET,width=binstep,log=False,align='edge',hatch='/',color='lime',alpha=0.5,label='THESEUS+ET on+offaxis short GRB')
#plt.bar((x1+x2)/2.,P_TH_offaxis_ET,width=(x2-x1),align='center',linewidth=5,alpha=0.2,edgecolor='green',label='THESEUS+ET short GRB including off-axis ')
#plt.bar((x1+x2)/2.,P_TH_offaxis_ETCE,width=(x2-x1),align='center',linewidth=5,alpha=0.3,edgecolor='magenta',label='THESEUS+ET+CE short GRB including off-axis ')
#plt.xlim(0.,13)
plt.xlim(0.,6)
plt.ylim(0,7.5)
plt.xlabel('redshift')
plt.ylabel(' short GRB [% in each z bin]')

#plt.legend(fontsize='small')
plt.legend()
plt.show()

#plt.savefig('SGRB_hist_ET_CE_offaxis_bin01.pdf')
#plt.savefig('SGRB_hist_ET_CE_offaxis_bin01.png',dpi=500)
plt.savefig('SGRB_hist_ET_2CE_offaxis_bin01.png',dpi=500)


k=sum(Nx)/sum(Nx0)

print('Total number of on- and off-axis GBR is ',k,' times larger than on-axis only GRBs')
print('(i.e. 12/yr on-axis and ',12*k,'/yr on- and off-axis)')

print('')
print('THESEUS+ET',100*sum(P_TH_ET),'%')
print('THESEUS+ET+CE',100*sum(P_TH_ETCE),'%')
print('THESEUS+ET+CE',100*sum(P_TH_ET2CE),'%')

print('')
print('Total GRB THESEUS (on+off axis) in 1(3.45)yr:', 12*k,'(',12*k*3.45,')')
print('Total GRB THESEUS+ET (on+off axis) in 1(3.45)yr:', 12*k*sum(P_TH_ET),'(',12*k*3.45*sum(P_TH_ET),')')
print('Total GRB THESEUS+ET+CE (on+off axis) in 1(3.45)yr:', 12*k*sum(P_TH_ETCE),'(',12*k*3.45*sum(P_TH_ETCE),')')
print('Total GRB THESEUS+ET+2CE (on+off axis) in 1(3.45)yr:', 12*k*sum(P_TH_ET2CE),'(',12*k*3.45*sum(P_TH_ET2CE),')')

#up to z=3.0
#k03=sum(Nx[0:10])/sum(Nx0[0:10])
# GRB with ET too


# only if bin <=0.1
print('')
#print('Total GRB THESEUS+2G (at z<0.1) in 3.45 yr: ',40*k*Fx[0])
#print('Total GRB THESEUS+2G (at z<0.08) in 3.45 yr: ',sum(40*k*Fx[0:4]))
#print('Total GRB THESEUS+2G (at z<0.06) in 3.45 yr: ',sum(40*k*Fx[0:3]))
