# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:56:34 2019

@author: Emre
"""

                                        #Part C 
# =============================================================================
def plot_panels(x,y,N):
        """
        plotting the panels normal with aid of the circle attibutes. 
    
        arg: two arrays of x,y and number of the panel number With N.
        
        return : None.
        """                                    
        N=N+2                                                                     
        R = (x.max() - x.min()) / 2  # radius of the circle
        x_center = (x.max() + x.min()) / 2  # x-coord of the center
        # define x-coord of the circle points
        x_circle = x_center + R * np.cos(np.linspace(0.0, 2 * math.pi, N +1)) 
        x_ends = np.copy(x_circle)  # projection of the x-coord on the surface
        y_ends = np.empty_like(x_ends)  # initialization of the y-coord Numpy array
           
        #x, y = np.append(x, x[0]), np.append(y, y[0])  # extend arrays using numpy.append 
        
        I = 0
        for i in range(N):
            while I < len(x) :
                if (x[I] <= x_ends[i] <= x[I + 1]) or (x[I + 1] <= x_ends[i] <= x[I]):
                    break
                else:
                    I += 1
            a = (y[I + 1] - y[I]) / (x[I + 1] - x[I]) # a is the slope 
            b = y[I + 1] - a * x[I + 1]   # b is evaluating with aid of the a.
            y_ends[i] = a * x_ends[i] + b
        y_ends[N] = y_ends[0]
    
        tx=x_ends[1:]-x_ends[:-1]
        ty=y_ends[1:]-y_ends[:-1]  
        nx=ty
        ny=-tx
        n_ = (nx**2+ny**2)**.5
        nx=nx/n_
        ny=ny/n_
        
        #Create list from the array for using pop command.
        x_ends=list(x_ends) 
        y_ends=list(y_ends)
        nx=list(nx)
        ny=list(ny)
        #Remove the first and end point for does not create normal.
        x_ends.pop()
        y_ends.pop()
        y_ends.pop(0)
        x_ends.pop(0)
        x_ends.pop(int(N/2)-1)
        y_ends.pop(int(N/2)-1)
        nx.pop(int(N/2)-1)
        ny.pop(int(N/2)-1)
        
        plt.quiver(x_ends,y_ends,nx,ny)
        return                               
# =============================================================================


# =============================================================================
def is_cusped(x,y):
        """
        Evaluating the is this airfoil Cusped or Pointed
    
        arg: two arrays of x and y.
        
        return : type of the trailing edge with string type.
        """ 
        # Exceed of the limit it is becoming pointed edge.
        limit = np.deg2rad(15)                                
        upper_slope = (y[0]-y[1])/(x[0]-x[1])                                   
        lower_slope = (y[-1]-y[-2])/(x[-1]-x[-2]) 
        
        # theta is the angle between upper and lower trailing edge surfaces.
        theta =np.arctan(upper_slope)-np.arctan(lower_slope)  
        
        if abs(theta) <= limit:
            status=('(Cusped)')
        else:
            status=('(Pointed)')
        return status