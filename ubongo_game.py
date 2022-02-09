# import standard library
import numpy as np
# import time
# import random

# start assumption: all pieces can fit on board without piece or board rotation
# start condition: pieces cannot be transposed...(for now and simplicity)

# ---------------- Setup 
# init of colour-coded playing pieces 
piece_blue = np.array([[1], [1], [1]])
piece_red = np.array([[1, 1], [1, 1]])
piece_green = np.array([[0, 1], [1, 1]])
piece_pink = np.array([[1, 1], [1, 0], [1, 0], [1, 0]])

# init of starting(default_board) and final boards
default_board = np.array([[1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
final_board = np.array([[2, 2, 2, 0], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]])

# ----------------- Functionality
# paste funtion for element-wise addition of piece and board content/slices at a certian location
def paste(board, piece, loc):
  loc_zip = zip(loc, piece.shape, board.shape)
  board_slices, piece_slices = zip(*map(paste_slices, loc_zip))
  board[board_slices] = piece[piece_slices] + board[board_slices]

# Obtain board and piece content for min and max coord_ increments
def paste_slices(tup):
  pos, w, max_w = tup
  board_min = max(pos, 0)
  board_max = min(pos+w, max_w)
  piece_min = -min(pos, 0)
  piece_max = max_w-max(pos+w, max_w)
  piece_max = piece_max if piece_max != 0 else None
  return slice(board_min, board_max), slice(piece_min, piece_max)

print(default_board,"\n")
## function_paste test
# pieceRed = np.array([[1, 1], [1, 1]])
# paste(default_board, pieceRed, (0,0))
# print(default_board,"\n")

# presets of playing piece-order, the algorithm will use to assert if its condition is met.
piece_order_1 = [piece_blue, piece_red, piece_green, piece_pink]
piece_order_2 = [piece_blue, piece_red, piece_green, piece_pink]

# returns starting_board size in (row, col)
board_size = default_board.shape

# ------------------------- Algorithm behaviour (not random)
for piece_1 in piece_order_1:
    og_temp_board = default_board
    # Fucked up loop 1
    for row_1 in range(board_size[0]):
        tempBoard_1 = default_board
        for col_1 in range(board_size[1]):
            # starting point of piece parsing with coordiinate (0,0)
            if row_1 == board_size[0]-2 or col_1 == board_size[1]-2:
                pass
            else:
                paste(tempBoard_1, piece_1, (row_1, col_1))
                # print(tempBoard_1, '\n')
                
            # resets board if any 3 playing pieces overlap, or any single piece overlaps with top-right board edge
            if 3 in tempBoard_1 and not tempBoard_1[0,3] == 1:
                tempBoard_1 = default_board
                
            for piece_2 in piece_order_2:
                # Fucked up loop 2
                for row_2 in range(board_size[0]):
                    tempBoard_2 = tempBoard_1
                    for col_2 in range(board_size[1]):
                        if row_2 == board_size[0]-2 or col_2 == board_size[1]-2:
                            pass
                        else:
                            paste(tempBoard_2, piece_2, (row_2, col_2))
                            # print(tempBoard_2, '\n')
                            
                        if 3 in tempBoard_2 and not tempBoard_2[0,3] == 1:
                            tempBoard_2 = tempBoard_1
                        og_temp_board = tempBoard_2
                        break
                    break
                        
        # final check to assert if the final board is equal to the loop output board
        if np.array_equal(final_board, default_board):
            print("All pieces fit perfectly on board")
            print("final: ", default_board)

#------------------------------------
## Try making the algorithm eliminate 'moves' by starting placement with the perfect playing pieces

# board_len = 0
# for pieces in piece_order_1:
#     if 0 in pieces:
#         fixed_length.append(pieces)
#     else:
#         irregular_length.append(pieces)

# while board_len < len(defaultBoard):
#     for board_row in board_normal_row:
#         if 0 in board_normal_row[board_len]:
#             irregular_board_length = board_normal_row[board_len]
#             board_len +=1
#             break
#         break




