# https://csacademy.com/app/graph_editor/

# def BFS(root, DICH, trees):
#     figure = []
#     close = []
#     figure = figure + trees[root]
#     while (len(figure) != 0):
#         close.append(figure[0])
#         if figure[0] == DICH:
#             return close
#         else:
#             figure = figure + trees[figure[0]]
#             del(figure[0])
#
#
# def main():
#     di = BFS(root, DICH, trees)
#     print(di)
# if __name__ == "__main__":
#     main()

class bfs:
    def __init__(self, trees, root, DICH):
        self.trees = trees
        self.DICH = DICH
        self.root = root
    def BFS(self):
        figure = []
        close = []
        figure = figure + self.trees[self.root]
        while (len(figure) != 0):
            close.append(figure[0])
            if figure[0] == self.DICH:
                return close
            else:
                figure = figure + self.trees[figure[0]]
                del (figure[0])
if __name__ == "__main__":
    trees = {0: [1, 3], 1: [2, 4], 2: [3, 4], 3: [5], 4: [5]}
    root = 0
    DICH = 5
    di = bfs(trees, root, DICH)
    print(di.BFS())
