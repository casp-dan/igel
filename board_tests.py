"""Test suite for board_object.

@author: Daniel Casper
@version: Fall 2023

I affirm that I have carried out my academic endeavors
with full academic honesty. [Daniel Casper]
"""

import testing as tests
from board import Board
from igel_aergern import IgelAergern

class Tests:

    def __init__(self):
        self.main = IgelAergern()
        tests.start_tests('starting tests now!!!')
        self.test_create_board()
        self.test_as_str()
        self.test_move_forward()
        self.test_move_sideways()
        self.test_win()
        self.test_add_tokens()
        self.test_empty_row()
        self.test_add_remove_lines()
        tests.finish_tests()


    def test_create_board(self):
        self.board = Board()
        tests.assert_equals('check for empty board list', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        
    def test_as_str(self):
        self.b_str=self.board.as_str()
        tests.assert_equals('a singular string that represents an empty boards state', '|||@|||||//||||||@||//||||@||||//|||||@|||//||@||||||//|||||||@|', self.b_str)
        self.board.board=[['','','','@A','D','D','AHADF','',''], ['','AS','','AB','','','@','',''],['','BAB','','','@','ABF','','',''],['','','','','AFB AD','@','','',''],['','','@','','','','','',''],['','','','','AFAB','','','@','']]
        self.b_str=self.board.as_str()
        tests.assert_equals('a singular string that represents a board with characters on it', '|||@A|D|D|AHADF||//|AS||AB|||@||//|BAB|||@|ABF|||//||||AFB AD|@|||//||@||||||//||||AFAB|||@|', self.b_str)
        
    def test_move_forward(self):   
        self.board.board=[['','R','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        row=self.board.board[0]
        self.board.move_forward(row,2)
        tests.assert_equals('move a token in row 1', [['','','R','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['R','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        row=self.board.board[1]
        self.board.move_forward(row,1)
        tests.assert_equals('move a token in row 2', [['','','','@','','','','',''], ['','R','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','R','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        row=self.board.board[2]
        self.board.move_forward(row,7)
        tests.assert_equals('move a token in row 3', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','R',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','R','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        row=self.board.board[3]
        self.board.move_forward(row,5)
        tests.assert_equals('move a token in row 4', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@R','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','R','','','','',''],['','','','','','','','@','']]
        row=self.board.board[4]
        self.board.move_forward(row,4)
        tests.assert_equals('move a token in row 5', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','R','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','R']]
        row=self.board.board[5]
        self.board.move_forward(row,9)
        tests.assert_equals('move a token in row 6', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','R']], self.board.board)

    def test_move_sideways(self):
        '''Testing the move sideways function in the board class. Not testing a sidestep up in row 1 or a sidestep down in row 6 as the player is not prompted for a 
           direction when they choose one of those two rows. Rather, the game will immediately move the piece in the proper direction in those cases.'''
        self.board.board=[['','R','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(0,1, -1)
        tests.assert_equals('Sidestep a token down from row 1', [['','','','@','','','','',''], ['','R','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['R','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(1,0, 1)
        tests.assert_equals('Sidestep a token up from row 2', [['R','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','R','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(2,6, 1)
        tests.assert_equals('Sidestep a token up from row 3', [['','','','@','','','','',''], ['','','','','','','@R','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','R','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(3,4, 1)
        tests.assert_equals('Sidestep a token up from row 4', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@R','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','R','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(4,3, 1)
        tests.assert_equals('Sidestep a token up from row 5', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','R','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['R','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(1,0, -1)
        tests.assert_equals('Sidestep a token down from row 2', [['','','','@','','','','',''], ['','','','','','','@','',''],['R','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','R','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(2,6, -1)
        tests.assert_equals('Sidestep a token down from row 3', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','R','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','R','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(3,4, -1)
        tests.assert_equals('Sidestep a token down from row 4', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','R','','','',''],['','','','','','','','@','']], self.board.board) 
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','R','','','','',''],['','','','','','','','@','']]
        self.board.move_sideways(4,3, -1)
        tests.assert_equals('Sidestep a token down from row 5', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','R','','','','@','']], self.board.board)
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','R']]
        self.board.move_sideways(5,8, 1)
        tests.assert_equals('Sidestep a token up from row 6', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','','R'],['','','','','','','','@','']], self.board.board)

    def test_win(self):
        self.board.board=[['','','','@','','','','','RG'], ['','','','','','','@','','B'],['','','','','@','','','','RPO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for R', 'R', winner)
        self.board.board=[['','','','@','','','','','GG'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for G', 'G', winner)
        self.board.board=[['','','','@','','','','','BG'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for B', 'B', winner)
        self.board.board=[['','','','@','','','','','YG'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for Y', 'Y', winner)
        self.board.board=[['','','','@','','','','','OG'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for O', 'O', winner)
        self.board.board=[['','','','@','','','','','PG'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a win scenario for P', 'P', winner)
        self.board.board=[['','','','@','','','','','G'], ['','','','','','','@','','YB'],['','','','','@','','','','PO'],['','','','','','@','','',''],['','','@','','','','','','OYP'],['','','','','','','','@','RGB']]
        self.board.add_lines()
        winner=self.board.get_winner()
        tests.assert_equals('Test for a still in progress game with no winner yet.', None, winner)

    def test_add_tokens(self):
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.add_tokens(2, 0, ['R'])
        tests.assert_equals('test the start up function to place tokens on the board', [['','','','@','','','','',''], ['R','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board )

    def test_empty_row(self):
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        empty=self.board.check_empty_row(3, ['R'])
        tests.assert_equals('test the function looking for empty rows', True, empty )
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','R','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        empty=self.board.check_empty_row(3, ['R'])
        tests.assert_equals('test the function looking for empty rows (not empty)', False, empty )

    def test_add_remove_lines(self):
        self.board.board=[['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']]
        self.board.add_lines()
        tests.assert_equals('check the add lines function', [['', '|', '', '|', '', '|', '@', '|', '', '|', '', '|', '', '|', '', '|', '', '//'], ['', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '@', '|', '', '|', '', '//'], ['', '|', '', '|', '', '|', '', '|', '@', '|', '', '|', '', '|', '', '|', '', '//'], ['', '|', '', '|', '', '|', '', '|', '', '|', '@', '|', '', '|', '', '|', '', '//'], ['', '|', '', '|', '@', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '//'], ['', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '', '|', '@', '|', '']], self.board.board)
        self.board.remove_lines()
        tests.assert_equals('check the remove lines function', [['','','','@','','','','',''], ['','','','','','','@','',''],['','','','','@','','','',''],['','','','','','@','','',''],['','','@','','','','','',''],['','','','','','','','@','']], self.board.board)


        

testing=Tests()