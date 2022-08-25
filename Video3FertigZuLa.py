import os
from manim import *
from manim.utils import tex_file_writing

#Screengrid: x:-7;+7      y:-4;+4
class ZweiBaumdiagrammeZuHaeufigkeitsnetz(Scene):
    def construct(self):
        #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)

        

        #Knoten Baum 2
        Tree2Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        Tree2Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1)
        
        #Tree1Root.color=RED

        
        #Ausgangspositionen
        #Tree1
        p1= [-3.75,1.5,0] #Root
        p2= [-5,0,0]      #Child1
        p3= [-2.5,0,0]    #Child2
        p4= [-6,-1.5,0]   #Grandchild1
        p5= [-4.5,-1.5,0] #Grandchild2
        p6= [-3,-1.5,0]   #Grandchild3
        p7= [-1.5,-1.5,0] #Grandchild4

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
        #Tree2
        q1= [3.75,1.5,0] #Root
        q2= [2.5,0,0]    #Child1
        q3= [5,0,0]      #Child2
        q4= [1.5,-1.5,0] #Grandchild1
        q5= [3,-1.5,0]   #Grandchild2
        q6= [4.5,-1.5,0] #Grandchild3
        q7= [6,-1.5,0]   #Grandchild4

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
        
        Tree1Child1Text = Tex(r"$A$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{A}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$A\cap B$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$A\cap\bar{B}$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$\bar{A}\cap B$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{A}\cap\bar{B}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)

        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$B$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{B}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$A\cap B$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$\bar{A}\cap B$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$A\cap\bar{B}$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{A}\cap\bar{B}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)



        #Zielpositionen
        #Tree1
        p1z= [-3.75,0,0] #Root
        p2z= [-3.75,2,0] #Child1
        p3z= [-3.75,-2,0]#Child2
        p4z= [-6,2,0]    #Grandchild1
        p5z= [-1.5,2,0]  #Grandchild2
        p6z= [-6,-2,0]   #Grandchild3
        p7z= [-1.5,-2,0] #Grandchild4

        dotp1z=Dot(p1z,fill_opacity=0)  #Root
        dotp2z=Dot(p2z,fill_opacity=0)  #Child1
        dotp3z=Dot(p3z,fill_opacity=0)  #Child2
        dotp4z=Dot(p4z,fill_opacity=0)  #Grandchild1
        dotp5z=Dot(p5z,fill_opacity=0)  #Grandchild2
        dotp6z=Dot(p6z,fill_opacity=0)  #Grandchild3
        dotp7z=Dot(p7z,fill_opacity=0)  #Grandchild4

        #Zielpositionen
        #Tree2
        q1z= [3.75,0,0]        #Root
        q2z= [1.5,0,0]         #Child1
        q3z= [6,0,0]           #Child2
        q4z= [1.5,2,0]         #Grandchild1
        q5z= [1.5,-2,0]        #Grandchild2
        q6z= [6,2,0]           #Grandchild3
        q7z= [6,-2,0]          #Grandchild4

        dotq1z=Dot(q1z,fill_opacity=0)  #Root
        dotq2z=Dot(q2z,fill_opacity=0)  #Child1
        dotq3z=Dot(q3z,fill_opacity=0)  #Child2
        dotq4z=Dot(q4z,fill_opacity=0)  #Grandchild1
        dotq5z=Dot(q5z,fill_opacity=0)  #Grandchild2
        dotq6z=Dot(q6z,fill_opacity=0)  #Grandchild3
        dotq7z=Dot(q7z,fill_opacity=0)  #Grandchild4


        #Position Häufigkeitsnetz
        #Tree1
        p1h= [0,0,0]        #Root
        p2h= [0,2,0]         #Child1
        p3h= [0,-2,0]           #Child2
        p4h= [-2.2,2,0]         #Grandchild1
        p5h= [2.2,2,0]        #Grandchild2
        p6h= [-2.2,-2,0]           #Grandchild3
        p7h= [2.2,-2,0]          #Grandchild4

        dotp1h=Dot(p1h,fill_opacity=0)  #Root
        dotp2h=Dot(p2h,fill_opacity=0)  #Child1
        dotp3h=Dot(p3h,fill_opacity=0)  #Child2
        dotp4h=Dot(p4h,fill_opacity=0)  #Grandchild1
        dotp5h=Dot(p5h,fill_opacity=0)  #Grandchild2
        dotp6h=Dot(p6h,fill_opacity=0)  #Grandchild3
        dotp7h=Dot(p7h,fill_opacity=0)  #Grandchild4

        #Tree2
        q1h= [0,0,0]        #Root
        q2h= [-2.25,0,0]         #Child1
        q3h= [2.25,0,0]           #Child2
        q4h= [-2.2,2,0]         #Grandchild1
        q5h= [-2.2,-2,0]        #Grandchild2
        q6h= [2.2,2,0]           #Grandchild3
        q7h= [2.2,-2,0]          #Grandchild4

        dotq1h=Dot(q1h,fill_opacity=0)  #Root
        dotq2h=Dot(q2h,fill_opacity=0)  #Child1
        dotq3h=Dot(q3h,fill_opacity=0)  #Child2
        dotq4h=Dot(q4h,fill_opacity=0)  #Grandchild1
        dotq5h=Dot(q5h,fill_opacity=0)  #Grandchild2
        dotq6h=Dot(q6h,fill_opacity=0)  #Grandchild3
        dotq7h=Dot(q7h,fill_opacity=0)  #Grandchild4


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
        
        
        
        #Zeichnet Baumdiagramm1 direkt
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        self.wait()
        #Zeichnet Baumdiagramm2 direkt
        self.add(Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
        self.wait()
        Tree1Root.color=RED
        Tree2Root.color=RED
        Tree1Grandchild1.color=RED
        Tree1Grandchild2.color=RED
        Tree1Grandchild3.color=RED
        Tree1Grandchild4.color=RED
        Tree2Grandchild1.color=RED
        Tree2Grandchild2.color=RED
        Tree2Grandchild3.color=RED
        Tree2Grandchild4.color=RED
        
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
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        
        #Animiert Baumdiagramm1 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotp1,dotp1z),ClockwiseTransform(dotp2,dotp2z),Transform(dotp3,dotp3z),Transform(dotp4,dotp4z),Transform(dotp5,dotp5z),Transform(dotp6,dotp6z),Transform(dotp7,dotp7z),run_time=5)

        #Animiert Baumdiagramm2 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotq1,dotq1z),ClockwiseTransform(dotq2,dotq2z),ClockwiseTransform(dotq3,dotq3z),ClockwiseTransform(dotq4,dotq4z),Transform(dotq5,dotq5z),ClockwiseTransform(dotq6,dotq6z),Transform(dotq7,dotq7z),run_time=5)
       
        #Animiert Baumdiagramm1 über Baumdiagramm2 zu Häufigkeitsnetz
        self.play(Transform(dotp1,dotp1h),Transform(dotp2,dotp2h),Transform(dotp3,dotp3h),Transform(dotp4,dotp4h),Transform(dotp5,dotp5h),Transform(dotp6,dotp6h),Transform(dotp7,dotp7h),Transform(dotq1,dotq1h),Transform(dotq2,dotq2h),Transform(dotq3,dotq3h),Transform(dotq4,dotq4h),Transform(dotq5,dotq5h),Transform(dotq6,dotq6h),Transform(dotq7,dotq7h),run_time=5)
        self.wait()



class ZweiBaumdiagrammeZuHaeufigkeitsnetzGN(Scene):
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
        p1= [-3.75,1.5,0] #Root
        p2= [-5,0,0]      #Child1
        p3= [-2.5,0,0]    #Child2
        p4= [-6.3,-1.5,0]   #Grandchild1
        p5= [-4.65,-1.5,0] #Grandchild2
        p6= [-2.85,-1.5,0]   #Grandchild3
        p7= [-1.2,-1.5,0] #Grandchild4

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
        #Tree2
        q1= [3.75,1.5,0] #Root
        q2= [2.5,0,0]    #Child1
        q3= [5,0,0]      #Child2
        q4= [1.2,-1.5,0] #Grandchild1
        q5= [2.85,-1.5,0]   #Grandchild2
        q6= [4.65,-1.5,0] #Grandchild3
        q7= [6.3,-1.5,0]   #Grandchild4

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



        #Zielpositionen
        #Tree1
        p1z= [-3.75,0,0] #Root
        p2z= [-3.75,2,0] #Child1
        p3z= [-3.75,-2,0]#Child2
        p4z= [-6,2,0]    #Grandchild1
        p5z= [-1.5,2,0]  #Grandchild2
        p6z= [-6,-2,0]   #Grandchild3
        p7z= [-1.5,-2,0] #Grandchild4

        dotp1z=Dot(p1z,fill_opacity=0)  #Root
        dotp2z=Dot(p2z,fill_opacity=0)  #Child1
        dotp3z=Dot(p3z,fill_opacity=0)  #Child2
        dotp4z=Dot(p4z,fill_opacity=0)  #Grandchild1
        dotp5z=Dot(p5z,fill_opacity=0)  #Grandchild2
        dotp6z=Dot(p6z,fill_opacity=0)  #Grandchild3
        dotp7z=Dot(p7z,fill_opacity=0)  #Grandchild4

        #Zielpositionen
        #Tree2
        q1z= [3.75,0,0]        #Root
        q2z= [1.5,0,0]         #Child1
        q3z= [6,0,0]           #Child2
        q4z= [1.5,2,0]         #Grandchild1
        q5z= [1.5,-2,0]        #Grandchild2
        q6z= [6,2,0]           #Grandchild3
        q7z= [6,-2,0]          #Grandchild4

        dotq1z=Dot(q1z,fill_opacity=0)  #Root
        dotq2z=Dot(q2z,fill_opacity=0)  #Child1
        dotq3z=Dot(q3z,fill_opacity=0)  #Child2
        dotq4z=Dot(q4z,fill_opacity=0)  #Grandchild1
        dotq5z=Dot(q5z,fill_opacity=0)  #Grandchild2
        dotq6z=Dot(q6z,fill_opacity=0)  #Grandchild3
        dotq7z=Dot(q7z,fill_opacity=0)  #Grandchild4


        #Position Häufigkeitsnetz
        #Tree1
        p1h= [0,0,0]        #Root
        p2h= [0,2,0]         #Child1
        p3h= [0,-2,0]           #Child2
        p4h= [-2.2,2,0]         #Grandchild1
        p5h= [2.2,2,0]        #Grandchild2
        p6h= [-2.2,-2,0]           #Grandchild3
        p7h= [2.2,-2,0]          #Grandchild4

        dotp1h=Dot(p1h,fill_opacity=0)  #Root
        dotp2h=Dot(p2h,fill_opacity=0)  #Child1
        dotp3h=Dot(p3h,fill_opacity=0)  #Child2
        dotp4h=Dot(p4h,fill_opacity=0)  #Grandchild1
        dotp5h=Dot(p5h,fill_opacity=0)  #Grandchild2
        dotp6h=Dot(p6h,fill_opacity=0)  #Grandchild3
        dotp7h=Dot(p7h,fill_opacity=0)  #Grandchild4

        #Tree2
        q1h= [0,0,0]        #Root
        q2h= [-2.25,0,0]         #Child1
        q3h= [2.25,0,0]           #Child2
        q4h= [-2.2,2,0]         #Grandchild1
        q5h= [-2.2,-2,0]        #Grandchild2
        q6h= [2.2,2,0]           #Grandchild3
        q7h= [2.2,-2,0]          #Grandchild4

        dotq1h=Dot(q1h,fill_opacity=0)  #Root
        dotq2h=Dot(q2h,fill_opacity=0)  #Child1
        dotq3h=Dot(q3h,fill_opacity=0)  #Child2
        dotq4h=Dot(q4h,fill_opacity=0)  #Grandchild1
        dotq5h=Dot(q5h,fill_opacity=0)  #Grandchild2
        dotq6h=Dot(q6h,fill_opacity=0)  #Grandchild3
        dotq7h=Dot(q7h,fill_opacity=0)  #Grandchild4


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
        
        
        
        #Zeichnet Baumdiagramm1 direkt
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        self.wait(3)
        #Zeichnet Baumdiagramm2 direkt
        self.add(Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
        self.wait(3)
        
        
        #Animiert Baumdiagramm1 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotp1,dotp1z),ClockwiseTransform(dotp2,dotp2z),Transform(dotp3,dotp3z),Transform(dotp4,dotp4z),Transform(dotp5,dotp5z),Transform(dotp6,dotp6z),Transform(dotp7,dotp7z),run_time=5)
        self.wait(3)
        #Animiert Baumdiagramm2 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotq1,dotq1z),ClockwiseTransform(dotq2,dotq2z),ClockwiseTransform(dotq3,dotq3z),ClockwiseTransform(dotq4,dotq4z),Transform(dotq5,dotq5z),ClockwiseTransform(dotq6,dotq6z),Transform(dotq7,dotq7z),run_time=5)
        self.wait(3)
        Tree1Root.color=RED
        Tree2Root.color=RED
        Tree1Grandchild1.color=RED
        Tree1Grandchild2.color=RED
        Tree1Grandchild3.color=RED
        Tree1Grandchild4.color=RED
        Tree2Grandchild1.color=RED
        Tree2Grandchild2.color=RED
        Tree2Grandchild3.color=RED
        Tree2Grandchild4.color=RED
        
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
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        self.wait(3)
        #Animiert Baumdiagramm1 über Baumdiagramm2 zu Häufigkeitsnetz
        self.play(Transform(dotp1,dotp1h),Transform(dotp2,dotp2h),Transform(dotp3,dotp3h),Transform(dotp4,dotp4h),Transform(dotp5,dotp5h),Transform(dotp6,dotp6h),Transform(dotp7,dotp7h),Transform(dotq1,dotq1h),Transform(dotq2,dotq2h),Transform(dotq3,dotq3h),Transform(dotq4,dotq4h),Transform(dotq5,dotq5h),Transform(dotq6,dotq6h),Transform(dotq7,dotq7h),run_time=5)
        self.wait(5)





class Scene2(Scene):
    def construct(self):
    #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)

        KnotenBaum1=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)


        #Knoten Baum 2
        Tree2Root=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)
        Tree2Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.1).set_z_index(1).scale(1.2)

        KnotenBaum2=VGroup(Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4)

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
        #try:
        #    Tree1RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        #except:
        #    path="C:/Users/abioh/Documents/Manim/Test/media/Tex"
        #    for filename in os.listdir(path):
        #        tex_file_writing.compile_tex(filename, "pdflatex",".dvi")
        
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


        MengenInKnotenBaum1=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)


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
        MengenInKnotenBaum2=VGroup(Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)


        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        HäufigkeitenBaum1=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)


        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        HäufigkeitenBaum2=VGroup(Tree2RootBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree2Grandchild1TextBetrag,Tree2Grandchild2TextBetrag,Tree2Grandchild3TextBetrag,Tree2Grandchild4TextBetrag)

        for x in range(len(KnotenBaum1)):
            KnotenBaum1[x].scale(1.2)
            KnotenBaum2[x].scale(1.2)
            MengenInKnotenBaum1[x].align_to(KnotenBaum1[x],UP).shift([0,-0.1,0])
            MengenInKnotenBaum2[x].align_to(KnotenBaum2[x],UP).shift([0,-0.1,0])
            HäufigkeitenBaum1[x].move_to(KnotenBaum1[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)
            HäufigkeitenBaum2[x].move_to(KnotenBaum2[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        #Zielpositionen
        #Tree1
        p1z= [-3.75,-0.5,0] #Root
        p2z= [-3.75,2,0] #Child1
        p3z= [-3.75,-3,0]#Child2
        p4z= [-6,2,0]    #Grandchild1
        p5z= [-1.5,2,0]  #Grandchild2
        p6z= [-6,-3,0]   #Grandchild3
        p7z= [-1.5,-3,0] #Grandchild4

        dotp1z=Dot(p1z,fill_opacity=0)  #Root
        dotp2z=Dot(p2z,fill_opacity=0)  #Child1
        dotp3z=Dot(p3z,fill_opacity=0)  #Child2
        dotp4z=Dot(p4z,fill_opacity=0)  #Grandchild1
        dotp5z=Dot(p5z,fill_opacity=0)  #Grandchild2
        dotp6z=Dot(p6z,fill_opacity=0)  #Grandchild3
        dotp7z=Dot(p7z,fill_opacity=0)  #Grandchild4

        #Zielpositionen
        #Tree2
        q1z= [3.75,-0.5,0]        #Root
        q2z= [1.5,-0.5,0]         #Child1
        q3z= [6,-0.5,0]           #Child2
        q4z= [1.5,2,0]         #Grandchild1
        q5z= [1.5,-3,0]        #Grandchild2
        q6z= [6,2,0]           #Grandchild3
        q7z= [6,-3,0]          #Grandchild4

        dotq1z=Dot(q1z,fill_opacity=0)  #Root
        dotq2z=Dot(q2z,fill_opacity=0)  #Child1
        dotq3z=Dot(q3z,fill_opacity=0)  #Child2
        dotq4z=Dot(q4z,fill_opacity=0)  #Grandchild1
        dotq5z=Dot(q5z,fill_opacity=0)  #Grandchild2
        dotq6z=Dot(q6z,fill_opacity=0)  #Grandchild3
        dotq7z=Dot(q7z,fill_opacity=0)  #Grandchild4


        #Position Häufigkeitsnetz
        #Tree1
        p1h= [0,-0.5,0]        #Root
        p2h= [0,2,0]         #Child1
        p3h= [0,-3,0]           #Child2
        p4h= [-4,2,0]         #Grandchild1
        p5h= [4,2,0]        #Grandchild2
        p6h= [-4,-3,0]           #Grandchild3
        p7h= [4,-3,0]          #Grandchild4

        dotp1h=Dot(p1h,fill_opacity=0)  #Root
        dotp2h=Dot(p2h,fill_opacity=0)  #Child1
        dotp3h=Dot(p3h,fill_opacity=0)  #Child2
        dotp4h=Dot(p4h,fill_opacity=0)  #Grandchild1
        dotp5h=Dot(p5h,fill_opacity=0)  #Grandchild2
        dotp6h=Dot(p6h,fill_opacity=0)  #Grandchild3
        dotp7h=Dot(p7h,fill_opacity=0)  #Grandchild4



        


        #Tree2
        q1h= [0,-0.5,0]        #Root
        q2h= [-4,-0.5,0]         #Child1
        q3h= [4,-0.5,0]           #Child2
        q4h= [-4,2,0]         #Grandchild1
        q5h= [-4,-3,0]        #Grandchild2
        q6h= [4,2,0]           #Grandchild3
        q7h= [4,-3,0]          #Grandchild4

        dotq1h=Dot(q1h,fill_opacity=0)  #Root
        dotq2h=Dot(q2h,fill_opacity=0)  #Child1
        dotq3h=Dot(q3h,fill_opacity=0)  #Child2
        dotq4h=Dot(q4h,fill_opacity=0)  #Grandchild1
        dotq5h=Dot(q5h,fill_opacity=0)  #Grandchild2
        dotq6h=Dot(q6h,fill_opacity=0)  #Grandchild3
        dotq7h=Dot(q7h,fill_opacity=0)  #Grandchild4
    




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

        self.add(HäufigkeitenBaum1,HäufigkeitenBaum2)

        #Zeichnet Baumdiagramm1 direkt
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        
        self.add(PvonN,PvonNQuer)
       
        self.add(PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)
       
        #Zeichnet Baumdiagramm2 direkt
        self.add(Tree2Root,Tree2RootText)
       
        self.add(Tree2Child1,Tree2Child2,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2Child1Text,Tree2Child2Text)
       
        self.add(Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
      

        self.add(PvonG,PvonGQuer)

     

        self.add(PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        self.wait(3)


        
        
        #self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        #self.remove(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer,PvonG,PvonGQuer,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        #self.wait()

        Tree1Root.color=RED
        Tree2Root.color=RED
        Tree1Grandchild1.color=RED
        Tree1Grandchild2.color=RED
        Tree1Grandchild3.color=RED
        Tree1Grandchild4.color=RED
        Tree2Grandchild1.color=RED
        Tree2Grandchild2.color=RED
        Tree2Grandchild3.color=RED
        Tree2Grandchild4.color=RED
        
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

        self.wait(2)

        #Animiert Baumdiagramm1 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotp1,dotp1z),ClockwiseTransform(dotp2,dotp2z),Transform(dotp3,dotp3z),Transform(dotp4,dotp4z),Transform(dotp5,dotp5z),Transform(dotp6,dotp6z),Transform(dotp7,dotp7z),run_time=5)

        #Animiert Baumdiagramm2 von Startposition in Zielposition
        self.play(ClockwiseTransform(dotq1,dotq1z),ClockwiseTransform(dotq2,dotq2z),ClockwiseTransform(dotq3,dotq3z),ClockwiseTransform(dotq4,dotq4z),Transform(dotq5,dotq5z),ClockwiseTransform(dotq6,dotq6z),Transform(dotq7,dotq7z),run_time=5)
       
        #Animiert Baumdiagramm1 über Baumdiagramm2 zu Häufigkeitsnetz
        self.play(Transform(dotp1,dotp1h),Transform(dotp2,dotp2h),Transform(dotp3,dotp3h),Transform(dotp4,dotp4h),Transform(dotp5,dotp5h),Transform(dotp6,dotp6h),Transform(dotp7,dotp7h),Transform(dotq1,dotq1h),Transform(dotq2,dotq2h),Transform(dotq3,dotq3h),Transform(dotq4,dotq4h),Transform(dotq5,dotq5h),Transform(dotq6,dotq6h),Transform(dotq7,dotq7h),run_time=5)
        self.wait(2)
        
        Tree1Root.color=WHITE
        Tree2Root.color=WHITE
        Tree1Grandchild1.color=WHITE
        Tree1Grandchild2.color=WHITE
        Tree1Grandchild3.color=WHITE
        Tree1Grandchild4.color=WHITE
        Tree2Grandchild1.color=WHITE
        Tree2Grandchild2.color=WHITE
        Tree2Grandchild3.color=WHITE
        Tree2Grandchild4.color=WHITE
        
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
        self.wait()

        
        self.remove(Tree1EdgeRootChild1,
        Tree1EdgeRootChild2,
        Tree2EdgeRootChild1,
        Tree2EdgeRootChild2,

        Tree1EdgeChild1Grandchild1,
        Tree1EdgeChild1Grandchild2,
        Tree1EdgeChild2Grandchild3,
        Tree1EdgeChild2Grandchild4,

        Tree2EdgeChild1Grandchild1,
        Tree2EdgeChild1Grandchild2,
        Tree2EdgeChild2Grandchild3,
        Tree2EdgeChild2Grandchild4)

        Tree1EdgeRootChild1=Line(dotp1.get_center(),dotp2.get_center(),color=BLUE)
        Tree1EdgeRootChild2=Line(dotp1.get_center(),dotp3.get_center(),color=BLUE)
        Tree1EdgeChild1Grandchild1=Line(dotp2.get_center(),dotp4.get_center(),color=RED)
        Tree1EdgeChild1Grandchild2=Line(dotp2.get_center(),dotp5.get_center(),color=RED)
        Tree1EdgeChild2Grandchild3=Line(dotp3.get_center(),dotp6.get_center(),color=RED)
        Tree1EdgeChild2Grandchild4=Line(dotp3.get_center(),dotp7.get_center(),color=RED)

        Tree2EdgeRootChild1=Line(dotq1.get_center(),dotq2.get_center(),color=BLUE)
        Tree2EdgeRootChild2= Line(dotq1.get_center(),dotq3.get_center(),color=BLUE)
        Tree2EdgeChild1Grandchild1= Line(dotq2.get_center(),dotq4.get_center(),color=RED)
        Tree2EdgeChild1Grandchild2=Line(dotq2.get_center(),dotq5.get_center(),color=RED)
        Tree2EdgeChild2Grandchild3= Line(dotq3.get_center(),dotq6.get_center(),color=RED)
        Tree2EdgeChild2Grandchild4=Line(dotq3.get_center(),dotq7.get_center(),color=RED)



        self.add(Tree1EdgeRootChild1,
        Tree1EdgeRootChild2,
        Tree2EdgeRootChild1,
        Tree2EdgeRootChild2,

        Tree1EdgeChild1Grandchild1,
        Tree1EdgeChild1Grandchild2,
        Tree1EdgeChild2Grandchild3,
        Tree1EdgeChild2Grandchild4,

        Tree2EdgeChild1Grandchild1,
        Tree2EdgeChild1Grandchild2,
        Tree2EdgeChild2Grandchild3,
        Tree2EdgeChild2Grandchild4)




        PvonN.next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer.next_to(Tree1EdgeRootChild2,LEFT,buff=0.1)
        PvonGBedN.next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)
        PvonGQuerBedN.next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)
        PvonGBedNQuer.next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)
        PvonGQuerBedNQuer.next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)
        PvonG.next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer.next_to(Tree2EdgeRootChild2,DOWN,buff=0.1)
        PvonNBedG.next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)
        PvonNQuerBedG.next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)
        PvonNBedGQuer.next_to(Tree2EdgeChild2Grandchild3,RIGHT,buff=0.1)
        PvonNQuerBedGQuer.next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        self.add(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer,PvonG,PvonGQuer,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        self.wait(5)

        EdgeRootNandG=DashedLine(Tree1Root,Tree1Grandchild1,dash_length=0.3,dashed_ratio=0.7,color=GREEN)
        EdgeRootNandGQuer=DashedLine(Tree1Root,Tree1Grandchild2,dash_length=0.3,dashed_ratio=0.7,color=GREEN)
        EdgeRootNQuerandG=DashedLine(Tree1Root,Tree1Grandchild3,dash_length=0.3,dashed_ratio=0.7,color=GREEN)
        EdgeRootNQuerandGQuer=DashedLine(Tree1Root,Tree1Grandchild4,dash_length=0.3,dashed_ratio=0.7,color=GREEN)
        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonN,LEFT, buff=0.6).shift([-0.2,0.2,0]).rotate(EdgeRootNandG.get_angle()-PI)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonN,RIGHT).shift([0,-0.2,0]).rotate(EdgeRootNandGQuer.get_angle())
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonNQuer,LEFT).shift([0.1,0.1,0]).rotate(EdgeRootNQuerandG.get_angle()-PI)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonNQuer,RIGHT).shift([0.4,-0.3,0]).rotate(EdgeRootNQuerandGQuer.get_angle())

        self.add(EdgeRootNandG,EdgeRootNandGQuer,EdgeRootNQuerandG,EdgeRootNQuerandGQuer,PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)
        self.wait(5)






