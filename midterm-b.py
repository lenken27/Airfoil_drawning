# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:56:01 2019

@author: Emre
"""

#                               Part B  
# =============================================================================
def plot_airfoil(x,y,name,status):
        """
        plotting airfoil surfaces and adjusting the boundarys
        
        arg: two arrays of x and y and name of the airfoil 
        and status is the define the cusped or pointed
        
        return : None
        """
        
        plt.figure(figsize= (8,6))
        plt.ylim(ymax=.5)
        plt.ylim(ymin=-.5)
        # Name and Kutto conditoin type had wroten togetter on the up side.
        title=(str(name)+str(status))
        plt.title(title, fontsize=15)                                 
        plt.plot(x,y,'--')
        plt.xlabel("X Coordinates",fontsize=15)
        plt.ylabel("Y Coordinates",fontsize=15)
        plt.axes().set_aspect(1,'datalim')
# =============================================================================
    
# =============================================================================
def plot_meancamberline(x,y):
        """
        plotting mean camber line that is middle line between upper an lower lines.
        
        arg: two arrays of x and y.
        
        return : None
        """    
        mcly=[]
        mclx=[]
        # ran is the limit of the loop.     
        ran=(len(y)-1)/2
        for i in range(int(ran)):
            mcly.append((y[i]+y[-i-1])/2)
            mclx.append((x[i]+x[-i-1])/2)
        
        mcly.append(0)
        mclx.append(0)    
        plt.plot(mclx,mcly,'r-')
        plt.axes().set_aspect(1,'datalim')
# =============================================================================

# =============================================================================
def plot_chordline(x,y):
        """
        plotting the chord line that is line between fist and last x points.
        
        arg: two arrays of x and y.
        
        return : None
        """     
        clx=[]    
        cly=[]
        ran=(len(y)-1)/2    
        cly.append(y[0])
        clx.append(x[0])
        cly.append(y[int(ran)])
        clx.append(x[int(ran)])
        
        plt.plot(clx,cly,'g-')
        # That is neccessary for the set the aspect ratios of the figure.
        plt.axes().set_aspect(1,'datalim')
# =============================================================================

# =============================================================================
def max_thickness(x,y):
        """
        plotting the maximum thickness 
        the max distance between upper and lower surfaces.
    
        arg: two arrays of x and y.
        
        return : maximum thickness length.
        """     
        mt=0
        t=0
        ran=(len(y)-1)/2
        for i in range(int(ran)):
            t=(y[i]-y[-i-1])
        # in the following loop evaluate the maximum thickness for every loop
        # if the previous is bigger than other stay same.
            if t >= mt:
                mt=t
                location=i
        
        mtx=[]
        mty=[]
        mty.append(y[location])
        mtx.append(x[location])
        mty.append(y[-location-1])
        mtx.append(x[-location-1])
        plt.text(0.55,0.35,"Maximum Thickness location: "+str(mt)+"c")
        plt.plot(mtx,mty,'b-')
        plt.axes().set_aspect(1,'datalim')
        return mt
# =============================================================================