from objects.characterClass.Classes import *
from objects.characterAbilities import *
from objects.item.ItemType import *
from objects.item.BagOfTeaPlusThree import BagOfTeaPlusThree
"""
    Python file containing static paths.
    Used by: "from objects/defaultConfig.StaticPaths import *
    Images, models, etc. are stored in public static variables here.
"""

# === [Game Balance] ===

PLAYER_MAX_ENERGY = 100
PLAYER_ENERGY_RECOVERY_DELAY = 2
PLAYER_ENERGY_RECOVERY_RATE = 20
MAX_PLAYERS = 4
PLAYER_MAX_HEALTH = 100
PLAYER_RESPAWN_DELAY = 10

# --- (AI) ---
ENEMY_MAX_ENERGY = 100
ENEMY_ENERGY_RECOVERY_RATE = 20
ENEMY_ENERGY_RECOVERY_DELAY = 2
ENEMY_AI_TICK_DELAY_RANGE = (0.5, 1.5)
ENEMY_AI_SIGHT_RANGE = 5
ENEMY_AI_SIGHT_LOSS_RANGE = 8
ENEMY_AI_ROAM_MAX_RANGE = 3
# --- ---

# --- (Default Creature) ---
CREATURE_DEFAULT_MAX_ENERGY = 100
CREATURE_DEFAULT_MAX_HEALTH = 100
CREATURE_DEFAULT_REACH = 1
CREATURE_BASE_DAMAGE = 30
# --- ---

# === ===

# === [Networking] ===
HOST_MAX_BACKLOG = 1000
CLIENT_TIMEOUT = 3000 # 3 Seconds
ACTION_NETWORKING_DICT = {Move.actionID:moveSync,
                          BasicAttack.actionID:singleTargetAttackSync}
ITEM_ID_DICT = {ItemType.BagOfTeaPlusThree:BagOfTeaPlusThree}
CLASSES_DICT = {Barbarian.classID:Barbarian, Thief.classID:Thief,
                Wizard.classID:Wizard, BaseClass.classID:BaseClass}
# === ===

# === [User Interface] ===
UI_WINDOW = "objects/mainMenu/UIContainer.png"
IMG_GRADIENT_1 = "objects/gameUI/source/UIGradient1.png"
PIERCEROMAN_FONT = "objects/mainMenu/PierceRoman.otf"
PIERCEROMAN_OFFSET_MC = (0, -0.03)

# --- (Win Screen) ---
WINSCREEN_CONTENT_HEIGHT_PERCENTAGE = 0.1
WINSCREEN_CONTENT_WIDTH_PERCENTAGE = 1
WINSCREEN_WINTEXT_Y_OFFSET = 0.1
WINSCREEN_FONT_SIZE = (0.075, 0.075)
WINSCREEN_WINTEXT_TEXT_OFFSET = (0, 0.08)
WINSCREEN_MESSAGE = """%s
Has Obtained the Legendary Bag of Tea +3 !
Submit Now to Your New Ruler, Mortals!"""
# --- ---

# --- (Respawn Screen) ---
RESPAWN_SCREEN_CONTENT_SPACING = 0.2
RESPAWN_SCREEN_CONTENT_HEIGHT_PERCENTAGE = 0.1
RESPAWN_SCREEN_CONTENT_WIDTH_PERCENTAGE = 0.6
RESPAWN_SCREEN_FONT_SIZE = (0.075, 0.075)
RESPAWN_BUTTON_DISABLED_COLOR = (0.75, 0.75, 0.75, 0.75)
RESPAWN_BUTTON_ENABLED_COLOR = (1, 1, 1, 1)
RESPAWN_BUTTON_TEXT_OFFSET = (0, -0.025)
# --- ---

# --- (Damage Text) ---
DAMAGE_TEXT_DESPAWN_DELAY = 2
DAMAGE_TEXT_COLOR_HEAL = (0, 1, 0, 1)
DAMAGE_TEXT_COLOR_DAMAGE = (1, 0, 0, 1)
DAMAGE_TEXT_COLOR_NEUTRAL = (1, 1, 0, 1)
DAMAGE_TEXT_SCALE = 0.7
DAMAGE_TEXT_INITIAL_JUMP_VELOCITY = .05
DAMAGE_TEXT_JUMP_VARIATION = .1
DAMAGE_TEXT_GRAVITY = -.1
# --- ---

