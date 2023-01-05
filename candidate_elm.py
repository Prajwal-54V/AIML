
import numpy as np
import pandas as pd
data = pd.DataFrame(pd.read_csv('3.csv'))
concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])


def learn(concepts, target):
    specific_h = concepts[0].copy()
    
    print("Initial specific hypothesis\n",specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range (len(specific_h))]
    print("Initital General hypothesis\n",general_h)
   
    for i, h in enumerate(concepts):
        if target[i] == "Y":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "N":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print("steps of Candidate Elemination Algorithem",i+1)
        print("Instance",h)
        print("S",i+1,'=',specific_h)
        print("G",i+1,'=',general_h) 
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices: 
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h, general_h
s_final, g_final = learn(concepts, target)
print("Final Specific hypothesis", s_final, sep="\n")
print("Final General hypothesis",g_final,sep='\n')


# import csv
# def get_domains(examples):
#     d = [set() for i in examples[0]]
    
#     for x in examples:
#         for i, xi in enumerate(x):
#             d[i].add(xi)
#     return [list(sorted(x)) for x in d]

# def more_general(h1, h2):
#     more_general_parts = []
#     for x, y in zip(h1, h2):
#         #print("More:",x,y)
#         mg = x == "?" or (x != "0" and (x == y or y == "0"))
#         more_general_parts.append(mg)
#     return all(more_general_parts)

# def fulfills(example, hypothesis):
#     return more_general(hypothesis, example)

# def min_generalizations(h, x):
#     h_new = list(h)
#     for i in range(len(h)):
#         if not fulfills(x[i:i+1], h[i:i+1]):
#             h_new[i] = '?' if h[i] != '0' else x[i]
#     return [tuple(h_new)]

# def min_specializations(h, domains, x):
#     results = []
#     for i in range(len(h)):
#         if h[i] == "?":
#             for val in domains[i]:
#                 if x[i] != val:
#                     h_new = h[:i] + (val,) + h[i+1:]
#                     results.append(h_new)
#         elif h[i] != "0":
#             h_new = h[:i] + ('0',) + h[i+1:]
#             results.append(h_new)
#     return results
                
# def generalize_S(x, G, S):
#     S_prev = list(S)
  
#     for s in S_prev:
#         #print(s)
#         if s not in S:
#             continue
#         if not fulfills(x, s):
#             S.remove(s)
#             Splus = min_generalizations(s, x)
            
#             S.update([h for h in Splus if any([more_general(g,h) for g in G])])
          
#             S.difference_update([h for h in S if any([more_general(h, h1) for h1 in S if h != h1])])
        
#     return S

# def specialize_G(x, domains, G, S):
#     G_prev = list(G)
#     for g in G_prev:
#         if g not in G:
#             continue
#         if fulfills(x, g):
#             G.remove(g)
#             Gminus = min_specializations(g, domains, x)
#             G.update([h for h in Gminus if any([more_general(h, s) for s in S])])
#             G.difference_update([h for h in G if any([more_general(g1, h) for g1 in G if h != g1])])
            
#     return G

# def candidate_elimination(examples):
#     domains = get_domains(examples)[:-1] 
#     print("It's me:",domains)
#     n = len(domains)
#     G = set([("?",)*n])
#     S = set([("0",)*n])
#     print("Maximally specific hypotheses - S ")
#     print("Maximally general hypotheses - G ")
#     i=0
#     print("\nS[0]:",str(S),"\nG[0]:",str(G))
#     for xcx in examples:
#         i=i+1
#         x, cx = xcx[:-1], xcx[-1]
#         if cx=='Y': 
#             G = {g for g in G if fulfills(x, g)}
#             S = generalize_S(x, G, S)
#         else:
#             S = {s for s in S if not fulfills(x, s)}
#             G = specialize_G(x, domains, G, S)
#         print("\nS[{0}]:".format(i),S)
#         print("G[{0}]:".format(i),G)
#     return

# with open('3.csv') as csvFile:
#     examples = [tuple(line) for line in csv.reader(csvFile)]
# #print(examples) 
    
# candidate_elimination(examples)
