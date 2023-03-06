import helper.data_handler as dh

if __name__ == '__main__':
    """Main function of the program"""
    distances = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')
    packages = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')

