'''
Created on:	Dec 20120

@author: Oualid

'''
import copy
import numpy as np
import matplotlib.pyplot as plt

class mamLD(object):
        
    def __init__(self, same_range):
        self.same_range = same_range

        
    def levenshtein_distance(self,in_path1, in_path2):
        path1 = copy.deepcopy(in_path1)
        path2 = copy.deepcopy(in_path2)
        
        path1_len = len(path1) # nombre de points du scanpath1 
        path2_len = len(path2) # nombre de points du scanpath2

        dist_mat = [[0]*(path2_len+1) for _ in range(path1_len+1)] 

        for i in range(1, path1_len+1):
            dist_mat[i][0] = i
        for j in range(1, path2_len+1):
            dist_mat[0][j] = j
        for i in range(1, path1_len+1):
            for j in range(1, path2_len+1):
                if( self._is_same_block(path1[i-1], path2[j-1]) ): #cela signifie qu'ils sont a une distance très petite (plus petit que le seuil) donc on dit qu'ils sont situés sur le même point/région 
                    dist_mat[i][j] = dist_mat[i-1][j-1] 
                else:
                    dist_mat[i][j] = min(
                        dist_mat[i-1][j]+1, # delete
                        dist_mat[i][j-1]+1, # insert
                        dist_mat[i-1][j-1]+1 # subistition
                    )
        return dist_mat[path1_len][path2_len]
    
    def _is_same_block(self, p1, p2):
            dist = self._calc_distance(p1, p2)
            if dist <= self.same_range:
                res = True
            else:
                res = False
            return res
        
    def _calc_distance(self, point1, point2):
        point1 = np.array(point1)
        point2 = np.array(point2)
        res = np.sqrt(np.sum((point1 - point2)**2))
        return res 
    
    
        

if __name__ == "__main__":
    a=[[88, 24,12], [56, 56,65], [40, 88,98]] #notre scanpath
    b=[[29, 15,34], [56, 56,65], [40, 88,98]]
    #b=[[72, 24,35], [56, 56,56], [40, 88,76]] #vrai scanapath
    ### test case: point
    mamLD = mamLD(same_range=5) # same_range c'est le seuil à partir lequelle on peut dire que deux points sont égaux
    print(mamLD.levenshtein_distance(a,b)) #donne le nombre de modifications à effectuer pour avoir deux scanpath égaux
       
