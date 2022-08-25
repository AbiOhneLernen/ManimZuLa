from manim import *

class Scene1(Scene):
    def construct(self):
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        
        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLACK, opacity=1)
        Tree1Child2.set_fill(BLACK, opacity=1)
        Tree1Grandchild1.set_fill(BLACK, opacity=1)
        Tree1Grandchild2.set_fill(BLACK, opacity=1)
        Tree1Grandchild3.set_fill(BLACK, opacity=1)
        Tree1Grandchild4.set_fill(BLACK, opacity=1)

        Knoten=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)

        

        p1= [0,2.5,0] #Root
        p2= [-3,0,0]      #Child1
        p3= [3,0,0]    #Child2
        p4= [-5,-2.5,0]   #Grandchild1
        p5= [-1.5,-2.5,0] #Grandchild2
        p6= [1.5,-2.5,0]   #Grandchild3
        p7= [5,-2.5,0] #Grandchild4

        dotp1=Dot(p1,fill_opacity=0)    #Root
        dotp2=Dot(p2,fill_opacity=0)    #Child1
        dotp3=Dot(p3,fill_opacity=0)    #Child2
        dotp4=Dot(p4,fill_opacity=0)    #Grandchild1
        dotp5=Dot(p5,fill_opacity=0)    #Grandchild2
        dotp6=Dot(p6,fill_opacity=0)    #Grandchild3
        dotp7=Dot(p7,fill_opacity=0)    #Grandchild4


        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)

        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1Text = Tex(r"$B$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2Text = Tex(r"$\bar{B}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1Text = Tex(r"$A$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2Text = Tex(r"$\bar{A}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3Text = Tex(r"$A$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4Text = Tex(r"$\bar{A}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1TextSchnitt = Tex(r"$A\cap B$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2TextSchnitt = Tex(r"$\bar{A}\cap B$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3TextSchnitt = Tex(r"$A\cap \bar{B}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4TextSchnitt = Tex(r"$\bar{A}\cap\bar{B}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)

        
        Tree1Grandchild1TextSchnitt.move_to(p4)
        Tree1Grandchild2TextSchnitt.move_to(p5)
        Tree1Grandchild3TextSchnitt.move_to(p6)
        Tree1Grandchild4TextSchnitt.move_to(p7)

        #"Updater" Kanten
        Tree1EdgeRootChild1=always_redraw(lambda: Line(dotp1.get_center(),dotp2.get_center()))
        Tree1EdgeRootChild2=always_redraw(lambda: Line(dotp1.get_center(),dotp3.get_center()))
        Tree1EdgeChild1Grandchild1=always_redraw(lambda: Line(dotp2.get_center(),dotp4.get_center()))
        Tree1EdgeChild1Grandchild2=always_redraw(lambda: Line(dotp2.get_center(),dotp5.get_center()))
        Tree1EdgeChild2Grandchild3=always_redraw(lambda: Line(dotp3.get_center(),dotp6.get_center()))
        Tree1EdgeChild2Grandchild4=always_redraw(lambda: Line(dotp3.get_center(),dotp7.get_center()))


        Kanten=VGroup(Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        MengenInKnotenSchnitt=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1TextSchnitt,Tree1Grandchild2TextSchnitt,Tree1Grandchild3TextSchnitt,Tree1Grandchild4TextSchnitt)

        self.add(Tree1Root,Tree1RootText)
        self.wait(3)
        self.add(Tree1Child1,Tree1Child2,Tree1Child1Text,Tree1Child2Text,Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.wait(3)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        #self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        self.wait(3)

        #self.add(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        #self.wait(3)

        self.remove(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        self.add(MengenInKnotenSchnitt)
        self.wait(3)

        Tree1RootText = Tex(r"$|\Omega|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{B}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|A\cap B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|\bar{A}\cap B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|A\cap \bar{B}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{A}\cap\bar{B}|$",font_size=40).set_z_index(2).scale(1.2)

        Häufigkeiten=VGroup(Tree1RootText,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        
        
        for x in range(len(Knoten)):
            Knoten[x].scale(1.5)
            MengenInKnotenSchnitt[x].align_to(Knoten[x],UP).shift([0,-0.1,0])
            Häufigkeiten[x].move_to(Knoten[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)
        
        self.add(Häufigkeiten)

        self.wait(3)

        #Wahrscheinlichkeiten
        PvonB=Tex(r"$P(B)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child1,UP).shift([0.5,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child2,UP).shift([-0.5,0.2,0])
        PvonABedB=Tex(r"$P_B(A)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP)
        PvonAQuerBedB=Tex(r"$P_B(\bar{A})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP).shift([0.15,0,0])
        PvonABedBQuer=Tex(r"$P_{\bar{B}} (A)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP).shift([-0.15,0,0])
        PvonAQuerBedBQuer=Tex(r"$P_{\bar{B}} (\bar{A})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP)

        self.add(PvonB,PvonBQuer,PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)
        self.wait(3)

        self.remove(PvonB,PvonBQuer,PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)
        
        PvonBBruch=Tex(r"$\frac{|B|}{|\Omega|}$").scale(1.2).next_to(Tree1Child1,UP).shift([0.5,0.2,0])
        PvonBQuerBruch=Tex(r"$\frac{|\bar{B}|}{|\Omega|}$").scale(1.2).next_to(Tree1Child2,UP).shift([-0.5,0.2,0])
        PvonABedBBruch=Tex(r"$\frac{|A\cap B|}{|B|}$").scale(1.2).next_to(Tree1Grandchild1,UP)
        PvonAQuerBedBBruch=Tex(r"$\frac{|\bar{A}\cap B|}{|B|}$").scale(1.2).next_to(Tree1Grandchild2,UP).shift([0.15,0,0])
        PvonABedBQuerBruch=Tex(r"$\frac{|A\cap \bar{B}|}{|\bar{B}|}$").scale(1.2).next_to(Tree1Grandchild3,UP).shift([-0.15,0,0])
        PvonAQuerBedBQuerBruch=Tex(r"$\frac{|\bar{A}\cap \bar{B}|}{|\bar{B}|}$").scale(1.2).next_to(Tree1Grandchild4,UP)

        self.add(PvonBBruch,PvonBQuerBruch,PvonABedBBruch,PvonAQuerBedBBruch,PvonABedBQuerBruch,PvonAQuerBedBQuerBruch)
        self.wait(5)








class Scene2(Scene):
    def construct(self):

        ZielText=Tex(r"Ziel: $P_N(G)$\\\\ berechnen").to_corner(UP+LEFT)
        ZielRahmen=SurroundingRectangle(ZielText)
        self.add(ZielText,ZielRahmen)
        self.wait(3)

        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        
        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLACK, opacity=1)
        Tree1Child2.set_fill(BLACK, opacity=1)
        Tree1Grandchild1.set_fill(BLACK, opacity=1)
        Tree1Grandchild2.set_fill(BLACK, opacity=1)
        Tree1Grandchild3.set_fill(BLACK, opacity=1)
        Tree1Grandchild4.set_fill(BLACK, opacity=1)

        Knoten=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)

        

        p1= [0,2.4,0] #Root
        p2= [-3.8,0.3,0]      #Child1
        p3= [3.8,0.3,0]    #Child2
        p4= [-6,-2,0]   #Grandchild1
        p5= [-1.5,-2,0] #Grandchild2
        p6= [1.5,-2,0]   #Grandchild3
        p7= [6,-2,0] #Grandchild4

        dotp1=Dot(p1,fill_opacity=0)    #Root
        dotp2=Dot(p2,fill_opacity=0)    #Child1
        dotp3=Dot(p3,fill_opacity=0)    #Child2
        dotp4=Dot(p4,fill_opacity=0)    #Grandchild1
        dotp5=Dot(p5,fill_opacity=0)    #Grandchild2
        dotp6=Dot(p6,fill_opacity=0)    #Grandchild3
        dotp7=Dot(p7,fill_opacity=0)    #Grandchild4


        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)

        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1Text = Tex(r"$N$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2Text = Tex(r"$\bar{N}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1Text = Tex(r"$N\cap G$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2Text = Tex(r"$N\cap\bar{G}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3Text = Tex(r"$\bar{N}\cap G$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4Text = Tex(r"$\bar{N}\cap\bar{G}$",font_size=40).set_z_index(2).scale(1.2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)

        #"Updater" Kanten
        Tree1EdgeRootChild1=always_redraw(lambda: Line(dotp1.get_center(),dotp2.get_center()))
        Tree1EdgeRootChild2=always_redraw(lambda: Line(dotp1.get_center(),dotp3.get_center()))
        Tree1EdgeChild1Grandchild1=always_redraw(lambda: Line(dotp2.get_center(),dotp4.get_center()))
        Tree1EdgeChild1Grandchild2=always_redraw(lambda: Line(dotp2.get_center(),dotp5.get_center()))
        Tree1EdgeChild2Grandchild3=always_redraw(lambda: Line(dotp3.get_center(),dotp6.get_center()))
        Tree1EdgeChild2Grandchild4=always_redraw(lambda: Line(dotp3.get_center(),dotp7.get_center()))


        Kanten=VGroup(Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)


        Tree1RootTextBetrag = Tex(r"$100$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$25$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$75$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$5$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$20$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$45$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$30$",font_size=40).set_z_index(2).scale(1.2)

        Häufigkeiten=VGroup(Tree1RootTextBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        
        
        for x in range(len(Knoten)):
            Knoten[x].scale(1.5)
            MengenInKnoten[x].align_to(Knoten[x],UP).shift([0,-0.1,0])
            Häufigkeiten[x].move_to(Knoten[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)
        
        self.add(Tree1Root,Tree1RootText)
        self.wait(3)
        self.add(Tree1Child1,Tree1Child1Text,Tree1EdgeRootChild1)
        self.wait(3)
        self.add(Tree1Child2,Tree1Child2Text,Tree1EdgeRootChild2)
        self.wait(3)
        self.add(Tree1Grandchild1,Tree1Grandchild3,Tree1Grandchild1Text,Tree1Grandchild3Text,Tree1EdgeChild1Grandchild1,Tree1EdgeChild2Grandchild3)
        self.wait(3)
        self.add(Tree1Grandchild2,Tree1Grandchild4,Tree1Grandchild2Text,Tree1Grandchild4Text,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild4)
        self.wait(3)

        Tree1Grandchild1.set_stroke(color=RED)
        Tree1Grandchild1Text.set_color(RED)

        self.wait(3)
        Tree1Grandchild1.set_stroke(color=WHITE)
        Tree1Grandchild1Text.set_color(WHITE)
        Tree1Grandchild2.set_stroke(color=RED)
        Tree1Grandchild2Text.set_color(RED)

        self.wait(3)

        Tree1Grandchild2.set_stroke(color=WHITE)
        Tree1Grandchild2Text.set_color(WHITE)
        Tree1Grandchild3.set_stroke(color=RED)
        Tree1Grandchild3Text.set_color(RED)

        self.wait(3)

        Tree1Grandchild3.set_stroke(color=WHITE)
        Tree1Grandchild3Text.set_color(WHITE)
        Tree1Grandchild4.set_stroke(color=RED)
        Tree1Grandchild4Text.set_color(RED)

        self.wait(3)

        Tree1Grandchild4.set_stroke(color=WHITE)
        Tree1Grandchild4Text.set_color(WHITE)

        self.wait(3)

        self.add(Tree1RootTextBetrag)
        self.wait(3)

        self.add(Tree1Child1TextBetrag)
        self.wait(3)

        self.add(Tree1Child2TextBetrag)
        self.wait(3)

        self.add(Tree1Grandchild1TextBetrag)
        self.wait(3)
        self.add(Tree1Grandchild2TextBetrag)
        self.wait(3)
        self.add(Tree1Grandchild3TextBetrag)
        self.wait(3)
        self.add(Tree1Grandchild4TextBetrag)
        self.wait(3)

        #Wahrscheinlichkeiten
        PvonB=Tex(r"$P(N)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{N})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonABedB=Tex(r"$P_N(G)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP).shift([-0.15,0,0])
        PvonAQuerBedB=Tex(r"$P_N(\bar{G})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonABedBQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonAQuerBedBQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0.15,0,0])

        Wahrscheinlichkeiten=VGroup(PvonB,PvonBQuer,PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)



        self.add(PvonB,PvonBQuer)
        self.wait(3)
        self.add(PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)
        self.wait(3)

        fractionB =VGroup(
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootTextBetrag),
                Tree1RootTextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonB,DOWN+RIGHT)
        
        fractionBQuer =VGroup(
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootTextBetrag),
                Tree1RootTextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonBQuer,DOWN+LEFT)

        fractionAB =VGroup(
                Tree1Grandchild1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child1TextBetrag),
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonABedB,DOWN+RIGHT)

        fractionAQuerB =VGroup(
                Tree1Grandchild2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child1TextBetrag),
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonAQuerBedB,DOWN+LEFT)
        
        fractionABQuer =VGroup(
                Tree1Grandchild3TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child2TextBetrag),
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonABedBQuer,DOWN+RIGHT)

        fractionAQuerBQuer =VGroup(
                Tree1Grandchild4TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child2TextBetrag),
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonAQuerBedBQuer,DOWN+LEFT)
        
        Brüche=VGroup(fractionB,fractionBQuer,fractionAB,fractionAQuerB,fractionABQuer,fractionAQuerBQuer)

        BruchBRechteck=SurroundingRectangle(fractionB)
        BruchBQuerRechteck=SurroundingRectangle(fractionBQuer)
        BruchABRechteck=SurroundingRectangle(fractionAB)
        BruchAQuerBRechteck=SurroundingRectangle(fractionAQuerB)
        BruchABQuerRechteck=SurroundingRectangle(fractionABQuer)
        BruchAQuerBQuerRechteck=SurroundingRectangle(fractionAQuerBQuer)

        BruchRechtecke=VGroup(BruchBRechteck,BruchBQuerRechteck,BruchABRechteck,BruchAQuerBRechteck,BruchABQuerRechteck,BruchAQuerBQuerRechteck)

        RahmenPBvonA=SurroundingRectangle(PvonABedB)
        self.add(RahmenPBvonA)
        self.wait(3)
        self.remove(RahmenPBvonA)
        self.play(FadeIn(BruchABRechteck),
        PvonABedB.animate.next_to(BruchABRechteck,UP)
        )
        Tree1Child1TextBetragCopy=Tree1Child1TextBetrag.copy()
        Tree1Grandchild1TextBetragCopy=Tree1Grandchild1TextBetrag.copy()
        self.add(fractionAB)
        self.play(Tree1Grandchild1TextBetragCopy.animate.move_to(fractionAB[0].get_center()))
        self.play(Tree1Child1TextBetragCopy.animate.move_to(fractionAB[2].get_center()))

        self.wait(3)

        self.remove(ZielRahmen,ZielText)
        self.play(FadeIn(BruchBRechteck,BruchBQuerRechteck,BruchAQuerBRechteck,BruchABQuerRechteck,BruchAQuerBQuerRechteck),
        PvonB.animate.next_to(BruchBRechteck,UP),
        PvonBQuer.animate.next_to(BruchBQuerRechteck,UP),
        PvonAQuerBedB.animate.next_to(BruchAQuerBRechteck,UP),
        PvonABedBQuer.animate.next_to(BruchABQuerRechteck,UP),
        PvonAQuerBedBQuer.animate.next_to(BruchAQuerBQuerRechteck,UP),        
        run_time=2)
        self.wait(5)






        Tree1RootTextBetragCopy=Tree1RootTextBetrag.copy()
        Tree1RootTextBetragCopy2=Tree1RootTextBetrag.copy()
        Tree1Child1TextBetragCopy2=Tree1Child1TextBetrag.copy()
        Tree1Child1TextBetragCopy3=Tree1Child1TextBetrag.copy()
        Tree1Child1TextBetragCopy4=Tree1Child1TextBetrag.copy()

        



        Tree1Child2TextBetragCopy=Tree1Child2TextBetrag.copy()
        Tree1Child2TextBetragCopy2=Tree1Child2TextBetrag.copy()
        Tree1Child2TextBetragCopy3=Tree1Child2TextBetrag.copy()
        Tree1Grandchild2TextBetragCopy=Tree1Grandchild2TextBetrag.copy()
        Tree1Grandchild3TextBetragCopy=Tree1Grandchild3TextBetrag.copy()
        Tree1Grandchild4TextBetragCopy=Tree1Grandchild4TextBetrag.copy()

        
        self.add(fractionB,fractionBQuer,fractionAQuerB,fractionABQuer,fractionAQuerBQuer,
        Tree1Child1TextBetragCopy2,Tree1Child2TextBetragCopy,Tree1Child2TextBetragCopy2,Tree1Grandchild2TextBetragCopy,Tree1Grandchild3TextBetragCopy,Tree1Grandchild4TextBetragCopy)
        self.play(Tree1Grandchild2TextBetragCopy.animate.move_to(fractionAQuerB[0].get_center()),
        Tree1Grandchild3TextBetragCopy.animate.move_to(fractionABQuer[0].get_center()),
        Tree1Grandchild4TextBetragCopy.animate.move_to(fractionAQuerBQuer[0].get_center()),
        Tree1Child1TextBetragCopy3.animate.move_to(fractionB[0].get_center()),
        Tree1Child2TextBetragCopy3.animate.move_to(fractionBQuer[0].get_center()),
        run_time=3.5)

        self.wait(3)

        self.play(Tree1RootTextBetragCopy.animate.move_to(fractionB[2].get_center()),
        Tree1RootTextBetragCopy2.animate.move_to(fractionBQuer[2].get_center()),
        Tree1Child1TextBetragCopy4.animate.move_to(fractionAQuerB[2].get_center()),
        Tree1Child2TextBetragCopy.animate.move_to(fractionABQuer[2].get_center()),
        Tree1Child2TextBetragCopy2.animate.move_to(fractionAQuerBQuer[2].get_center()),

        run_time=3.5)
        self.wait(5)
        PvonBCopy=PvonB.copy()
        PvonBQuerCopy=PvonBQuer.copy()
        PvonABedBCopy=PvonABedB.copy()
        PvonAQuerBedBCopy=PvonAQuerBedB.copy()
        PvonABedBQuerCopy=PvonABedBQuer.copy()
        PvonAQuerBedBQuerCopy=PvonAQuerBedBQuer.copy()
        WahrscheinlichkeitenCopy=VGroup(PvonBCopy,PvonBQuerCopy,PvonABedBCopy,PvonAQuerBedBCopy,PvonABedBQuerCopy,PvonAQuerBedBQuerCopy)

        Wahrscheinlichkeiten.set_color(BLACK).set_z_index(-1)
        TabelleBedN = MobjectTable(
            [[PvonB,PvonBQuer],[PvonABedB,PvonAQuerBedB],[PvonABedBQuer,PvonAQuerBedBQuer]],
            include_outer_lines=True).move_to([-4,0,0])
        
        self.add(WahrscheinlichkeitenCopy)

        HäufigkeitenCopys=VGroup(Tree1Child1TextBetragCopy,Tree1Grandchild1TextBetragCopy,Tree1RootTextBetragCopy,
        Tree1RootTextBetragCopy2,
        Tree1Child1TextBetragCopy2,
        Tree1Child1TextBetragCopy3,
        Tree1Child1TextBetragCopy4,
        Tree1RootTextBetragCopy,
        Tree1RootTextBetragCopy2,
        Tree1Child1TextBetragCopy2,
        Tree1Child1TextBetragCopy3,
        Tree1Child1TextBetragCopy4,
        Tree1Grandchild2TextBetragCopy,
        Tree1Grandchild3TextBetragCopy,
        Tree1Grandchild4TextBetragCopy,
        Tree1Child2TextBetragCopy2,
        Tree1Child2TextBetragCopy3,Tree1Child2TextBetragCopy)
        self.wait(3)


        self.play(FadeOut(Häufigkeiten,MengenInKnoten,Kanten,Knoten,Brüche,BruchRechtecke,HäufigkeitenCopys))
        self.play(PvonBCopy.animate.move_to(TabelleBedN[0][0]),
        PvonBQuerCopy.animate.move_to(TabelleBedN[0][1]),
        PvonABedBCopy.animate.move_to([TabelleBedN[0][0].get_x(),TabelleBedN[6][0].get_y(),0]),
        PvonAQuerBedBCopy.animate.move_to([TabelleBedN[0][1].get_x(),TabelleBedN[6][0].get_y(),0]),
        PvonABedBQuerCopy.animate.move_to([TabelleBedN[0][0].get_x(),TabelleBedN[6][0].get_y()-(TabelleBedN[0][1].get_y()-TabelleBedN[6][0].get_y()),0]),
        PvonAQuerBedBQuerCopy.animate.move_to([TabelleBedN[0][1].get_x(),TabelleBedN[6][0].get_y()-(TabelleBedN[0][1].get_y()-TabelleBedN[6][0].get_y()),0]),
        FadeIn(TabelleBedN),
        run_time=5)
        for i in range(len(TabelleBedN)):
                print(TabelleBedN[i])
        self.wait(3)

        TabelleBedN.add_highlighted_cell((2,1), color=RED).add_highlighted_cell((3,1), color=RED).add_highlighted_cell((2,2), color=RED).add_highlighted_cell((3,2), color=RED)
        TabelleBedN.add_highlighted_cell((1,1), color=BLUE).add_highlighted_cell((1,2), color=BLUE)  
        self.wait(3)

        PvonG=Tex(r"$P(G)$",font_size=40).set_z_index(2).scale(1.2).move_to([-PvonBQuerCopy.get_x(),PvonBCopy.get_y(),0])
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40).set_z_index(2).scale(1.2).move_to([-PvonBQuerCopy.get_x(),PvonABedBCopy.get_y(),0])
        self.add(PvonG)
        self.wait(3)
        self.add(PvonNBedG)
        self.wait(3)

        self.remove(TabelleBedN,WahrscheinlichkeitenCopy,PvonG,PvonNBedG)








        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)

        

        #Knoten Baum 2
        Tree2Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree2Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        
        #Tree1Root.color=RED


       
        
        #Ausgangspositionen
        #Tree1
        p1= [-3.75,2.4,0] #Root
        p2= [-5.3,0.3,0]      #Child1
        p3= [-2.2,0.3,0]    #Child2
        p4= [-6.3,-2,0]   #Grandchild1
        p5= [-4.6,-2,0] #Grandchild2
        p6= [-2.9,-2,0]   #Grandchild3
        p7= [-1.2,-2,0] #Grandchild4

        dotp1=Dot(p1,fill_opacity=0)    #Root
        dotp2=Dot(p2,fill_opacity=0)    #Child1
        dotp3=Dot(p3,fill_opacity=0)    #Child2
        dotp4=Dot(p4,fill_opacity=0)    #Grandchild1
        dotp5=Dot(p5,fill_opacity=0)    #Grandchild2
        dotp6=Dot(p6,fill_opacity=0)    #Grandchild3
        dotp7=Dot(p7,fill_opacity=0)    #Grandchild4


        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4)
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7)

       
        
        #Ausgangspositionen
        #Tree1
        p1= [-3.75,2.4,0] #Root
        p2= [-5.3,0.3,0]      #Child1
        p3= [-2.2,0.3,0]    #Child2
        p4= [-6.3,-2,0]   #Grandchild1
        p5= [-4.6,-2,0] #Grandchild2
        p6= [-2.9,-2,0]   #Grandchild3
        p7= [-1.2,-2,0] #Grandchild4


        #Ausgangspositionen
        #Tree2
        q1= [3.75,2.4,0] #Root
        q2= [2.2,0.3,0]    #Child1
        q3= [5.3,0.3,0]      #Child2
        q4= [1.2,-2,0] #Grandchild1
        q5= [2.9,-2,0]   #Grandchild2
        q6= [4.6,-2,0] #Grandchild3
        q7= [6.3,-2,0]   #Grandchild4

        dotq1=Dot(q1,fill_opacity=0)    #Root
        dotq2=Dot(q2,fill_opacity=0)    #Child1
        dotq3=Dot(q3,fill_opacity=0)    #Child2
        dotq4=Dot(q4,fill_opacity=0)    #Grandchild1
        dotq5=Dot(q5,fill_opacity=0)    #Grandchild2
        dotq6=Dot(q6,fill_opacity=0)    #Grandchild3
        dotq7=Dot(q7,fill_opacity=0)    #Grandchild4

        Tree2Root.move_to(q1)
        Tree2Child1.move_to(q2)
        Tree2Child2.move_to(q3)
        Tree2Grandchild1.move_to(q4)
        Tree2Grandchild2.move_to(q5)
        Tree2Grandchild3.move_to(q6)
        Tree2Grandchild4.move_to(q7)

        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLACK, opacity=1)
        Tree1Child2.set_fill(BLACK, opacity=1)
        Tree1Grandchild1.set_fill(BLACK, opacity=1)
        Tree1Grandchild2.set_fill(BLACK, opacity=1)
        Tree1Grandchild3.set_fill(BLACK, opacity=1)
        Tree1Grandchild4.set_fill(BLACK, opacity=1)

        Tree2Root.set_fill(BLACK, opacity=1)
        Tree2Child1.set_fill(BLACK, opacity=1)
        Tree2Child2.set_fill(BLACK, opacity=1)
        Tree2Grandchild1.set_fill(BLACK, opacity=1)
        Tree2Grandchild2.set_fill(BLACK, opacity=1)
        Tree2Grandchild3.set_fill(BLACK, opacity=1)
        Tree2Grandchild4.set_fill(BLACK, opacity=1)
        
        #Beschriftung Knoten
        #Tree1
        try:
            Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        except:
            path="C:/Users/abioh/Documents/Manim/Test/media/Tex"
            for filename in os.listdir(path):
                tex_file_writing.compile_tex(filename, "pdflatex",".dvi")
        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        
        Tree1Child1Text = Tex(r"$N$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{N}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$N\cap G$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$N\cap\bar{G}$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$\bar{N}\cap G$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{N}\cap\bar{G}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)

        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$G$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{G}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$N\cap G$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$\bar{N}\cap G$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$N\cap\bar{G}$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{N}\cap\bar{G}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)



    




        #Updater Text
        Tree1RootText.add_updater(lambda m: Tree1RootText.move_to(dotp1.get_center()))
        Tree1Child1Text.add_updater(lambda m: Tree1Child1Text.move_to(dotp2.get_center()))   
        Tree1Child2Text.add_updater(lambda m: Tree1Child2Text.move_to(dotp3.get_center())) 
        Tree1Grandchild1Text.add_updater(lambda m: Tree1Grandchild1Text.move_to(dotp4.get_center())) 
        Tree1Grandchild2Text.add_updater(lambda m: Tree1Grandchild2Text.move_to(dotp5.get_center())) 
        Tree1Grandchild3Text.add_updater(lambda m: Tree1Grandchild3Text.move_to(dotp6.get_center())) 
        Tree1Grandchild4Text.add_updater(lambda m: Tree1Grandchild4Text.move_to(dotp7.get_center())) 

        Tree2RootText.add_updater(lambda m: Tree2RootText.move_to(dotq1.get_center()))
        Tree2Child1Text.add_updater(lambda m: Tree2Child1Text.move_to(dotq2.get_center()))   
        Tree2Child2Text.add_updater(lambda m: Tree2Child2Text.move_to(dotq3.get_center())) 
        Tree2Grandchild1Text.add_updater(lambda m: Tree2Grandchild1Text.move_to(dotq4.get_center())) 
        Tree2Grandchild2Text.add_updater(lambda m: Tree2Grandchild2Text.move_to(dotq5.get_center())) 
        Tree2Grandchild3Text.add_updater(lambda m: Tree2Grandchild3Text.move_to(dotq6.get_center())) 
        Tree2Grandchild4Text.add_updater(lambda m: Tree2Grandchild4Text.move_to(dotq7.get_center())) 
    
        #Updater Knoten
        Tree1Root.add_updater(lambda m: Tree1Root.move_to(dotp1.get_center()))            
        Tree1Child1.add_updater(lambda m: Tree1Child1.move_to(dotp2.get_center()))            
        Tree1Child2.add_updater(lambda m: Tree1Child2.move_to(dotp3.get_center()))            
        Tree1Grandchild1.add_updater(lambda m: Tree1Grandchild1.move_to(dotp4.get_center()))            
        Tree1Grandchild2.add_updater(lambda m: Tree1Grandchild2.move_to(dotp5.get_center()))            
        Tree1Grandchild3.add_updater(lambda m: Tree1Grandchild3.move_to(dotp6.get_center()))            
        Tree1Grandchild4.add_updater(lambda m: Tree1Grandchild4.move_to(dotp7.get_center()))      

        Tree2Root.add_updater(lambda m: Tree2Root.move_to(dotq1.get_center()))            
        Tree2Child1.add_updater(lambda m: Tree2Child1.move_to(dotq2.get_center()))            
        Tree2Child2.add_updater(lambda m: Tree2Child2.move_to(dotq3.get_center()))            
        Tree2Grandchild1.add_updater(lambda m: Tree2Grandchild1.move_to(dotq4.get_center()))            
        Tree2Grandchild2.add_updater(lambda m: Tree2Grandchild2.move_to(dotq5.get_center()))            
        Tree2Grandchild3.add_updater(lambda m: Tree2Grandchild3.move_to(dotq6.get_center()))            
        Tree2Grandchild4.add_updater(lambda m: Tree2Grandchild4.move_to(dotq7.get_center()))   

        #"Updater" Kanten
        Tree1EdgeRootChild1=always_redraw(lambda: Line(dotp1.get_center(),dotp2.get_center()))
        Tree1EdgeRootChild2=always_redraw(lambda: Line(dotp1.get_center(),dotp3.get_center()))
        Tree1EdgeChild1Grandchild1=always_redraw(lambda: Line(dotp2.get_center(),dotp4.get_center()))
        Tree1EdgeChild1Grandchild2=always_redraw(lambda: Line(dotp2.get_center(),dotp5.get_center()))
        Tree1EdgeChild2Grandchild3=always_redraw(lambda: Line(dotp3.get_center(),dotp6.get_center()))
        Tree1EdgeChild2Grandchild4=always_redraw(lambda: Line(dotp3.get_center(),dotp7.get_center()))

        Tree2EdgeRootChild1=always_redraw(lambda: Line(dotq1.get_center(),dotq2.get_center()))
        Tree2EdgeRootChild2=always_redraw(lambda: Line(dotq1.get_center(),dotq3.get_center()))
        Tree2EdgeChild1Grandchild1=always_redraw(lambda: Line(dotq2.get_center(),dotq4.get_center()))
        Tree2EdgeChild1Grandchild2=always_redraw(lambda: Line(dotq2.get_center(),dotq5.get_center()))
        Tree2EdgeChild2Grandchild3=always_redraw(lambda: Line(dotq3.get_center(),dotq6.get_center()))
        Tree2EdgeChild2Grandchild4=always_redraw(lambda: Line(dotq3.get_center(),dotq7.get_center()))
        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree1Child1,UP).shift([-0.2,0,0])
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree1Child2,UP).shift([0.2,0,0])
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP).shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree2Child1,UP).shift([0.2,0,0])
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree2Child2,UP).shift([-0.2,0,0])
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild1,UP).shift([-0.4,0,0])
        PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        
        #Zeichnet Baumdiagramm1 direkt
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        #self.add(WahrscheinlichkeitenBaum1)
        self.wait(3)
        self.add(PvonN,PvonNQuer)
        self.wait(3)
        self.add(PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)
        self.wait(3)
        #Zeichnet Baumdiagramm2 direkt
        self.add(Tree2Root,Tree2RootText)
        self.wait(3)
        self.add(Tree2Child1,Tree2Child2,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2Child1Text,Tree2Child2Text)
        self.wait(3)
        self.add(Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
        self.wait(3)

        self.add(PvonG,PvonGQuer)

        self.wait(3)

        self.add(PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        self.wait(5)

        self.remove(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        self.remove(Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
        
        #self.add(TabelleBedN)
        

        WahrscheinlichkeitenBaum2Copy=WahrscheinlichkeitenBaum2.copy().set_color(WHITE)

        WahrscheinlichkeitenBaum2.set_color(BLACK).set_z_index(-1)
        TabelleBedG = MobjectTable(
            [[PvonG,PvonGQuer],[PvonNBedG,PvonNQuerBedG],[PvonNBedGQuer,PvonNQuerBedGQuer]],
            include_outer_lines=True).move_to([4,0,0])
        
        WahrscheinlichkeitenBaum1Copy=WahrscheinlichkeitenBaum1.copy().set_color(WHITE)
        WahrscheinlichkeitenBaum1.set_color(BLACK).set_z_index(-1)
        self.add(WahrscheinlichkeitenBaum1Copy)
        TabelleBedN = MobjectTable(
            [[PvonN,PvonNQuer],[PvonGBedN,PvonGQuerBedN],[PvonGBedNQuer,PvonGQuerBedNQuer]],
            include_outer_lines=True).move_to([-4,0,0])

        #self.play(FadeOut(Häufigkeiten,MengenInKnoten,Kanten,Knoten,Brüche,BruchRechtecke,HäufigkeitenCopys))
        self.play(WahrscheinlichkeitenBaum2Copy[0].animate.move_to(TabelleBedG[0][0]),
        WahrscheinlichkeitenBaum2Copy[1].animate.move_to(TabelleBedG[0][1]),
        WahrscheinlichkeitenBaum2Copy[2].animate.move_to([TabelleBedG[0][0].get_x(),TabelleBedG[6][0].get_y(),0]),
        WahrscheinlichkeitenBaum2Copy[3].animate.move_to([TabelleBedG[0][1].get_x(),TabelleBedG[6][0].get_y(),0]),
        WahrscheinlichkeitenBaum2Copy[4].animate.move_to([TabelleBedG[0][0].get_x(),TabelleBedG[6][0].get_y()-(TabelleBedG[0][1].get_y()-TabelleBedG[6][0].get_y()),0]),
        WahrscheinlichkeitenBaum2Copy[5].animate.move_to([TabelleBedG[0][1].get_x(),TabelleBedG[6][0].get_y()-(TabelleBedG[0][1].get_y()-TabelleBedG[6][0].get_y()),0]),
        FadeIn(TabelleBedN,TabelleBedG),
        WahrscheinlichkeitenBaum1Copy[0].animate.move_to(TabelleBedN[0][0]),
        WahrscheinlichkeitenBaum1Copy[1].animate.move_to(TabelleBedN[0][1]),
        WahrscheinlichkeitenBaum1Copy[2].animate.move_to([TabelleBedN[0][0].get_x(),TabelleBedN[6][0].get_y(),0]),
        WahrscheinlichkeitenBaum1Copy[3].animate.move_to([TabelleBedN[0][1].get_x(),TabelleBedN[6][0].get_y(),0]),
        WahrscheinlichkeitenBaum1Copy[4].animate.move_to([TabelleBedN[0][0].get_x(),TabelleBedN[6][0].get_y()-(TabelleBedN[0][1].get_y()-TabelleBedN[6][0].get_y()),0]),
        WahrscheinlichkeitenBaum1Copy[5].animate.move_to([TabelleBedN[0][1].get_x(),TabelleBedN[6][0].get_y()-(TabelleBedN[0][1].get_y()-TabelleBedN[6][0].get_y()),0]),
        run_time=5)

        self.wait(3)
        TabelleBedN.add_highlighted_cell((1,1), color=BLUE).add_highlighted_cell((1,2), color=BLUE)
        TabelleBedG.add_highlighted_cell((1,1), color=BLUE).add_highlighted_cell((1,2), color=BLUE)

        self.wait(3)
        TabelleBedG.add_highlighted_cell((2,1), color=RED).add_highlighted_cell((3,1), color=RED).add_highlighted_cell((2,2), color=RED).add_highlighted_cell((3,2), color=RED)
        TabelleBedN.add_highlighted_cell((2,1), color=RED).add_highlighted_cell((3,1), color=RED).add_highlighted_cell((2,2), color=RED).add_highlighted_cell((3,2), color=RED)

        self.wait(3)
        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40).set_z_index(2).scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40).set_z_index(2).scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        RahmenSchnittwahrscheinlichkeiten=SurroundingRectangle(Schnittwahrscheinlichkeiten,color=WHITE).set_fill(color=GREEN,opacity=1)
        self.add(Schnittwahrscheinlichkeiten,RahmenSchnittwahrscheinlichkeiten)
        
        
        self.wait(3)
        #self.remove(TabelleBedG,TabelleBedN,WahrscheinlichkeitenBaum1Copy,WahrscheinlichkeitenBaum2,WahrscheinlichkeitenBaum2Copy)
        self.clear()
        self.add(Schnittwahrscheinlichkeiten)
        SchnittwahrscheinlichkeitenCopy=Schnittwahrscheinlichkeiten.copy()

        self.play(FadeIn(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text),
        Schnittwahrscheinlichkeiten[0].animate.next_to(Tree1Grandchild1,DOWN).scale(0.75),
        Schnittwahrscheinlichkeiten[1].animate.next_to(Tree1Grandchild2,DOWN).scale(0.75),
        Schnittwahrscheinlichkeiten[2].animate.next_to(Tree1Grandchild3,DOWN).scale(0.75),
        Schnittwahrscheinlichkeiten[3].animate.next_to(Tree1Grandchild4,DOWN).scale(0.75),
        SchnittwahrscheinlichkeitenCopy[0].animate.next_to(Tree2Grandchild1,DOWN).scale(0.75),
        SchnittwahrscheinlichkeitenCopy[2].animate.next_to(Tree2Grandchild2,DOWN).scale(0.75),
        SchnittwahrscheinlichkeitenCopy[1].animate.next_to(Tree2Grandchild3,DOWN).scale(0.75),
        SchnittwahrscheinlichkeitenCopy[3].animate.next_to(Tree2Grandchild4,DOWN).scale(0.75),
        run_time=2.5)
        self.wait(3)

        Tree1Root.set_stroke(color=RED)
        Tree1Child1.set_stroke(color=RED)
        Tree1Grandchild1.set_stroke(color=RED)
        Tree1EdgeChild1Grandchild1.set_color(RED)
        Tree1EdgeRootChild1.set_color(RED)
        Schnittwahrscheinlichkeiten[0].set_color(RED)

        Tree2Root.set_stroke(color=RED)
        Tree2Child1.set_stroke(color=RED)
        Tree2Grandchild1.set_stroke(color=RED)
        Tree2EdgeChild1Grandchild1.set_color(RED)
        Tree2EdgeRootChild1.set_color(RED)
        SchnittwahrscheinlichkeitenCopy[0].set_color(RED)
        self.wait(3)

        Tree1Root.set_stroke(color=WHITE)
        Tree1Child1.set_stroke(color=WHITE)
        Tree1Grandchild1.set_stroke(color=WHITE)
        Tree1EdgeChild1Grandchild1.set_color(WHITE)
        Tree1EdgeRootChild1.set_color(WHITE)
        Schnittwahrscheinlichkeiten[0].set_color(WHITE)

        Tree2Root.set_stroke(color=WHITE)
        Tree2Child1.set_stroke(color=WHITE)
        Tree2Grandchild1.set_stroke(color=WHITE)
        Tree2EdgeChild1Grandchild1.set_color(WHITE)
        Tree2EdgeRootChild1.set_color(WHITE)
        SchnittwahrscheinlichkeitenCopy[0].set_color(WHITE)


        Tree1Root.set_stroke(color=RED)
        Tree1Child1.set_stroke(color=RED)
        Tree1Grandchild2.set_stroke(color=RED)
        Tree1EdgeChild1Grandchild2.set_color(RED)
        Tree1EdgeRootChild1.set_color(RED)
        Schnittwahrscheinlichkeiten[1].set_color(RED)

        Tree2Root.set_stroke(color=RED)
        Tree2Child2.set_stroke(color=RED)
        Tree2Grandchild3.set_stroke(color=RED)
        Tree2EdgeChild2Grandchild3.set_color(RED)
        Tree2EdgeRootChild2.set_color(RED)
        SchnittwahrscheinlichkeitenCopy[1].set_color(RED)

        self.wait(3)
        Tree1Root.set_stroke(color=WHITE)
        Tree1Child1.set_stroke(color=WHITE)
        Tree1Grandchild2.set_stroke(color=WHITE)
        Tree1EdgeChild1Grandchild2.set_color(WHITE)
        Tree1EdgeRootChild1.set_color(WHITE)
        Schnittwahrscheinlichkeiten[1].set_color(WHITE)

        Tree2Root.set_stroke(color=WHITE)
        Tree2Child2.set_stroke(color=WHITE)
        Tree2Grandchild3.set_stroke(color=WHITE)
        Tree2EdgeChild2Grandchild3.set_color(WHITE)
        Tree2EdgeRootChild2.set_color(WHITE)
        SchnittwahrscheinlichkeitenCopy[1].set_color(WHITE)

        Tree1Root.set_stroke(color=RED)
        Tree1Child2.set_stroke(color=RED)
        Tree1Grandchild3.set_stroke(color=RED)
        Tree1EdgeChild2Grandchild3.set_color(RED)
        Tree1EdgeRootChild2.set_color(RED)
        Schnittwahrscheinlichkeiten[2].set_color(RED)

        Tree2Root.set_stroke(color=RED)
        Tree2Child1.set_stroke(color=RED)
        Tree2Grandchild2.set_stroke(color=RED)
        Tree2EdgeChild1Grandchild2.set_color(RED)
        Tree2EdgeRootChild1.set_color(RED)
        SchnittwahrscheinlichkeitenCopy[2].set_color(RED)

        self.wait(3)

        Tree1Root.set_stroke(color=WHITE)
        Tree1Child2.set_stroke(color=WHITE)
        Tree1Grandchild3.set_stroke(color=WHITE)
        Tree1EdgeChild2Grandchild3.set_color(WHITE)
        Tree1EdgeRootChild2.set_color(WHITE)
        Schnittwahrscheinlichkeiten[2].set_color(WHITE)

        Tree2Root.set_stroke(color=WHITE)
        Tree2Child1.set_stroke(color=WHITE)
        Tree2Grandchild2.set_stroke(color=WHITE)
        Tree2EdgeChild1Grandchild2.set_color(WHITE)
        Tree2EdgeRootChild1.set_color(WHITE)
        SchnittwahrscheinlichkeitenCopy[2].set_color(WHITE)


        Tree1Root.set_stroke(color=RED)
        Tree1Child2.set_stroke(color=RED)
        Tree1Grandchild4.set_stroke(color=RED)
        Tree1EdgeChild2Grandchild4.set_color(RED)
        Tree1EdgeRootChild2.set_color(RED)
        Schnittwahrscheinlichkeiten[3].set_color(RED)

        Tree2Root.set_stroke(color=RED)
        Tree2Child2.set_stroke(color=RED)
        Tree2Grandchild4.set_stroke(color=RED)
        Tree2EdgeChild2Grandchild4.set_color(RED)
        Tree2EdgeRootChild2.set_color(RED)
        SchnittwahrscheinlichkeitenCopy[3].set_color(RED)


        self.wait(3)
        self.clear()
        Überblick=Text("Überblick: Alle Wahrscheinlichkeiten").to_edge(UP)
        ul=Underline(Überblick)
        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40).set_z_index(2).scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40).set_z_index(2).scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        self.add(Überblick,ul,TabelleBedG,TabelleBedN,WahrscheinlichkeitenBaum1Copy,WahrscheinlichkeitenBaum2Copy,Schnittwahrscheinlichkeiten,RahmenSchnittwahrscheinlichkeiten)
        self.wait(5)






        





