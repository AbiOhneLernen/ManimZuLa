from manim import *
#20x5=100 Personen-Icons als Sample
P1x1=SVGMobject("PersonIcon.svg",fill_color=WHITE,height=0.9,stroke_color=BLACK,z_index=3)
Personen = VGroup(P1x1, *[P1x1.copy() for x in range(99)])
Personen.arrange_in_grid(rows=5,cols=20,buff=[0.35,0.25,0])




#Grupierung der Gymnasiasten
Gym = VGroup()
for x in range(100):
    if(x%20<10):
        Gym.add(Personen[x])
KlammerGym=Brace(Gym).next_to(Gym,DOWN)
TextGym=Text("Gymnasiasten", color=BLUE).next_to(KlammerGym,0.1*DOWN).scale(0.7)


#Grupierung der nicht-Gymnasiasten
notGym = VGroup()
for x in range(100):
    if(x%20>=10):
        notGym.add(Personen[x])
KlammerNotGym=Brace(notGym).next_to(notGym,DOWN)
TextNotGym=Text("Nicht-Gymnasiasten", color=RED).next_to(KlammerNotGym,0.1*DOWN).scale(0.7)


#Grupperung der Gymnasiasten mit niedrigem sozioökonomischem Status (5)
GymNiedrig = VGroup(*[Gym[x] for x in range(5)])


#Grupperung der nicht-Gymnasiasten mit niedrigem sozioökonomischem Status (20)
notGymNiedrig=VGroup(*[notGym[x] for x in range(20)])

#Jeweils gelber Rahmen um beide Gruppen mit niedrigem s.ö. Status
RahmenGymNiedrig=always_redraw(lambda: SurroundingRectangle(GymNiedrig,color='#FFFF00', buff=0.1,stroke_width=10,z_index=0).set_fill('#FFFF00',opacity=1))
RahmenNotGymNiedrig=always_redraw(lambda:SurroundingRectangle(notGymNiedrig,color='#FFFF00', buff=0.1,stroke_width=10,z_index=0).set_fill('#FFFF00',opacity=1))



#Grupierung Gymnasiasten mit mittlerem s.ö. Status
GymNichtNiedrig=VGroup(*[Gym[x+5] for x in range(45)])

#Grupierung nicht-Gymnasiasten mit mittlerem s.ö. Status
notGymNichtNiedrig=VGroup(*[notGym[x+20] for x in range(30)])

#Grupierung nicht-Gymnasiasten mit hohem s.ö. Status
#notGymHoch=VGroup(P16x5,P17x5,P18x5,P19x5,P20x5)

#Grupierung aller mit niedrigem Status
Niedrig=VGroup()
Niedrig.add(*[Gym[x] for x in range(5)]).add(*[notGym[x] for x in range(20)])