class NurBaum1(Scene):
    def construct(self):
    #Knoten Baum 1
        Tree1Root=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Child1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Child2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Grandchild1=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Grandchild2=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Grandchild3=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree1Grandchild4=Rectangle(color='#FFFFFF', height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)

        KnotenBaum1=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)


        



        

        #Ausgangspositionen
        #Tree1
        p1= [0,2.4,0] #Root
        p2= [-3.5,0.3,0]      #Child1
        p3= [3.5,0.3,0]    #Child2
        p4= [-6,-2,0]   #Grandchild1
        p5= [-1.4,-2,0] #Grandchild2
        p6= [1.4,-2,0]   #Grandchild3
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

       
        
        


        #Nicht transparente Knoten
        Tree1Root.set_fill(BLACK, opacity=1)
        Tree1Child1.set_fill(BLACK, opacity=1)
        Tree1Child2.set_fill(BLACK, opacity=1)
        Tree1Grandchild1.set_fill(BLACK, opacity=1)
        Tree1Grandchild2.set_fill(BLACK, opacity=1)
        Tree1Grandchild3.set_fill(BLACK, opacity=1)
        Tree1Grandchild4.set_fill(BLACK, opacity=1)

        
        
        #Beschriftung Knoten
        #Tree1
        
        
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


        MengenInKnotenBaum1=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)


       

        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2).scale(1.2)

        HäufigkeitenBaum1=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)


       
        for x in range(len(KnotenBaum1)):
            KnotenBaum1[x].scale(1.2)
            MengenInKnotenBaum1[x].align_to(KnotenBaum1[x],UP).shift([0,-0.1,0])
            HäufigkeitenBaum1[x].move_to(KnotenBaum1[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        #Zielpositionen
        #Tree1
        p1z= [-3.75,-0.5,0] #Root
        p2z= [-3.75,2,0] #Child1
        p3z= [-3.75,-3,0]#Child2
        p4z= [-6,2,0]    #Grandchild1
        p5z= [-1.5,2,0]  #Grandchild2
        p6z= [-6,-3,0]   #Grandchild3
        p7z= [-1.5,-3,0] #Grandchild4

        dotp1z=Dot(p1z,fill_opacity=0)  #Root
        dotp2z=Dot(p2z,fill_opacity=0)  #Child1
        dotp3z=Dot(p3z,fill_opacity=0)  #Child2
        dotp4z=Dot(p4z,fill_opacity=0)  #Grandchild1
        dotp5z=Dot(p5z,fill_opacity=0)  #Grandchild2
        dotp6z=Dot(p6z,fill_opacity=0)  #Grandchild3
        dotp7z=Dot(p7z,fill_opacity=0)  #Grandchild4

        #Zielpositionen
        #Tree2
        q1z= [3.75,-0.5,0]        #Root
        q2z= [1.5,-0.5,0]         #Child1
        q3z= [6,-0.5,0]           #Child2
        q4z= [1.5,2,0]         #Grandchild1
        q5z= [1.5,-3,0]        #Grandchild2
        q6z= [6,2,0]           #Grandchild3
        q7z= [6,-3,0]          #Grandchild4

        dotq1z=Dot(q1z,fill_opacity=0)  #Root
        dotq2z=Dot(q2z,fill_opacity=0)  #Child1
        dotq3z=Dot(q3z,fill_opacity=0)  #Child2
        dotq4z=Dot(q4z,fill_opacity=0)  #Grandchild1
        dotq5z=Dot(q5z,fill_opacity=0)  #Grandchild2
        dotq6z=Dot(q6z,fill_opacity=0)  #Grandchild3
        dotq7z=Dot(q7z,fill_opacity=0)  #Grandchild4


        #Position Häufigkeitsnetz
        #Tree1
        p1h= [0,-0.5,0]        #Root
        p2h= [0,2,0]         #Child1
        p3h= [0,-3,0]           #Child2
        p4h= [-4,2,0]         #Grandchild1
        p5h= [4,2,0]        #Grandchild2
        p6h= [-4,-3,0]           #Grandchild3
        p7h= [4,-3,0]          #Grandchild4

        dotp1h=Dot(p1h,fill_opacity=0)  #Root
        dotp2h=Dot(p2h,fill_opacity=0)  #Child1
        dotp3h=Dot(p3h,fill_opacity=0)  #Child2
        dotp4h=Dot(p4h,fill_opacity=0)  #Grandchild1
        dotp5h=Dot(p5h,fill_opacity=0)  #Grandchild2
        dotp6h=Dot(p6h,fill_opacity=0)  #Grandchild3
        dotp7h=Dot(p7h,fill_opacity=0)  #Grandchild4



        


        #Tree2
        q1h= [0,-0.5,0]        #Root
        q2h= [-4,-0.5,0]         #Child1
        q3h= [4,-0.5,0]           #Child2
        q4h= [-4,2,0]         #Grandchild1
        q5h= [-4,-3,0]        #Grandchild2
        q6h= [4,2,0]           #Grandchild3
        q7h= [4,-3,0]          #Grandchild4

        dotq1h=Dot(q1h,fill_opacity=0)  #Root
        dotq2h=Dot(q2h,fill_opacity=0)  #Child1
        dotq3h=Dot(q3h,fill_opacity=0)  #Child2
        dotq4h=Dot(q4h,fill_opacity=0)  #Grandchild1
        dotq5h=Dot(q5h,fill_opacity=0)  #Grandchild2
        dotq6h=Dot(q6h,fill_opacity=0)  #Grandchild3
        dotq7h=Dot(q7h,fill_opacity=0)  #Grandchild4
    




        #Updater Text
        Tree1RootText.add_updater(lambda m: Tree1RootText.move_to(dotp1.get_center()))
        Tree1Child1Text.add_updater(lambda m: Tree1Child1Text.move_to(dotp2.get_center()))   
        Tree1Child2Text.add_updater(lambda m: Tree1Child2Text.move_to(dotp3.get_center())) 
        Tree1Grandchild1Text.add_updater(lambda m: Tree1Grandchild1Text.move_to(dotp4.get_center())) 
        Tree1Grandchild2Text.add_updater(lambda m: Tree1Grandchild2Text.move_to(dotp5.get_center())) 
        Tree1Grandchild3Text.add_updater(lambda m: Tree1Grandchild3Text.move_to(dotp6.get_center())) 
        Tree1Grandchild4Text.add_updater(lambda m: Tree1Grandchild4Text.move_to(dotp7.get_center())) 

       
    
        #Updater Knoten
        Tree1Root.add_updater(lambda m: Tree1Root.move_to(dotp1.get_center()))            
        Tree1Child1.add_updater(lambda m: Tree1Child1.move_to(dotp2.get_center()))            
        Tree1Child2.add_updater(lambda m: Tree1Child2.move_to(dotp3.get_center()))            
        Tree1Grandchild1.add_updater(lambda m: Tree1Grandchild1.move_to(dotp4.get_center()))            
        Tree1Grandchild2.add_updater(lambda m: Tree1Grandchild2.move_to(dotp5.get_center()))            
        Tree1Grandchild3.add_updater(lambda m: Tree1Grandchild3.move_to(dotp6.get_center()))            
        Tree1Grandchild4.add_updater(lambda m: Tree1Grandchild4.move_to(dotp7.get_center()))      

        

        #"Updater" Kanten
        Tree1EdgeRootChild1=always_redraw(lambda: Line(dotp1.get_center(),dotp2.get_center()))
        Tree1EdgeRootChild2=always_redraw(lambda: Line(dotp1.get_center(),dotp3.get_center()))
        Tree1EdgeChild1Grandchild1=always_redraw(lambda: Line(dotp2.get_center(),dotp4.get_center()))
        Tree1EdgeChild1Grandchild2=always_redraw(lambda: Line(dotp2.get_center(),dotp5.get_center()))
        Tree1EdgeChild2Grandchild3=always_redraw(lambda: Line(dotp3.get_center(),dotp6.get_center()))
        Tree1EdgeChild2Grandchild4=always_redraw(lambda: Line(dotp3.get_center(),dotp7.get_center()))

        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree1Child1,UP).shift([0.9,0.2,0])
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree1Child2,UP).shift([-0.9,0.2,0])
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP).shift([0,0,0])
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)
        PABSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,DOWN)
        PABQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,DOWN)
        PAQuerBSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,DOWN)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,DOWN)
        

        self.add(HäufigkeitenBaum1)

        #Zeichnet Baumdiagramm1 direkt
        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree1EdgeRootChild1,Tree1EdgeRootChild2,Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)
        
        self.add(PvonN,PvonNQuer)
       
        self.add(PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)
        self.add(PABSchnitt,PABQuerSchnitt,PAQuerBQuerSchnitt,PAQuerBSchnitt)

       
        #self.wait(3)