class Scene3(Scene):
    def construct(self):
        Tree1Root=Square(color='#FFFFFF', side_length=3).set_z_index(1)
        Tree1Child1=Rectangle(color='#FFFFFF', height=1.75, width=3).set_z_index(1)
        Tree1Child2=Rectangle(color='#FFFFFF', height=1.25, width=3).set_z_index(1)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=1.75, width=1.8).set_z_index(1)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=1.75, width=1.2).set_z_index(1)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=1.25, width=1.4).set_z_index(1)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=1.25, width=1.6).set_z_index(1)
        
        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLUE, opacity=1).set_stroke(opacity=0)
        Tree1Child2.set_fill(RED, opacity=1).set_stroke(opacity=0)
        Tree1Grandchild1.set_fill(GREEN, opacity=1).set_stroke(opacity=0)
        Tree1Grandchild2.set_fill(YELLOW, opacity=1).set_stroke(opacity=0)
        Tree1Grandchild3.set_fill(PURPLE, opacity=1).set_stroke(opacity=0)
        Tree1Grandchild4.set_fill(ORANGE, opacity=1).set_stroke(opacity=0)

        p1= [0,2.4,0] #Root
        p2= [-3.8,0.3,0]      #Child1
        p3= [3.8,0.3,0]    #Child2
        p4= [-6.1,-2,0]   #Grandchild1
        p5= [-1.5,-2,0] #Grandchild2
        p6= [1.5,-2,0]   #Grandchild3
        p7= [6.1,-2,0] #Grandchild4

        dotp1=Dot(p1,fill_opacity=0)    #Root
        dotp2=Dot(p2,fill_opacity=0)    #Child1
        dotp3=Dot(p3,fill_opacity=0)    #Child2
        dotp4=Dot(p4,fill_opacity=0)    #Grandchild1
        dotp5=Dot(p5,fill_opacity=0)    #Grandchild2
        dotp6=Dot(p6,fill_opacity=0)    #Grandchild3
        dotp7=Dot(p7,fill_opacity=0)    #Grandchild4


        Tree1Root.move_to(p1)
        Tree1Child1.align_to(Tree1Root,UP)
        Tree1Child2.align_to(Tree1Root,DOWN)
        Tree1Child1Copy=Tree1Child1.copy()
        Tree1Child2Copy=Tree1Child2.copy()
        #Tree1Child1.move_to(p2)
        #Tree1Child2.move_to(p3)
        #Tree1Grandchild1.move_to(p4)
        #Tree1Grandchild2.move_to(p5)
        #Tree1Grandchild3.move_to(p6)
        #Tree1Grandchild4.move_to(p7)

        Knoten=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)

        Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2).scale(1.2).move_to(p1)
        Tree1Child1Text = always_redraw(lambda:Tex(r"$B$",font_size=40).set_z_index(2).scale(1.2).move_to(Tree1Child1.get_center()))
        Tree1Child2Text = always_redraw(lambda:Tex(r"$\bar{B}$",font_size=40).set_z_index(2).scale(1.2).move_to(Tree1Child2.get_center()))
        Tree1Grandchild1Text = Tex(r"${{A}}\cap {{B}}$",font_size=40).set_z_index(2).scale(1.2).move_to([Tree1Grandchild1.get_x(),-3.3,0])
        Tree1Grandchild2Text = Tex(r"$\bar{{{A}}}\cap {{B}}$",font_size=40).set_z_index(2).scale(1.2).move_to([Tree1Grandchild2.get_x(),-3.3,0])
        Tree1Grandchild3Text = Tex(r"${{A}}\cap \bar{{{B}}}$",font_size=40).set_z_index(2).scale(1.2).move_to([Tree1Grandchild3.get_x(),-3.3,0])
        Tree1Grandchild4Text = Tex(r"$\bar{{{A}}}\cap\bar{{{B}}}$",font_size=40).set_z_index(2).scale(1.2).move_to([Tree1Grandchild4.get_x(),-3.3,0])

        #"Updater" Kanten
        Tree1EdgeRootChild1=always_redraw(lambda: Line(Tree1Root.get_center(),Tree1Child1.get_center()))
        Tree1EdgeRootChild2=always_redraw(lambda: Line(Tree1Root.get_center(),Tree1Child2.get_center()))
        Tree1EdgeChild1Grandchild1=always_redraw(lambda: Line(Tree1Child1.get_center(),Tree1Grandchild1.get_center()))
        Tree1EdgeChild1Grandchild2=always_redraw(lambda: Line(Tree1Child1.get_center(),Tree1Grandchild2.get_center()))
        Tree1EdgeChild2Grandchild3=always_redraw(lambda: Line(Tree1Child2.get_center(),Tree1Grandchild3.get_center()))
        Tree1EdgeChild2Grandchild4=always_redraw(lambda: Line(Tree1Child2.get_center(),Tree1Grandchild4.get_center()))

        self.add(Tree1Root,Tree1RootText)
        self.wait(3)


        self.remove(Tree1RootText)
        self.add(Tree1Child1,Tree1Child2,Tree1Child1Copy,Tree1Child2Copy,Tree1Child1Text,Tree1Child2Text)
        self.wait(3)


        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.play(Tree1Child1.animate.move_to(p2),Tree1Child2.animate.move_to(p3),FadeIn(Tree1RootText),run_time=2)
        self.wait(3)
        Tree1Grandchild1.align_to(Tree1Child1,LEFT+UP)
        Tree1Grandchild2.align_to(Tree1Child1,RIGHT+UP)
        Tree1Grandchild1Text.next_to(Tree1Grandchild1,DOWN).shift([-0.1,0,0])
        Tree1Grandchild2Text.next_to(Tree1Grandchild1Text,RIGHT)

        Tree1Grandchild3.align_to(Tree1Child2,LEFT+UP)
        Tree1Grandchild4.align_to(Tree1Child2,RIGHT+UP)
        Tree1Grandchild3Text.next_to(Tree1Grandchild3,DOWN).shift([-0.1,0,0])
        Tree1Grandchild4Text.next_to(Tree1Grandchild3Text,RIGHT)

        self.add(Tree1Grandchild1,Tree1Grandchild1Text)
        self.add(Tree1Grandchild2,Tree1Grandchild2Text)

        self.wait(3)


        
        self.add(Tree1Grandchild4,Tree1Grandchild4Text)
        self.add(Tree1Grandchild3,Tree1Grandchild3Text)

        self.wait(3)
        
        Tree1Grandchild1Copy=Tree1Grandchild1.copy()
        Tree1Grandchild2Copy=Tree1Grandchild2.copy()  
        Tree1Grandchild3Copy=Tree1Grandchild3.copy()
        Tree1Grandchild4Copy=Tree1Grandchild4.copy()
        self.add(Tree1Grandchild1Copy,Tree1Grandchild2Copy,Tree1Grandchild3Copy,Tree1Grandchild4Copy,
        Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        self.play(Tree1Grandchild1.animate.move_to(p4),
        Tree1Grandchild2.animate.move_to(p5),
        Tree1Grandchild3.animate.move_to(p6),
        Tree1Grandchild4.animate.move_to(p7),
        Tree1Grandchild1Text.animate.move_to([p4[0],-3.3,0]),
        Tree1Grandchild2Text.animate.move_to([p5[0],-3.3,0]),
        Tree1Grandchild3Text.animate.move_to([p6[0],-3.3,0]),
        Tree1Grandchild4Text.animate.move_to([p7[0],-3.3,0]),
        run_time=3
        )
        self.wait(3)

        CircleB=Circle(0.3,PURE_RED,z_index=2).move_to(Tree1Child1.get_center())
        CircleBQuer=Circle(0.3,PURE_RED,z_index=2).move_to(Tree1Child2.get_center())
        
        self.add(CircleB,CircleBQuer)
        self.wait(3)

        RechteckAandB=Rectangle(PURE_GREEN,height=0.6,width=0.5,z_index=2).align_to(Tree1Grandchild1Text,LEFT+DOWN).shift([-0.05,-0.05,0])
        
        RechteckAandBQuer=Rectangle(PURE_GREEN,height=0.6,width=0.5,z_index=2).align_to(Tree1Grandchild2Text,LEFT+DOWN).shift([-0.05,-0.05,0])
        RechteckAQuerandBQuer=Rectangle(PURE_GREEN,height=0.6,width=0.5,z_index=2).align_to(Tree1Grandchild3Text,LEFT+DOWN).shift([-0.05,-0.05,0])
        RechteckAQuerandB=Rectangle(PURE_GREEN,height=0.6,width=0.5,z_index=2).align_to(Tree1Grandchild4Text,LEFT+DOWN).shift([-0.05,-0.05,0])
        self.add(RechteckAandB,RechteckAandBQuer,RechteckAQuerandBQuer,RechteckAQuerandB)
        
        self.wait(3)

        CircleBCopy=CircleB.copy().align_to(Tree1Grandchild1Text,RIGHT+DOWN).shift([0.12,-0.12,0])
        CircleBCopy2=CircleB.copy().align_to(Tree1Grandchild2Text,RIGHT+DOWN).shift([0.12,-0.12,0])

        CircleBQuerCopy=CircleBQuer.copy().align_to(Tree1Grandchild3Text,RIGHT+DOWN).shift([0.12,-0.12,0])
        CircleBQuerCopy2=CircleBQuer.copy().align_to(Tree1Grandchild4Text,RIGHT+DOWN).shift([0.12,-0.12,0])

        self.add(CircleBCopy,CircleBCopy2,CircleBQuerCopy,CircleBQuerCopy2)
        self.wait(5)











        self.clear()

        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        
        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLACK, opacity=1)
        Tree1Child2.set_fill(BLACK, opacity=1)
        Tree1Grandchild1.set_fill(BLACK, opacity=1)
        Tree1Grandchild2.set_fill(BLACK, opacity=1)
        Tree1Grandchild3.set_fill(BLACK, opacity=1)
        Tree1Grandchild4.set_fill(BLACK, opacity=1)

        Knoten=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)

        Tree1Root.move_to(p1)
        Tree1Child1.move_to(p2)
        Tree1Child2.move_to(p3)
        Tree1Grandchild1.move_to(p4).shift([0.2,0,0])
        Tree1Grandchild2.move_to(p5)
        Tree1Grandchild3.move_to(p6)
        Tree1Grandchild4.move_to(p7).shift([-0.2,0,0])
        Tree1Grandchild1Text.move_to(p4).shift([0.2,0,0])
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7).shift([-0.2,0,0])

        self.remove(Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)
        
        Tree1EdgeRootChild1=Line(Tree1Root.get_center(),Tree1Child1.get_center())
        Tree1EdgeRootChild2=Line(Tree1Root.get_center(),Tree1Child2.get_center())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1.get_center(),Tree1Grandchild1.get_center())     
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1.get_center(),Tree1Grandchild2.get_center())
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2.get_center(),Tree1Grandchild3.get_center())
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2.get_center(),Tree1Grandchild4.get_center())
        
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        Tree1Child1Text = Tex(r"$B$",font_size=40).set_z_index(2).scale(1.2).move_to(Tree1Child1.get_center())
        Tree1Child2Text = Tex(r"$\bar{B}$",font_size=40).set_z_index(2).scale(1.2).move_to(Tree1Child2.get_center())

        Tree1RootTextBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{B}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|A\cap B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|\bar{A}\cap B|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|A\cap \bar{B}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{A}\cap\bar{B}|$",font_size=40).set_z_index(2).scale(1.2)

        Häufigkeiten=VGroup(Tree1RootTextBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        
        MengenInKnoten=VGroup(Tree1RootText,
        Tree1Child1Text,
        Tree1Child2Text,
        Tree1Grandchild1Text,
        Tree1Grandchild2Text,
        Tree1Grandchild3Text,
        Tree1Grandchild4Text)
        for x in range(len(Knoten)):
            Knoten[x].scale(1.5)
            MengenInKnoten[x].align_to(Knoten[x],UP).shift([0,-0.1,0])
            Häufigkeiten[x].move_to(Knoten[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        self.add(Tree1Root,Tree1RootText)
        self.add(Tree1Child1,Tree1Child2,Tree1Child1Text,Tree1Child2Text,Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4)

        self.wait(3)

        self.add(Häufigkeiten)
        self.wait(3)

        #Wahrscheinlichkeiten
        PvonB=Tex(r"$P(B)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonABedB=Tex(r"$P_B(A)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP).shift([-0.15,0,0])
        PvonAQuerBedB=Tex(r"$P_B(\bar{A})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonABedBQuer=Tex(r"$P_{\bar{B}} (A)$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonAQuerBedBQuer=Tex(r"$P_{\bar{B}} (\bar{A})$",font_size=40).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0.15,0,0])

        PvonBRechteck=SurroundingRectangle(PvonB)
        PvonBQuerRechteck=SurroundingRectangle(PvonBQuer)
        PvonABedBRechteck=SurroundingRectangle(PvonABedB)
        PvonAQuerBedBRechteck=SurroundingRectangle(PvonAQuerBedB)
        PvonABedBQuerRechteck=SurroundingRectangle(PvonABedBQuer)
        PvonAQuerBedBQuerRechteck=SurroundingRectangle(PvonAQuerBedBQuer)

        #self.add(PvonB,PvonBQuer,PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)
        self.add(PvonBRechteck,PvonBQuerRechteck,PvonABedBRechteck,PvonAQuerBedBRechteck,PvonABedBQuerRechteck,PvonAQuerBedBQuerRechteck)
        self.wait(3)

        self.remove(PvonBRechteck,PvonBQuerRechteck)
        self.add(PvonB,PvonBQuer)

        self.wait(3)

        BedingteWahrscheinlichkeiten=VGroup(PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer).set_color(PURE_RED)
        #BedingteWahrscheinlichkeitenRechteck=SurroundingRectangle(BedingteWahrscheinlichkeiten,PURE_RED)
        self.remove(PvonABedBRechteck,PvonAQuerBedBRechteck,PvonABedBQuerRechteck,PvonAQuerBedBQuerRechteck)
        self.add(PvonABedB,PvonAQuerBedB,PvonABedBQuer,PvonAQuerBedBQuer)

        self.wait(3)
        BedingteWahrscheinlichkeiten.set_color(WHITE)
        Tree1Grandchild1.set_stroke(color=RED)
        Tree1EdgeChild1Grandchild1.set_color(RED)
        Tree1Grandchild1Text.set_color(RED)
        Tree1Grandchild1TextBetrag.set_color(RED)


        self.remove(PvonBRechteck,PvonBQuerRechteck,PvonABedBRechteck,PvonAQuerBedBRechteck,PvonABedBQuerRechteck,PvonAQuerBedBQuerRechteck)

        self.wait(3)

        Tree1Child1.set_stroke(color=GREEN)
        Tree1Child1Text.set_color(GREEN)
        Tree1Child1TextBetrag.set_color(GREEN)

        self.wait(3)

        Tree1Child1TextBetragCopy=Tree1Child1TextBetrag.copy()
        Tree1Grandchild1TextBetragCopy=Tree1Grandchild1TextBetrag.copy()
        
        fraction =VGroup(
                Tree1Grandchild1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Grandchild1TextBetrag),
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonABedB,DOWN+RIGHT)

        BruchABRechteck=SurroundingRectangle(fraction)
        self.play(FadeIn(BruchABRechteck),PvonABedB.animate.next_to(BruchABRechteck,UP))
        self.wait(3)
        self.add(fraction,Tree1Child1TextBetragCopy,Tree1Grandchild1TextBetragCopy)
        self.play(Tree1Grandchild1TextBetragCopy.animate.move_to(fraction[0].get_center()),run_time=2.5)
        self.wait(3)
        self.play(Tree1Child1TextBetragCopy.animate.move_to(fraction[2].get_center()),run_time=2.5)

        self.wait(3)


        Tree1Grandchild2.set_stroke(color=RED)
        Tree1EdgeChild1Grandchild2.set_color(RED)
        Tree1Grandchild2Text.set_color(RED)
        Tree1Grandchild2TextBetrag.set_color(RED)

        Tree1Grandchild3.set_stroke(color=RED)
        Tree1EdgeChild2Grandchild3.set_color(RED)
        Tree1Grandchild3Text.set_color(RED)
        Tree1Grandchild3TextBetrag.set_color(RED)

        Tree1Grandchild4.set_stroke(color=RED)
        Tree1EdgeChild2Grandchild4.set_color(RED)
        Tree1Grandchild4Text.set_color(RED)
        Tree1Grandchild4TextBetrag.set_color(RED)

        Tree1Child2.set_stroke(color=GREEN)
        Tree1EdgeRootChild2.set_color(GREEN)
        Tree1EdgeRootChild1.set_color(GREEN)
        Tree1Child2Text.set_color(GREEN)
        Tree1Child2TextBetrag.set_color(GREEN)

        Tree1Root.set_stroke(color=BLUE)
        Tree1RootText.set_color(BLUE)
        Tree1RootTextBetrag.set_color(BLUE)




        fractionB =VGroup(
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child1TextBetrag),
                Tree1RootTextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonB,DOWN+RIGHT)
        
        fractionBQuer =VGroup(
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Child2TextBetrag),
                Tree1RootTextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonBQuer,DOWN+LEFT)

        fractionAQuerB =VGroup(
                Tree1Grandchild2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Grandchild2TextBetrag),
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonAQuerBedB,DOWN+LEFT)
        
        fractionABQuer =VGroup(
                Tree1Grandchild3TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Grandchild3TextBetrag),
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonABedBQuer,DOWN+RIGHT)

        fractionAQuerBQuer =VGroup(
                Tree1Grandchild4TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1Grandchild4TextBetrag),
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN).align_to(PvonAQuerBedBQuer,DOWN+LEFT)
        

        BruchBRechteck=SurroundingRectangle(fractionB)
        BruchBQuerRechteck=SurroundingRectangle(fractionBQuer)
        BruchAQuerBRechteck=SurroundingRectangle(fractionAQuerB)
        BruchABQuerRechteck=SurroundingRectangle(fractionABQuer)
        BruchAQuerBQuerRechteck=SurroundingRectangle(fractionAQuerBQuer)

        self.play(FadeIn(BruchBRechteck,BruchBQuerRechteck,BruchAQuerBRechteck,BruchABQuerRechteck,BruchAQuerBQuerRechteck),
        PvonB.animate.next_to(BruchBRechteck,UP),
        PvonBQuer.animate.next_to(BruchBQuerRechteck,UP),
        PvonAQuerBedB.animate.next_to(BruchAQuerBRechteck,UP),
        PvonABedBQuer.animate.next_to(BruchABQuerRechteck,UP),
        PvonAQuerBedBQuer.animate.next_to(BruchAQuerBQuerRechteck,UP),        
        run_time=2)
        self.wait(3)





        Tree1RootTextBetragCopy=Tree1RootTextBetrag.copy()
        Tree1RootTextBetragCopy2=Tree1RootTextBetrag.copy()
        Tree1Child1TextBetragCopy2=Tree1Child1TextBetrag.copy()
        Tree1Child1TextBetragCopy3=Tree1Child1TextBetrag.copy()
        Tree1Child1TextBetragCopy4=Tree1Child1TextBetrag.copy()

        



        Tree1Child2TextBetragCopy=Tree1Child2TextBetrag.copy()
        Tree1Child2TextBetragCopy2=Tree1Child2TextBetrag.copy()
        Tree1Child2TextBetragCopy3=Tree1Child2TextBetrag.copy()
        Tree1Grandchild2TextBetragCopy=Tree1Grandchild2TextBetrag.copy()
        Tree1Grandchild3TextBetragCopy=Tree1Grandchild3TextBetrag.copy()
        Tree1Grandchild4TextBetragCopy=Tree1Grandchild4TextBetrag.copy()


        self.add(fractionB,fractionBQuer,fractionAQuerB,fractionABQuer,fractionAQuerBQuer,
        Tree1Child1TextBetragCopy2,Tree1Child2TextBetragCopy,Tree1Child2TextBetragCopy2,Tree1Grandchild2TextBetragCopy,Tree1Grandchild3TextBetragCopy,Tree1Grandchild4TextBetragCopy)
        self.play(Tree1Grandchild2TextBetragCopy.animate.move_to(fractionAQuerB[0].get_center()),
        Tree1Grandchild3TextBetragCopy.animate.move_to(fractionABQuer[0].get_center()),
        Tree1Grandchild4TextBetragCopy.animate.move_to(fractionAQuerBQuer[0].get_center()),
        Tree1Child1TextBetragCopy3.animate.move_to(fractionB[0].get_center()),
        Tree1Child2TextBetragCopy3.animate.move_to(fractionBQuer[0].get_center()),
        run_time=3.5)
        self.play(Tree1RootTextBetragCopy.animate.move_to(fractionB[2].get_center()),
        Tree1RootTextBetragCopy2.animate.move_to(fractionBQuer[2].get_center()),
        Tree1Child1TextBetragCopy4.animate.move_to(fractionAQuerB[2].get_center()),
        Tree1Child2TextBetragCopy.animate.move_to(fractionABQuer[2].get_center()),
        Tree1Child2TextBetragCopy2.animate.move_to(fractionAQuerBQuer[2].get_center()),

        run_time=3.5)

        self.wait(5)

        

        





