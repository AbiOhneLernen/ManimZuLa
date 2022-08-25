from manim import *

class Quiz(Scene):
    def construct(self):
        Überschrift=Text("Quiz").to_edge(UP)
        ul=Underline(Überschrift)

        self.add(Überschrift,ul)

        AnteilErkrankteText=Tex(r"Anteil Erkrankter:\ 1\%").next_to(Überschrift,DOWN).to_edge(LEFT)
        Sensitivität=Tex(r"Sensitivität:\ 90\%").next_to(AnteilErkrankteText,DOWN).to_edge(LEFT)
        Spezifität=Tex(r"Spezifität:\ 97\%").next_to(Sensitivität,DOWN).to_edge(LEFT)
        Angaben=VGroup(AnteilErkrankteText,Sensitivität,Spezifität)
        RahmenAngaben=SurroundingRectangle(Angaben)
        self.add(AnteilErkrankteText,Sensitivität,Spezifität,RahmenAngaben)
        Testergebnis=Tex(r"Testergebnis").next_to(RahmenAngaben,DOWN).to_edge(LEFT)
        ul2=Underline(Testergebnis)
        Positiv=Tex(r"positiv $\Rightarrow$  infiziert").next_to(Testergebnis,DOWN).to_edge(LEFT)
        Negativ=Tex(r"negativ $\Rightarrow$ nicht infiziert").next_to(Positiv,DOWN).to_edge(LEFT)
        TestergebnisVGroup=VGroup(Testergebnis,Positiv,Negativ,ul2)
        TestergebnisRahmen=SurroundingRectangle(TestergebnisVGroup, color=RED)

        self.add(TestergebnisVGroup,TestergebnisRahmen)

        Frage1=Tex(r"Frage 1: Wie hoch ist die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person tatsächlich infiziert ist, wenn sie ein positives Testergebnis erhalten hat?").next_to(Überschrift,DOWN).next_to(RahmenAngaben,RIGHT)
        self.add(Frage1)
        self.wait(5)

