# init_ubongo_game

Aim of this project is to develop and extend current working model of ubongo game to work with selected piece and board.


Extended optimizations (to work with and playing shap and board) are possible as a next step.


Current algoorithm that handels the functionality.
'''
The algorithm should work as follows,
- A first piece is selected from order_1 and inserted in the playing board at the starting coord_(0,0) og_board = temp_board.
- A second piece from order_2 is taken and added to this coord_ as well(temp_board is refreshed).
- If the sum of this addition on the board results in a 3 or the missing piece of the board is filled by any object from either order_list, temp_board reverts back to og_board. 
- The next piece from order_2 is taken, and added to new temp_board and the loop checks again.
- If all the pieces in order_2 are used, the coordinate shifts and the loop starts again keeping the last board with cell content < 3 and missing board piece, unfilled
- If all conditions are met and the resulting board from the loop matches the final_board, game is finished
- The process can be visualized with the PNG-file
'''
