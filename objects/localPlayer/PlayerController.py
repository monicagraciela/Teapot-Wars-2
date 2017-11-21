from direct.actor.Actor import Actor
from .CameraSystem import CameraSystem
from ..characters.teapot.Teapot import Teapot
from .InputSystem import InputSystem
from objects.gameUI.BarUI import BarUI
from objects.defaultConfig.Consts import *

class PlayerController ():
    """
        The Player class lets the user play the game.
        Handles client side player systems such as input, camera, and gameplay.
    """
    def __init__ (self, initialPos, gameManager, charClass):
        self._gameManager = gameManager # Reference to gameManager for callbacks
        base.disableMouse() # Disables default Panda3D camera control
        # Initialize this clients gameObject:
        self._character = Teapot(initialPos, "player").np
        # Initialize Camera Input:
        self.cameraSystem = CameraSystem(target=self._character)
        # Initialize the player's Input and UI:
        self.inputSystem = InputSystem(self, gameManager.getTileMap())
        #self.maxEnergy
        #self.currentEnergy
        self._gridPos = initialPos
        gameManager.getTileMap().spawnObject(self, initialPos)
        self._charClass = charClass
        self._energy = PLAYER_MAX_ENERGY
        self._energyBar = BarUI(self._character, ENERGY_BAR_OFFSET, 1,
                                ENERGY_BAR_FG_COLOR, ENERGY_BAR_BG_COLOR)
        self._currentActionSequence = None

    def drainEnergy (self, energyCost):
        """
            Drains energy and returns true if there was enough energy for the
             action.
            If there is not enough energy to perform the action, returns false
             and activates a UI warning.
        """
        if self._energy - energyCost < 0:
            # TODO: Perform energy warning!
            return False
        else:
            self._energy -= energyCost
            self.updateEnergyBar()
            return True

    def updateEnergyBar (self):
        """
            Visually updates the energyBar value.
        """
        percentage = self._energy / PLAYER_MAX_ENERGY
        self._energyBar.setValue(percentage)

    def getGridPosition (self):
        return self._gridPos

    def getClass (self):
        return self._charClass

    def getClassAbilities (self):
        return self._charClass.classAbilities

    def getCharacter (self):
        return self._character

    def updateGridPosition (self, newPos):
        self._gridPos = newPos

    def startAction (self, actionSequence):
        """ Assigns and starts the current action sequence """
        #TODO Figure out what to do when action is already running!
        self._currentActionSequence = actionSequence
        self._currentActionSequence.start()

    def cancelCurrentAction (self):
        """ Cancels the _currentActionSequence """
        if self._currentActionSequence:
            self._currentActionSequence.pause()
            self._currentActionSequence = None

    # Define equality and representation functions for searching.
    def __eq__ (self, other):
        if not isinstance(other, PlayerController): return False
        return True # This is the one and only player controller