class HäufigkeitsnetzNurRandereignisse(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)



        #Knoten Baum 2
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        


        #Position Häufigkeitsnetz
        #Tree1
        p1= [0,0,0]        #Root
        p2= [0,2.5,0]         #Child1
        p3= [0,-2.5,0]           #Child2
        p4= [-4,2.5,0]         #Grandchild1
        p5= [4,2.5,0]        #Grandchild2
        p6= [-4,-2.5,0]           #Grandchild3
        p7= [4,-2.5,0]          #Grandchild4




        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)


        #Tree2
        q1= [0,0,0]        #Root
        q2= [-4,0,0]         #Child1
        q3= [4,0,0]           #Child2
        q4= [-4,2.5,0]         #Grandchild1
        q5= [-4,-2.5,0]        #Grandchild2
        q6= [4,2.5,0]           #Grandchild3
        q7= [4,-2.5,0]          #Grandchild4

        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)

        #Nicht transparente Knoten
        #Tree1Root.set_fill(BLACK, opacity=1)
        #Tree1Child1.set_fill(BLACK, opacity=1)
        #Tree1Child2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild1.set_fill(BLACK, opacity=1)
        #Tree1Grandchild2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild3.set_fill(BLACK, opacity=1)
        #Tree1Grandchild4.set_fill(BLACK, opacity=1)

        #Tree2Child1.set_fill(BLACK, opacity=1)
        #Tree2Child2.set_fill(BLACK, opacity=1)

        
        #Beschriftung Knoten
        #Tree1
        
        
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree1Child1Text = Tex(r"$K$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$T$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{T}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$10.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$100$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$9.900$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$90$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$297$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$10$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$9.603$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$387$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$9.613$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_left(),Tree1Grandchild1.get_right())
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_right(),Tree1Grandchild2.get_left())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_left(),Tree1Grandchild3.get_right())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_right(),Tree1Grandchild4.get_left())

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())
        Tree2EdgeChild1Grandchild1=Line(Tree2Child1.get_top(),Tree1Grandchild1.get_bottom())
        Tree2EdgeChild1Grandchild2=Line(Tree2Child1.get_bottom(),Tree1Grandchild3.get_top())
        Tree2EdgeChild2Grandchild3=Line(Tree2Child2.get_top(),Tree1Grandchild2.get_bottom())
        Tree2EdgeChild2Grandchild4=Line(Tree2Child2.get_bottom(),Tree1Grandchild4.get_top())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$1\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_K(T)$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{K}} (\bar{T})$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)#.shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_J(V)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2EdgeChild1Grandchild1,RIGHT,buff=0.1)#.shift([-0.4,0,0])
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#00B0F0'),Tree1Child2.set_color('#00B0F0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color(PURE_RED),Tree2Child2.set_color(PURE_RED))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#00B0F0'),Tree1Child2Text.set_color('#00B0F0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color(PURE_RED),Tree2Child2Text.set_color(PURE_RED))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#00B0F0'),Tree1Child2TextBetrag.set_color('#00B0F0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color(PURE_RED),Tree2Child2TextBetrag.set_color(PURE_RED))#.set_color('#FFFFFF')

        
        

        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText)

        #GELB .set_color('#FFFF00')


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        #self.add(Tree1Child1TextBetrag)
        #self.add(Tree1RootBetrag.set_color('#FFFF00'))
        #self.add(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        #self.add(PvonGBedN)

        self.add(PvonN)

        


        #self.add(PvonN,PvonNQuer)
        #self.add(PvonG,PvonGQuer)

        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree2Child1TextBetrag)
        #self.add(Tree1Child2TextBetrag)
        #self.add(Tree2Child2TextBetrag)
        
        Fokus=SurroundingRectangle(PvonGBedN,color='#7030A0')
        Fokus2=SurroundingRectangle(PvonGQuerBedNQuer,color='#7030A0')
        self.add(Fokus,Fokus2)
        
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)

        PvonGBedN[0][3].set_color(PURE_RED)
        PvonGBedN[0][1].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][1].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][2].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][4].set_color(PURE_RED)
        PvonGQuerBedNQuer[0][5].set_color(PURE_RED)
        #PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN)
        self.add(PvonGBedN,PvonGQuerBedNQuer)


