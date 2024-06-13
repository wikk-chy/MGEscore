import pandas as pd
import csv
from tqdm import tqdm


def check_max_significance(lst, times, counts, threshold):
    max_value = max(lst)
    sorted_values = sorted(lst, reverse=True)
    second_largest_value = sorted_values[1]

    if max_value > times * second_largest_value and sum(counts) > threshold:
        return lst.index(max_value) + 1
    else:
        return 404

def cal_score(gene, rankings, i):
    score = rankings[gene].max() / rankings[gene][i]
    return score

def cal_mean_score(cell_types, cluster, gene_scores, footprint):
    cluster_score = []
    cluster = cell_types[cluster]
    for key in cluster:
        cluster_score.append(gene_scores[key])
    if len(cluster_score) > 1:
        mean_score = sum(cluster_score) / len(cluster_score)
        score = mean_score * footprint[0] + max(cluster_score) * footprint[1]
    else:
        score = cluster_score[0]
    return score

def get_result(result, mapping):
    return mapping.get(result, 'Undefined')

def deal_celltype_dict(cell_types):
    mapping = {idx + 1: cell_type for idx, cell_type in enumerate(cell_types.keys())}
    cluster_lst = list(cell_types.keys())
    column_names = [gene for genes in cell_types.values() for gene in genes]
    return mapping, cluster_lst, column_names

def define_celltype(matrix, cell_types,
              footprint, times, threshold):
    rankings = matrix.rank(method='min', ascending=False)
    mapping, cluster_lst, column_names = deal_celltype_dict(cell_types)
    with open('matrix-cluster-tmp.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['cluster'])
        for i in tqdm(range(len(rankings)), desc='Processing files'):
            gene_scores = {}
            for gene in column_names:
                gene_score = cal_score(gene, 
                                       rankings=rankings,
                                       i=i)
                gene_scores[gene] = gene_score
            cluster_scores = []
            for cluster in cluster_lst:
                cluster_score = cal_mean_score(cell_types, 
                                               cluster=cluster, 
                                               gene_scores=gene_scores,
                                               footprint=footprint)
                cluster_scores.append(cluster_score)

            counts = matrix.iloc[i, :]
            result = check_max_significance(cluster_scores,
                                            times=times,
                                            counts=counts,
                                            threshold=threshold)
            output = get_result(result, mapping=mapping)
            row = [output]
            writer.writerow(row)