class NurBaum2(Scene):
    def construct(self):
    
        #Knoten Baum 2
        Tree2Root=Rectangle( height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Child1=Rectangle(height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Child2=Rectangle(height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Grandchild1=Rectangle(color=PURE_RED, height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Grandchild2=Rectangle(color=PURE_RED, height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Grandchild3=Rectangle(color=PURE_RED, height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)
        Tree2Grandchild4=Rectangle(color=PURE_RED, height=0.75, width=1.214).set_z_index(1).scale(1.2).scale(1.2)

        KnotenBaum2=VGroup(Tree2Root,Tree2Child1,Tree2Child2,Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4)

        #Tree1Root.color=RED


        

       


        #Ausgangspositionen
        #Tree2
        q1= [0,2.4,0] #Root
        q2= [-3.5,0.3,0]      #Child1
        q3= [3.5,0.3,0]    #Child2
        q4= [-6,-2,0]   #Grandchild1
        q5= [-1.4,-2,0] #Grandchild2
        q6= [1.4,-2,0]   #Grandchild3
        q7= [6,-2,0] #Grandchild4

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
       

        Tree2Root.set_fill(BLACK, opacity=1)
        Tree2Child1.set_fill(BLACK, opacity=1)
        Tree2Child2.set_fill(BLACK, opacity=1)
        Tree2Grandchild1.set_fill(BLACK, opacity=1)
        Tree2Grandchild2.set_fill(BLACK, opacity=1)
        Tree2Grandchild3.set_fill(BLACK, opacity=1)
        Tree2Grandchild4.set_fill(BLACK, opacity=1)
        
        #Beschriftung Knoten
       

        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Child1Text = Tex(r"$G$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Child2Text = Tex(r"$\bar{G}$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Grandchild1Text = Tex(r"$N\cap G$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild2Text = Tex(r"$\bar{N}\cap G$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild3Text = Tex(r"$N\cap\bar{G}$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild4Text = Tex(r"$\bar{N}\cap\bar{G}$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)
        MengenInKnotenBaum2=VGroup(Tree2RootText,Tree2Child1Text,Tree2Child2Text,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2).scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40,color=PURE_RED).set_z_index(2).scale(1.2)

        HäufigkeitenBaum2=VGroup(Tree2RootBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree2Grandchild1TextBetrag,Tree2Grandchild2TextBetrag,Tree2Grandchild3TextBetrag,Tree2Grandchild4TextBetrag)

        for x in range(len(KnotenBaum2)):
            KnotenBaum2[x].scale(1.2)
            MengenInKnotenBaum2[x].align_to(KnotenBaum2[x],UP).shift([0,-0.1,0])
            HäufigkeitenBaum2[x].move_to(KnotenBaum2[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

        #Updater Text


        Tree2RootText.add_updater(lambda m: Tree2RootText.move_to(dotq1.get_center()))
        Tree2Child1Text.add_updater(lambda m: Tree2Child1Text.move_to(dotq2.get_center()))   
        Tree2Child2Text.add_updater(lambda m: Tree2Child2Text.move_to(dotq3.get_center())) 
        Tree2Grandchild1Text.add_updater(lambda m: Tree2Grandchild1Text.move_to(dotq4.get_center())) 
        Tree2Grandchild2Text.add_updater(lambda m: Tree2Grandchild2Text.move_to(dotq5.get_center())) 
        Tree2Grandchild3Text.add_updater(lambda m: Tree2Grandchild3Text.move_to(dotq6.get_center())) 
        Tree2Grandchild4Text.add_updater(lambda m: Tree2Grandchild4Text.move_to(dotq7.get_center())) 
    
        #Updater Knoten
       
        Tree2Root.add_updater(lambda m: Tree2Root.move_to(dotq1.get_center()))            
        Tree2Child1.add_updater(lambda m: Tree2Child1.move_to(dotq2.get_center()))            
        Tree2Child2.add_updater(lambda m: Tree2Child2.move_to(dotq3.get_center()))            
        Tree2Grandchild1.add_updater(lambda m: Tree2Grandchild1.move_to(dotq4.get_center()))            
        Tree2Grandchild2.add_updater(lambda m: Tree2Grandchild2.move_to(dotq5.get_center()))            
        Tree2Grandchild3.add_updater(lambda m: Tree2Grandchild3.move_to(dotq6.get_center()))            
        Tree2Grandchild4.add_updater(lambda m: Tree2Grandchild4.move_to(dotq7.get_center()))   

        #"Updater" Kanten


        Tree2EdgeRootChild1=always_redraw(lambda: Line(dotq1.get_center(),dotq2.get_center()))
        Tree2EdgeRootChild2=always_redraw(lambda: Line(dotq1.get_center(),dotq3.get_center()))
        Tree2EdgeChild1Grandchild1=always_redraw(lambda: Line(dotq2.get_center(),dotq4.get_center()))
        Tree2EdgeChild1Grandchild2=always_redraw(lambda: Line(dotq2.get_center(),dotq5.get_center()))
        Tree2EdgeChild2Grandchild3=always_redraw(lambda: Line(dotq3.get_center(),dotq6.get_center()))
        Tree2EdgeChild2Grandchild4=always_redraw(lambda: Line(dotq3.get_center(),dotq7.get_center()))
        


        #Wahrscheinlichkeiten
    


        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree2Child1,UP).shift([0.9,0.1,0])
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).scale(1.2).next_to(Tree2Child2,UP).shift([-0.9,0.1,0])
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild1,UP).shift([0,0,0])
        PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)

        PABSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree2Grandchild1,DOWN)
        PABQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,DOWN)
        PAQuerBSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,DOWN)
        PAQuerBQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,DOWN)

        self.add(HäufigkeitenBaum2)

        
       
        #Zeichnet Baumdiagramm2 direkt
        self.add(Tree2Root,Tree2RootText)
        self.add(PABSchnitt,PABQuerSchnitt,PAQuerBQuerSchnitt,PAQuerBSchnitt)
       
        self.add(Tree2Child1,Tree2Child2,Tree2EdgeRootChild1,Tree2EdgeRootChild2,Tree2Child1Text,Tree2Child2Text)
       
        self.add(Tree2Grandchild1,Tree2Grandchild2,Tree2Grandchild3,Tree2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4,Tree2Grandchild1Text,Tree2Grandchild2Text,Tree2Grandchild3Text,Tree2Grandchild4Text)
      

        self.add(PvonG,PvonGQuer)

     

        self.add(PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        #self.wait(3)




class ZeichneHäufigkeitsnetzSchritt1(Scene):
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


        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Line(Tree1Root.get_top(),Tree1Child1.get_bottom())
        Tree1EdgeRootChild2=Line(Tree1Root.get_bottom(),Tree1Child2.get_top())
        Tree1EdgeChild1Grandchild1=Line(Tree1Child1,Tree1Grandchild1)
        Tree1EdgeChild1Grandchild2=Line(Tree1Child1,Tree1Grandchild2)
        Tree1EdgeChild2Grandchild3=Line(Tree1Child2,Tree1Grandchild3)
        Tree1EdgeChild2Grandchild4=Line(Tree1Child2,Tree1Grandchild4)

        Tree2EdgeRootChild1=Line(Tree1Root.get_left(),Tree2Child1.get_right())
        Tree2EdgeRootChild2=Line(Tree1Root.get_right(),Tree2Child2.get_left())


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild1,UP).shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        #PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild1,UP).shift([-0.4,0,0])
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2).set_color('#00B050')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text).set_color('#00B050')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag).set_color('#00B050')




        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1RootBetrag,Tree1RootText,Tree1Child1TextBetrag,Tree1Child1Text,Tree1Child2TextBetrag,Tree1Child2Text)

        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        self.add(Tree2Child1,Tree2Child2,Tree2Child1TextBetrag,Tree2Child1Text,Tree2Child2TextBetrag,Tree2Child2Text)

        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)

        self.add(PvonN,PvonNQuer,PvonG,PvonGQuer)



