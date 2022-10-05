# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.find_and_compress(src)
        dst_parent = self.find_and_compress(dst)

        if src_parent == dst_parent:
            return

        src_rank = self.ranks[src_parent]
        dst_rank = self.ranks[dst_parent]

        if src_rank < dst_rank:
            # "Copy" over rows (i.e. update row count of destination parent)
            self.row_counts[dst_parent] += self.row_counts[src_parent]

            # "Erase file content" (i.e. change row count to 0 for source parent)
            self.row_counts[src_parent] = 0

            # "Create symlink" (i.e. update "pointer" of source parent to destination parent)
            self.parents[src_parent] = dst_parent

            # Update rank of source parent to reflect it is now just a symlink
            src_rank = 0

            # Check if max row count needs to be updated
            if self.row_counts[dst_parent] > self.max_row_count:
                self.max_row_count = self.row_counts[dst_parent]

        else:
            # "Copy" over rows (i.e. update row count of destination parent)
            self.row_counts[src_parent] += self.row_counts[dst_parent]

            # "Erase file content" (i.e. change row count to 0 for source parent)
            self.row_counts[dst_parent] = 0

            # "Create symlink" (i.e. update "pointer" of source parent to destination parent)
            self.parents[dst_parent] = src_parent

            # Check if same rank before updating dst rank
            if src_rank == dst_rank:
                src_rank += 1

            # Update rank of source parent to reflect it is now just a symlink
            dst_rank = 0

            # Check if max row count needs to be updated
            if self.row_counts[src_parent] > self.max_row_count:
                self.max_row_count = self.row_counts[src_parent]

        return

    def find_and_compress(self, table):
        path_to_compress = []

        # Loop until root is reached
        while self.parents[table] != table:
            path_to_compress.append(table)
            table = self.parents[table]

        # For increased readability, save last table value into a properly named variable
        root_parent = table

        # Depth needs to be at least 2, otherwise nothing to compress
        if len(path_to_compress) > 1:
            # Last item in list is already directly connected to root, no need to compress
            for index in path_to_compress[:-1]:
                self.parents[index] = root_parent

        return root_parent


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(src - 1, dst - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
