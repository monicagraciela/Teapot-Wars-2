from objects.characterClass.Classes import *
from objects.characterAbilities import *
"""
    Python file containing static paths.
    Used by: "from objects/defaultConfig.StaticPaths import *
    Images, models, etc. are stored in public static variables here.
"""

# === [Game Balance] ===

# --- (Default Creature) ---
CREATURE_MAX_ENERGY = 100
# --- ---

PLAYER_MAX_ENERGY = 100
PLAYER_ENERGY_RECOVERY_DELAY = 2
PLAYER_ENERGY_RECOVERY_RATE = 5
MAX_PLAYERS = 4
PLAYER_MAX_HEALTH = 100
# === ===

# === [Networking] ===
HOST_MAX_BACKLOG = 1000
CLIENT_TIMEOUT = 3000 # 3 Seconds
ACTION_NETWORKING_DICT = {Move.actionID:moveSync}
# === ===

# === [User Interface] ===
UI_WINDOW = "objects/mainMenu/UIContainer.png"
PIERCEROMAN_FONT = "objects/mainMenu/PierceRoman.otf"
PIERCEROMAN_OFFSET_MC = (0, -0.03)

# --- (Join Party Options) ---
JOPTS_CONTROL_TOP_MARGIN = 0.2
JOPTS_CONTROL_SPACING = 0.3
JOPTS_CONTROL_HEIGHT = 0.2
# --- ---

# --- (Class Picker) ---
CPKR_CONTROL_TOP_MARGIN = 0.031
CPKR_CONTROL_SIDES_MARGIN = 0.04
CPKR_TITLE_HEIGHT_RATIO = 0.1
CPKR_INFO_HEIGHT_RATIO = 0.2
CPKR_PIERCEROMAN_OFFSET_TC = (0, -0.11)
CPKR_PIERCEROMAN_OFFSET_TL = (-0.7, -0.07)
CPKR_INFO_WRAP_DEFAULT = 19
CPKR_INFO_FONT_SIZE_DEFAULT = (0.075, 0.075)
# Represented in a grid:
CPKR_CLASSES_LIST = [
[(Barbarian, "objects/characterClass/icons/BarbarianIcon.png"),
 (BaseClass, "objects/characterClass/icons/WizardIcon.png")],
[(Barbarian, "objects/characterClass/icons/BarbarianIcon.png")]
                    ]
CPKR_BUTTONCONTAINER_MARGIN = 0.1
CPKR_BUTTONCONTAINER_WIDTH_PERCENTAGE = 0.7
# --- ---

# --- (Name Picker) ---
NPKR_WIDTH_PERCENTAGE = 0.5 # In terms of screen width
NPKR_HEIGHT_PERCENTAGE = 0.1 # In terms of screen height
NPKR_ENTRY_WIDTH_PERCENTAGE = 0.6 # How long compared to confirm button.
NPKR_ENTRY_FONT_SIZE = (0.075, 0.075)
NPKR_ENTRY_INITIAL_TEXT = "Enter Name"
NPKR_ENTRY_FONT_OFFSET = (0, -0.03)
# --- ---

# --- (Health and Energy Bars) ---
ENERGY_BAR_FG_COLOR = (1, 0.843137, 0, 1)
ENERGY_BAR_BG_COLOR = (0, 0, 0, 1)
ENERGY_BAR_OFFSET = (0,0,2)
# --- ---

# --- (Party UI) ---
PARTY_NAME_MAX = 15
PARTY_LIST_WIDTH_PERCENTAGE = 0.25
PARTY_LIST_HEIGHT_PERCENTAGE = 0.75
PARTY_LIST_ALPHA = 0.5
PARTY_LIST_NAME_PARTITION = 0.2
PARTY_LIST_ICON_PARTITION = 0.7
PARTY_LIST_HEALTH_PARTITION = 0.1
PARTY_LIST_HEALTH_FG_COLOR = (0, 0.75, 0, 1)
PARTY_LIST_HEALTH_BG_COLOR = (0.75, 0, 0, 1)
PARTY_NAME_FONT_SIZE = (0.05, 0.05)
PARTY_NAME_FONT_OFFSET = (0, -0.075)
# --- ---

#=== ===

# === [Camera] ===
TILEMAP_ORBITER_HEIGHT = 5
TILEMAP_ORBITER_SPEED = 0.25
TILEMAP_ORBITER_MIN_INTERVAL = 3
TILEMAP_ORBITER_MAX_INTERVAL = 5
TILEMAP_ORBITER_MIN_VERTICAL_ANGLE = 1
TILEMAP_ORBITER_MAX_VERTICAL_ANGLE = 1.5
TILEMAP_ORBITER_MIN_DIST = 6
TILEMAP_ORBITER_MAX_DIST = 20
# === ===
