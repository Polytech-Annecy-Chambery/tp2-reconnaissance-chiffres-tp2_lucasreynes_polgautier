from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        
        for i in range(self.H):
            for c in range (self.W):
                if self.pixels[i][c] <= S:
                    im_bin.pixels [i][c]=0
                else
                    im_bin.pixels [i][c]=255
        return im_bin
                
    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
         new_im = Image()
        
        Lmin = self.H-1
        Lmax = 0
        Cmin = self.H-1
        Cmax = 0
        
        for l in range (self.H):
            for c in range (self.W):
                if self.pixels[l][c] == 0:
                    
                    if l<Lmin :
                        Lmin = l
                    if l>Lmax :
                        Lmax = l
                    if c<Cmin :
                        Cmin = c
                    if c>Cmax :
                        Cmax = c
            new_im.set_pixels(self.pixels[Lmin :Lmax+1, Cmin:Cmax+1])
            return new_im
                        

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        
        im_res = Image()
        
        pixels_resized = resize(self.pixels, (new_H,new_W), 0)
        im_res.set_pixels(np.uint8(pixels_resized*255))
        
        return im_res


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
          def similitude(self, im):
      n=0
      for l in range(self.H):
            for c in range(self.W) :
                if self.pixels[l][c] == im.pixel[l][c]:
                    n+=1
                return n/(self.H*self.W)