# --- (Join Party Options) ---
JOPTS_CONTROL_TOP_MARGIN = 0.2
JOPTS_CONTROL_SPACING = 0.3
JOPTS_CONTROL_HEIGHT = 0.2
JOPTS_BUTTON_BORDER_WIDTH = (0.03, 0.03)
JOPTS_BUTON_FONT_SIZE = (0.08, 0.08)
JOPTS_BUTON_FONT_OFFSET = (0, -.02)
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
    [Barbarian, Thief],
    [Wizard],
]
CPKR_BUTTONCONTAINER_MARGIN = 0.1
CPKR_BUTTONCONTAINER_WIDTH_PERCENTAGE = 0.7
# --- ---

# --- (Main Menu) ---
TITLE_SCREEN_BACKGROUND_PATH = "objects/mainMenu/TitleScreen.png"
TITLE_SCREEN_CONTAINER_PATH = "objects/mainMenu/TitleScreenContainer.png"
TITLE_PATH = "objects/mainMenu/Title.png"
TITLE_MARGIN = 0.1
# --- ---

# --- (Name Picker) ---
NPKR_WIDTH_PERCENTAGE = 0.5 # In terms of screen width
NPKR_HEIGHT_PERCENTAGE = 0.1 # In terms of screen height
NPKR_ENTRY_WIDTH_PERCENTAGE = 0.6 # How long compared to confirm button.
NPKR_ENTRY_FONT_SIZE = (0.075, 0.075)
NPKR_ENTRY_INITIAL_TEXT = "Enter Name"
NPKR_ENTRY_FONT_OFFSET = (0, -0.03)
NPKR_BUTTON_BORDER_WIDTH = (0.03, 0.03)
NPKR_BUTTON_FONT_SIZE = (0.075, 0.075)
NPKR_BUTTON_FONT_OFFSET = (0, -0.02)
# --- ---

# --- (Health and Energy Bars) ---
ENERGY_BAR_FG_COLOR = (1, 0.843137, 0, 1)
ENERGY_BAR_BG_COLOR = (0, 0, 0, 1)
ENERGY_BAR_OFFSET = (0,0,1.5)
HEALTH_BAR_OFFSET = (0,0,2)
HEALTH_BAR_FG_COLOR = (0, 1, 0, 1)
HEALTH_BAR_BG_COLOR = (1, 0, 0, 1)
# --- ---

# --- (Name Displays) ---
NAME_DISPLAY_OFFSET = (0, 0, 1)
NAME_DISPLAY_SCALE = 0.7
NAME_DISPLAY_COLOR = (1, 1, 1, 1)
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

# --- (Ability Bar) ---
ABILITYBAR_WIDTH_PERCENTAGE = 0.8
ABILITYBAR_HEIGHT_PERCENTAGE = 0.125
ABILITYBAR_ALPHA = 0.5
ABILITYBAR_HOTKEY_SIZE = 0.15
ABILITYBAR_SPACING = 0.05
ABILITYBAR_HOTKEY_OFFSET = (0, 0.1)
ABILITYBAR_HOTKEY_SCALE = (0.07, 0.07)
ABILITYBAR_ACTIVE_COLOR = (1, 1, 0.33, 1)
ABILITYBAR_DEFAULT_COLOR = (1, 1, 1, 1)
# --- ---

# --- (Game Guide) ---
GAMEGUIDE_TEXT = \
"""Welcome to Teapot Wars 2.
To start a game, press the 'Host Game' button in the Main Menu.
Other players that wish to join must press the 'Join Party' button
and fill out the correct IP Address.
To get the IP Address, have host check their command prompt:
[Host Started at ???.???.??.???]
Once you begin and pick a class and name,
use your abilities (bound to hotkeys) to take down foes!

Cooperate or compete to find and defeat the enemy
and recover the Legendary Bag of Tea +3

Good luck, hunters!
"""
GAMEGUIDE_CONTENT_WIDTH_PERCENTAGE = 0.75
GAMEGUIDE_CONTENT_HEIGHT_PERCENTAGE = 1
GAMEGUIDE_FONT_SIZE = (0.075, 0.075)
GAMEGUIDE_TEXT_OFFSET = (0, 0.8)
GAMEGUIDE_CLOSE_BUTTON_OFFSET = (0, -0.7)
GAMEGUIDE_CLOSE_BUTTON_SIZE_X = 0.6
GAMEGUIDE_CLOSE_BUTTON_SIZE_Y = 0.1
GAMEGUIDE_CLOSE_BUTTON_TEXT_OFFSET = (0, -0.02)
GAMEGUIDE_BUTTON_BORDER_WIDTH = (0.03, 0.03)
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
