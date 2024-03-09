from annoy import AnnoyIndex
import os
import pickle

class VectorDB:
    def __init__(self, vector_length=512, index_file='vector_db.ann', metadata_file='vector_db_meta.pkl'):
        self.vector_length = vector_length
        self.index_file = index_file
        self.metadata_file = metadata_file
        self.index = AnnoyIndex(vector_length, 'angular')
        self.metadata = {}
        if os.path.exists(self.index_file) and os.path.exists(self.metadata_file):
            self.index.load(self.index_file)
            with open(self.metadata_file, 'rb') as f:
                self.metadata = pickle.load(f)

    def add_item(self, vector, metadata):
        item_index = len(self.metadata)
        self.index.add_item(item_index, vector)
        self.metadata[item_index] = metadata

    def build(self, n_trees=10):
        self.index.build(n_trees)
        self.index.save(self.index_file)
        with open(self.metadata_file, 'wb') as f:
            pickle.dump(self.metadata, f)

    def find_similar(self, vector, n=1):
        indices, distances = self.index.get_nns_by_vector(vector, n, include_distances=True)
        results = [(self.metadata[i], distances[i]) for i in indices]
        return results