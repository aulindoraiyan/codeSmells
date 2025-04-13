class Nose:
    """
    Creates a Nose which can smell. Might represent a Robot, Human, or Cyborg nose.
    """

    MAX_AIR_TANK_LEVEL = 20

    def __init__(self, allergies=None, is_robot=False, air_tank_capacity_liters=None):
        self.smelled_smells = set()
        self.immune_response = False
        self.is_robot = is_robot
        self.allergies = allergies or []
        self.air_tank_capacity_liters = air_tank_capacity_liters or self.MAX_AIR_TANK_LEVEL
        self.current_air_tank_level = 0
        self.is_running = False

    def smell(self, odor):
        """
        Smell an odor. Logic varies based on whether the nose is a robot, human, or cyborg.
        """
        if self.is_robot:
            self._smell_as_robot(odor)
        else:
            self._smell_as_human(odor)

    def _smell_as_robot(self, odor):
        """Handle smelling logic for robots."""
        if self.current_air_tank_level < self.air_tank_capacity_liters:
            self.smelled_smells.add(odor)
            self.current_air_tank_level += 1
        else:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")

    def _smell_as_human(self, odor):
        """Handle smelling logic for humans and cyborgs."""
        if self.immune_response:
            raise RuntimeError("Nose cannot smell when immune response is active.")
        if odor in self.allergies:
            self.immune_response = True
        else:
            self.smelled_smells.add(odor)

    def rest(self):
        """
        Rest the nose.

        Resets the immune response for humans and air tank for robots, and both for cyborgs.
        """
        self.immune_response = False
        self.current_air_tank_level = 0
        self.is_running = False

    def get_smelled_smells(self):
        """
        Return a copy of the set of previously encountered odors.
        """
        return self.smelled_smells.copy()


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")
