import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    df = np.array (list)
    mean_rows = [df[[0, 1, 2]].mean(), df[[3, 4, 5]].mean(), df[[6, 7, 8]].mean()]
    mean_columns = [df[[0, 3, 6]].mean(), df[[1, 4, 7]].mean(), df[[2, 5, 8]].mean()]    
    
    var_rows = [df[[0, 1, 2]].var(), df[[3, 4, 5]].var(), df[[6, 7, 8]].var()]
    var_columns = [df[[0, 3, 6]].var(), df[[1, 4, 7]].var(), df[[2, 5, 8]].var()]   

    std_rows = [df[[0, 1, 2]].std(), df[[3, 4, 5]].std(), df[[6, 7, 8]].std()]
    std_columns = [df[[0, 3, 6]].std(), df[[1, 4, 7]].std(), df[[2, 5, 8]].std()]   

    max_rows = [df[[0, 1, 2]].max(), df[[3, 4, 5]].max(), df[[6, 7, 8]].max()]
    max_columns = [df[[0, 3, 6]].max(), df[[1, 4, 7]].max(), df[[2, 5, 8]].max()]   

    min_rows = [df[[0, 1, 2]].min(), df[[3, 4, 5]].min(), df[[6, 7, 8]].min()]
    min_columns = [df[[0, 3, 6]].min(), df[[1, 4, 7]].min(), df[[2, 5, 8]].min()]  

    sum_rows = [df[[0, 1, 2]].sum(), df[[3, 4, 5]].sum(), df[[6, 7, 8]].sum()]
    sum_columns = [df[[0, 3, 6]].sum(), df[[1, 4, 7]].sum(), df[[2, 5, 8]].sum()]  

    return {
        'mean':[mean_columns, mean_rows, df.mean()],
        'variance': [var_columns, var_rows, df.var()],
        'standard deviation': [std_columns, std_rows, df.std()],
        'max': [max_columns, max_rows, df.max()],
        'min': [min_columns, min_rows, df.min()],
        'sum': [sum_columns, sum_rows, df.sum()]
    }