class ZeichneHäufigkeitsnetzSchritt2(Scene):
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


        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

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
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)
        PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT,buff=0.1)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)


        #PowerPointGrün: .set_color('#00B050')

        self.add(Tree1Root.set_color(PURE_RED),Tree1Child1,Tree1Child2,Tree1RootBetrag.set_color(PURE_RED),Tree1RootText.set_color(PURE_RED),Tree1Child1TextBetrag,Tree1Child1Text,Tree1Child2TextBetrag,Tree1Child2Text)

        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.add(PvonG,PvonGQuer,PvonN,PvonNQuer)

        
        
        
        
        
        self.add(Tree2Child1,Tree2Child2,Tree2Child1TextBetrag,Tree2Child1Text,Tree2Child2TextBetrag,Tree2Child2Text)

        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)






        self.add(Tree1Grandchild1.set_color(PURE_RED),Tree1Grandchild1Text.set_color(PURE_RED),Tree1Grandchild1TextBetrag.set_color(PURE_RED))

        self.add(Tree1EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild1)

        self.add(PvonGBedN,PvonNBedG)






        self.add(Tree1Grandchild3.set_color(PURE_RED),Tree1Grandchild3Text.set_color(PURE_RED),Tree1Grandchild3TextBetrag.set_color(PURE_RED))

        self.add(Tree1EdgeChild2Grandchild3,Tree2EdgeChild1Grandchild2)

        self.add(PvonGBedNQuer,PvonNQuerBedG)



        self.add(Tree1Grandchild2.set_color(PURE_RED),Tree1Grandchild2Text.set_color(PURE_RED),Tree1Grandchild2TextBetrag.set_color(PURE_RED))

        self.add(Tree1EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3)
        
        self.add(PvonGQuerBedN,PvonNBedGQuer)




        self.add(Tree1Grandchild4.set_color(PURE_RED),Tree1Grandchild4Text.set_color(PURE_RED),Tree1Grandchild4TextBetrag.set_color(PURE_RED))

        self.add(Tree1EdgeChild2Grandchild4,Tree2EdgeChild2Grandchild4)

        self.add(PvonGQuerBedNQuer,PvonNQuerBedGQuer)



