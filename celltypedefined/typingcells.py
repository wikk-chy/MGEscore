from .utils import define_celltype
import pandas as pd

def typing_matrix(input_path, cell_types, 
                  footprint=[0.7, 0.3], times=1.5, threshold=3):
    matrix = pd.read_csv(input_path, index_col='cell')
    define_celltype(matrix, cell_types,
              footprint=footprint, times=times, threshold=threshold)
    df1 = pd.read_csv(input_path, index_col=None)
    df2 = pd.read_csv('matrix-cluster-tmp.csv', index_col=None)
    merged_df = pd.concat([df1, df2], axis=1)
    return merged_df
    
    

