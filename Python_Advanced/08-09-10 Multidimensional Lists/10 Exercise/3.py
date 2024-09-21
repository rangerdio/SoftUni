# # rows = int(input())
# # matrix = []
# # cols = 0
# # for row in range(rows):
# #     sublist = list(input())
# #     cols = len(sublist)
# #     matrix.append(sublist)
# rows = 5
# cols = 5
# matrix = [
#           ['0', 'K', '0', 'K', '0'],
#           ['K', '0', '0', '0', 'K'],
#           ['0', '0', 'K', '0', '0'],
#           ['K', '0', '0', '0', 'K'],
#           ['0', 'K', '0', 'K', '0']
#           ]
#
#
# def find_knights(matrix_: matrix, ):
#     knights_ = []
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == 'K':
#                 knights_.append([row, col])
#     return knights_
#
#
# def find_wins():
#     return
#
#
# knights = find_knights(matrix)
# # print(knights)
# # 0 1
# koko = []
# for knight in knights:
#     knight_row = knight[0]
#     knight_col = knight[1]
#     moves = [[knight_row - 2, knight_col + 1], [knight_row - 1, knight_col + 2], [knight_row + 1, knight_col + 2], [knight_row + 2, knight_col + 1],
#              [knight_row + 2, knight_col - 1], [knight_row + 1, knight_col - 2], [knight_row - 1, knight_col - 1], [knight_row - 2, knight_col - 2]]
#     wins_current_knight = {}
#     # wins_current_knight = {knight: [+1], }
#     points = 0
#     list_wins = []
#     for move in moves:
#         if move in knights:
#             # print(knight)
#             # print(move)
#             # print(knights)
#             # print(wins_current_knight)
#
#             points += 1
#             list_wins.append(move)
#     wins_current_knight[str(knight)] = [points, list_wins]
#     koko.append(wins_current_knight)
#
# print(koko)