class ZeichneHäufigkeitsnetzSchnittwahrscheinlichkeiten(Scene):
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


        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

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
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)
        PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT,buff=0.1)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)


        #PowerPointGrün: .set_color('#00B050')

        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1RootBetrag,Tree1RootText,Tree1Child1TextBetrag,Tree1Child1Text,Tree1Child2TextBetrag,Tree1Child2Text)

        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.add(PvonG,PvonGQuer,PvonN,PvonNQuer)

        
        
        
        
        
        self.add(Tree2Child1,Tree2Child2,Tree2Child1TextBetrag,Tree2Child1Text,Tree2Child2TextBetrag,Tree2Child2Text)

        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)






        self.add(Tree1Grandchild1,Tree1Grandchild1Text,Tree1Grandchild1TextBetrag)

        self.add(Tree1EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild1)

        self.add(PvonGBedN,PvonNBedG)






        self.add(Tree1Grandchild3,Tree1Grandchild3Text,Tree1Grandchild3TextBetrag)

        self.add(Tree1EdgeChild2Grandchild3,Tree2EdgeChild1Grandchild2)

        self.add(PvonGBedNQuer,PvonNQuerBedG)



        self.add(Tree1Grandchild2,Tree1Grandchild2Text,Tree1Grandchild2TextBetrag)

        self.add(Tree1EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3)
        
        self.add(PvonGQuerBedN,PvonNBedGQuer)




        self.add(Tree1Grandchild4,Tree1Grandchild4Text,Tree1Grandchild4TextBetrag)

        self.add(Tree1EdgeChild2Grandchild4,Tree2EdgeChild2Grandchild4)

        self.add(PvonGQuerBedNQuer,PvonNQuerBedGQuer)



        

        ArrowPNGSchnitt=Arrow(end=Tree1Grandchild1.get_corner(DOWN+RIGHT),start=Tree1Root.get_corner(UP+LEFT)).scale(1.25)
        EdgePNGQuerSchnitt=Arrow(end=Tree1Grandchild2.get_corner(DOWN+LEFT),start=Tree1Root.get_corner(UP+RIGHT)).scale(1.25)
        EdgePNQuerGSchnitt=Arrow(end=Tree1Grandchild3.get_corner(UP+RIGHT),start=Tree1Root.get_corner(DOWN+LEFT)).scale(1.25)
        EdgePNQuerGQuerSchnitt=Arrow(end=Tree1Grandchild4.get_corner(UP+LEFT),start=Tree1Root.get_corner(DOWN+RIGHT)).scale(1.25)

        self.add(ArrowPNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)


        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(ArrowPNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        self.add(Schnittwahrscheinlichkeiten)


class ZeichneHäufigkeitsnetzMitPfeilen(Scene):
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


        Tree1RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$|N|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$|\bar{N}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$|G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$|\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild1TextBetrag = Tex(r"$|N\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild2TextBetrag = Tex(r"$|\bar{N}\cap G|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild3TextBetrag = Tex(r"$|N\cap \bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Grandchild4TextBetrag = Tex(r"$|\bar{N}\cap\bar{G}|$",font_size=40).set_z_index(2)#.scale(1.2)

        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)

        for x in range(len(KnotenHäufigkeitsnetz)):
            KnotenHäufigkeitsnetz[x].scale(1.2)
            MengenInKnoten[x].align_to(KnotenHäufigkeitsnetz[x],UP).shift([0,-0.1,0])
            HäufigkeitenHäufigkeitsnetz[x].move_to(KnotenHäufigkeitsnetz[x].get_bottom()+[0,0.1,0],aligned_edge=DOWN)


        

          
         

        #"Updater" Kanten
        Tree1EdgeRootChild1=Arrow(start=Tree1Root.get_top(),end=Tree1Child1.get_bottom(),tip_length=0.3).scale(1.5)
        Tree1EdgeRootChild2=Arrow(start=Tree1Root.get_bottom(),end=Tree1Child2.get_top(),tip_length=0.3).scale(1.5)
        Tree1EdgeChild1Grandchild1=Arrow(start=Tree1Child1.get_left(),end=Tree1Grandchild1.get_right(),tip_length=0.3).scale(1.3)
        Tree1EdgeChild1Grandchild2=Arrow(start=Tree1Child1.get_right(),end=Tree1Grandchild2.get_left(),tip_length=0.3).scale(1.3)
        Tree1EdgeChild2Grandchild3=Arrow(start=Tree1Child2.get_left(),end=Tree1Grandchild3.get_right(),tip_length=0.3).scale(1.3)
        Tree1EdgeChild2Grandchild4=Arrow(start=Tree1Child2.get_right(),end=Tree1Grandchild4.get_left(),tip_length=0.3).scale(1.3)

        Tree2EdgeRootChild1=Arrow(start=Tree1Root.get_left(),end=Tree2Child1.get_right(),tip_length=0.3).scale(1.3)
        Tree2EdgeRootChild2=Arrow(start=Tree1Root.get_right(),end=Tree2Child2.get_left(),tip_length=0.3).scale(1.3)
        Tree2EdgeChild1Grandchild1=Arrow(start=Tree2Child1.get_top(),end=Tree1Grandchild1.get_bottom(),tip_length=0.3).scale(1.5)
        Tree2EdgeChild1Grandchild2=Arrow(start=Tree2Child1.get_bottom(),end=Tree1Grandchild3.get_top(),tip_length=0.3).scale(1.5)

        Tree2EdgeChild2Grandchild3=Arrow(start=Tree2Child2.get_top(),end=Tree1Grandchild2.get_bottom(),tip_length=0.3).scale(1.5)
        Tree2EdgeChild2Grandchild4=Arrow(start=Tree2Child2.get_bottom(),end=Tree1Grandchild4.get_top(),tip_length=0.3).scale(1.5)


        


        #Wahrscheinlichkeiten
        PvonN=Tex(r"$P(N)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{N})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$P_N(G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)
        PvonGQuerBedN=Tex(r"$P_N(\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{N}} (G)$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{N}} (\bar{G})$",font_size=40,color=RED).set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$P(G)$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{G})$",font_size=40,color=BLUE).set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_G(N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)
        PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT,buff=0.1)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color=RED).set_z_index(2).next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1,Tree1Child2,Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1,Tree2Child2)
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text,Tree1Child2Text,Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text,Tree2Child2Text)
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag)


        #PowerPointGrün: .set_color('#00B050')

        self.add(Tree1Root,Tree1Child1,Tree1Child2,Tree1RootBetrag,Tree1RootText,Tree1Child1TextBetrag,Tree1Child1Text,Tree1Child2TextBetrag,Tree1Child2Text)

        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)
        self.add(PvonG,PvonGQuer,PvonN,PvonNQuer)

        
        
        
        
        
        self.add(Tree2Child1,Tree2Child2,Tree2Child1TextBetrag,Tree2Child1Text,Tree2Child2TextBetrag,Tree2Child2Text)

        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)






        self.add(Tree1Grandchild1,Tree1Grandchild1Text,Tree1Grandchild1TextBetrag)

        self.add(Tree1EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild1)

        self.add(PvonGBedN,PvonNBedG)






        self.add(Tree1Grandchild3,Tree1Grandchild3Text,Tree1Grandchild3TextBetrag)

        self.add(Tree1EdgeChild2Grandchild3,Tree2EdgeChild1Grandchild2)

        self.add(PvonGBedNQuer,PvonNQuerBedG)



        self.add(Tree1Grandchild2,Tree1Grandchild2Text,Tree1Grandchild2TextBetrag)

        self.add(Tree1EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3)
        
        self.add(PvonGQuerBedN,PvonNBedGQuer)




        self.add(Tree1Grandchild4,Tree1Grandchild4Text,Tree1Grandchild4TextBetrag)

        self.add(Tree1EdgeChild2Grandchild4,Tree2EdgeChild2Grandchild4)

        self.add(PvonGQuerBedNQuer,PvonNQuerBedGQuer)



        

        ArrowPNGSchnitt=Arrow(end=Tree1Grandchild1.get_corner(DOWN+RIGHT),start=Tree1Root.get_corner(UP+LEFT),tip_length=0.3).scale(1.25)
        EdgePNGQuerSchnitt=Arrow(end=Tree1Grandchild2.get_corner(DOWN+LEFT),start=Tree1Root.get_corner(UP+RIGHT),tip_length=0.3).scale(1.25)
        EdgePNQuerGSchnitt=Arrow(end=Tree1Grandchild3.get_corner(UP+RIGHT),start=Tree1Root.get_corner(DOWN+LEFT),tip_length=0.3).scale(1.25)
        EdgePNQuerGQuerSchnitt=Arrow(end=Tree1Grandchild4.get_corner(UP+LEFT),start=Tree1Root.get_corner(DOWN+RIGHT),tip_length=0.3).scale(1.25)

        self.add(ArrowPNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        print(ArrowPNGSchnitt.get_tip_length(),Tree2EdgeChild1Grandchild1.get_tip_length())

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(ArrowPNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        self.add(Schnittwahrscheinlichkeiten)








        #PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonN,LEFT, buff=0.6).shift([-0.2,0.2,0]).rotate(EdgeRootNandG.get_angle()-PI)
        #PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonN,RIGHT).shift([0,-0.2,0]).rotate(EdgeRootNandGQuer.get_angle())
        #PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonNQuer,LEFT).shift([0.1,0.1,0]).rotate(EdgeRootNQuerandG.get_angle()-PI)
        #PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).scale(1.2).next_to(PvonNQuer,RIGHT).shift([0.4,-0.3,0]).rotate(EdgeRootNQuerandGQuer.get_angle())



class BeispielZeichneHäufigkeitsnetzErstesEreignis(Scene):
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
        Tree1Child1Text = Tex(r"$V$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{V}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$V\cap J$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$V\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$\bar{V}\cap J$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{V}\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$J$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{J}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$N\cap J$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$\bar{V}\cap J$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$V\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{V}\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$100.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$600$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$99.400$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$120$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$480$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$91.520$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$8.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$92.000$",font_size=40).set_z_index(2)#.scale(1.2)
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
        PvonN=Tex(r"$P(V)$",font_size=40,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$\frac{1}{5}$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild2,UP)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild3,UP)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{V}} (\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree1Grandchild4,UP).shift([0.4,0,0])

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_J(V)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2EdgeChild1Grandchild1,RIGHT,buff=0.1)#.shift([-0.4,0,0])
        #PvonNQuerBedG=Tex(r"$P_G(\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild2,UP)#.shift([-0.15,0,0])
        #PvonNBedGQuer=Tex(r"$P_{\bar{G}} (N)$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild3,UP)#.shift([0.15,0,0])
        #PvonNQuerBedGQuer=Tex(r"$P_{\bar{G}} (\bar{N})$",font_size=40,color='#FF0000').set_z_index(2).scale(1.2).next_to(Tree2Grandchild4,UP).shift([0.1,0,0])

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#0070C0'),Tree1Child2.set_color('#0070C0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color('#00B0F0'),Tree2Child2.set_color('#00B0F0'))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#0070C0'),Tree1Child2Text.set_color('#0070C0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color('#00B0F0'),Tree2Child2Text.set_color('#00B0F0'))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#0070C0'),Tree1Child2TextBetrag.set_color('#0070C0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color('#00B0F0'),Tree2Child2TextBetrag.set_color('#00B0F0'))#.set_color('#FFFFFF')




        self.add(Tree1Root.set_color('#FFFF00'),Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText.set_color('#FFFF00'))

        


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        self.add(Tree1Child1TextBetrag)
        self.add(Tree1RootBetrag.set_color('#FFFF00'))
        #self.add(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        self.add(PvonGBedN)

        self.add(PvonG)

        


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

        self.add(Tree1Grandchild1TextBetrag)
        self.add(Tree2Child1TextBetrag)
        self.add(Tree1Child2TextBetrag)
        self.add(Tree2Child2TextBetrag)
        
        
        
        self.add(Tree1Grandchild2TextBetrag)
        self.add(Tree1Grandchild3TextBetrag)
        self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(N\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(N\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{N}\cap G)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{N}\cap\bar{G})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        #self.add(Schnittwahrscheinlichkeiten)







