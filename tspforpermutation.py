from sys import maxsize
from itertools import permutations

t = 4

def gezginSatici(graph, baslangic):
    
    tepeler = []                                                               #kaynak tepe noktası dışındaki tüm tepe noktalarını listeye eklenir.
    for i in range(t):
        if i != baslangic:
            tepeler.append(i)
            
    
    min_yol = maxsize                                                          #en kısa yolu Hamilton döngüsü mantığıyla saklanır.
    permutasyon = permutations(tepeler)
    
    for i in permutasyon:
        mevcut_yol = 0                                                         
        k = baslangic
        for j in i:
            mevcut_yol += graph[k][j]
            k = j
        mevcut_yol += graph[k][baslangic]    
        
        min_yol = min(min_yol , mevcut_yol)                                    #en kısa yol hangisiyse onu alırız.
        
    return min_yol    


if __name__ == "__main__":                                                                    
    baslangic = 0
    graph = [[0, 10, 15, 20],[10, 0, 35, 25],[15, 35, 0, 30],[20, 25, 30, 0]]
    
    print(gezginSatici(graph, baslangic))
    
            
    
        
    
                                    