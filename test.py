import os
import pandas as pd
from celltypedefined.typingcells import typing_matrix

cell_types = {
    'B_cells': ['Cd79a', 'Bank1'],
    'T_cells': ['St8sia6'],
    'NK_cells': ['Ccl5', 'Gzma'],
    'Neutrophils': ['S100a8', 'S100a9', 'Retnlg'],
    'Macrophages': ['Kcnip4', 'Chil3'],
    'Fibroblasts': ['Col3a1', 'Col1a2'],
    'Epithelial_cells': ['Sftpb', 'Sftpa1'],
    'Endothelial_cells': ['Prickle2', 'Cldn5']
}
os.makedirs('results', exist_ok=True)

for file in os.listdir('Demo'):
    input = os.path.join('Demo', file)
    results = typing_matrix(input, cell_types, 
                            footprint=[0.4, 0.6], 
                            times=1.1, threshold=2)
    id = file.split('.')[0]
    results.to_csv(f'./results/{id}-cluster.csv')