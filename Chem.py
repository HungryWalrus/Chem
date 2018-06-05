from tkinter import *
from tkinter import ttk
import random
H = ['Hydrogen', '1', 1.008, 2.1]
He = ['Helium', '2', 4.003, 0.0]
Li = ['Lithium', '3', 6.941, 1.0]
Be = ['Be', '4', 9.012, 1.5]
B = ['Boron', '5', 10.811, 2.0]
C = ['Carbon', '6', 12.011, 2.5]
N = ['Nitrogen', '7', 14.007, 3.0]
O = ['Oxygen', '8', 15.999, 3.5]
F = ['Fluorine', '9', 18.998, 4.0]
Ne = ['Neon', '10', 20.180, 0.0]
Na = ['Sodium', '11', 22.990, 0.9]
Mg = ['Magnesium', '12', 24.305, 1.2]
Al = ['Aluminum', '13', 26.982, 1.5]
Si = ['Silicon', '14', 28.086, 1.8]
P = ['Phosphorous', '15', 30.974, 2.1]
S = ['Sulfur', '16', 32.066, 2.5]
Cl = ['Chlorine', '17', 35.453, 3.0, '3.16', '[Ne] 3s2 3p5', '1s2 1p6 2s2 2p6 3s2 3p5']
Ar = ['Argon', '18', 39.948, 0.0]
K = ['Potassium', '19', 39.098, 0.8]
Ca = ['Calcium', '20', 40.078, 1.0]
Sc = ['Scandium', '21', 44.956, 1.3]
Ti = ['Titanium', '22', 47.88, 1.6]
V = ['Vanadium', '23', 50.942, 1.6]
Cr = ['Chromium', '24', 51.996, 1.6]
Mn = ['Manganese', '25', 54.938, 1.5]
Fe = ['Iron', '26', 55.845, 1.8]
Co = ['Cobalt', '27', 58.933, 1.8]
Ni = ['Nickel', '28', 58.693, 1.8]
Cu = ['Copper', '29', 63.536, 1.9]
Zn = ['Zinc', '30', 65.38, 1.6]
Ga = ['Gallium', '31', 69.723, 1.6]
Ge = ['Germanium', '32', 72.631, 1.8]
As = ['Arsenic', '33', 74.922, 2.0]
Se = ['Selenium', '34', 78.971, 2.4]
Br = ['Bromine', '35', 79.904, 2.8]
Kr = ['Krypton', '36', 84.798, 0.0]
Rb = ['Rubidium', '37', 85.468, 0.8]
Sr = ['Stronium', '38', 87.62, 1.0]
Y = ['Yitrium', '39', 88.906, 1.2]
Zr = ['Zirconium', '40', 91.224, 1.4]
Nb = ['Neobium' '41', 92.906, 1.6]
Mo = ['Molybdenum', '42', 95.95, 1.8]
Tc = ['Technetium', '43', 98.907, 1.9]
Ru = ['Ruthenium', '44', 101.07, 2.2]
Rh = ['Rhodium', '45', 102.906, 2.2]
Pd = ['Palladium', '46', 106.42, 2.2]
Ag = ['Silver', '47', 107.868, 1.9]
Cd = ['Cadmium', '48', 112.414, 1.7]
In = ['Indium', '49', 114.818, 1.7]
Sn = ['Tin', '50', 118.711, 1.8]
Sb = ['Antimony', '51', 121.760, 1.9]
Te = ['Tellurium', '52', 127.6, 2.1]
I = ['Iodine', '53', 126.904, 2.5]
Xe = ['Xenon', '54', 131.298, 0.0]
Cs = ['Cesium', '55', 132.905, 0.8]
Ba = ['Barium', '56', 137.328, 0.9]
La = ['Lanthanum', '57', 138.905, 1.1]
Ce = ['Cerium', '58', 140.116, 1.1]
Pr = ['Praseodymium', '59', 140.908, 1.1]
Nd = ['Neodymium', '60', 144.243, 1.1]
Pm = ['Promethium', '61', 144.913, 1.1]
Sm = ['Samarium', '62', 150.36, 1.2]
Eu = ['Europium', '63', 151.964, 1.2]
Gd = ['Gadolinium', '64', 157.25, 1.2]
Tb = ['Terbium', '65', 158.925, 1.1]
Dy = ['Dysprosium', '66', 162.500, 1.2]
Ho = ['Holmium', '67', 164.930, 1.2]
Er = ['Erbium', '68', 167.259, 1.2]
Tm = ['Thulium', '69', 168.934, 1.3]
Yb = ['Ytterbium', '70', 173.055, 1.1]
Lu = ['Lutetium', '71', 174.967, 1.3]
Hf = ['Hafnium', '72', 178.49, 1.3]
Ta = ['Tantalum', '73', 180.948, 1.5]
W = ['Tungsten', '74', 183.85, 2.4]
Re = ['Rhenium', '75', 186.207, 1.9]
Os = ['Osmium', '76', 190.23, 2.2]
Ir = ['Iridium', '77', 192.22, 2.2]
Pt = ['Platinum', '78', 195.08, 2.2]
Au = ['Gold', '79', 196.967, 2.4]
Hg = ['Mercury', '80', 200.59, 1.9]
Tl = ['Thallium', '81', 204.383, 1.8]
Pb = ['Lead', '82', 207.2, 1.8]
Bi = ['Bismuth', '83', 208.980], 1.9
Po = ['Polonium', '84', 208.982, 2.0]
At = ['Astatine', '85', 209.987, 2.2]
Rn = ['Radon', '86', 222.018, 0.0]
Fr = ['Francium', '87', 223.020, 0.7]
Ra = ['Radium', '88', 226.025, 0.9]
Ac = ['Actinium', '89', 227.028, 1.1]
Th = ['Thorium', '90', 232.038, 1.3]
Pa = ['Protactinium', '91', 231.036, 1.5]
U = ['Uranium', '92', 238.039, 1.4]
Np = ['Neptunium', '93', 237.048, 1.4]
Pu = ['Plutonium', '94', 244.064, 1.3]
Am = ['Americium', '95', 243.061, 1.1]
Cm = ['Curium', '96', 247.070, 1.3]
Bk = ['Berkelium', '97', 247.070, 1.3]
Cf = ['Californium', '98', 251.080, 1.3]
Es = ['Einsteinium', '99', 254, 1.3]
Fm = ['Fermium', '100', 257.095, 1.3]
Md = ['Mendelevium', '101', 258.1, 1.3]
No = ['Nobelium', '102', 259.101, 1.3]
Lr = ['Lawrencium', '103', 262, 1.3]
Rf = ['Rutherfordium', '104', 261, 0.0]
Db = ['Dubnium', '105', 262, 0.0]
Sg = ['Seaborgium', '106', 266, 0.0]
Bh = ['Bohrium', '107', 264, 0.0]
Hs = ['Hassium', '108', 269, 0.0]
Mt = ['Meitnerium', '109', 268, 0.0]
Ds = ['Darmstadtium', '110', 278, 0.0]
Rg = ['Roentgenium', '111', 280, 0.0]
Cn = ['Copernicium', '112', 285, 0.0]
Nh = ['Nihonium', '113', 286, 0.0]
Fl = ['Flerovium', '114', 289, 0.0]
Mc = ['Moscovium', '115', 289, 0.0]
Lv = ['Livermorium', '116', 293, 0.0]
Ts = ["Tennessine", '117', 294, 0.0]
Og = ["Oganesson", '118', 294, 0.0]
Elements = ('H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
            'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
            'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Ti', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr',
            'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf'
            'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og')
