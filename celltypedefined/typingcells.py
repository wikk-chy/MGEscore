from .utils import define_celltype, deal_celltype_dict
import pandas as pd

###cell_dict
# cell_types = {
#     'B_cells': ['Dennd5b', 'Pax5'],
#     'T_cells': ['Cd28'],
#     'NK_cells': ['Il2rb', 'Cd7'],
#     'Neutrophils': ['G0s2'],
#     'Macrophages': ['Il1r2'],
#     'Fibroblasts': ['Col1a1', 'Apoa1'],
#     'Epithelial_cells': ['Sftpc'],
#     'Endothelial_cells': ['Npr3', 'Vwf']
# }

def typing_matrix(input_path, cell_types, 
                  footprint=[0.7, 0.3], times=1.5, threshold=3):
    matrix = pd.read_csv(input_path, index_col='cell')
    define_celltype(matrix, cell_types,
              footprint=footprint, times=times, threshold=threshold)
    df1 = pd.read_csv(input_path, index_col=None)
    df2 = pd.read_csv('matrix-cluster-tmp.csv', index_col=None)
    merged_df = pd.concat([df1, df2], axis=1)
    return merged_df
    
    

