# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def phone_book_dict(queries):
    results = []
    phone_dict = {}

    for query in queries:
        if query.type == "add":
            # Adds or updates key and value
            phone_dict[query.number] = query.name
        elif query.type == "find":
            if query.number in phone_dict:
                results.append(phone_dict[query.number])
            else:
                message = "not found"
                results.append(message)
        elif query.type == "del":
            if query.number in phone_dict:
                del phone_dict[query.number]

    return results


def direct_addressing(queries):
    assignment_max = (10 ** 7) + 1
    results = []
    # Initialize array with one index value for every possible phone number per assignment max number values
    # Note this is potentially a huge waste of space
    phone_book = [None] * (assignment_max)

    for query in queries:
        if query.type == "add":
            phone_book[query.number] = query.name
        elif query.type == "find":
            if phone_book[query.number] is None:
                message = "not found"
                results.append(message)
            else:
                results.append(phone_book[query.number])
        elif query.type == "del":
            phone_book[query.number] = None

    return results


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    # write_responses(process_queries_naive(read_queries()))
    # write_responses(direct_addressing(read_queries()))
    write_responses(phone_book_dict(read_queries()))

