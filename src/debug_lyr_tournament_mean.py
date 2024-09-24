import pandas as pd
from more_itertools import collapse


def print_csv(csv_file_name: str):
    df = pd.read_csv(csv_file_name)
    print(df)


def my_mean(x):
    # should just be pairs of (primary, secondary)
    # df_to_text(x)
    assert len(x['matched_attr_tuples'].tolist()) == 2
    merged = list(collapse(
        [eval(l) for l in x['matched_attr_tuples'].tolist()], base_type=tuple))
    # return x.mean(numeric_only=True).concat(
    #     pd.Series([[eval(l) if type(l) is str else l for l in merged]],
    #               index=['matched_attr_tuples']))
    return pd.concat([x.mean(numeric_only=True), pd.Series([[eval(l) if type(l) is str else l for l in merged]], index=['matched_attr_tuples'])])


def test_case_1():
    test_df = pd.read_csv(
        "/Users/jackhu/Library/CloudStorage/OneDrive-UniversityofMiami/Documents/randomIdeas/data/240320153032.csv")
    test_mean = test_df.mean()
    print(test_mean)


def test_case_2():
    # Perhaps it is the tuples?
    test_df2 = pd.DataFrame({'a': [(0, 1), (1, 2)]})
    print(test_df2.to_string())
    test_mean_2 = test_df2.mean()
    print(test_mean_2)


def test_case_3():
    # load dfs.
    prim_matched = pd.read_csv('/Users/jackhu/Library/CloudStorage/OneDrive-UniversityofMiami/Documents/randomIdeas/data/240320153032.csv')
    matched = pd.read_csv('/Users/jackhu/Library/CloudStorage/OneDrive-UniversityofMiami/Documents/randomIdeas/data/240320153032a.csv')

    concat_df1 = pd.concat([prim_matched, matched])
    # print(concat_df1)

    # Operation on prim_matched involving reordering the concatenated dataframe
    # and stuff.
    col_mask = ['OutID', 'RAout', 'DECout', 'InID', 'RAin', 'DECin', 'pos_error_Temporary']

    # prim_matched = concat_df1.groupby(concat_df1.index).apply(my_mean).drop(
    #     columns=col_mask).rename(columns={'match_err': 'pos_error_Temporary'})
    prim_matched = concat_df1.groupby(concat_df1.index).apply(my_mean)
    # prim_matched = concat_df1.groupby(concat_df1.index)['matched_attr_tuples']

    print(prim_matched)


if __name__ == "__main__":
    # Do test case(s).
    test_case_3()
