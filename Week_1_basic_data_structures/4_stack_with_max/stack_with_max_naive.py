
import sys


class FastStackMax():
    def __init__(self):
        self.__stack = []
        self.max_values = [float("-inf")]

    def Push(self, a):
        # Check if new value should be added to max_value list
        if a >= self.max_values[-1]:
            self.max_values.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        # Check if current popped value needs to be removed from max_value list as well
        if self.__stack[-1] == self.max_values[-1]:
            self.max_values.pop()
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        # Return the last item in max_value as it is the current stack max
        return self.max_values[-1]


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()
    fast_stack = FastStackMax()

    num_queries = int(sys.stdin.readline())
    # for _ in range(num_queries):
    #     query = sys.stdin.readline().split()
    #
    #     if query[0] == "push":
    #         stack.Push(int(query[1]))
    #     elif query[0] == "pop":
    #         stack.Pop()
    #     elif query[0] == "max":
    #         print(stack.Max())
    #     else:
    #         assert 0
    #
    # print("-------------")

    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            fast_stack.Push(int(query[1]))
        elif query[0] == "pop":
            fast_stack.Pop()
        elif query[0] == "max":
            print(fast_stack.Max())
        else:
            assert 0