class HäufigkeitsnetzSensitifitätSpezifitätKonkreteWerte(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)



        #Knoten Baum 2
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        


        #Position Häufigkeitsnetz
        #Tree1
        p1= [0,0,0]        #Root
        p2= [0,2.5,0]         #Child1
        p3= [0,-2.5,0]           #Child2
        p4= [-4,2.5,0]         #Grandchild1
        p5= [4,2.5,0]        #Grandchild2
        p6= [-4,-2.5,0]           #Grandchild3
        p7= [4,-2.5,0]          #Grandchild4




        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)


        #Tree2
        q1= [0,0,0]        #Root
        q2= [-4,0,0]         #Child1
        q3= [4,0,0]           #Child2
        q4= [-4,2.5,0]         #Grandchild1
        q5= [-4,-2.5,0]        #Grandchild2
        q6= [4,2.5,0]           #Grandchild3
        q7= [4,-2.5,0]          #Grandchild4

        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)

        #Nicht transparente Knoten
        #Tree1Root.set_fill(BLACK, opacity=1)
        #Tree1Child1.set_fill(BLACK, opacity=1)
        #Tree1Child2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild1.set_fill(BLACK, opacity=1)
        #Tree1Grandchild2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild3.set_fill(BLACK, opacity=1)
        #Tree1Grandchild4.set_fill(BLACK, opacity=1)

        #Tree2Child1.set_fill(BLACK, opacity=1)
        #Tree2Child2.set_fill(BLACK, opacity=1)

        
        #Beschriftung Knoten
        #Tree1
        
        
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree1Child1Text = Tex(r"$K$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$T$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{T}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$10.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$100$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$9.900$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$90$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$297$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$10$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$9.603$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$387$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$9.613$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_left(),Tree1Grandchild1.get_right())
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_right(),Tree1Grandchild2.get_left())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_left(),Tree1Grandchild3.get_right())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_right(),Tree1Grandchild4.get_left())

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())
        Tree2EdgeChild1Grandchild1=Line(Tree2Child1.get_top(),Tree1Grandchild1.get_bottom())
        Tree2EdgeChild1Grandchild2=Line(Tree2Child1.get_bottom(),Tree1Grandchild3.get_top())
        Tree2EdgeChild2Grandchild3=Line(Tree2Child2.get_top(),Tree1Grandchild2.get_bottom())
        Tree2EdgeChild2Grandchild4=Line(Tree2Child2.get_bottom(),Tree1Grandchild4.get_top())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$1\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$90\%$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$97\%$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)#.shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        #PvonNBedG=Tex(r"$P_T(K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)#.shift([-0.4,0,0])
        PvonNBedG=Tex(r"$\frac{90}{387}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT)
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{T}} (K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT, buff=0.1)#.shift([0.15,0,0])
        PvonNBedGQuer=Tex(r"$\frac{10}{9.613}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT)
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{T}} (\bar{K})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#00B0F0'),Tree1Child2.set_color('#00B0F0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color(PURE_RED),Tree2Child2.set_color(PURE_RED))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#00B0F0'),Tree1Child2Text.set_color('#00B0F0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color(PURE_RED),Tree2Child2Text.set_color(PURE_RED))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#00B0F0'),Tree1Child2TextBetrag.set_color('#00B0F0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color(PURE_RED),Tree2Child2TextBetrag.set_color(PURE_RED))#.set_color('#FFFFFF')

        
        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        self.add(Tree1Root.set_color('#FFFF00'),Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText.set_color('#FFFF00'))

        #GELB .set_color('#FFFF00')


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        self.add(Tree1Child1TextBetrag.set_color('#00B0F0'))
        self.add(Tree1Child2TextBetrag.set_color('#00B0F0'))
        self.add(Tree1RootBetrag.set_color('#FFFF00'))
        self.add(Tree1Grandchild1TextBetrag)
        self.add(Tree1Grandchild3TextBetrag)
        self.add(Tree1Grandchild4TextBetrag)
        self.add(Tree1Grandchild2TextBetrag)
        self.add(Tree2Child1TextBetrag.set_color(PURE_RED))
        self.add(Tree2Child2TextBetrag.set_color(PURE_RED))

        Fokus=SurroundingRectangle(PvonNBedG,color='#7030A0')
        Fokus2=SurroundingRectangle(PvonNBedGQuer,color='#7030A0')
        self.add(Fokus,Fokus2)


        FokusKnoten=VGroup(Tree1Grandchild2,Tree1Grandchild4,Fokus2)
        Fokus3=SurroundingRectangle(FokusKnoten,color=PURE_RED)
        #self.add(Fokus3)
        #self.add(Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        #self.add(PvonGBedN)

        self.add(PvonN)

        


        #self.add(PvonN,PvonNQuer)
        #self.add(PvonG,PvonGQuer)

        

        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree2Child1TextBetrag)
        #self.add(Tree1Child2TextBetrag)
        #self.add(Tree2Child2TextBetrag)
        
        
        
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)

        
        
        #PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN)
        self.add(PvonGBedN,PvonGQuerBedNQuer)

        self.add(PvonNBedG)
        self.add(PvonNBedGQuer)

        #PvonNBedG[0][3].set_color('#00B0F0')
        PvonNBedG[0][3].set_color(PURE_RED)
        PvonNBedG[0][4].set_color(PURE_RED)
        PvonNBedG[0][5].set_color(PURE_RED)
        PvonNBedGQuer[0][3].set_color(PURE_RED)
        PvonNBedGQuer[0][4].set_color(PURE_RED)
        PvonNBedGQuer[0][5].set_color(PURE_RED)
        PvonNBedGQuer[0][6].set_color(PURE_RED)
        PvonNBedGQuer[0][7].set_color(PURE_RED)
        
        #PvonNBedGQuer[0][5].set_color(PURE_RED)




