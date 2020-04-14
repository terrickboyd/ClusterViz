# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:59:36 2020

@author: Terrick Boyd
"""

import PIL.ImageTk
import PIL.Image
from tkinter import *
print("importing libraries...")
from progress.bar import Bar
bar = Bar('Processing', max=17)
import tkinter as tk          
bar.next()      
from tkinter import font  as tkfont 
bar.next()
from tkinter import ttk
bar.next()
from tkinter import filedialog
bar.next()
import numpy as np
bar.next()
import pandas as pd
bar.next()
import matplotlib.pyplot as plt
bar.next()
from sklearn.manifold import Isomap
bar.next()
from sklearn.decomposition import SparsePCA
bar.next()
from sklearn.decomposition import PCA
bar.next()
from sklearn.manifold import TSNE
bar.next()
from sklearn.preprocessing import StandardScaler
bar.next()
from tkinter import  DISABLED
NORM_FONT = ("Helvetica", 10)
bar.finish()
print("Done importing libraries... ")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) 
        

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, so the one we want visible
        # can be raised above the others
        container = tk.Frame(self)
        #container.iconbitmap('clienticon.ico')
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    
       
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
   

        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
    def init_window(self):
            menu = Menu(self.container)
            self.container.config(menu=self.menu)
            #create file object for file button and add commands
            preprocess = Menu(menu)
            preprocess.add_command(label='Print')
            preprocess.add_command(label='Quit')
            preprocess.add_command(label='Save as...')
            #file.add_command(label='Exit', command = self.client_exit)
            menu.add_cascade(label='File', menu=preprocess)
            #create file object for home button
            home=Menu(menu)
            home.add_command(label='ClusterViz Home')
            menu.add_cascade(label='Home', menu=home)
            #create file object for visualization button
            visualization=Menu(self.menu)
            visualization=Menu(self.menu, tearoff=0)
            #create file object for tools button
            tools=Menu(menu)
            tools.add_command(label='Preferences')
            menu.add_cascade(label='Tools', menu=tools)
            
            #create undo object for undo and add commands
            edit=Menu(menu)
            edit.add_command(label='Redo')
            edit.add_command(label='Undo')
            menu.add_cascade(label='Edit', menu=edit)
            #create file object for help button
            help=Menu(menu)
            help.add_command(label='ClusterViz tutorial')
            help.add_command(label='About...')
            menu.add_cascade(label='Help', menu=help)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("ClusterViz")
        
        label = tk.Label(self, text="Welcome To ClusterViz", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Algorithms",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Information",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
#        self.menu = Menu(self.controller)
#        self.controller.config(menu=self.menu)
#        #create file object for file button and add commands
#        preprocess = Menu(self.menu)
#        preprocess.add_command(label='Print')
#        preprocess.add_command(label='Quit')
#        preprocess.add_command(label='Save as...')
#        #file.add_command(label='Exit', command = self.client_exit)
#        self.menu.add_cascade(label='Program', menu=preprocess)
#        #create file object for home button
#        self.home=Menu(self.menu)
#        self.home.add_command(label='ClusterViz Home')
#        self.menu.add_cascade(label='Home', menu=self.home)
#        #create file object for visualization button
#        visualization=Menu(self.menu)
#        visualization=Menu(self.menu, tearoff=0)
#        visualization.add_command(label='TSNE Parameters', command = lambda: self.popupmsg("""T-Distributed Stochastic Neighbor Embedding is a technique which attempts to keep the closest neighbors of each high-dimensional point the same in the low-dimensional projection by using pairwise distances as conditional probabilities of a point neighboring another point. """)
#        visualization.add_command(label='PCA Parameters', command = lambda: self.popupmsg("""Principal Component Analysis finds the principal components of a dataset. PCA transforms the data into a new, lower-dimensional subspace. In the new coordinate system, the first axis corresponds to the first principal component, which is the component that explains the greatest amount of the variance in the data.""")
#        visualization.add_command(label='Sparse PCA Parameters', command = lambda: self.popupmsg("""Sparse PCA is a  technique that extends the classic method of principal component analysis (PCA) for the reduction of dimensionality of data by introducing sparsity structures to the input variables.""")
#        visualization.add_command(label='ISOMAP Parameters', command = lambda: self.popupmsg("""Isomap is a nonlinear dimensionality reduction algorithm used for computing the low-dimensional embedding of a set of high-dimensional data points. The Isomap algorithm provides a simple method for estimating the intrinsic geometry of a data manifold based on a rough estimate of each data point’s neighbors on the manifold. """)
#        #create file object for tools button
#        self.tools=Menu(self.menu)
#        self.tools.add_command(label='Preferences')
#        self.menu.add_cascade(label='Tools', menu=self.tools)
#        
#        #create undo object for undo and add commands
#        self.edit=Menu(self.menu)
#        self.edit.add_command(label='Redo')
#        self.edit.add_command(label='Undo')
#        self.menu.add_cascade(label='Edit', menu=self.edit)
#        #create file object for help button
#        self.help=Menu(self.menu)
#        self.help.add_command(label='ClusterViz tutorial')
#        self.help.add_command(label='About...')
#        self.menu.add_cascade(label='Help', menu=self.help)
        
    def popupmsg(self,msg):
        popup = tk.Tk()
        popup.wm_title("Algorithm Descriptions")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller      
        label = tk.Label(self, text="ClusterViz", font=controller.title_font)
        label.grid(sticky="N")
        self._dataPane = tk.Frame(self)
        self._dataPane.grid(row = 1, column = 0)
        # select visualizer
        self.var1 = tk.StringVar (value = "Off")
        self.var2 = tk.StringVar (value = "Off")
        self.var3 = tk.StringVar (value = "Off")
        self.var4 = tk.StringVar (value = "Off")
        self.var5 = tk.StringVar (value = "Off")
        self._buttonPane = tk.Frame(self)
        self._buttonPane.grid(row = 0, column = 0)
        
        self.button1 = ttk.Button(self._buttonPane, text = "PCA",  command = self._OnClick1(self))
        self.button1.grid(row = 0, column = 1)
        self.button4 = ttk.Button(self._buttonPane, text = "TSNE", command = self._OnClick4(self))
        self.button4.grid(row= 0, column = 0)
        self.button2 = ttk.Button(self._buttonPane, text = "Sparse PCA",  command = self._OnClick2(self))
        self.button2.grid(row = 0, column = 4)
        self.button3 = ttk.Button(self._buttonPane, text = "ISOMAP",  command = self._OnClick3(self))
        self.button3.grid(row= 0, column = 5)
        self.button7=ttk.Button(self._buttonPane, text ="Algorithm Descriptions", command = lambda: self.popupmsg("""        T-Distributed Stochastic Neighbor Embedding is a technique which attempts to keep the closest neighbors of each high-dimensional point the same in the low-dimensional projection by using pairwise distances as conditional probabilities of a point neighboring another point. 

        Principal Component Analysis finds the principal components of a dataset. PCA transforms the data into a new, lower-dimensional subspace. In the new coordinate system, the first axis corresponds to the first principal component, which is the component that explains the greatest amount of the variance in the data.

        Sparse PCA is a  technique that extends the classic method of principal component analysis (PCA) for the reduction of dimensionality of data by introducing sparsity structures to the input variables.

        Isomap is a nonlinear dimensionality reduction algorithm used for computing the low-dimensional embedding of a set of high-dimensional data points. The Isomap algorithm provides a simple method for estimating the intrinsic geometry of a data manifold based on a rough estimate of each data point’s neighbors on the manifold. """))
        self.button7.grid(row= 0, column = 6)
        self.button5=ttk.Button(self._buttonPane, text ="Read Me", command = lambda: self.popupmsg("""        Algorithm buttons will remain disabled until both input .csv and label .csv files are selected! (Both files should have no header)

        First, click on input data and select any csv file you want to use, (must have no header) next click on label and select another csv file to use for the label(must also have no header).

        Finally select any of the algorithm buttons to begin creating scatter plots, all components will be saved to .xlsx files. """))
        self.button5.grid(row= 0, column = 7)
        self.button6=ttk.Button(self._dataPane, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        self.button6.grid(row= 0, column = 8)
        self.grid_rowconfigure(0, weight=1)
  
        self.databutton=ttk.Button(self._dataPane,  text ="*Open file...")
        self.databutton.grid(row= 0, column = 2)
       
        self.labelbutton=ttk.Button(self._dataPane,  text ="*Open label...", command=self.callback)
        self.labelbutton.grid(row= 0, column = 4, sticky =  "nsew")
        
        self.button7=ttk.Button(self._dataPane,  text ="Algorithm Parameters", command = lambda: self.popupmsg("""        T-Distributed Stochastic Neighbor Embedding has the following default parameters n_components=2, verbose=1, perplexity=40, number of iterations=300

        Principal Component Analysis has the following default parameters n_components=2

        Sparse PCA has the following default parameters n_components=2
        
        Isomap has the following default parameters n_components=2"""))
        self.button7.grid(row= 0, column = 6, sticky =  "nsew")
   
        # attach an event handler to the listBox when left mouse button is released
        self.labelbutton.bind("<ButtonRelease-1>", self.get)
        self.databutton.bind("<ButtonRelease-1>", self.getInput)
        self.button1.bind("<ButtonRelease-1>", self._OnClick1)
        self.button2.bind("<ButtonRelease-1>", self._OnClick2)
        self.button3.bind("<ButtonRelease-1>", self._OnClick3)
        self.button4.bind("<ButtonRelease-1>", self._OnClick4)
        
        self.button1.config(state = DISABLED)
        self.button2.config(state = DISABLED)
        self.button3.config(state = DISABLED)
        self.button4.config(state = DISABLED)
        

   
    def get(self, event):
        print("Please select file name for label: \n")
        self.labelVar = filedialog.askopenfilename(initialdir = "C:\\Users\\tb47\\Desktop\\GUI\\",title = "Select label file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.labelVar)
        return self.labelVar

                                  

    def getInput(self, event):
        print("Please select file name for data frame: \n")
        self.dfLabel = filedialog.askopenfilename(initialdir = "C:\\Users\\tb47\\Desktop\\GUI\\",title = "Select dataframe file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        print(self.dfLabel)
        return self.dfLabel

    def callback(self):
        self.button1['state'] = NORMAL
        self.button2['state'] = NORMAL
        self.button3['state'] = NORMAL
        self.button4['state'] = NORMAL
        

    def _OnClick1(self, event):
        if self.var1.get() == "Off":
            self.var1.set("On") 
        elif self.var1.get() == "On":
            self.var1.set("Off")
            print("PCA is running...")
            label = pd.read_csv(self.labelVar,header=None)[0].tolist()#,header=None
            df = pd.read_csv(self.dfLabel,header=None)
            data, label = df, label
            #Standdardize the data 
            data = StandardScaler().fit_transform(data)
            
            
            # apply PCA 
            pca = PCA(n_components= 2)
            
            # get 1st and 2nd components
            pca.fit(data)
            principalComponents = pca.fit_transform(data)
            principalDf = pd.DataFrame(data = principalComponents, columns = ['Component 1', 'Component 2'])
            print ("Our principal components are: ")
            print(principalComponents)
            X_r1 = principalComponents[:,0]
            X_r2 = principalComponents[:,1]
            unique = np.unique(label)
            print(len(np.unique(label)))
            try:
                plt.scatter(X_r1, X_r2, c = label)
            except:
                    print("Data matrix does not match label matrix (Select input file and label, remove headers)")
            name = 'PCA'  #CHANGE FILENAME HERE *************************************************************************
            plt.title(name  + " Clusters: " +  str(len(unique)))
            plt.savefig(name + ".png") 
            plt.show()
            plt.clf()
        
            # save  1st and 2nd components to csv     
            principalDf.to_excel("PCA_Components.xlsx") #Names of 1st and 2nd components to EXCEL here *************************************************************************
                       
    def _OnClick2(self, event):
        if self.var2.get() == "Off":
            self.var2.set("On") 
        elif self.var2.get() == "On":
            self.var2.set("Off")
            print("Sparse PCA is running...")
            label = pd.read_csv(self.labelVar,header=None)[0].tolist()
            df = pd.read_csv(self.dfLabel,header=None)
            data, label = df, label
            #Standdardize the data 
            data = StandardScaler().fit_transform(data)
           
            
            # apply PCA 
            sparsepca = SparsePCA(n_components= 2)
            
            # get 1st and 2nd components
            sparsepca.fit(data)
            SparseprincipalComponents = sparsepca.fit_transform(data)
            SparseprincipalDf = pd.DataFrame(data = SparseprincipalComponents, columns = ['Component 1', 'Component 2'])
            print ("Our principal components are: ")
            print(SparseprincipalComponents)
            X_r1 = SparseprincipalComponents[:,0]
            X_r2 = SparseprincipalComponents[:,1]
            unique = np.unique(label)
            print(len(np.unique(label))+"*************************")
            try:
                plt.scatter(X_r1, X_r2, c = label)
            except:
                print("Data matrix does not match label matrix (Select input file and label, remove headers)")
           
            name = 'Sparse_PCA'  #CHANGE FILENAME HERE *************************************************************************
            #plt.legend(unique, loc=8, ncol=5,fontsize='x-small')
            plt.title(name  + " Clusters: " +  str(len(unique)))
            plt.show()
            plt.savefig(name + ".png")
            plt.clf()
        
            # save  1st and 2nd components to csv     
            SparseprincipalDf.to_excel("Sparse_PCA_Components.xlsx") #Names of 1st and 2nd components to EXCEL here *************************************************************************
    def _OnClick3(self, event):
        if self.var3.get() == "Off":
            self.var3.set("On") 
        elif self.var3.get() == "On":
            self.var3.set("Off") 
            print("Isomap is running...")
            label = pd.read_csv(self.labelVar,header=None)[0].tolist() 
            df = pd.read_csv(self.dfLabel,header=None)
            array = df.copy()
            label = label
        
            iso = Isomap(n_components=2)
            iso.fit(array)
            manifold_2Da = iso.transform(df)
            manifold_2D = pd.DataFrame(manifold_2Da, columns=['Component 1', 'Component 2'])
            principalDf = pd.DataFrame(data = manifold_2Da, columns = ['Component 1', 'Component 2'])
        
            X1 = manifold_2D['Component 1']
            X2 = manifold_2D['Component 2']
        
            unique = np.unique(label)
           
            try:
                plt.scatter(X1, X2, c = label)    
            except:
                print("data matrix does not match label matrix (Select input file and label, remove headers)")
            
            #plt.legend(unique, loc=8, ncol=5,fontsize='x-small')
            name = 'ISOMAP' #CHANGE FILENAME HERE *************************************************************************
            
            plt.title(name  + " Clusters: " +  str(len(unique)) )  
            plt.savefig(name + ".png")
            plt.show()
            plt.clf()
            principalDf.to_excel("ISOMAP_COMPONENTS.xlsx") #Names of 1st and 2nd components to EXCEL here *************************************************************************
    def _OnClick4(self, event):
        if self.var5.get() == "Off":
            self.var5.set("On") 
        elif self.var5.get() == "On":
            self.var5.set("Off")          
            print("TSNE is running...")
            label = pd.read_csv(self.labelVar, header=None)[0].tolist() 
            df = pd.read_csv(self.dfLabel,header=None)
            tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
            tsne_results = tsne.fit_transform(df)
            principalDf = pd.DataFrame(data = tsne_results, columns = ['Component 1', 'Component 2'])
            
            X1 = tsne_results[:,0]
            X2 = tsne_results[:,1]
            unique = np.unique(label)
            name = "TSNE" #CHANGE FILENAME HERE *****************************************************************
            try:
                plt.scatter(X1, X2, c = label)   
            except:
                print("Data matrix does not match label matrix (Select input file and label, remove headers)")
            plt.title(name + " Clusters: " +  str(len(unique))  )  
            #plt.legend(unique, loc=8, ncol=5,fontsize='x-small')
           
            plt.savefig(name + ".png")
            plt.show()
            #close the file
            plt.clf()
            principalDf.to_excel("TSNE_Components.xlsx") #Names of components to EXCEL here **********************************************************
    def popupmsg(self,msg):
        popup = tk.Tk()
        popup.wm_title("Algorithm Descriptions")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="How To", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button2=tk.Button(self, text ="Read Me", command = lambda: self.popupmsg("""        Algorithm buttons will remain disabled until both input .csv and label .csv files are selected! (Both files should have no header)

        First, click on input data and select any csv file you want to use, (must have no header) next click on label and select another csv file to use for the label(must also have no header).

        Finally select any of the algorithm buttons to begin creating scatter plots, all components will be saved to .xlsx files. """))
        button2.pack()
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
    def popupmsg(self,msg):
        popup = tk.Tk()
        popup.wm_title("Algorithm Descriptions")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

       

if __name__ == "__main__":
    app = SampleApp()
    app.iconbitmap('clienticon.ico')
    app.mainloop()