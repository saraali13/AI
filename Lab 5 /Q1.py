import chess
import random


def evaluate_board(board):
    """Simple evaluation function for chess positions"""
    if board.is_checkmate():
        return float('-inf') if board.turn == chess.WHITE else float('inf')
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    # Basic material count evaluation
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value

    return score


def beam_search(board, beam_width, depth_limit):
    """Beam search for best chess move sequence"""
    # Initial state is the current board with no moves made yet
    current_beam = [([], board.copy())]

    for depth in range(depth_limit):
        next_beam = []

        for move_sequence, current_board in current_beam:
            # Generate all legal moves
            for move in current_board.legal_moves:
                new_board = current_board.copy()
                new_board.push(move)
                new_sequence = move_sequence + [move]
                score = evaluate_board(new_board)
                next_beam.append((new_sequence, new_board, score))

        # Sort by evaluation score and keep only top beam_width moves
        next_beam.sort(key=lambda x: x[2], reverse=current_board.turn == chess.WHITE)
        current_beam = [(seq, board) for seq, board, score in next_beam[:beam_width]]

    # Return the best move sequence and its score
    if not current_beam:
        return [], 0
    best_sequence, best_board, best_score = next_beam[0]
    return best_sequence, best_score



board = chess.Board()
beam_width = 3
depth_limit = 2

best_move_sequence, best_score = beam_search(board, beam_width, depth_limit)
print("Best move sequence:", [move.uci() for move in best_move_sequence])
print("Evaluation score:", best_score)
