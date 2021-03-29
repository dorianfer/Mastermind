from tkinter import *
from random import randrange

solution=[]
reponse=[]
choix=[]
solutionEn=[]
nb=0
def aide():
    fene=Tk()
    fene.geometry("550x125")
    fene.title("mode d'emploi")
    label=Label(fene,text="Le but du jeu est de découvrir le code secret. Pour y parvenir tu peux rentrer 12 codes de couleurs.")
    label.grid()
    label1=Label(fene,text="Chaque couleur bien placées l'ordinateur donnera à droite de votre réponse un cercle jaune")
    label1.grid()
    label2=Label(fene,text="pour chaque couleur mal placées l'ordinateur donnera un cercle rouge")
    label2.grid()
    label3=Label(fene,text="et si tu rentres une couleur qui ne fait pas parti du code secret il n'y aura rien aucun cercle.")
    label3.grid()
    label4=Label(fene,text="Si vous voulez avoir la solution, veuillez écrire : solution.")
    label4.grid()
    label5=Label(fene,text="Bonne chance !")
    label5.grid()
    
    
def alea():
    global solution,color,solutionEn
    color=["blanc","jaune","orange","rouge","rose","vert","bleu","gris","solution"]#création d'une bibliothèque de couleur
    for i in range(4):
        solution.append(color[randrange(0,8)])
    english=["white","yellow","orange","red","pink","green","blue","grey"]
    for rang in range (len(solution)):
        for indice in range (len(color)-1):# on fait len(color)-1 pour pas prendre le mot solution
            if solution[rang]==color[indice] :
                solutionEn.append(english[indice])



def gagne():
    gagner=Label(fen,text="Bravo vous avez gagné!!! :D")
    gagner.grid(row=4,column=5)
        
def perdu():
    perd=Label(fen,text="Vous avez perdu. T^T")
    perd.grid(row=4,column=5)
def abandon():
    aban=Label(fen,text="Vous avez abandonné. T^T")
    aban.grid(row=4,column=5)
def analyse():
    global reponse,x1,y1,x2,y2
    other=[]
    reponse=[]
    autre=[]
    for rang in range (len(choix)) :
        if choix[rang]==solution[rang]:
            reponse.append("B")

            
        if choix[rang]!=solution[rang]:
            other.append(solution[rang])
            autre.append(choix[rang])
            
            
    for rang in range (len(other)):
        for indice in range(len(autre)):
            if autre[indice]==other[rang]:
                reponse.append("M")
                other[rang]=("")
                autre[indice]=(" ")


    vx1=x1
    vy1=y1
    vx2=x2
    vy2=y2
    for rang in range (len(reponse)):
        if choix!=solution:
            x1=vx2+rang*20+10*(rang+1)
            y1=vy1+10
            x2=x1+20
            y2=y1+20
            if reponse[rang]=="B":
                saisie="yellow"
            else:
                saisie="red"
            can.create_oval(x1,y1,x2,y2,fill=saisie)

               
    

def translate():
    global saisie,color
    english=["white","yellow","orange","red","pink","green","blue","grey"]
    for rang in range (len(color)-1):
        if saisie==color[rang] :
            saisie=english[rang]
            choix.append(color[rang])

def resultat():
    global solutionEn,nb
    nb=48
    for rang in range(len(solutionEn)):
        hori=nb%4
        verti=nb//4
        x1=700//5*hori
        y1=600//13*verti
        x2=700//5*(hori+1)
        y2=600//13*(verti+1)
        can.create_oval(x1,y1,x2,y2,fill=solutionEn[rang])
        nb=nb+1
    can.create_text(x2+70,y2-23,text="Voici la solution")

def cercle(event):
    global nb,x1,y1,x2,y2,choix,essais,solution,saisie
    saisie=entrée.get()
    if saisie==color[8]:
        abandon()
        resultat()
    
    translate()

        
    if nb<48:
        hori=nb%4
        verti=nb//4
        x1=700//5*hori
        y1=600//13*verti
        x2=700//5*(hori+1)
        y2=600//13*(verti+1)
        can.create_oval(x1,y1,x2,y2,fill=saisie)
        nb=nb+1
        if len(choix)==4:
            analyse()
            if choix==solution:
                gagne()
                resultat()
            choix=[]
            

    if nb==48:
        perdu()
        resultat()
        





fen=Tk()
fen.geometry("700x700")
fen.title("Mastermind")

can=Canvas(fen,width=700,height=600,bg="white")
can.grid(row=1,column=5,columnspan=9)
label=Label(fen,text="Choisisez: blanc, jaune, orange, rouge, rose, vert, bleu, gris ou solution.")
label.grid(row=3,column=5)

Bquit=Button(fen,text="quitter",command=fen.destroy)
Bquit.grid(row=4,column=13)
Baide=Button(fen,text="mode d'emploi",command=aide)
Baide.grid(row=3,column=13)
entrée=Entry(fen)
entrée.bind("<Return>",cercle)
entrée.grid(row=4,column=9)



alea()
can.create_line(700//5*4,0,700//5*4,600//13*12)
can.create_line(0,600//13*12,700,600//13*12)
fen.mainloop()