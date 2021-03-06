# trivial baseline control policy. checks forward, left and right sonars and if
# forward reports the largest distance move forward and if left/right reports
# largest distance turn (on spot) left/right.
class BaselinePolicy(object):

    def action_given_state(self, state):
        # expects FurthestSonarIdxer which will directly emit what
        # this policy chooses as an action
        return state

    def train(self, state_1, action, reward, state_2):
        pass

    def debug_model(self):
        pass

    def end_of_episode(self):
        pass