class HäufigkeitsnetzNurRandereignisse(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)



        #Knoten Baum 2
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        


        #Position Häufigkeitsnetz
        #Tree1
        p1= [0,0,0]        #Root
        p2= [0,2.5,0]         #Child1
        p3= [0,-2.5,0]           #Child2
        p4= [-4,2.5,0]         #Grandchild1
        p5= [4,2.5,0]        #Grandchild2
        p6= [-4,-2.5,0]           #Grandchild3
        p7= [4,-2.5,0]          #Grandchild4




        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)


        #Tree2
        q1= [0,0,0]        #Root
        q2= [-4,0,0]         #Child1
        q3= [4,0,0]           #Child2
        q4= [-4,2.5,0]         #Grandchild1
        q5= [-4,-2.5,0]        #Grandchild2
        q6= [4,2.5,0]           #Grandchild3
        q7= [4,-2.5,0]          #Grandchild4

        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)

        #Nicht transparente Knoten
        #Tree1Root.set_fill(BLACK, opacity=1)
        #Tree1Child1.set_fill(BLACK, opacity=1)
        #Tree1Child2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild1.set_fill(BLACK, opacity=1)
        #Tree1Grandchild2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild3.set_fill(BLACK, opacity=1)
        #Tree1Grandchild4.set_fill(BLACK, opacity=1)

        #Tree2Child1.set_fill(BLACK, opacity=1)
        #Tree2Child2.set_fill(BLACK, opacity=1)

        
        #Beschriftung Knoten
        #Tree1
        
        
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree1Child1Text = Tex(r"$K$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$T$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{T}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$10.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$100$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$9.900$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$90$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$297$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$10$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$9.603$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$387$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$9.613$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_left(),Tree1Grandchild1.get_right())
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_right(),Tree1Grandchild2.get_left())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_left(),Tree1Grandchild3.get_right())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_right(),Tree1Grandchild4.get_left())

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())
        Tree2EdgeChild1Grandchild1=Line(Tree2Child1.get_top(),Tree1Grandchild1.get_bottom())
        Tree2EdgeChild1Grandchild2=Line(Tree2Child1.get_bottom(),Tree1Grandchild3.get_top())
        Tree2EdgeChild2Grandchild3=Line(Tree2Child2.get_top(),Tree1Grandchild2.get_bottom())
        Tree2EdgeChild2Grandchild4=Line(Tree2Child2.get_bottom(),Tree1Grandchild4.get_top())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$1\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_K(T)$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{K}} (\bar{T})$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)#.shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_J(V)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2EdgeChild1Grandchild1,RIGHT,buff=0.1)#.shift([-0.4,0,0])
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#00B0F0'),Tree1Child2.set_color('#00B0F0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color(PURE_RED),Tree2Child2.set_color(PURE_RED))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#00B0F0'),Tree1Child2Text.set_color('#00B0F0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color(PURE_RED),Tree2Child2Text.set_color(PURE_RED))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#00B0F0'),Tree1Child2TextBetrag.set_color('#00B0F0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color(PURE_RED),Tree2Child2TextBetrag.set_color(PURE_RED))#.set_color('#FFFFFF')

        
        

        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText)

        #GELB .set_color('#FFFF00')


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        #self.add(Tree1Child1TextBetrag)
        #self.add(Tree1RootBetrag.set_color('#FFFF00'))
        #self.add(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        #self.add(PvonGBedN)

        self.add(PvonN)

        


        #self.add(PvonN,PvonNQuer)
        #self.add(PvonG,PvonGQuer)

        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree2Child1TextBetrag)
        #self.add(Tree1Child2TextBetrag)
        #self.add(Tree2Child2TextBetrag)
        
        Fokus=SurroundingRectangle(PvonGBedN,color='#7030A0')
        Fokus2=SurroundingRectangle(PvonGQuerBedNQuer,color='#7030A0')
        self.add(Fokus,Fokus2)
        
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)

        PvonGBedN[0][3].set_color(PURE_RED)
        PvonGBedN[0][1].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][1].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][2].set_color('#00B0F0')
        PvonGQuerBedNQuer[0][4].set_color(PURE_RED)
        PvonGQuerBedNQuer[0][5].set_color(PURE_RED)
        #PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN)
        self.add(PvonGBedN,PvonGQuerBedNQuer)