lowerlphabet = 'abcdefghijklmnopqrstuvwxyz'
one2ninepluszero = '1234567890'
upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#The Goal of this program is to make it so the user can type in a compound and the program will return the mass of the compound
def doStuff():
    if Entry1.get().startswith(Elements):
        individualvalues = ['0']
        length = 1
        valuess = Entry1.get()
        for i in valuess:
            valuesss = individualvalues[len(individualvalues) - 1]
            if str(individualvalues[len(individualvalues) - 1]).isupper() and str(i).isupper() and str(individualvalues[len(individualvalues) - 1]) in upperalphabet:
                individualvalues.append('1')
                individualvalues.append(i)
            elif len(valuesss) == 2 and valuesss[1].islower() and str(i).isupper():
                individualvalues.append('1')
                individualvalues.append(i)
            else:
                individualvalues.append(i)
            if str(individualvalues[len(individualvalues) - 2]).isupper() and i.islower() and i in lowerlphabet and str(individualvalues[len(individualvalues) - 2]) in upperalphabet:
                individualvalues.append(str(individualvalues[len(individualvalues) - 2]) + str(individualvalues[len(individualvalues) - 1]))
                del individualvalues[len(individualvalues) - 2]
                del individualvalues[len(individualvalues) - 2]
            if individualvalues[len(individualvalues) - 2] in one2ninepluszero and i in one2ninepluszero:
                individualvalues.append(str(individualvalues[len(individualvalues) - 2]) + str(individualvalues[len(individualvalues) - 1]))
                del individualvalues[len(individualvalues) - 2]
                del individualvalues[len(individualvalues) - 2]
        if individualvalues[len(individualvalues) - 1] in Elements:
            individualvalues.append('1')
        del individualvalues[0]
        Entry1.delete(0, END)
        Entry1.insert(0, individualvalues)
        currentNunmberLength = 0
        numbers = []
        newLength = len(individualvalues)
        otherNumberLength = 0
        numbers = []
        while True:
            if individualvalues[currentNunmberLength] in Elements:
                if individualvalues[currentNunmberLength] == Elements[0]:
                    numbers.append(H[2])
                elif individualvalues[currentNunmberLength] == Elements[1]:
                    numbers.append(He[2])
                elif individualvalues[currentNunmberLength] == Elements[2]:
                    numbers.append(Li[2])
                elif individualvalues[currentNunmberLength] == Elements[3]:
                    numbers.append(Be[2])
                elif individualvalues[currentNunmberLength] == Elements[4]:
                    numbers.append(B[2])
                elif individualvalues[currentNunmberLength] == Elements[5]:
                    numbers.append(C[2])
                elif individualvalues[currentNunmberLength] == Elements[6]:
                    numbers.append(N[2])
                elif individualvalues[currentNunmberLength] == Elements[7]:
                    numbers.append(O[2])
                elif individualvalues[currentNunmberLength] == Elements[8]:
                    numbers.append(F[2])
                elif individualvalues[currentNunmberLength] == Elements[9]:
                    numbers.append(Ne[2])
                elif individualvalues[currentNunmberLength] == Elements[10]:
                    numbers.append(Na[2])
                elif individualvalues[currentNunmberLength] == Elements[11]:
                    numbers.append(Mg[2])
                elif individualvalues[currentNunmberLength] == Elements[12]:
                    numbers.append(Al[2])
                elif individualvalues[currentNunmberLength] == Elements[13]:
                    numbers.append(Si[2])
                elif individualvalues[currentNunmberLength] == Elements[14]:
                    numbers.append(P[2])
                elif individualvalues[currentNunmberLength] == Elements[15]:
                    numbers.append(S[2])
                elif individualvalues[currentNunmberLength] == Elements[16]:
                    numbers.append(Cl[2])
                elif individualvalues[currentNunmberLength] == Elements[17]:
                    numbers.append(Ar[2])
                elif individualvalues[currentNunmberLength] == Elements[18]:
                    numbers.append(K[2])
                elif individualvalues[currentNunmberLength] == Elements[19]:
                    numbers.append(Ca[2])
                elif individualvalues[currentNunmberLength] == Elements[20]:
                    numbers.append(Sc[2])
                elif individualvalues[currentNunmberLength] == Elements[21]:
                    numbers.append(Ti[2])
                elif individualvalues[currentNunmberLength] == Elements[22]:
                    numbers.append(V[2])
                elif individualvalues[currentNunmberLength] == Elements[23]:
                    numbers.append(Cr[2])
                elif individualvalues[currentNunmberLength] == Elements[24]:
                    numbers.append(Mn[2])
                elif individualvalues[currentNunmberLength] == Elements[25]:
                    numbers.append(Fe[2])
                elif individualvalues[currentNunmberLength] == Elements[26]:
                    numbers.append(Co[2])
                elif individualvalues[currentNunmberLength] == Elements[27]:
                    numbers.append(Ni[2])
                elif individualvalues[currentNunmberLength] == Elements[28]:
                    numbers.append(Cu[2])
                elif individualvalues[currentNunmberLength] == Elements[29]:
                    numbers.append(Zn[2])
                elif individualvalues[currentNunmberLength] == Elements[30]:
                    numbers.append(Ga[2])
                elif individualvalues[currentNunmberLength] == Elements[31]:
                    numbers.append(Ge[2])
                elif individualvalues[currentNunmberLength] == Elements[32]:
                    numbers.append(As[2])
                elif individualvalues[currentNunmberLength] == Elements[33]:
                    numbers.append(Se[2])
                elif individualvalues[currentNunmberLength] == Elements[34]:
                    numbers.append(Br[2])
                elif individualvalues[currentNunmberLength] == Elements[35]:
                    numbers.append(Kr[2])
                elif individualvalues[currentNunmberLength] == Elements[36]:
                    numbers.append(Rb[2])
                elif individualvalues[currentNunmberLength] == Elements[37]:
                    numbers.append(Sr[2])
                elif individualvalues[currentNunmberLength] == Elements[38]:
                    numbers.append(Y[2])
                elif individualvalues[currentNunmberLength] == Elements[39]:
                    numbers.append(Zr[2])
                elif individualvalues[currentNunmberLength] == Elements[40]:
                    numbers.append(Nb[2])
                elif individualvalues[currentNunmberLength] == Elements[41]:
                    numbers.append(Mo[2])
                elif individualvalues[currentNunmberLength] == Elements[42]:
                    numbers.append(Tc[2])
                elif individualvalues[currentNunmberLength] == Elements[43]:
                    numbers.append(Ru[2])
                elif individualvalues[currentNunmberLength] == Elements[44]:
                    numbers.append(Rh[2])
                elif individualvalues[currentNunmberLength] == Elements[45]:
                    numbers.append(Pd[2])
                elif individualvalues[currentNunmberLength] == Elements[46]:
                    numbers.append(Ag[2])
                elif individualvalues[currentNunmberLength] == Elements[47]:
                    numbers.append(Cd[2])
                elif individualvalues[currentNunmberLength] == Elements[48]:
                    numbers.append(In[2])
                elif individualvalues[currentNunmberLength] == Elements[49]:
                    numbers.append(Sn[2])
                elif individualvalues[currentNunmberLength] == Elements[50]:
                    numbers.append(Sb[2])
                elif individualvalues[currentNunmberLength] == Elements[51]:
                    numbers.append(Te[2])
                elif individualvalues[currentNunmberLength] == Elements[52]:
                    numbers.append(I[2])
                elif individualvalues[currentNunmberLength] == Elements[53]:
                    numbers.append(Xe[2])
                elif individualvalues[currentNunmberLength] == Elements[54]:
                    numbers.append(Cs[2])
                elif individualvalues[currentNunmberLength] == Elements[55]:
                    numbers.append(Ba[2])
                elif individualvalues[currentNunmberLength] == Elements[56]:
                    numbers.append(La[2])
                elif individualvalues[currentNunmberLength] == Elements[57]:
                    numbers.append(Ce[2])
                elif individualvalues[currentNunmberLength] == Elements[58]:
                    numbers.append(Pr[2])
                elif individualvalues[currentNunmberLength] == Elements[59]:
                    numbers.append(Nd[2])
                elif individualvalues[currentNunmberLength] == Elements[60]:
                    numbers.append(Pm[2])
                elif individualvalues[currentNunmberLength] == Elements[61]:
                    numbers.append(Sm[2])
                elif individualvalues[currentNunmberLength] == Elements[62]:
                    numbers.append(Eu[2])
                elif individualvalues[currentNunmberLength] == Elements[63]:
                    numbers.append(Gd[2])
                elif individualvalues[currentNunmberLength] == Elements[64]:
                    numbers.append(Tb[2])
                elif individualvalues[currentNunmberLength] == Elements[65]:
                    numbers.append(Dy[2])
                elif individualvalues[currentNunmberLength] == Elements[66]:
                    numbers.append(Ho[2])
                elif individualvalues[currentNunmberLength] == Elements[67]:
                    numbers.append(Er[2])
                elif individualvalues[currentNunmberLength] == Elements[68]:
                    numbers.append(Tm[2])
                elif individualvalues[currentNunmberLength] == Elements[69]:
                    numbers.append(Yb[2])
                elif individualvalues[currentNunmberLength] == Elements[70]:
                    numbers.append(Lu[2])
                elif individualvalues[currentNunmberLength] == Elements[71]:
                    numbers.append(Hf[2])
                elif individualvalues[currentNunmberLength] == Elements[72]:
                    numbers.append(Ta[2])
                elif individualvalues[currentNunmberLength] == Elements[73]:
                    numbers.append(W[2])
                elif individualvalues[currentNunmberLength] == Elements[74]:
                    numbers.append(Re[2])
                elif individualvalues[currentNunmberLength] == Elements[75]:
                    numbers.append(Os[2])
                elif individualvalues[currentNunmberLength] == Elements[76]:
                    numbers.append(Ir[2])
                elif individualvalues[currentNunmberLength] == Elements[77]:
                    numbers.append(Pt[2])
                elif individualvalues[currentNunmberLength] == Elements[78]:
                    numbers.append(Au[2])
                elif individualvalues[currentNunmberLength] == Elements[79]:
                    numbers.append(Hg[2])
                elif individualvalues[currentNunmberLength] == Elements[80]:
                    numbers.append(Ti[2])
                elif individualvalues[currentNunmberLength] == Elements[81]:
                    numbers.append(Pb[2])
                elif individualvalues[currentNunmberLength] == Elements[82]:
                    numbers.append(Bi[2])
                elif individualvalues[currentNunmberLength] == Elements[83]:
                    numbers.append(Po[2])
                elif individualvalues[currentNunmberLength] == Elements[84]:
                    numbers.append(At[2])
                elif individualvalues[currentNunmberLength] == Elements[85]:
                    numbers.append(Rn[2])
                elif individualvalues[currentNunmberLength] == Elements[86]:
                    numbers.append(Fr[2])
                elif individualvalues[currentNunmberLength] == Elements[87]:
                    numbers.append(Ra[2])
                elif individualvalues[currentNunmberLength] == Elements[88]:
                    numbers.append(Ac[2])
                elif individualvalues[currentNunmberLength] == Elements[89]:
                    numbers.append(Th[2])
                elif individualvalues[currentNunmberLength] == Elements[90]:
                    numbers.append(Pa[2])
                elif individualvalues[currentNunmberLength] == Elements[91]:
                    numbers.append(U[2])
                elif individualvalues[currentNunmberLength] == Elements[92]:
                    numbers.append(Np[2])
                elif individualvalues[currentNunmberLength] == Elements[93]:
                    numbers.append(Pu[2])
                elif individualvalues[currentNunmberLength] == Elements[94]:
                    numbers.append(Am[2])
                elif individualvalues[currentNunmberLength] == Elements[95]:
                    numbers.append(Cm[2])
                elif individualvalues[currentNunmberLength] == Elements[96]:
                    numbers.append(Bk[2])
                elif individualvalues[currentNunmberLength] == Elements[97]:
                    numbers.append(Cf[2])
                elif individualvalues[currentNunmberLength] == Elements[98]:
                    numbers.append(Es[2])
                elif individualvalues[currentNunmberLength] == Elements[99]:
                    numbers.append(Fm[2])
                elif individualvalues[currentNunmberLength] == Elements[100]:
                    numbers.append(Md[2])
                elif individualvalues[currentNunmberLength] == Elements[101]:
                    numbers.append(No[2])
                elif individualvalues[currentNunmberLength] == Elements[102]:
                    numbers.append(Lr[2])
                elif individualvalues[currentNunmberLength] == Elements[103]:
                    numbers.append(Rf[2])
                elif individualvalues[currentNunmberLength] == Elements[104]:
                    numbers.append(Db[2])
                elif individualvalues[currentNunmberLength] == Elements[105]:
                    numbers.append(Sg[2])
                elif individualvalues[currentNunmberLength] == Elements[106]:
                    numbers.append(Bh[2])
                elif individualvalues[currentNunmberLength] == Elements[107]:
                    numbers.append(Hs[2])
                elif individualvalues[currentNunmberLength] == Elements[108]:
                    numbers.append(Mt[2])
                elif individualvalues[currentNunmberLength] == Elements[109]:
                    numbers.append(Ds[2])
                elif individualvalues[currentNunmberLength] == Elements[110]:
                    numbers.append(Rg[2])
                elif individualvalues[currentNunmberLength] == Elements[111]:
                    numbers.append(Cn[2])
                elif individualvalues[currentNunmberLength] == Elements[112]:
                    numbers.append(Nh[2])
                elif individualvalues[currentNunmberLength] == Elements[113]:
                    numbers.append(Fl[2])
                elif individualvalues[currentNunmberLength] == Elements[114]:
                    numbers.append(Mc[2])
                elif individualvalues[currentNunmberLength] == Elements[115]:
                    numbers.append(Lv[2])
                elif individualvalues[currentNunmberLength] == Elements[116]:
                    numbers.append(Ts[2])
                elif individualvalues[currentNunmberLength] == Elements[117]:
                    numbers.append(Og[2])
                currentNunmberLength = currentNunmberLength + 1
                if currentNunmberLength == newLength:
                    break
                otherNumberLength = len(numbers) - 1

            elif int(individualvalues[currentNunmberLength]) in range(1, 99):
                numbers[otherNumberLength] = float(numbers[otherNumberLength]) * float(
                    individualvalues[currentNunmberLength])
                currentNunmberLength = currentNunmberLength + 1
                if currentNunmberLength == newLength:
                    break

        while True:
            if len(numbers) != 1:
                numbers[0] = numbers[0] + numbers[1]
                del numbers[1]
            if len(numbers) == 1:
                break
        Entry1.delete(0, END)
        Entry1.insert(0, numbers)
root = Tk()

root.configure(background="#77CC5C")

root.title("")

lbl = Label(root, text="Enter a compound", bg="#77CC5C").grid(row=0, column=0)

Entry1 = Entry(root,)
Entry1.grid(row=1, column=0)

evaluate = Button(root, text="get mass", command = doStuff,)
evaluate.grid(row=2, column=0)

lbl2  = Label(root, text="Note this program does \n not work with nonsimple \n compounds such as Na(No3)3",).grid(row=3, column=0)
evaluate.bind("<Button-1>",)

root.mainloop()