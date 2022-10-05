# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return

        if self.ranks[src_parent] < self.ranks[dst_parent]:
            # "Copy" over rows (i.e. update row count of destination parent)
            self.row_counts[dst_parent] += self.row_counts[src_parent]

            # "Erase file content" (i.e. change row count to 0 for source parent)
            self.row_counts[src_parent] = 0

            # "Create symlink" (i.e. update "pointer" of source parent to destination parent)
            self.parents[src_parent] = dst_parent

            # Update rank of source parent to reflect it is now just a symlink
            self.ranks[src_parent] = 0

            return


        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return

    def get_parent(self, table):
        return self.parents[table]


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