class CountInt(Animation):
            def __init__(self, number: DecimalNumber, start: int, end: int, **kwargs) -> None:
                # Pass number as the mobject of the animation
                super().__init__(number,  **kwargs)
                # Set start and end
                self.start = start
                self.end = end

            def interpolate_mobject(self, alpha: int) -> None:
                # Set value of DecimalNumber according to alpha
                value = self.start + (alpha * (self.end - self.start))
                self.mobject.set_value(value)



class AnimationSpezifitätSensitivität100Prozent(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)



        #Knoten Baum 2
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        


        #Position Häufigkeitsnetz
        #Tree1
        p1= [0,0,0]        #Root
        p2= [0,2.5,0]         #Child1
        p3= [0,-2.5,0]           #Child2
        p4= [-4,2.5,0]         #Grandchild1
        p5= [4,2.5,0]        #Grandchild2
        p6= [-4,-2.5,0]           #Grandchild3
        p7= [4,-2.5,0]          #Grandchild4




        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)


        #Tree2
        q1= [0,0,0]        #Root
        q2= [-4,0,0]         #Child1
        q3= [4,0,0]           #Child2
        q4= [-4,2.5,0]         #Grandchild1
        q5= [-4,-2.5,0]        #Grandchild2
        q6= [4,2.5,0]           #Grandchild3
        q7= [4,-2.5,0]          #Grandchild4

        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)

        #Nicht transparente Knoten
        #Tree1Root.set_fill(BLACK, opacity=1)
        #Tree1Child1.set_fill(BLACK, opacity=1)
        #Tree1Child2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild1.set_fill(BLACK, opacity=1)
        #Tree1Grandchild2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild3.set_fill(BLACK, opacity=1)
        #Tree1Grandchild4.set_fill(BLACK, opacity=1)

        #Tree2Child1.set_fill(BLACK, opacity=1)
        #Tree2Child2.set_fill(BLACK, opacity=1)

        
        #Beschriftung Knoten
        #Tree1
        
        
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree1Child1Text = Tex(r"$K$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$T$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{T}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$10.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$100$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$9.900$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$90$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$297$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$10$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$9.603$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$387$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$9.613$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_left(),Tree1Grandchild1.get_right())
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_right(),Tree1Grandchild2.get_left())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_left(),Tree1Grandchild3.get_right())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_right(),Tree1Grandchild4.get_left())

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())
        Tree2EdgeChild1Grandchild1=Line(Tree2Child1.get_top(),Tree1Grandchild1.get_bottom())
        Tree2EdgeChild1Grandchild2=Line(Tree2Child1.get_bottom(),Tree1Grandchild3.get_top())
        Tree2EdgeChild2Grandchild3=Line(Tree2Child2.get_top(),Tree1Grandchild2.get_bottom())
        Tree2EdgeChild2Grandchild4=Line(Tree2Child2.get_bottom(),Tree1Grandchild4.get_top())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$1\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$90\%$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$97\%$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)#.shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        #PvonNBedG=Tex(r"$P_T(K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)#.shift([-0.4,0,0])
        PvonNBedG=Tex(r"$\frac{90}{387}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT)
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{T}} (K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT, buff=0.1)#.shift([0.15,0,0])
        PvonNBedGQuer=Tex(r"$\frac{10}{9.613}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT)
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{T}} (\bar{K})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#00B0F0'),Tree1Child2.set_color('#00B0F0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color(PURE_RED),Tree2Child2.set_color(PURE_RED))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#00B0F0'),Tree1Child2Text.set_color('#00B0F0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color(PURE_RED),Tree2Child2Text.set_color(PURE_RED))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#00B0F0'),Tree1Child2TextBetrag.set_color('#00B0F0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color(PURE_RED),Tree2Child2TextBetrag.set_color(PURE_RED))#.set_color('#FFFFFF')

        
        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        self.add(Tree1Root.set_color('#FFFF00'),Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText.set_color('#FFFF00'))

        #GELB .set_color('#FFFF00')


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        self.add(Tree1Child1TextBetrag.set_color('#00B0F0'))
        self.add(Tree1Child2TextBetrag.set_color('#00B0F0'))
        self.add(Tree1RootBetrag.set_color('#FFFF00'))
        self.add(Tree1Grandchild1TextBetrag)
        self.add(Tree1Grandchild3TextBetrag)
        self.add(Tree1Grandchild4TextBetrag)
        self.add(Tree1Grandchild2TextBetrag)
        self.add(Tree2Child1TextBetrag.set_color(PURE_RED))
        self.add(Tree2Child2TextBetrag.set_color(PURE_RED))

        Fokus=SurroundingRectangle(PvonNBedG,color='#7030A0')
        Fokus2=SurroundingRectangle(PvonNBedGQuer,color='#7030A0')
        self.add(Fokus,Fokus2)


        FokusKnoten=VGroup(Tree1Grandchild2,Tree1Grandchild4,Fokus2)
        Fokus3=SurroundingRectangle(FokusKnoten,color=PURE_RED)
        #self.add(Fokus3)
        #self.add(Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        #self.add(PvonGBedN)

        self.add(PvonN)

        


        #self.add(PvonN,PvonNQuer)
        #self.add(PvonG,PvonGQuer)

        

        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree2Child1TextBetrag)
        #self.add(Tree1Child2TextBetrag)
        #self.add(Tree2Child2TextBetrag)
        
        
        
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)

        RahmenSensitivität=SurroundingRectangle(PvonGBedN,color='#00B050')
        self.add(RahmenSensitivität)
        TextSensitivität=Tex("Sensitivität",color='#00B050').next_to(RahmenSensitivität,UP)
        self.add(TextSensitivität)

        TextSpezifität=Tex("Spezifität").next_to(PvonGQuerBedNQuer,DOWN)
        self.add(TextSpezifität)


        RahmenPrävalenz=SurroundingRectangle(PvonN,color='#00B0F0')
        self.add(RahmenPrävalenz)

        Ungefähr23Prozent=Tex(r"$23\%\approx$",font_size=40,color='#7030A0').next_to(Fokus,LEFT,buff=0.1)
        self.add(Ungefähr23Prozent)

        Ungefähr0Komma1Prozent=Tex(r"$\approx 0,1\%$",font_size=40,color='#7030A0').next_to(Fokus2,RIGHT,buff=0.1)
        self.add(Ungefähr0Komma1Prozent)
        
        #PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN)
        self.add(PvonGBedN,PvonGQuerBedNQuer)

        self.add(PvonNBedG)
        self.add(PvonNBedGQuer)



        #PvonNBedG[0][3].set_color('#00B0F0')
        PvonNBedG[0][3].set_color(PURE_RED)
        PvonNBedG[0][4].set_color(PURE_RED)
        PvonNBedG[0][5].set_color(PURE_RED)
        PvonNBedGQuer[0][3].set_color(PURE_RED)
        PvonNBedGQuer[0][4].set_color(PURE_RED)
        PvonNBedGQuer[0][5].set_color(PURE_RED)
        PvonNBedGQuer[0][6].set_color(PURE_RED)
        PvonNBedGQuer[0][7].set_color(PURE_RED)


        #PvonN=always_redraw(lambda:Brace(EreignisAStart,DOWN))
        #Brace(EreignisAStart,direction=[0, -1, 0.]).add_updater(lambda BraceA: BraceA.next_to(EreignisAStart,DOWN))
        #BraceB=always_redraw(lambda:Brace(EreignisBStart,direction=[0, -1, 0.]).next_to(EreignisBStart,DOWN))
        #PvonA=always_redraw(lambda:Integer(number=round((EreignisAStart.get_width())/4*100)).next_to(BraceA,DOWN))
        #PvonB=always_redraw(lambda:Integer(number=round(EreignisBStart.get_width()/4*100)).next_to(BraceB,DOWN))
        
        
        #self.play(CountInt(PvonN,start=0,end=100),rate_function=linear,run_time=10)

        #self.wait(5)
        
        #PvonNBedGQuer[0][5].set_color(PURE_RED)




