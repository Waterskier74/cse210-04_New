from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        
    def get_score(self):
        """Gets the gem's score.
        
        Returns:
            int: score value.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (int): The given score.
        """
        self._score = score

