import pandas as pd
import numpy as np
import sys
import os
import pydot
from treelib import Tree, Node
import class_tree_node as diag_tree

"""
Description: This function creates slices of data, a slice is all the nodes that lie under a single parent
this is done to avoid id confusion among nodes, as it was found that some parents/leaves had the same id
plus it will be easy to build a tree for each slice. 
"""


def create_index_data_slices(data):
    data_slices = []
    current_parent_index = 0
    for i, row in data.iterrows():
        if row['parent_id'] == 1 or row['parent_id'] == 2:
            if i > 0:
                data_slices.append([current_parent_index, i-1])
            current_parent_index = i
    return data_slices
    pass


"""
Description: This function creates dictionary of automd questions 
"""


def create_ques_dictionary(data):
    data_dict = {}
    for index, row in data.iterrows():
        if row['id'] not in data_dict:
            data_dict[row['id']] = row['question']
        pass
    return data_dict
    pass


"""
Description: This function will create a tree from the data slice
"""


def visualise_tree_from_slice(data):
    tree = Tree()
    for index, item in data.iterrows():
        if not tree.contains(item['id']):
            if item['parent_id'] == 1 or item['parent_id'] ==2:
                tree.create_node(item['answer'], item['id'])
            else:
                tree.create_node(item['answer'], item['id'], parent=item['parent_id'])
    tree.show()
    return tree
    pass


def build_tree_from_slice(data, ques_dict):
    leaf_nodes_list = data[data['difficulty'].notnull()]
    tree = diag_tree.ym_diag_tree()
    for index, item in data.iterrows():
        if item['parent_id'] == 1 or item['parent_id'] == 2:
            # root node
            tree.add_node(item['id'], ques_dict[item['id']], item['answer'], -1, False)
        else:
            if item['id'] not in list(leaf_nodes_list['id']):
                if item['id'] not in ques_dict:
                    tree.add_node(item['id'], '', item['answer'], item['parent_id'], False)
                else:
                    tree.add_node(item['id'], ques_dict[item['id']], item['answer'], item['parent_id'], False)
            else:
                # leaf nodes = no questions
                tree.add_node(item['id'], '', item['answer'], item['parent_id'], True)
    return tree
    pass


def main():
    ans_data = []
    ques_data = []
    ans_file_path = os.getcwd() + '/automd_data/automd_answers.csv'
    ques_file_path = os.getcwd() + '/automd_data/automd_questions.csv'
    if os.path.isfile(ans_file_path):
        ans_data = pd.read_csv(ans_file_path, error_bad_lines=False)
    if os.path.isfile(ques_file_path):
        ques_data = pd.read_csv(ques_file_path, error_bad_lines=False)
    # get data slices
    data_slices = create_index_data_slices(ans_data)
    ques_dict = create_ques_dictionary(ques_data)
    print("data slices: ")
    print(data_slices)
    # leaf nodes
    leaf_nodes = ans_data[ans_data['difficulty'].notnull()]
    forest = []
    for slice in data_slices:
        temp_tree = build_tree_from_slice(ans_data.iloc[slice[0]:slice[1]], ques_dict)
        temp_tree.show_tree(temp_tree.root, '|____')
        temp_tree.traverse_tree();
        forest.append(temp_tree)
        input("Press enter to continue...")
        pass
    # visualise_tree_from_slice(ans_data.iloc[slice[0]:slice[1]])
    # for tree in forest:
    #     tree.search_sent('Feel - I feel it (i.e. hesitation, shimmy, vibration, or a pull)--Drifts- Gradual movements to one side.')
    #     pass
    pass


main()


