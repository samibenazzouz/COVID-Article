import matplotlib.pyplot as plt
def SIRModel(initialDATA,h,n):

    """ initialDATA=[S0,E0,I0,R0,rho,beta,alpha,gamma]   
        h=delta_t               
        n est le nombre de points  
    """   
    S=[]
    E=[]
    I=[]
    R=[]
    Time=[]
    S.append(initialDATA[0])
    E.append(initialDATA[1])
    I.append(initialDATA[2])
    R.append(initialDATA[3])
    Time.append(0)
    rho=initialDATA[4]
    beta=initialDATA[5]
    alpha=initialDATA[6]
    gamma=initialDATA[7]
    for i in range(1,n+1):
        newS=S[-1]-h*rho*beta*(I[-1])*(S[-1])
        newE=E[-1]+h*(rho*beta*S[-1]*I[-1]-alpha*E[-1])
        newI=I[-1]+h*(alpha*E[-1]-gamma*I[-1])
        newR=R[-1]+h*gamma*I[-1]
        S.append(newS)
        E.append(newE)
        I.append(newI)
        R.append(newR)
        Time.append(i*h)

    return [Time,S,E,I,R]


beta=1.75
alpha=0.2
gamma=0.5
N=10000
S0=1-1/N
E0=1/N
I0=0
R0=0
init1=[S0,E0,I0,R0,1,beta,alpha,gamma]
init2=[S0,E0,I0,R0,0.8,beta,alpha,gamma]
init3=[S0,E0,I0,R0,0.5,beta,alpha,gamma]
init4=[S0,E0,I0,R0,0.2,beta,alpha,gamma]



Tab1=SIRModel(init1,1,200)
Tab2=SIRModel(init2,1,200)
Tab3=SIRModel(init3,1,200)
Tab4=SIRModel(init4,1,200)




plt.style.use('ggplot')
plt.xlabel('Jours')
plt.ylabel('Fraction de la population')
plt.title('COVID19 SEIR Model')
plt.plot(Tab1[0],Tab1[2],label="Individus exposés ρ=1" )
plt.plot(Tab1[0],Tab1[3],label="Individus infectés ρ=1" )
plt.plot(Tab2[0],Tab2[2],label="Individus exposés ρ=0.8" )
plt.plot(Tab2[0],Tab2[3],label="Individus infectés ρ=0.8" )
plt.plot(Tab3[0],Tab3[2],label="Individus exposés ρ=0.5" )
plt.plot(Tab3[0],Tab3[3],label="Individus infectés ρ=0.5" )

plt.legend()


plt.legend()
plt.grid(color='w', linewidth=0.5)
#plt.show()
plt.savefig('plot.png', dpi = 300)