class Scene4(Scene):
    def construct(self):
        Überschrift=Text("Vierfeldertafeln...").to_edge(UP)
        ul=Underline(Überschrift)
        EreignisA=Tex(r"$A$")
        EreignisAQuer=Tex(r"$\bar{A}$")
        EreignisB=Tex(r"$B$")
        EreignisBQuer=Tex(r"$\bar{B}$")

        

        #Wahrscheinlichkeiten
        PvonA=Tex(r"$P(A)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonAQuer=Tex(r"$P(\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonB=Tex(r"$P(B)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PABSchnitt=Tex(r"$P(A\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PABQuerSchnitt= Tex(r"$P(A\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBSchnitt = Tex(r"$P(\bar{A}\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{A}\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PABSchnitt,PABQuerSchnitt,PAQuerBSchnitt,PAQuerBQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        PvonOmega=Tex(r"$P(\Omega)$",font_size=40).set_z_index(2)
        TabelleWahrscheinlichkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA,EreignisAQuer,EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB,PABSchnitt,PAQuerBSchnitt,PvonB],[EreignisBQuer,PABQuerSchnitt,PAQuerBQuerSchnitt,PvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PvonA,PvonAQuer,PvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_edge(LEFT).shift([-0.3,0,0])
        

        
        
        ÜberschriftTabelleW=Text("mit Wahrscheinlichkeiten",font_size=35).next_to(TabelleWahrscheinlichkeiten,UP)

        

        #Häufigkeiten
        HvonA=Tex(r"$|A|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonAQuer=Tex(r"$|\bar{A}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HvonB=Tex(r"$|B|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonBQuer=Tex(r"$|\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HABSchnitt=Tex(r"$|A\cap B|$",font_size=40).set_z_index(2)#.scale(1.2)
        HABQuerSchnitt= Tex(r"$|A\cap\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBSchnitt = Tex(r"$|\bar{A}\cap B|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBQuerSchnitt = Tex(r"$|\bar{A}\cap\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HvonOmega=Tex(r"$|\Omega|$",font_size=40).set_z_index(2)
        
        
        ÜberschriftTabelleH=Text("mit absoluten Häufigkeiten",font_size=35).next_to(ÜberschriftTabelleW,RIGHT,buff=0.6)

        Häufigkeiten=VGroup(HvonA,HvonAQuer,HvonB,HvonBQuer,HABSchnitt,HABQuerSchnitt,HAQuerBSchnitt,HAQuerBQuerSchnitt,HvonOmega)
        TabelleHäufigkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA.copy(),EreignisAQuer.copy(),EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB.copy(),HABSchnitt,HAQuerBSchnitt,HvonB],[EreignisBQuer.copy(),HABQuerSchnitt,HAQuerBQuerSchnitt,HvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),HvonA,HvonAQuer,HvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).next_to(ÜberschriftTabelleH,DOWN).shift([-0.2,0,0])
        
        
        LinkeSeite=VGroup(ÜberschriftTabelleW,TabelleWahrscheinlichkeiten)
        RahmenLinks=SurroundingRectangle(LinkeSeite,buff=0.15)

        RechteSeite=VGroup(ÜberschriftTabelleH,TabelleHäufigkeiten)
        RahmenRechts=SurroundingRectangle(RechteSeite,buff=0.15)


        self.add(Überschrift,ul)
        self.wait(3)
        self.add(ÜberschriftTabelleW)
        self.wait(3)

        self.add(ÜberschriftTabelleH)

        self.wait(3)

        self.add(TabelleWahrscheinlichkeiten,RahmenLinks)


        for x in [EreignisA,EreignisAQuer,EreignisB,EreignisBQuer,PvonOmega,PABSchnitt,PABQuerSchnitt,PAQuerBSchnitt,PAQuerBQuerSchnitt,PvonA,PvonAQuer,PvonB,PvonBQuer]:
                x.set_color(BLACK)

        self.wait(3)
        EreignisA.set_color(WHITE)
        EreignisAQuer.set_color(WHITE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        self.wait(3)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        EreignisB.set_color(WHITE)
        EreignisBQuer.set_color(WHITE)
        self.wait(3)
        PvonA.set_color(WHITE)
        PvonAQuer.set_color(WHITE)
        
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        self.wait(3)
        PvonB.set_color(WHITE)
        PvonBQuer.set_color(WHITE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((3,4), color=PURE_BLUE).add_highlighted_cell((2,4), color=PURE_BLUE)
        self.wait(3)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        Schnittwahrscheinlichkeiten.set_color(WHITE)
        self.wait(3)


        RahmenABQuer=SurroundingRectangle(PABQuerSchnitt,color=RED)
        self.add(RahmenABQuer)
        self.wait(3)
        Spalte=SurroundingRectangle(TabelleWahrscheinlichkeiten.get_columns()[1],z_index=2,color=RED)
        self.add(Spalte)

        self.wait(3)

        Zeile=SurroundingRectangle(TabelleWahrscheinlichkeiten.get_rows()[2],color=RED)
        self.add(Zeile)


        self.wait(3)

        self.remove(Zeile,Spalte,RahmenABQuer)

        self.wait(3)

        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,4), color=PURPLE)
        PvonOmega.set_color(WHITE)
        self.wait(3)
        self.play(Transform(PvonOmega,Tex("$1$").move_to(PvonOmega)))

        self.wait(3)


        self.remove(RahmenLinks)
        self.add(TabelleHäufigkeiten,RahmenRechts)
        Häufigkeiten.set_color(BLACK)
        EreignisA.set_color(WHITE)
        EreignisAQuer.set_color(WHITE)
        EreignisB.set_color(WHITE)
        EreignisBQuer.set_color(WHITE)
        TabelleHäufigkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        
        self.wait(3)
        HvonA.set_color(WHITE)
        HvonAQuer.set_color(WHITE)
        HvonB.set_color(WHITE)
        HvonBQuer.set_color(WHITE)
        TabelleHäufigkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,4), color=PURE_BLUE).add_highlighted_cell((3,4), color=PURE_BLUE)
        
        self.wait(3)
        HABSchnitt.set_color(WHITE)
        HABQuerSchnitt.set_color(WHITE)
        HAQuerBSchnitt.set_color(WHITE)
        HAQuerBQuerSchnitt.set_color(WHITE)
        TabelleHäufigkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)

        self.wait(3)
        


        HvonOmega.set_color(WHITE)
        TabelleHäufigkeiten.add_highlighted_cell((4,4), color=PURPLE)
        self.wait(3)
        
        
        PHvonA=VGroup(PvonA,HvonA).arrange(DOWN)
        PHvonAQuer=VGroup(PvonAQuer,HvonAQuer).arrange(DOWN)
        PHvonB=VGroup(PvonB,HvonB).arrange(DOWN)
        PHvonBQuer=VGroup(PvonBQuer,HvonBQuer).arrange(DOWN)
        PHABSchnitt=VGroup(PABSchnitt,HABSchnitt).arrange(DOWN)
        PHABQuerSchnitt= VGroup(PABQuerSchnitt,HABQuerSchnitt).arrange(DOWN)
        PHAQuerBSchnitt = VGroup(PAQuerBSchnitt,HAQuerBSchnitt).arrange(DOWN)
        PHAQuerBQuerSchnitt = VGroup(PAQuerBQuerSchnitt,HAQuerBQuerSchnitt).arrange(DOWN)
        PHvonOmega=VGroup(PvonOmega,HvonOmega).arrange(DOWN)
        
        PHVGroup=VGroup(PHvonA,PHvonAQuer,PHvonB,PHvonBQuer,PHABSchnitt,PHABQuerSchnitt,PHAQuerBSchnitt,PHAQuerBQuerSchnitt,PHvonOmega)

        

        self.remove(TabelleWahrscheinlichkeiten,TabelleHäufigkeiten)
        self.remove(RahmenRechts)

        for i in range(len(PHVGroup)):
                PHVGroup[i][1].set_opacity(0)
        TabelleBeideHSchwarz = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA.copy(),EreignisAQuer.copy(),EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB.copy(),PHABSchnitt.copy(),PHAQuerBSchnitt.copy(),PHvonB.copy()],[EreignisBQuer.copy(),PHABQuerSchnitt.copy(),PHAQuerBQuerSchnitt.copy(),PHvonBQuer.copy()],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PHvonA.copy(),PHvonAQuer.copy(),PHvonOmega.copy()]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_corner(LEFT+DOWN).shift([-0.2,0,0])
        TabelleBeideHSchwarz.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleBeideHSchwarz.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        TabelleBeideHSchwarz.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleBeideHSchwarz.add_highlighted_cell((2,4), color=PURE_BLUE).add_highlighted_cell((3,4), color=PURE_BLUE)
        TabelleBeideHSchwarz.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        TabelleBeideHSchwarz.add_highlighted_cell((4,4), color=PURPLE)
        
        self.add(TabelleBeideHSchwarz)
        for i in range(len(PHVGroup)):
                PHVGroup[i][0].set_opacity(0)
                PHVGroup[i][1].set_opacity(1)
        TabelleBeidePSchwarz = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA.copy(),EreignisAQuer.copy(),EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB.copy(),PHABSchnitt.copy(),PHAQuerBSchnitt.copy(),PHvonB.copy()],[EreignisBQuer.copy(),PHABQuerSchnitt.copy(),PHAQuerBQuerSchnitt.copy(),PHvonBQuer.copy()],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PHvonA.copy(),PHvonAQuer.copy(),PHvonOmega.copy()]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_corner(RIGHT+DOWN).shift([0.2,0,0])
        TabelleBeidePSchwarz.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleBeidePSchwarz.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        TabelleBeidePSchwarz.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleBeidePSchwarz.add_highlighted_cell((2,4), color=PURE_BLUE).add_highlighted_cell((3,4), color=PURE_BLUE)
        TabelleBeidePSchwarz.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        TabelleBeidePSchwarz.add_highlighted_cell((4,4), color=PURPLE)
        
        self.add(TabelleBeidePSchwarz)

        self.wait(3)
        ÜberschriftTabelleBeide=Text("mit Wahrscheinlichkeiten und absoluten Häufigkeiten",font_size=35).next_to(TabelleBeidePSchwarz.copy().move_to([0,TabelleBeidePSchwarz.get_y(),0]),UP)

        BeideÜberschriften=VGroup(ÜberschriftTabelleH,ÜberschriftTabelleW)
        self.remove(ÜberschriftTabelleH,ÜberschriftTabelleW)
        self.add(ÜberschriftTabelleBeide)
        self.play(TabelleBeidePSchwarz.animate.move_to([0,TabelleBeidePSchwarz.get_y(),0]),TabelleBeideHSchwarz.animate.move_to([0,TabelleBeidePSchwarz.get_y(),0]),run_time=3)


        self.wait(3)
        self.remove(ÜberschriftTabelleBeide)
        self.add(ÜberschriftTabelleH,ÜberschriftTabelleW)
        self.play(TabelleBeideHSchwarz.animate.to_corner(DOWN+LEFT).shift([-0.2,0,0]),TabelleBeidePSchwarz.animate.to_corner(DOWN+RIGHT).shift([0.2,0,0]),run_time=3)
        self.wait(3)
        self.remove(TabelleBeideHSchwarz,TabelleBeidePSchwarz)

        #Häufigkeiten
        HvonA=Tex(r"$|A|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonAQuer=Tex(r"$|\bar{A}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HvonB=Tex(r"$|B|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonBQuer=Tex(r"$|\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HABSchnitt=Tex(r"$|A\cap B|$",font_size=40).set_z_index(2)#.scale(1.2)
        HABQuerSchnitt= Tex(r"$|A\cap\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBSchnitt = Tex(r"$|\bar{A}\cap B|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBQuerSchnitt = Tex(r"$|\bar{A}\cap\bar{B}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HvonOmega=Tex(r"$|\Omega|$",font_size=40).set_z_index(2)

        Häufigkeiten=VGroup(HvonA,HvonAQuer,HvonB,HvonBQuer,HABSchnitt,HABQuerSchnitt,HAQuerBSchnitt,HAQuerBQuerSchnitt,HvonOmega)
        TabelleHäufigkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA.copy(),EreignisAQuer.copy(),EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB.copy(),HABSchnitt,HAQuerBSchnitt,HvonB],[EreignisBQuer.copy(),HABQuerSchnitt,HAQuerBQuerSchnitt,HvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),HvonA,HvonAQuer,HvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_edge(RIGHT).shift([-0.2,0,0])
        
        TabelleHäufigkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)

        TabelleHäufigkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,4), color=PURE_BLUE).add_highlighted_cell((3,4), color=PURE_BLUE)

        TabelleHäufigkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)

        TabelleHäufigkeiten.add_highlighted_cell((4,4), color=PURPLE)


        #Wahrscheinlichkeiten
        PvonA=Tex(r"$P(A)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonAQuer=Tex(r"$P(\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonB=Tex(r"$P(B)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PABSchnitt=Tex(r"$P(A\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PABQuerSchnitt= Tex(r"$P(A\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBSchnitt = Tex(r"$P(\bar{A}\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{A}\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PABSchnitt,PABQuerSchnitt,PAQuerBSchnitt,PAQuerBQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        PvonOmega=Tex(r"$P(\Omega)$",font_size=40).set_z_index(2)
        TabelleWahrscheinlichkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA,EreignisAQuer,EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB,PABSchnitt,PAQuerBSchnitt,PvonB],[EreignisBQuer,PABQuerSchnitt,PAQuerBQuerSchnitt,PvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PvonA,PvonAQuer,PvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_edge(LEFT).shift([-0.3,0,0])
        
        TabelleWahrscheinlichkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((3,4), color=PURE_BLUE).add_highlighted_cell((2,4), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,4), color=PURPLE)


        self.add(TabelleWahrscheinlichkeiten,TabelleHäufigkeiten)
        self.wait(3)
        
        WzuH=CurvedArrow([-0.1,0.5,0],[1,0.5,0],color=RED).flip(axis=[1., 0, 0.])
        MalOmega=Tex(r"$\cdot |\Omega|$",color=RED).scale(1.2).next_to(WzuH,UP,buff=0.1)
        self.add(WzuH,MalOmega)
        self.wait(3)
        HzuW=CurvedArrow([-0.1,0.5,0],[1,0.5,0],color=YELLOW).flip(axis=[0,1,0]).next_to(WzuH,DOWN)
        GeteiltDurchOmega=Tex(r"$\divisionsymbol{|\Omega|}$",color=YELLOW).scale(1.2).next_to(HzuW,DOWN,buff=0.1)

        self.add(HzuW,GeteiltDurchOmega)
        self.wait(3)

        self.remove(TabelleHäufigkeiten,TabelleWahrscheinlichkeiten,HzuW,WzuH,GeteiltDurchOmega,MalOmega)

        EreignisA=Tex(r"$G$")
        EreignisAQuer=Tex(r"$\bar{G}$")
        EreignisB=Tex(r"$N$")
        EreignisBQuer=Tex(r"$\bar{N}$")

        #Häufigkeiten
        HvonA=Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonAQuer=Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HvonB=Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        HvonBQuer=Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        HABSchnitt=Tex(r"$|G\cap N|$",font_size=40).set_z_index(2)#.scale(1.2)
        HABQuerSchnitt= Tex(r"$|G\cap\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBSchnitt = Tex(r"$|\bar{G}\cap N|$",font_size=40).set_z_index(2)#.scale(1.2)
        HAQuerBQuerSchnitt = Tex(r"$|\bar{G}\cap\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        HvonOmega=Tex(r"$|\Omega|$",font_size=40).set_z_index(2)

        Häufigkeiten=VGroup(HvonA,HvonAQuer,HvonB,HvonBQuer,HABSchnitt,HABQuerSchnitt,HAQuerBSchnitt,HAQuerBQuerSchnitt,HvonOmega)
        TabelleHäufigkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA.copy(),EreignisAQuer.copy(),EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB.copy(),HABSchnitt,HAQuerBSchnitt,HvonB],[EreignisBQuer.copy(),HABQuerSchnitt,HAQuerBQuerSchnitt,HvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),HvonA,HvonAQuer,HvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_edge(RIGHT).shift([-0.2,0,0])
        
        TabelleHäufigkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)

        TabelleHäufigkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleHäufigkeiten.add_highlighted_cell((2,4), color=PURE_BLUE).add_highlighted_cell((3,4), color=PURE_BLUE)

        TabelleHäufigkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)

        TabelleHäufigkeiten.add_highlighted_cell((4,4), color=PURPLE)


        #Wahrscheinlichkeiten
        PvonA=Tex(r"$P(G)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonAQuer=Tex(r"$P(\bar{G})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonB=Tex(r"$P(N)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{N})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PABSchnitt=Tex(r"$P(G\cap N)$",font_size=40).set_z_index(2)#.scale(1.2)
        PABQuerSchnitt= Tex(r"$P(G\cap\bar{N})$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBSchnitt = Tex(r"$P(\bar{G}\cap N)$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{G}\cap\bar{N})$",font_size=40).set_z_index(2)#.scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PABSchnitt,PABQuerSchnitt,PAQuerBSchnitt,PAQuerBQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        PvonOmega=Tex(r"$P(\Omega)$",font_size=40).set_z_index(2)
        TabelleWahrscheinlichkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA,EreignisAQuer,EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB,PABSchnitt,PAQuerBSchnitt,PvonB],[EreignisBQuer,PABQuerSchnitt,PAQuerBQuerSchnitt,PvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PvonA,PvonAQuer,PvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_edge(LEFT).shift([-0.3,0,0])
        
        TabelleWahrscheinlichkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((3,4), color=PURE_BLUE).add_highlighted_cell((2,4), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,4), color=PURPLE)


        self.add(TabelleHäufigkeiten,TabelleWahrscheinlichkeiten)
        self.wait(3)
        RechteSeite=VGroup(ÜberschriftTabelleH,TabelleHäufigkeiten)
        RahmenRechts=SurroundingRectangle(RechteSeite,buff=0.05)
        self.add(RahmenRechts)
        self.wait(3)
        self.play(Transform(HvonOmega,Tex(r"$100$").move_to(HvonOmega)))
        self.wait(3)
        self.play(Transform(HvonA,Tex(r"$50$").move_to(HvonA)))
        self.wait(3)
        self.play(Transform(HvonAQuer,Tex(r"$50$").move_to(HvonAQuer)))
        self.wait(3)
        self.play(Transform(HABSchnitt,Tex(r"$5$").move_to(HABSchnitt)))
        self.wait(3)
        self.play(Transform(HABQuerSchnitt,Tex(r"$45$").move_to(HABQuerSchnitt)))
        self.wait(3)
        self.play(Transform(HAQuerBSchnitt,Tex(r"$20$").move_to(HAQuerBSchnitt)))
        self.wait(3)
        self.play(Transform(HAQuerBQuerSchnitt,Tex(r"$30$").move_to(HAQuerBQuerSchnitt)))
        self.wait(3)
        self.play(Transform(HvonB,Tex(r"$25$").move_to(HvonB)))
        self.wait(3)
        self.play(Transform(HvonBQuer,Tex(r"$75$").move_to(HvonBQuer)))
        self.wait(3)
        self.remove(RahmenRechts)
        self.wait(3)
        self.add(HzuW.shift([0,-1.5,0]),GeteiltDurchOmega.next_to(HzuW,DOWN,buff=0.1))

        self.wait(3)
        GeteiltDurch100=Tex(r"$\divisionsymbol 100$",color=YELLOW).scale(1.2).next_to(HzuW,DOWN,buff=0.1)
        HvonOmegaCopy=HvonOmega.copy()

        self.play(HvonOmegaCopy.copy().animate.align_to(GeteiltDurch100,RIGHT+DOWN).set_opacity(0),Transform(GeteiltDurchOmega,GeteiltDurch100),run_time=3)
        self.wait(3)

        self.play(Transform(PvonOmega,Tex(r"$100\%$").move_to(PvonOmega)),
        Transform(PvonA,Tex(r"$50\%$").move_to(PvonA)),
        Transform(PvonAQuer,Tex(r"$50\%$").move_to(PvonAQuer)),
        Transform(PABSchnitt,Tex(r"$5\%$").move_to(PABSchnitt)),
        Transform(PABQuerSchnitt,Tex(r"$45\%$").move_to(PABQuerSchnitt)),
        Transform(PAQuerBSchnitt,Tex(r"$20\%$").move_to(PAQuerBSchnitt)),
        Transform(PAQuerBQuerSchnitt,Tex(r"$30\%$").move_to(PAQuerBQuerSchnitt)),
        Transform(PvonB,Tex(r"$25\%$").move_to(PvonB)),
        Transform(PvonBQuer,Tex(r"$75\%$").move_to(PvonBQuer)),
        run_time=2)

        self.wait(3)

        self.play(Transform(PvonOmega,Tex(r"$1$").move_to(PvonOmega)),
        Transform(PvonA,Tex(r"$0.5$").move_to(PvonA)),
        Transform(PvonAQuer,Tex(r"$0.5$").move_to(PvonAQuer)),
        Transform(PABSchnitt,Tex(r"$0.05$").move_to(PABSchnitt)),
        Transform(PABQuerSchnitt,Tex(r"$0.45$").move_to(PABQuerSchnitt)),
        Transform(PAQuerBSchnitt,Tex(r"$0.2$").move_to(PAQuerBSchnitt)),
        Transform(PAQuerBQuerSchnitt,Tex(r"$0.3$").move_to(PAQuerBQuerSchnitt)),
        Transform(PvonB,Tex(r"$0.25$").move_to(PvonB)),
        Transform(PvonBQuer,Tex(r"$0.75$").move_to(PvonBQuer)),
        run_time=2)

        self.wait(3)

        self.play(Transform(PvonOmega,Tex(r"$\frac{100}{100}$").move_to(PvonOmega)),
        Transform(PvonA,Tex(r"$\frac{50}{100}$").move_to(PvonA)),
        Transform(PvonAQuer,Tex(r"$\frac{50}{100}$").move_to(PvonAQuer)),
        Transform(PABSchnitt,Tex(r"$\frac{5}{100}$").move_to(PABSchnitt)),
        Transform(PABQuerSchnitt,Tex(r"$\frac{45}{100}$").move_to(PABQuerSchnitt)),
        Transform(PAQuerBSchnitt,Tex(r"$\frac{20}{100}$").move_to(PAQuerBSchnitt)),
        Transform(PAQuerBQuerSchnitt,Tex(r"$\frac{30}{100}$").move_to(PAQuerBQuerSchnitt)),
        Transform(PvonB,Tex(r"$\frac{25}{100}$").move_to(PvonB)),
        Transform(PvonBQuer,Tex(r"$\frac{75}{100}$").move_to(PvonBQuer)),
        run_time=2)

        self.wait(5)




class Scene5(Scene):
    def construct(self):
        EreignisA=Tex(r"$A$")
        EreignisAQuer=Tex(r"$\bar{A}$")
        EreignisB=Tex(r"$B$")
        EreignisBQuer=Tex(r"$\bar{B}$")

        

        #Wahrscheinlichkeiten
        PvonA=Tex(r"$P(A)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonAQuer=Tex(r"$P(\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PvonB=Tex(r"$P(B)$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child1,UP).shift([1.1,0.2,0])
        PvonBQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)#.next_to(Tree1Child2,UP).shift([-1.1,0.2,0])
        PABSchnitt=Tex(r"$P(A\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PABQuerSchnitt= Tex(r"$P(A\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBSchnitt = Tex(r"$P(\bar{A}\cap B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{A}\cap\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        
        Schnittwahrscheinlichkeiten=VGroup(PABSchnitt,PABQuerSchnitt,PAQuerBSchnitt,PAQuerBQuerSchnitt).arrange(buff=0.5).to_edge(DOWN)
        PvonOmega=Tex(r"$P(\Omega)$",font_size=40).set_z_index(2)
        TabelleWahrscheinlichkeiten = MobjectTable(
        [[EreignisA.copy().set_color(BLACK).set_z_index(-10),EreignisA,EreignisAQuer,EreignisA.copy().set_color(BLACK).set_z_index(-10)],[EreignisB,PABSchnitt,PAQuerBSchnitt,PvonB],[EreignisBQuer,PABQuerSchnitt,PAQuerBQuerSchnitt,PvonBQuer],[EreignisA.copy().set_color(BLACK).set_z_index(-10),PvonA,PvonAQuer,PvonOmega]],
        include_outer_lines=True,v_buff=0.3, h_buff=0.5)
        
        TabelleWahrscheinlichkeiten.add_highlighted_cell((1,2), color=BLUE).add_highlighted_cell((1,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,1), color=PURE_BLUE).add_highlighted_cell((3,1), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,2), color=BLUE).add_highlighted_cell((4,3), color=BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((3,4), color=PURE_BLUE).add_highlighted_cell((2,4), color=PURE_BLUE)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((2,2), color=GREEN).add_highlighted_cell((2,3), color=GREEN).add_highlighted_cell((3,2), color=GREEN).add_highlighted_cell((3,3), color=GREEN)
        TabelleWahrscheinlichkeiten.add_highlighted_cell((4,4), color=PURPLE)

        
        ÜberschriftTabelleW=Text("Vierfeldertafel mit Wahrscheinlichkeiten",font_size=35).next_to(TabelleWahrscheinlichkeiten,UP)

        self.add(TabelleWahrscheinlichkeiten,ÜberschriftTabelleW)

        self.wait(5)

        Überblick=Text("Überblick: Alle Wahrscheinlichkeiten").to_edge(UP)
        ul=Underline(Überblick)
        PNGSchnitt=Tex(r"$P(A\cap B)$",font_size=40).set_z_index(2).scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(A\cap\bar{B})$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGSchnitt = Tex(r"$P(\bar{A}\cap B)$",font_size=40).set_z_index(2).scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{A}\cap\bar{B})$",font_size=40).set_z_index(2).scale(1.2)
        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt).arrange(DOWN,buff=0.83)
        

        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(A)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonNQuer=Tex(r"$P(\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonGBedN=Tex(r"$P_A(B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonGQuerBedN=Tex(r"$P_A(\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonGBedNQuer=Tex(r"$P_{\bar{A}} (B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{A}} (\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(B)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonGQuer=Tex(r"$P(\bar{B})$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonNBedG=Tex(r"$P_B(A)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonNQuerBedG=Tex(r"$P_B(\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonNBedGQuer=Tex(r"$P_{\bar{B}} (A)$",font_size=40).set_z_index(2)#.scale(1.2)
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{B}} (\bar{A})$",font_size=40).set_z_index(2)#.scale(1.2)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        
        #Wahrscheinlichkeiten=Text("Wahrscheinlichkeiten",font_size=30)
        inBaumdiagrammen=Text("... in Baumdiagrammen",font_size=30)
        #WahrscheinlichkeitenImBaumdiagramm=VGroup(Wahrscheinlichkeiten,inBaumdiagrammen).arrange(DOWN)
        
        TabelleBedG = MobjectTable(
            [[PvonG,PvonGQuer],[PvonNBedG,PvonNQuerBedG],[PvonNBedGQuer,PvonNQuerBedGQuer]],
            include_outer_lines=True,v_buff=0.3, h_buff=0.5).to_corner(DOWN+LEFT)
        
        TabelleBedN = MobjectTable(
            [[PvonN,PvonNQuer],[PvonGBedN,PvonGQuerBedN],[PvonGBedNQuer,PvonGQuerBedNQuer]],
            include_outer_lines=True,v_buff=0.3, h_buff=0.5).next_to(TabelleBedG,UP)
        
        inBaumdiagrammen.next_to(TabelleBedN,UP).shift([1.4,0,0])
        
        
        
        TabelleBedN.add_highlighted_cell((1,1), color=BLUE).add_highlighted_cell((1,2), color=BLUE)
        TabelleBedG.add_highlighted_cell((1,1), color=BLUE).add_highlighted_cell((1,2), color=BLUE)

        TabelleBedG.add_highlighted_cell((2,1), color=RED).add_highlighted_cell((3,1), color=RED).add_highlighted_cell((2,2), color=RED).add_highlighted_cell((3,2), color=RED)
        TabelleBedN.add_highlighted_cell((2,1), color=RED).add_highlighted_cell((3,1), color=RED).add_highlighted_cell((2,2), color=RED).add_highlighted_cell((3,2), color=RED)

        Schnittwahrscheinlichkeiten.next_to(TabelleBedN,RIGHT).shift([0,TabelleBedN.get_top()[1]-SurroundingRectangle(Schnittwahrscheinlichkeiten).get_top()[1],0])

        RahmenSchnittwahrscheinlichkeiten=SurroundingRectangle(Schnittwahrscheinlichkeiten,color=WHITE).set_fill(color=GREEN,opacity=1)

        inDerVierfeldertafel=Text("... in der Vierfeldertafel",font_size=30).next_to(TabelleWahrscheinlichkeiten.copy().to_edge(RIGHT).shift([0,-0.18,0]),UP,buff=0.35)
        #mitWahrscheinlichkeiten=Text("mit Wahrscheinlichkeiten",font_size=30)
        #VierfeldertafelmitWahrscheinlichkeiten=VGroup(Vierfeldertafel,mitWahrscheinlichkeiten).arrange(DOWN).next_to(TabelleWahrscheinlichkeiten.to_edge(RIGHT).shift([0,-0.2,0]),UP)

        self.play(FadeIn(inBaumdiagrammen,Überblick,ul,TabelleBedG,TabelleBedN,WahrscheinlichkeitenBaum1,WahrscheinlichkeitenBaum2,Schnittwahrscheinlichkeiten,RahmenSchnittwahrscheinlichkeiten),
        TabelleWahrscheinlichkeiten.animate.to_edge(RIGHT).shift([0,-0.18,0]),
        Transform(ÜberschriftTabelleW,inDerVierfeldertafel))
        
        self.wait(3)

        PvonAQuerBedB=Tex(r"$P_B(\bar{A})$",font_size=40).set_z_index(2).scale(1.2).next_to(TabelleWahrscheinlichkeiten,DOWN,buff=0.8).align_to(TabelleWahrscheinlichkeiten,LEFT)

        fractionAQuerB =VGroup(Tex(r"$=$",font_size=40).scale(1.2),
                VGroup(
                Tex(r"$P_B(\bar{A})$",font_size=40).scale(1.2).set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tex(r"$P_B(\bar{A})$",font_size=40).scale(1.2)),
                Tex(r"$P(B)$",font_size=40).scale(1.2).set_color(BLACK).set_z_index(-1)).arrange(DOWN)
        ).arrange(RIGHT).next_to(PvonAQuerBedB,RIGHT)

        self.add(PvonAQuerBedB,fractionAQuerB)
        self.wait(3)
        RahmenPvonB=SurroundingRectangle(PvonB.copy().move_to(fractionAQuerB[1][2]),color=BLUE)
        RahmenSchnittwahrscheinlichkeit=SurroundingRectangle(PAQuerBSchnitt.copy().move_to(fractionAQuerB[1][0]),color=GREEN)
        self.play(FadeIn(RahmenSchnittwahrscheinlichkeit),PAQuerBSchnitt.copy().set_z_index(2).animate.move_to(fractionAQuerB[1][0]),run_time=2.5)
        self.wait(3)
        self.play(FadeIn(RahmenPvonB),PvonB.copy().set_z_index(2).animate.move_to(fractionAQuerB[1][2]),run_time=2.5)

        self.wait(5)




class Scene4Video1(Scene):
    def construct(self):
        
        
        xStart=2
        yStart=2
        EreignisAStart=Rectangle(height=4,width=xStart,color=BLUE,z_index=-1).set_fill(BLUE,opacity=1).move_to([-6,0,0]).set_stroke(BLACK,opacity=0)
        EreignisBStart=Rectangle(height=4,width=yStart,color=RED,z_index=-1).set_fill(RED,opacity=1).next_to(EreignisAStart,buff=[0,0,0]).set_stroke(BLACK,opacity=0)
        Ereignisraum=Rectangle(height=4,width=4,z_index=-1).align_to(EreignisAStart,LEFT+DOWN)
        EreignisraumText=Tex(r"$\Omega$").move_to(Ereignisraum.get_center())
        EreignisAStartText=always_redraw(lambda:Tex(r"$A$",color=BLACK).move_to(EreignisAStart.get_center()))
        EreignisBStartText=always_redraw(lambda:Tex(r"$\bar{A}$",color=BLACK).move_to(EreignisBStart.get_center()))


        self.add(Ereignisraum,EreignisraumText)
        self.wait(3)
        self.remove(Ereignisraum,EreignisraumText)
        self.add(EreignisAStart,EreignisBStart,EreignisAStartText,EreignisBStartText)
        self.wait(3)
       




        #Zweites Diagramm
        EreignisA=EreignisAStart.copy().next_to(EreignisBStart,RIGHT,buff=[0.55,0,0])
        EreignisB=EreignisBStart.copy().next_to(EreignisA,RIGHT,buff=[0,0,0])
        EreignisAText=EreignisAStartText.copy().move_to(EreignisA)
        EreignisBText=EreignisBStartText.copy().move_to(EreignisB)
 
        


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
        EreignisA.set_color(GREEN)
        self.remove(EreignisAText)
        self.add(BedingungA)
        #self.wait(2)
        self.add(EreignisAcapBText,EreignisAcapnotBText)
        self.remove(EreignisBText)
        self.add(EreignisnotAcapnotBText,EreignisnotAcapBText)
        self.add(BedingungB)
        EreignisB.set_color(PURPLE)
        self.wait(3)
        

        GanzesQuadrat=VGroup(EreignisA,EreignisB,BedingungA,BedingungB)
        
        BedingungACopy=Rectangle(height=aStart,width=EreignisA.get_width(),color=YELLOW,z_index=2).set_fill(YELLOW,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0)


        fraction = always_redraw(lambda:VGroup(
                BedingungB.copy(),
                Line(LEFT, RIGHT).match_width(GanzesQuadrat),
                GanzesQuadrat.copy()
            ).arrange(DOWN).move_to([4.55,0,0]))
       
        BeschriftungBruchZähler=always_redraw(lambda:Tex(r"$|\bar{A}\cap B|$",color=BLACK,z_index=3).move_to(fraction[0].get_center()))
        
        BedingungACopy=BedingungA.copy()
        BedingungACopy2=BedingungA.copy()
        BedingungBCopy=BedingungB.copy()
        EreignisAcapBTextCopy=EreignisAcapBText.copy()
        EreignisAcapBTextCopy2=EreignisAcapBText.copy()
        EreignisnotAcapBTextCopy=EreignisnotAcapBText.copy()


        fracBlack=always_redraw(lambda:VGroup(
                BedingungB.copy().set_fill(BLACK,opacity=0).set_z_index(-10),
                Line(LEFT, RIGHT).match_width(GanzesQuadrat),
                GanzesQuadrat.copy().set_fill(BLACK,opacity=0).set_z_index(-10)
            ).arrange(DOWN).move_to([4.55,0,0]))

        GanzesQuadratCopy=GanzesQuadrat.copy().set_z_index(1)
        BeschriftungBruchNenner=always_redraw(lambda:Tex(r"$|\Omega|$",color=WHITE,z_index=2).move_to(fracBlack[2].get_center()))

        self.wait(3)
        self.play(FadeIn(fracBlack),BedingungBCopy.animate.move_to(fracBlack[0].get_center()),run_time=2)#,EreignisnotAcapBTextCopy.animate.move_to(fracBlack[0].get_center()),rate_func=linear,run_time=2)
        #self.add(BeschriftungBruchZähler)
        self.remove(EreignisnotAcapBTextCopy)
        self.wait(5)
        self.play(GanzesQuadratCopy.animate.move_to(fracBlack[2].get_center()),rate_func=linear,run_time=2)
        self.add(BeschriftungBruchNenner)
        self.remove(EreignisAcapBTextCopy2,EreignisnotAcapBTextCopy)
        self.remove(fracBlack,BedingungACopy,BedingungACopy2,BedingungBCopy,GanzesQuadrat)
        self.add(fraction)
        self.wait(3)

        self.wait(5)




class Scene5Video1(Scene):
    def construct(self):
        xStart=2.5
        yStart=1.5
        Ereignisraum=Rectangle(height=4,width=4).move_to([-5,0,0])
        EreignisraumText=Tex(r"$\Omega$",color=WHITE).move_to(Ereignisraum.get_center())
        EreignisAStart=Rectangle(height=xStart,width=4,color=BLUE,z_index=-1).set_fill(BLUE,opacity=1).next_to(Ereignisraum,buff=0.9).set_stroke(BLACK,opacity=0)
        EreignisBStart=Rectangle(height=yStart,width=4,color=RED,z_index=-1).set_fill(RED,opacity=1).next_to(EreignisAStart,DOWN,buff=[0,0,0]).set_stroke(BLACK,opacity=0)
        EreignisAStartText=always_redraw(lambda:Tex(r"$B$",color=BLACK).move_to(EreignisAStart.get_center()))
        EreignisBStartText=always_redraw(lambda:Tex(r"$\bar{B}$",color=BLACK).move_to(EreignisBStart.get_center()))
        ErsteTeilung=VGroup(EreignisAStart,EreignisBStart,EreignisAStartText,EreignisBStartText).next_to(Ereignisraum,buff=0.9)

        
        self.add(Ereignisraum,EreignisraumText)
        self.wait(3)
        self.add(EreignisAStart,EreignisAStartText,EreignisBStart,EreignisBStartText)
        self.wait(3)


        EreignisA=EreignisAStart.copy().next_to(EreignisAStart,RIGHT,buff=0.9)
        EreignisAText=EreignisAStartText.copy().move_to(EreignisA.get_center())
        EreignisB=EreignisBStart.copy().next_to(EreignisBStart,RIGHT,buff=0.9)
        EreignisBText=EreignisBStartText.copy().move_to(EreignisB.get_center())


        self.add(EreignisA,EreignisB,EreignisAText,EreignisBText)
        
        SchnittA=Rectangle(height=xStart,width=1.58,color=GREEN,z_index=0).set_fill(GREEN,opacity=1).align_to(EreignisA,LEFT+DOWN).set_stroke(BLACK,opacity=0)
        SchnittB=Rectangle(height=xStart,width=2.42,color=YELLOW,z_index=0).set_fill(YELLOW,opacity=1).next_to(SchnittA,RIGHT,buff=0).set_stroke(BLACK,opacity=0)
        SchnittAText=Tex(r"$A\cap B$",color=BLACK,z_index=1).move_to(SchnittA.get_center())
        SchnittBText=Tex(r"$\bar{A}\cap B$",color=BLACK,z_index=1).move_to(SchnittB.get_center())

        SchnittC=Rectangle(height=1.5,width=2.2,color=PURPLE,z_index=0).set_fill(PURPLE,opacity=1).next_to(EreignisA,DOWN,buff=0).set_stroke(BLACK,opacity=0).align_to(SchnittA,LEFT)
        SchnittD=Rectangle(height=1.5,width=1.8,color=ORANGE,z_index=0).set_fill(ORANGE,opacity=1).next_to(SchnittC,RIGHT,buff=0).set_stroke(BLACK,opacity=0)
        SchnittCText=Tex(r"$A\cap \bar{B}$",color=BLACK,z_index=1).move_to(SchnittC.get_center())
        SchnittDText=Tex(r"$\bar{A}\cap \bar{B}$",color=BLACK,z_index=1).move_to(SchnittD.get_center())

        self.add(SchnittA,SchnittB,SchnittAText,SchnittBText)
        self.add(SchnittC,SchnittD,SchnittCText,SchnittDText)
        self.wait(5)




        