class Scene1(Scene):
    def construct(self):
        
        #Zeigt 100 Personen

        self.add(Personen)

        self.wait(2)

        #Färbt Gymnasiasten Blau
        self.play(FadeIn(KlammerGym,TextGym),Gym.animate.set_fill(BLUE))
        self.wait(2)
        #Gelber Rahmen um Gymnasiasten mit niedrigem Status
        self.play(FadeIn(RahmenGymNiedrig))
        self.wait(2)
        #Färbt nicht-Gymnasiasten Rot
        self.play(FadeIn(KlammerNotGym,TextNotGym,RahmenNotGymNiedrig),notGym.animate.set_fill(RED))


        self.wait(2)
        BedingteWahrscheinlichkeitOhneBedingung=Tex(r"$P(G)$",substrings_to_isolate="G").to_edge(UP).set_color_by_tex("G",BLUE)
        BedingteWahrscheinlichkeit=Tex(r"$P_\textbf{N}(G)$",substrings_to_isolate=["N","G"]).to_edge(UP)
        BedingteWahrscheinlichkeit.set_color_by_tex("N",YELLOW).set_color_by_tex("G",BLUE)
        self.play(FadeIn(BedingteWahrscheinlichkeitOhneBedingung))
        self.wait(2)
        self.play(TransformMatchingShapes(BedingteWahrscheinlichkeitOhneBedingung,BedingteWahrscheinlichkeit),run_time=4)
        self.wait(2)
        #Macht alle Gruppen mit nicht niedrigem Status transparenter
        self.play(GymNichtNiedrig.animate.set_fill(opacity=0.3).set_stroke(opacity=0.3),
                    notGymNichtNiedrig.animate.set_fill(opacity=0.3).set_stroke(opacity=0.3),
                    run_time=4)
        
        
        self.wait(2)
        

        for x in Niedrig:
            x.scale(1.3)
        

        #Nur noch niedriger Status
        self.play(FadeOut(  GymNichtNiedrig,
                            notGymNichtNiedrig,
                            KlammerGym,
                            KlammerNotGym,
                            TextGym,
                            TextNotGym
                            ),
                        Niedrig.animate.arrange_in_grid(cols=5,buff=(1.2,0.25)).move_to([-3.1,0,0]),
                        BedingteWahrscheinlichkeit.animate.move_to([3,0,0]).scale(1.4),
                        run_time=4)

        self.wait(2)
        

        KlammerZähler=Brace(GymNiedrig,direction=[1, 0, 0.]).next_to(GymNiedrig,RIGHT)
        Zähler=Integer(5,z_index=2).set_color(BLUE).scale(1.5).next_to(KlammerZähler,RIGHT)
        KlammerNotGymNiedrig=Brace(notGymNiedrig,direction=[1, 0, 0.]).next_to(notGymNiedrig,RIGHT)
        AnzahlNotGymNiedrig=Integer(20,z_index=2).set_color(RED).scale(1.5).next_to(KlammerNotGymNiedrig,RIGHT)
        Zähler2=Zähler.copy()
        Zähler3=Zähler.copy()
        Zähler4=Zähler.copy()

        GelbesRechteck=VGroup(RahmenGymNiedrig,RahmenNotGymNiedrig)
        CopyGelbesRechteck=GelbesRechteck.copy()
        AnzahlNotGymNiedrig2=AnzahlNotGymNiedrig.copy()

        #Zeigt Anzahl Gymnasisaten bzw. nicht-Gymnasiasten mit niedrigem Status
        self.add(Zähler,KlammerZähler,AnzahlNotGymNiedrig,KlammerNotGymNiedrig)

        self.wait(2)


        #Bruch der bedingten Wahrscheinlichkeit
        Bruch=Tex(r"$={{{5}} \over {{5}}+{{20}}}$").set_color_by_tex("5",BLACK).set_color_by_tex("20",BLACK).scale(1.8).next_to(BedingteWahrscheinlichkeit,RIGHT)
        Bruch2=Tex(r"$={{{5}} \over {{25}}}$",substrings_to_isolate=["5","25"]).set_color_by_tex("5",BLACK).set_color_by_tex("25",YELLOW).scale(1.8).next_to(Bruch,DOWN-[0.1,0,0])

      
       
        #Animiert Zahlen zu Bruch
        self.play(Zähler3.animate.move_to(Bruch[1].get_center()),
                Zähler2.animate.move_to(Bruch[3].get_center()),
                AnzahlNotGymNiedrig2.animate.move_to(Bruch[5].get_center()),
                FadeIn(Bruch),run_time=3)
        

        self.wait(2)
        self.play(FadeIn(Bruch2),Zähler4.animate.move_to(Bruch2[2]),Transform(CopyGelbesRechteck,Bruch2[4]),run_time=2.5)

        self.wait(4)




