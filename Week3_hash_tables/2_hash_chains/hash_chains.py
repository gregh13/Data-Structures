# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


def _hash_func(string, buckets):
    _multiplier = 263
    _prime = 1000000007
    ans = 0
    for c in reversed(string):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans % buckets


def write_chain(chain):
    print(' '.join(chain))


def dictionary_solution():

    bucket_count = int(input())
    string_dict = {x: [] for x in range(bucket_count)}

    n = int(input())
    for i in range(n):
        query = Query(input().split())
        if query.type == "check":
            check_list = string_dict[query.ind]
            write_chain(reversed(check_list))
        elif query.type == "add":
            hash_val = _hash_func(query.s, bucket_count)
            string_dict[hash_val].append(query.s)
        else:
            found = False
            hash_val = _hash_func(query.s, bucket_count)
            hashed_list = string_dict[hash_val]
            if query.s in hashed_list:
                found = True
            if query.type == "find":
                if found:
                    print("yes")
                else:
                    print("no")
            elif query.type == "del":
                if found:
                    hashed_list.remove(query.s)










class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    # bucket_count = int(input())
    # proc = QueryProcessor(bucket_count)
    # proc.process_queries()
    dictionary_solution()