class HerleitungFormel(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)



        #Knoten Baum 2
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        


        #Position Häufigkeitsnetz
        #Tree1
        p1= [0,0,0]        #Root
        p2= [0,2.5,0]         #Child1
        p3= [0,-2.5,0]           #Child2
        p4= [-4,2.5,0]         #Grandchild1
        p5= [4,2.5,0]        #Grandchild2
        p6= [-4,-2.5,0]           #Grandchild3
        p7= [4,-2.5,0]          #Grandchild4




        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)


        #Tree2
        q1= [0,0,0]        #Root
        q2= [-4,0,0]         #Child1
        q3= [4,0,0]           #Child2
        q4= [-4,2.5,0]         #Grandchild1
        q5= [-4,-2.5,0]        #Grandchild2
        q6= [4,2.5,0]           #Grandchild3
        q7= [4,-2.5,0]          #Grandchild4

        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)

        #Nicht transparente Knoten
        #Tree1Root.set_fill(BLACK, opacity=1)
        #Tree1Child1.set_fill(BLACK, opacity=1)
        #Tree1Child2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild1.set_fill(BLACK, opacity=1)
        #Tree1Grandchild2.set_fill(BLACK, opacity=1)
        #Tree1Grandchild3.set_fill(BLACK, opacity=1)
        #Tree1Grandchild4.set_fill(BLACK, opacity=1)

        #Tree2Child1.set_fill(BLACK, opacity=1)
        #Tree2Child2.set_fill(BLACK, opacity=1)

        
        #Beschriftung Knoten
        #Tree1
        
        
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree1Child1Text = Tex(r"$K$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$T$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{T}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$T\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$T\cap \bar{K}$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$\bar{T}\cap K$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{T}\cap\bar{K}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$10.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$100$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$9.900$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$90$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$297$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$10$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$9.603$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$387$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$9.613$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_left(),Tree1Grandchild1.get_right())
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_right(),Tree1Grandchild2.get_left())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_left(),Tree1Grandchild3.get_right())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_right(),Tree1Grandchild4.get_left())

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())
        Tree2EdgeChild1Grandchild1=Line(Tree2Child1.get_top(),Tree1Grandchild1.get_bottom())
        Tree2EdgeChild1Grandchild2=Line(Tree2Child1.get_bottom(),Tree1Grandchild3.get_top())
        Tree2EdgeChild2Grandchild3=Line(Tree2Child2.get_top(),Tree1Grandchild2.get_bottom())
        Tree2EdgeChild2Grandchild4=Line(Tree2Child2.get_bottom(),Tree1Grandchild4.get_top())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(K)$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{K})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_K(T)$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_K(\bar{T})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{K}} (T)$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{K}}(\bar{T})$",font_size=40).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)#.shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(T)$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{T})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_T(K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)#.shift([-0.4,0,0])
        #PvonNBedG=Tex(r"$\frac{90}{387}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT)
        PvonNQuerBedG=Tex(r"$P_T(\bar{K})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild1Grandchild2,LEFT, buff=0.1)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{T}} (K)$",font_size=40).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT, buff=0.1)#.shift([0.15,0,0])
        #PvonNBedGQuer=Tex(r"$\frac{10}{9.613}$",font_size=40).scale(1.3).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT)
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{T}} (\bar{K})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#00B0F0'),Tree1Child2.set_color('#00B0F0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color(PURE_RED),Tree2Child2.set_color(PURE_RED))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#00B0F0'),Tree1Child2Text.set_color('#00B0F0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color(PURE_RED),Tree2Child2Text.set_color(PURE_RED))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#00B0F0'),Tree1Child2TextBetrag.set_color('#00B0F0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color(PURE_RED),Tree2Child2TextBetrag.set_color(PURE_RED))#.set_color('#FFFFFF')

        
        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        self.add(Tree1Root.set_color('#FFFF00'),Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText.set_color('#FFFF00'))

        #GELB .set_color('#FFFF00')


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        #self.add(Tree1Child1TextBetrag.set_color('#00B0F0'))
        #self.add(Tree1Child2TextBetrag.set_color('#00B0F0'))
        #self.add(Tree1RootBetrag.set_color('#FFFF00'))
        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree2Child1TextBetrag.set_color(PURE_RED))
        #self.add(Tree2Child2TextBetrag.set_color(PURE_RED))

        Fokus=SurroundingRectangle(PvonNBedG,color='#7030A0')
        Fokus2=SurroundingRectangle(PvonNBedGQuer,color='#7030A0')
        #self.add(Fokus,Fokus2)


        FokusKnoten=VGroup(Tree1Grandchild2,Tree1Grandchild4,Fokus2)
        Fokus3=SurroundingRectangle(FokusKnoten,color=PURE_RED)
        #self.add(Fokus3)
        #self.add(Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        #self.add(PvonGBedN)

        self.add(PvonN)

        


        #self.add(PvonN,PvonNQuer)
        #self.add(PvonG,PvonGQuer)

        

        #self.add(Tree1Grandchild1TextBetrag)
        #self.add(Tree2Child1TextBetrag)
        #self.add(Tree1Child2TextBetrag)
        #self.add(Tree2Child2TextBetrag)
        
        
        
        #self.add(Tree1Grandchild2TextBetrag)
        #self.add(Tree1Grandchild3TextBetrag)
        #self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)

        RahmenSensitivität=SurroundingRectangle(PvonGBedN,color='#00B050')
        self.add(RahmenSensitivität)
        TextSensitivität=Tex("Sensitivität",color='#00B050').next_to(RahmenSensitivität,UP)
        #self.add(TextSensitivität)

        TextSpezifität=Tex("Spezifität",color='#FFC000').next_to(PvonGQuerBedNQuer,DOWN)
        #self.add(TextSpezifität)
        RahmenSpezifität=SurroundingRectangle(PvonGQuerBedNQuer,color='#FFC000')
        self.add(RahmenSpezifität)

        RahmenPrävalenz=SurroundingRectangle(PvonN,color='#00B0F0')
        self.add(RahmenPrävalenz)

        Ungefähr23Prozent=Tex(r"$23\%\approx$",font_size=40,color='#7030A0').next_to(Fokus,LEFT,buff=0.1)
        #self.add(Ungefähr23Prozent)

        Ungefähr0Komma1Prozent=Tex(r"$\approx 0,1\%$",font_size=40,color='#7030A0').next_to(Fokus2,RIGHT,buff=0.1)
        #self.add(Ungefähr0Komma1Prozent)
        
        #PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN)
        self.add(PvonGQuerBedNQuer.set_color('#FFC000'))
        self.add(PvonGBedN.set_color('#00B050'))

        #self.add(PvonNBedG)
        #self.add(PvonNBedGQuer)

        self.add(PvonNQuer.set_color('#00B0F0'))
        self.add(PvonGQuerBedN.set_color('#00B050'))
        self.add(PvonGBedNQuer.set_color('#FFC000'))


        self.add(PvonNBedG.set_color('#7030A0'),Fokus)



        #PvonNBedG[0][3].set_color('#00B0F0')
        #PvonNBedG[0][3].set_color(PURE_RED)
        #PvonNBedG[0][4].set_color(PURE_RED)
        #PvonNBedG[0][5].set_color(PURE_RED)
        #PvonNBedGQuer[0][3].set_color(PURE_RED)
        #PvonNBedGQuer[0][4].set_color(PURE_RED)
        #PvonNBedGQuer[0][5].set_color(PURE_RED)
        #PvonNBedGQuer[0][6].set_color(PURE_RED)
        #PvonNBedGQuer[0][7].set_color(PURE_RED)
