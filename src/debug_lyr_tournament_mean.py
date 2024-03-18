import pandas as pd

if __name__ == "__main__":
    test_df = pd.read_csv("/Users/jackhu/Library/CloudStorage/OneDrive-UniversityofMiami/Documents/randomIdeas/data/240318160109.csv")
    # print(test_df.to_string())
    test_mean = test_df.mean()
    print(test_mean)

    # Perhaps it is the tuples?
    # test_df2 = pd.DataFrame({'a': [(0, 1), (1, 2)]})
    # print(test_df2.to_string())
    # test_mean_2 = test_df2.mean()
    # print(test_mean_2)
