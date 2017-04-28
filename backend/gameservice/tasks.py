from gameservice import models
from gameservice.arena import Arena

# TODO: Add a celery task that plays the game
def run_contest(contest_id):
    contest = models.Contest.get(id=contest_id)
    if not contest:
        return False
    arena = Arena(contest)
    arena.play()
    return True