class Scene2(Scene):
    def construct(self):
        
        Überschrift=Tex(r"Ziel: Berechnung von $P_B(A)$").to_edge(UP)
        ul=Underline(Überschrift)
        self.add(Überschrift,ul)
        self.wait(2)


        xStart=2
        yStart=2
        EreignisAStart=Rectangle(height=4,width=xStart,color=BLUE,z_index=-1).set_fill(BLUE,opacity=1).move_to([-6,-0.2,0]).set_stroke(BLACK,opacity=0)
        EreignisBStart=Rectangle(height=4,width=yStart,color=RED,z_index=-1).set_fill(RED,opacity=1).next_to(EreignisAStart,buff=[0,0,0]).set_stroke(BLACK,opacity=0)
        Ereignisraum=Rectangle(height=4,width=4,z_index=-1).align_to(EreignisAStart,LEFT+DOWN)
        EreignisraumText=Tex(r"$\Omega$").move_to(Ereignisraum.get_center())
        EreignisAStartText=always_redraw(lambda:Tex(r"$A$",color=BLACK).move_to(EreignisAStart.get_center()))
        EreignisBStartText=always_redraw(lambda:Tex(r"$\bar{A}$",color=BLACK).move_to(EreignisBStart.get_center()))


        ÜberschriftLinkesDiagramm=Tex(r"Alle Möglichkeiten").move_to((EreignisAStart.get_top()+EreignisBStart.get_top())/2+[0,0.5,0])
        
        xMitte=0.75
        yMitte=3.25
        EreignisAMitte=Rectangle(height=4,width=xMitte,color=BLUE).set_fill(BLUE,opacity=1).align_to(EreignisAStart, LEFT+UP).set_stroke(BLACK,opacity=0)
        EreignisBMitte=Rectangle(height=4,width=yMitte,color=RED).set_fill(RED,opacity=1).next_to(EreignisAMitte,buff=[0,0,0]).set_stroke(BLACK,opacity=0)
        
        xEnde=2.2
        yEnde=1.8
        EreignisAEnde=Rectangle(height=4,width=xEnde,color=BLUE).set_fill(BLUE,opacity=1).align_to(EreignisAStart, LEFT+UP).set_stroke(BLACK,opacity=0)
        EreignisBEnde=Rectangle(height=4,width=yEnde,color=RED).set_fill(RED,opacity=1).next_to(EreignisAEnde,buff=[0,0,0]).set_stroke(BLACK,opacity=0)

        BraceA=always_redraw(lambda:Brace(EreignisAStart,DOWN))
        BraceB=always_redraw(lambda:Brace(EreignisBStart,direction=[0, -1, 0.]).next_to(EreignisBStart,DOWN))
        PvonA=always_redraw(lambda:Integer(number=round((EreignisAStart.get_width())/4*100)).next_to(BraceA,DOWN))
        PvonB=always_redraw(lambda:Integer(number=round(EreignisBStart.get_width()/4*100)).next_to(BraceB,DOWN))


        self.add(Ereignisraum,EreignisraumText,ÜberschriftLinkesDiagramm)
        self.wait(3)
        self.remove(Ereignisraum,EreignisraumText)
        self.add(EreignisAStart,EreignisBStart,EreignisAStartText,EreignisBStartText)
        self.wait(2)
        self.add(BraceA,BraceB,PvonA,PvonB)
        self.wait(3)
        self.play(Transform(EreignisAStart,EreignisAMitte),Transform(EreignisBStart,EreignisBMitte),CountInt(PvonA, round(xStart/4*100), round(xMitte/4*100)),CountInt(PvonB,round(yStart/4*100),round(yMitte/4*100)),rate_func=linear,run_time=2)
        
        self.play(Transform(EreignisAStart,EreignisAEnde),Transform(EreignisBStart,EreignisBEnde),CountInt(PvonA, round(xMitte/4*100), round(xEnde/4*100)),CountInt(PvonB,round(yMitte/4*100),round(yEnde/4*100)),rate_func=linear,run_time=2)
        self.wait(2)


        #Zweites Diagramm
        EreignisA=EreignisAStart.copy().next_to(EreignisBStart,RIGHT,buff=[0.55,0,0])
        EreignisB=EreignisBStart.copy().next_to(EreignisA,RIGHT,buff=[0,0,0])
        EreignisAText=EreignisAStartText.copy().move_to(EreignisA)
        EreignisBText=EreignisBStartText.copy().move_to(EreignisB)
 
        ÜberschriftRechtesDiagramm=Tex(r"...unter der Bedingung").move_to((EreignisA.get_top()+EreignisB.get_top())/2+[0,0.5,0])


        aLinieStart=Line(start=[0,0,0],end=[1,0,0],color=BLACK,z_index=-10)
        bLinieStart=Line(start=[0,0,0],end=[2,0,0],color=BLACK,z_index=-10)
        aStart=1
        bStart=2
        BedingungA=always_redraw(lambda:Rectangle(height=aLinieStart.get_length(),width=EreignisAStart.get_width(),color=YELLOW,z_index=0).set_fill(YELLOW,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0))
        BedingungB=always_redraw(lambda:Rectangle(height=bLinieStart.get_length(),width=EreignisBStart.get_width(),color=ORANGE,z_index=0).set_fill(ORANGE,opacity=1).align_to(EreignisB,RIGHT+DOWN).set_stroke(BLACK,opacity=0))
        EreignisAcapnotBText=always_redraw(lambda:Tex(r"$A\cap \bar{B}$",color=BLACK,z_index=3).move_to(EreignisA.get_center()+[0,aLinieStart.get_length()/2,0]))
        EreignisnotAcapnotBText=always_redraw(lambda:Tex(r"$\bar{A}\cap \bar{B}$",color=BLACK,z_index=3).move_to(EreignisB.get_center()+[0,bLinieStart.get_length()/2,0]))
        EreignisAcapBText=always_redraw(lambda:Tex(r"$A\cap B$",color=BLACK,z_index=3).move_to(BedingungA.get_center()))
        EreignisnotAcapBText=always_redraw(lambda:Tex(r"$\bar{A}\cap B$",color=BLACK,z_index=3).move_to(BedingungB.get_center()))

        self.add(EreignisA,EreignisB,EreignisAText,EreignisBText)
        self.wait(2)
        EreignisA.set_color(GREEN)
        self.remove(EreignisAText)
        self.add(BedingungA)
        self.add(EreignisAcapBText,EreignisAcapnotBText)
        self.wait(2)
        self.remove(EreignisBText)
        self.add(EreignisnotAcapnotBText,EreignisnotAcapBText)
        self.add(BedingungB)
        EreignisB.set_color(PURPLE)
        self.wait(2)
        self.add(ÜberschriftRechtesDiagramm)
        
        self.remove(EreignisA,EreignisB,EreignisAcapBText,EreignisAcapnotBText,EreignisnotAcapnotBText,EreignisnotAcapBText)

        EreignisA=always_redraw(lambda:EreignisAStart.copy().next_to(EreignisBStart,RIGHT,buff=[0.55,0,0]).set_fill(GREEN,opacity=0.2))
        EreignisB=always_redraw(lambda:EreignisBStart.copy().next_to(EreignisA,RIGHT,buff=[0,0,0]).set_fill(PURPLE,opacity=0.2))
        
        self.add(EreignisA,EreignisB,EreignisAcapBText,EreignisAcapnotBText,EreignisnotAcapnotBText,EreignisnotAcapBText)
        xEndeEnde=1.55
        yEndeEnde=2.45
        EreignisAEndeEnde=Rectangle(height=4,width=xEndeEnde,color=BLUE).set_fill(BLUE,opacity=1).align_to(EreignisAStart, LEFT+UP).set_stroke(BLACK,opacity=0)
        EreignisBEndeEnde=Rectangle(height=4,width=yEndeEnde,color=RED).set_fill(RED,opacity=1).next_to(EreignisAEndeEnde,buff=[0,0,0]).set_stroke(BLACK,opacity=0)

        aMitte=1.75
        bMitte=1.5
        aLinieMitte=Line(start=[0,0,0],end=[2.5,0,0],color=BLACK,z_index=-10)
        bLinieMitte=Line(start=[0,0,0],end=[1.5,0,0],color=BLACK,z_index=-10)
        BedingungACopy=Rectangle(height=aStart,width=EreignisA.get_width(),color=YELLOW,z_index=2).set_fill(YELLOW,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0)

        BedingungACopyMitte=Rectangle(height=aMitte,width=EreignisA.get_width(),color=YELLOW,z_index=2).set_fill(YELLOW,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0)
        aEnde=2
        bEnde=2.5
        aLinieEnde=Line(start=[0,0,0],end=[2,0,0],color=BLACK,z_index=-10)
        bLinieEnde=Line(start=[0,0,0],end=[2.5,0,0],color=BLACK,z_index=-10)


        xEndeEndeEnde=2.45
        yEndeEndeEnde=1.55

        EreignisAEndeEndeEnde=Rectangle(height=4,width=xEndeEndeEnde,color=BLUE).set_fill(BLUE,opacity=1).align_to(EreignisAStart, LEFT+UP).set_stroke(BLACK,opacity=0)
        EreignisBEndeEndeEnde=Rectangle(height=4,width=yEndeEndeEnde,color=RED).set_fill(RED,opacity=1).next_to(EreignisAEndeEndeEnde,buff=[0,0,0]).set_stroke(BLACK,opacity=0)

        self.wait(2)


        fraction = always_redraw(lambda:VGroup(
                BedingungA.copy(),
                Line(LEFT, RIGHT).match_width(VGroup(
                    BedingungA.copy(),
                    Tex("+"),
                    BedingungB.copy(),
                ).arrange(RIGHT, buff=SMALL_BUFF)),
                VGroup(
                    BedingungA.copy(),
                    Tex("+"),
                    BedingungB.copy(),
                ).arrange(RIGHT, buff=SMALL_BUFF)
            ).arrange(DOWN).move_to([4.55,-0.85,0]))
        
        BeschriftungBruchZähler=always_redraw(lambda:Tex(r"$|A\cap B|$",color=BLACK,z_index=3).move_to(fraction[0].get_center()))
        BeschriftungBruchNennerSummand1=always_redraw(lambda:Tex(r"$|A\cap B|$",color=BLACK,z_index=3).move_to(fraction[2][0].get_center()))
        BeschriftungBruchNennerSummand2=always_redraw(lambda:Tex(r"$|\bar{A}\cap B|$",color=BLACK,z_index=3).move_to(fraction[2][2].get_center()))
        ÜberschriftBruch=Tex(r"$P_B(A)$").move_to([fraction.get_x(),ÜberschriftRechtesDiagramm.get_y(),0])#,substrings_to_isolate=["B","A"]).set_color_by_tex("B",YELLOW).set_color_by_tex("A",BLUE)

       

        BedingungACopy=BedingungA.copy()
        BedingungACopy2=BedingungA.copy()
        BedingungBCopy=BedingungB.copy()
        EreignisAcapBTextCopy=EreignisAcapBText.copy()
        EreignisAcapBTextCopy2=EreignisAcapBText.copy()
        EreignisnotAcapBTextCopy=EreignisnotAcapBText.copy()


        fracBlack=always_redraw(lambda:VGroup(
                BedingungA.copy().set_fill(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(VGroup(
                    BedingungA.copy().set_fill(BLACK).set_z_index(-1),
                    Tex("+"),
                    BedingungB.copy().set_fill(BLACK).set_z_index(-1),
                ).arrange(RIGHT, buff=SMALL_BUFF)),
                VGroup(
                    BedingungA.copy().set_fill(BLACK).set_z_index(-1),
                    Tex("+"),
                    BedingungB.copy().set_fill(BLACK).set_z_index(-1),
                ).arrange(RIGHT, buff=SMALL_BUFF)
            ).arrange(DOWN).move_to([4.55,-0.85,0]))

        self.play(FadeIn(ÜberschriftBruch))
        self.wait(3)
        self.play(FadeIn(fracBlack),BedingungACopy.animate.move_to(fracBlack[0].get_center()),EreignisAcapBTextCopy.animate.move_to(fracBlack[0].get_center()),rate_func=linear,run_time=5)
        self.add(BeschriftungBruchZähler)
        self.remove(EreignisAcapBTextCopy)
        self.wait(5)
        self.play(BedingungACopy2.animate.move_to(fracBlack[2][0].get_center()),EreignisAcapBTextCopy2.animate.move_to(fracBlack[2][0].get_center()),BedingungBCopy.animate.move_to(fracBlack[2][2].get_center()),EreignisnotAcapBTextCopy.animate.move_to(fracBlack[2][2].get_center()),rate_func=linear,run_time=2)
        self.add(BeschriftungBruchNennerSummand1,BeschriftungBruchNennerSummand2)
        self.remove(EreignisAcapBTextCopy2,EreignisnotAcapBTextCopy)
        self.remove(fracBlack,BedingungACopy,BedingungACopy2,BedingungBCopy)
        self.add(fraction)
        self.wait(3)
        self.play(Transform(EreignisAStart,EreignisAEndeEnde),Transform(EreignisBStart,EreignisBEndeEnde),run_time=3)
        self.play(Transform(EreignisAStart,EreignisAEndeEndeEnde),Transform(EreignisBStart,EreignisBEndeEndeEnde),run_time=3)
        self.wait(3)
        self.play(Transform(aLinieStart,aLinieMitte),Transform(bLinieStart,bLinieMitte),run_time=3)
        self.play(Transform(aLinieStart,aLinieEnde),Transform(bLinieStart,bLinieEnde),run_time=3)

        self.wait(5)







class Scene3(Scene):
    def construct(self):
        xStart=2.5
        yStart=1.5

        Überschrift=Tex("Alternative Vorgehensweise").to_edge(UP)
        ul=Underline(Überschrift)
        self.add(Überschrift,ul)
        self.wait(2)
        EreignisAStart=Rectangle(height=xStart,width=4,color=BLUE,z_index=-1).set_fill(BLUE,opacity=1).move_to([-5,0.7,0]).set_stroke(BLACK,opacity=0)
        EreignisBStart=Rectangle(height=yStart,width=4,color=RED,z_index=-1).set_fill(RED,opacity=1).next_to(EreignisAStart,DOWN,buff=[0,0,0]).set_stroke(BLACK,opacity=0)
        EreignisAStartText=always_redraw(lambda:Tex(r"$B$",color=BLACK).move_to(EreignisAStart.get_center()))
        EreignisBStartText=always_redraw(lambda:Tex(r"$\bar{B}$",color=BLACK).move_to(EreignisBStart.get_center()))


        ÜberschriftLinkesDiagramm=Tex(r"Alle Möglichkeiten").move_to(EreignisAStart.get_top()+[0,0.5,0])
        
        self.add(EreignisAStart,EreignisAStartText,EreignisBStart,EreignisBStartText,ÜberschriftLinkesDiagramm)
        self.wait(3)

        EreignisA=EreignisAStart.copy().next_to(EreignisAStart,RIGHT,buff=0.75)
        EreignisAText=EreignisAStartText.copy().move_to(EreignisA.get_center())
        EreignisB=EreignisBStart.copy().next_to(EreignisBStart,RIGHT,buff=0.75).set_fill(opacity=0.2)
        EreignisBText=EreignisBStartText.copy().move_to(EreignisB.get_center())

        ÜberschriftRechtesDiagramm=Tex(r"...unter der Bedingung").move_to(EreignisA.get_top()+[0,0.5,0])

        self.add(EreignisA,EreignisB,EreignisAText,EreignisBText,ÜberschriftRechtesDiagramm)
        self.wait(3)
        
        SchnittA=Rectangle(height=xStart,width=1.58,color=YELLOW,z_index=0).set_fill(YELLOW,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0)
        SchnittB=Rectangle(height=xStart,width=2.42,color=ORANGE,z_index=0).set_fill(ORANGE,opacity=1).next_to(SchnittA,RIGHT,buff=0).set_stroke(BLACK,opacity=0)
        SchnittAText=Tex(r"$A\cap B$",color=BLACK,z_index=1).move_to(SchnittA.get_center())
        SchnittBText=Tex(r"$\bar{A}\cap B$",color=BLACK,z_index=1).move_to(SchnittB.get_center())

        self.add(SchnittA,SchnittB,SchnittAText,SchnittBText)
        self.wait(3)



        SchnittACopy=SchnittA.copy()
        SchnittACopy2=SchnittA.copy()

        SchnittBCopy=SchnittB.copy()
        SchnittATextCopy=SchnittAText.copy()
        SchnittATextCopy2=SchnittAText.copy()

        SchnittBTextCopy=SchnittBText.copy()


        fraction = always_redraw(lambda:VGroup(
                SchnittA.copy(),
                Line(LEFT, RIGHT).match_width(VGroup(
                    SchnittA.copy(),
                    Tex("+"),
                    SchnittB.copy(),
                ).arrange(RIGHT, buff=SMALL_BUFF)),
                VGroup(
                    SchnittA.copy(),
                    Tex("+"),
                    SchnittB.copy(),
                ).arrange(RIGHT, buff=SMALL_BUFF)
            ).arrange(DOWN).move_to([4.55,-0.85,0]))


        fracBlack=always_redraw(lambda:VGroup(
            SchnittA.copy().set_fill(BLACK).set_z_index(-1),
            Line(LEFT, RIGHT).match_width(VGroup(
                SchnittA.copy().set_fill(BLACK).set_z_index(-1),
                Tex("+"),
                SchnittB.copy().set_fill(BLACK).set_z_index(-1),
            ).arrange(RIGHT, buff=SMALL_BUFF)),
            VGroup(
                SchnittA.copy().set_fill(BLACK).set_z_index(-1),
                Tex("+"),
                SchnittB.copy().set_fill(BLACK).set_z_index(-1),
            ).arrange(RIGHT, buff=SMALL_BUFF)
        ).arrange(DOWN).move_to([4.55,-0.85,0]))
        ÜberschriftBruch=Tex(r"$P_B(A)$").move_to([fraction.get_x(),ÜberschriftRechtesDiagramm.get_y(),0])#,substrings_to_isolate=["B","A"]).set_color_by_tex("B",YELLOW).set_color_by_tex("A",BLUE)        
        self.add(ÜberschriftBruch)
        self.wait(2)
        self.play(FadeIn(fracBlack),SchnittACopy.animate.move_to(fracBlack[0].get_center()),SchnittATextCopy.animate.move_to(fracBlack[0].get_center()),SchnittACopy2.animate.move_to(fracBlack[2][0].get_center()),SchnittATextCopy2.animate.move_to(fracBlack[2][0].get_center()),SchnittBCopy.animate.move_to(fracBlack[2][2].get_center()),SchnittBTextCopy.animate.move_to(fracBlack[2][2].get_center()),rate_func=linear,run_time=3)
        BeschriftungBruchZähler=always_redraw(lambda:Tex(r"$|A\cap B|$",color=BLACK,z_index=3).move_to(fraction[0].get_center()))
        BeschriftungBruchNennerSummand1=always_redraw(lambda:Tex(r"$|A\cap B|$",color=BLACK,z_index=3).move_to(fraction[2][0].get_center()))
        BeschriftungBruchNennerSummand2=always_redraw(lambda:Tex(r"$|\bar{A}\cap B|$",color=BLACK,z_index=3).move_to(fraction[2][2].get_center()))
        self.add(BeschriftungBruchZähler,BeschriftungBruchNennerSummand1,BeschriftungBruchNennerSummand2)
        self.remove(SchnittACopy,SchnittACopy2,SchnittATextCopy,SchnittATextCopy2,SchnittBCopy,SchnittBTextCopy,fracBlack)
        self.add(fraction)
        self.wait(5)