class BeispielAnimationWahrscheinlichkeiten(Scene):
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
        Tree1Child1Text = Tex(r"$V$",font_size=40).set_z_index(2)
        Tree1Child2Text = Tex(r"$\bar{V}$",font_size=40).set_z_index(2)
        Tree1Grandchild1Text = Tex(r"$V\cap J$",font_size=40).set_z_index(2)
        Tree1Grandchild2Text = Tex(r"$V\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree1Grandchild3Text = Tex(r"$\bar{V}\cap J$",font_size=40).set_z_index(2)
        Tree1Grandchild4Text = Tex(r"$\bar{V}\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree1RootText.move_to(p1)
        Tree1Child1Text.move_to(p2)
        Tree1Child2Text.move_to(p3)
        Tree1Grandchild1Text.move_to(p4)
        Tree1Grandchild2Text.move_to(p5)
        Tree1Grandchild3Text.move_to(p6)
        Tree1Grandchild4Text.move_to(p7)




        #Tree2
        Tree2RootText = Tex(r"$\Omega$",font_size=40).set_z_index(2)
        Tree2Child1Text = Tex(r"$J$",font_size=40).set_z_index(2)
        Tree2Child2Text = Tex(r"$\bar{J}$",font_size=40).set_z_index(2)
        Tree2Grandchild1Text = Tex(r"$N\cap J$",font_size=40).set_z_index(2)
        Tree2Grandchild2Text = Tex(r"$\bar{V}\cap J$",font_size=40).set_z_index(2)
        Tree2Grandchild3Text = Tex(r"$V\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree2Grandchild4Text = Tex(r"$\bar{V}\cap\bar{J}$",font_size=40).set_z_index(2)
        Tree2RootText.move_to(q1)
        Tree2Child1Text.move_to(q2)
        Tree2Child2Text.move_to(q3)
        Tree2Grandchild1Text.move_to(q4)
        Tree2Grandchild2Text.move_to(q5)
        Tree2Grandchild3Text.move_to(q6)
        Tree2Grandchild4Text.move_to(q7)


        Tree1RootBetrag = Tex(r"$100.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child1TextBetrag = Tex(r"$600$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Child2TextBetrag = Tex(r"$99.400$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild1TextBetrag = Tex(r"$120$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild2TextBetrag = Tex(r"$7880$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild3TextBetrag = Tex(r"$480$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree1Grandchild4TextBetrag = Tex(r"$91.520$",font_size=40).set_z_index(2)#.scale(1.2)



        Tree2RootBetrag = Tex(r"$|\Omega|$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child1TextBetrag = Tex(r"$8.000$",font_size=40).set_z_index(2)#.scale(1.2)
        Tree2Child2TextBetrag = Tex(r"$92.000$",font_size=40).set_z_index(2)#.scale(1.2)
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
        PvonN=Tex(r"$P(V)$",font_size=40,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)
        PvonNQuer=Tex(r"$P(\bar{V})$",font_size=40 ,color='#0070C0').set_z_index(2).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)
        PvonGBedN=Tex(r"$\frac{1}{5}$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild1Grandchild1,UP,buff=0.1)#.shift([-0.1,0,0])
        PvonGQuerBedN=Tex(r"$P_V(\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild1Grandchild2,UP,buff=0.1)#.shift([-0.15,0,0])
        PvonGBedNQuer=Tex(r"$P_{\bar{V}} (J)$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild2Grandchild3,DOWN,buff=0.1)#.shift([0.15,0,0])
        PvonGQuerBedNQuer=Tex(r"$P_{\bar{V}} (\bar{J})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree1EdgeChild2Grandchild4,DOWN,buff=0.1)

        WahrscheinlichkeitenBaum1=VGroup(PvonN,PvonNQuer,PvonGBedN,PvonGQuerBedN,PvonGBedNQuer,PvonGQuerBedNQuer)

        PvonG=Tex(r"$8\%$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild1,UP,buff=0.1)
        PvonGQuer=Tex(r"$P(\bar{J})$",font_size=40,color='#00B0F0').set_z_index(2).next_to(Tree2EdgeRootChild2,UP,buff=0.1)
        PvonNBedG=Tex(r"$P_J(V)$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)#.shift([-0.4,0,0])
        PvonNQuerBedG=Tex(r"$P_J(\bar{V})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)#.shift([-0.15,0,0])
        PvonNBedGQuer=Tex(r"$P_{\bar{J}} (V)$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild2Grandchild3,RIGHT,buff=0.1)#.shift([0.15,0,0])
        PvonNQuerBedGQuer=Tex(r"$P_{\bar{J}} (\bar{V})$",font_size=40,color='#FF0000').set_z_index(2).next_to(Tree2EdgeChild2Grandchild4,RIGHT,buff=0.1)

        WahrscheinlichkeitenBaum2=VGroup(PvonG,PvonGQuer)#,PvonNBedG,PvonNQuerBedG,PvonNBedGQuer,PvonNQuerBedGQuer)
        KnotenHäufigkeitsnetz=VGroup(Tree1Root,Tree1Child1.set_color('#0070C0'),Tree1Child2.set_color('#0070C0'),Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4,Tree2Child1.set_color('#00B0F0'),Tree2Child2.set_color('#00B0F0'))#.set_color('#FFFFFF')
        MengenInKnoten=VGroup(Tree1RootText,Tree1Child1Text.set_color('#0070C0'),Tree1Child2Text.set_color('#0070C0'),Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text,Tree2Child1Text.set_color('#00B0F0'),Tree2Child2Text.set_color('#00B0F0'))#.set_color('#FFFFFF')
        HäufigkeitenHäufigkeitsnetz=VGroup(Tree1RootBetrag,Tree1Child1TextBetrag.set_color('#0070C0'),Tree1Child2TextBetrag.set_color('#0070C0'),Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag,Tree2Child1TextBetrag.set_color('#00B0F0'),Tree2Child2TextBetrag.set_color('#00B0F0'))#.set_color('#FFFFFF')




        self.add(Tree1Root.set_color('#FFFF00'),Tree1Child1,Tree1Child2,Tree2Child1,Tree2Child2)
        self.add(Tree1Grandchild1,Tree1Grandchild2,Tree1Grandchild3,Tree1Grandchild4)
        self.add(Tree1RootText.set_color('#FFFF00'))

        


        self.add(Tree1Child1Text,Tree1Child2Text)
        self.add(Tree2Child1Text,Tree2Child2Text)
        self.add(Tree1Grandchild1Text,Tree1Grandchild2Text,Tree1Grandchild3Text,Tree1Grandchild4Text)

        self.add(Tree1Child1TextBetrag)
        self.add(Tree1RootBetrag.set_color('#FFFF00'))
        #self.add(Tree1RootBetrag,Tree1Child1TextBetrag,Tree1Child2TextBetrag,Tree2Child1TextBetrag,Tree2Child2TextBetrag,Tree1Grandchild1TextBetrag,Tree1Grandchild2TextBetrag,Tree1Grandchild3TextBetrag,Tree1Grandchild4TextBetrag)
        self.add(PvonGBedN)

        self.add(PvonG)

        


        

        EdgePNGSchnitt=Line(Tree1Grandchild1.get_corner(DOWN+RIGHT),Tree1Root.get_corner(UP+LEFT))
        EdgePNGQuerSchnitt=Line(Tree1Grandchild2.get_corner(DOWN+LEFT),Tree1Root.get_corner(UP+RIGHT))
        EdgePNQuerGSchnitt=Line(Tree1Grandchild3.get_corner(UP+RIGHT),Tree1Root.get_corner(DOWN+LEFT))
        EdgePNQuerGQuerSchnitt=Line(Tree1Grandchild4.get_corner(UP+LEFT),Tree1Root.get_corner(DOWN+RIGHT))

        self.add(EdgePNGSchnitt,EdgePNGQuerSchnitt,EdgePNQuerGQuerSchnitt,EdgePNQuerGSchnitt)
        self.add(Tree2EdgeRootChild1,Tree2EdgeRootChild2)
        self.add(Tree1EdgeChild1Grandchild1,Tree1EdgeChild1Grandchild2,Tree1EdgeChild2Grandchild3,Tree1EdgeChild2Grandchild4,Tree2EdgeChild1Grandchild1,Tree2EdgeChild1Grandchild2,Tree2EdgeChild2Grandchild3,Tree2EdgeChild2Grandchild4)
        self.add(Tree1EdgeRootChild1,Tree1EdgeRootChild2)

        self.add(Tree1Grandchild1TextBetrag)
        self.add(Tree2Child1TextBetrag)
        self.add(Tree1Child2TextBetrag)
        self.add(Tree2Child2TextBetrag)
        
        
        
        self.add(Tree1Grandchild2TextBetrag)
        self.add(Tree1Grandchild3TextBetrag)
        self.add(Tree1Grandchild4TextBetrag)

        PNGSchnitt=Tex(r"$P(V\cap J)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)
        PNGQuerSchnitt= Tex(r"$P(V\cap\bar{J})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNGQuerSchnitt.get_center()).shift([0.8,-0.2,0])
        PNQuerGSchnitt = Tex(r"$P(\bar{V}\cap J)$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGSchnitt.get_center()).shift([0.8,-0.2,0])#.scale(1.2)
        PNQuerGQuerSchnitt = Tex(r"$P(\bar{V}\cap\bar{J})$",font_size=40,color=GREEN).set_z_index(2).move_to(EdgePNQuerGQuerSchnitt.get_center()).shift([0.8,0.2,0])#.scale(1.2)

        Schnittwahrscheinlichkeiten=VGroup(PNGSchnitt,PNGQuerSchnitt,PNQuerGSchnitt,PNQuerGQuerSchnitt)#.arrange(buff=1).next_to(Tree1Child2,DOWN, buff=0.25)

        self.add(Schnittwahrscheinlichkeiten)
        self.add(PvonN,PvonNQuer)
        self.add(PvonGQuer)
        self.add(PvonGBedNQuer,PvonGQuerBedN,PvonGQuerBedNQuer)
        self.add(PvonGQuer,PvonN,PvonNQuer)
        self.add(PvonNBedG,PvonNBedGQuer,PvonNQuerBedG,PvonNQuerBedGQuer)



        fractionV =VGroup(
                Tree1Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree1EdgeRootChild1,RIGHT,buff=0.1)

        fractionVQuer =VGroup(
                Tree1Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree1EdgeRootChild2,RIGHT,buff=0.1)

        fractionJQuer =VGroup(
                Tree2Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeRootChild2,RIGHT,buff=0.1)

        fractionVundJ =VGroup(
                Tree1Grandchild1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(EdgePNGSchnitt,RIGHT,buff=0.1)

        fractionVundJQuer =VGroup(
                Tree1Grandchild3TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(EdgePNGQuerSchnitt,RIGHT,buff=0.1)


        fractionVQuerundJ =VGroup(
                Tree1Grandchild2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(EdgePNQuerGSchnitt,RIGHT,buff=0.1)


        fractionVQuerundJQuer =VGroup(
                Tree1Grandchild4TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree1RootBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(EdgePNQuerGQuerSchnitt,RIGHT,buff=0.1)

        fractionVBedJ =VGroup(
                Tree1Grandchild1TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree2Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeChild1Grandchild1,LEFT,buff=0.1)

        fractionVQuerBedJ =VGroup(
                Tree1Grandchild2TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree2Child1TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeChild1Grandchild2,LEFT,buff=0.1)

        fractionVBedJQuer =VGroup(
                Tree1Grandchild3TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree2Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeChild2Grandchild3,LEFT,buff=0.1)

        fractionVQuerBedJQuer =VGroup(
                Tree1Grandchild4TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree2Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeChild2Grandchild4,LEFT,buff=0.1)

        fractionJQuerBedV =VGroup(
                Tree1Grandchild3TextBetrag.copy().set_color(BLACK).set_z_index(-1),
                Line(LEFT, RIGHT).match_width(Tree1RootBetrag),
                Tree2Child2TextBetrag.copy().set_color(BLACK).set_z_index(-1)
        ).arrange(DOWN,buff=0.05).next_to(Tree2EdgeChild2Grandchild3,LEFT,buff=0.1)


        self.wait(3)
        self.add(fractionV)
        self.play(Tree1Child1TextBetrag.copy().animate.move_to(fractionV[0]),Tree1RootBetrag.copy().animate.move_to(fractionV[2]),run_time=3)
        self.wait(5)


