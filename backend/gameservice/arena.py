import json
import subprocess
import tempfile

from django.utils import timezone
from gameservice import models
from utils import bash, Logger, deadline

class Arena(object):
    def __init__(self, contest, game):
        self.contest = contest
        self.logger = Logger(self.__class__.__name__)

        move_timeout = self.contest.move_timeout
        if not move_timeout:
            move_timeout = self.contest.game.move_timeout
        self._execute = deadline(move_timeout)(self._execute)

    def _execute(self, script, stdin, language):
        "Generate stdout by executing the script with given stdin."
        if language.lower() != 'python':
            raise Exception('Language not supported: {}'.format(language))

        if language == 'python':
            fd, filename = tempfile.mktemp(suffix=".py")
            os.write(fd, script)
            stdout = bash("python " + filename, stdin=stdin)
            os.close(fd)
            return stdout

        # TODO: Add support for more languages
        return ''

    def _parse_move(self, move):
        """Parse the move outcome from umpire and determine
            1. The next board configuration
            2. If the move is valid
            3. If the player has won
        """
        move = json.loads(move)
        board = move['board']
        is_valid = move['is_valid']
        is_winner = move['is_winner']
        return board, is_valid, is_winner

    def _save_history(self, player, move):
        models.ContestHistory.objects.create(contest=self.contest,
            player=player, move_played=move, creation_time=timezone.now())

    def _set_winner(self, player):
        if player == self.contest.player1:
            self.contest.winner = 'Player1'
        else:
            self.contest.winner = 'Player2'
        self.contest.save()

    def play(self):
        board = self._execute(self.contest.game.starter, self.contest.options, self.contest.game.language)

        # swap players if neccessary
        player1 = self.contest.player1 if self.contest.starter == 'Player1' else self.contest.player2
        player2 = self.contest.player1 if self.contest.starter == 'Player2' else self.contest.player2

        # get hand on the submission1
        submission1 = self.contest.submission1 if self.contest.submission1.player == player1 else self.contest.submission2
        submission2 = self.contest.submission2 if self.contest.submission2.player == player2 else self.contest.submission1

        moves_played = 0
        while True:
            move1 = self._execute(submission1.code_snippet, board, submission1.language)
            board, is_valid, is_winner = self._parse_move(self._execute(self.contest.game.umpire, move1, self.contest.game.language))

            self._save_history(player1, move1)
            if not is_valid:
                self._set_winner(player2)
                break

            if is_winner:
                self._set_winner(player1)
                break

            moves_played += 1
            if moves_played > self.contest.game.max_moves:
                break

            move2 = self._execute(submission2.code_snippet, board, submission2.language)
            board, is_valid, is_winner = self._parse_move(self._execute(self.contest.game.umpire, move2, self.contest.game.language))

            self._save_history(player2, move2)
            if not is_valid:
                self._set_winner(player1)
                break

            if is_winner:
                self._set_winner(player2)
                break

            moves_played += 1
            if moves_played > self.contest.game.max_moves:
                break