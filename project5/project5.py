import hashlib
import time

class MerkleTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.levels = []
        self.build_tree()

    def build_tree(self):
        current_level = self.leaves

        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                if i+1 < len(current_level):
                    node_hash = self._hash_nodes(current_level[i], current_level[i+1])
                else:
                    node_hash = self._hash_nodes(current_level[i], current_level[i])
                next_level.append(node_hash)
            current_level = next_level
            self.levels.append(current_level)

    def get_root_hash(self):
        if len(self.levels) > 0:
            return self.levels[-1][0]
        else:
            return None

    def _hash_nodes(self, node1, node2):
        concat_data = str(node1) + str(node2)
        return hashlib.sha256(concat_data.encode('utf-8')).hexdigest()

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution Time: {:.6f} seconds".format(execution_time))
        return result
    return wrapper

# 测试代码
@measure_execution_time
def test_merkle_tree():
    leaves = [1, 2, 3, 4, 5, 6, 7, 8]
    tree = MerkleTree(leaves)
    root_hash = tree.get_root_hash()
    print('Root hash:', root_hash)

test_merkle_tree()