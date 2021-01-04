# Quantile is a generalization of the median and represents the value under which 
# a certain percentile of the data lies. The median represents the value under which 
# 50% of the data lies. 

def quantile(the_list, percent):
    ''' Returns the pth value (percentile) in the_list'''
    p_index = int(percent * len(the_list))
    return sorted(the_list)[p_index]

