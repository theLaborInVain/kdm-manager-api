"""

    This module is used to move survivor attribute values out of the Survivor
    object, which was getting a bit junked up.

    There is a corresponding models/ file for this asset module, but working
    with these 'assets' isn't really something we do in the API.

"""

attributes = [
    'Movement',
    'Accuracy',
    'Strength',
    'Evasion',
    'Luck',
    'Speed',
    'bleeding_tokens'
]

#   default attribute values

defaults = {
    "Movement": 5,
    "max_bleeding_tokens": 5,
}


#   survivor sheet armor locations, damage types

armor_locations = ['Head', 'Body', 'Arms', 'Waist', 'Legs']

damage_locations = [
    "brain_damage_light",
    "head_damage_heavy",
    "arms_damage_light",    "arms_damage_heavy",
    "body_damage_light",    "body_damage_heavy",
    "waist_damage_light",   "waist_damage_heavy",
    "legs_damage_light",    "legs_damage_heavy",
]


#   meta/API attributes

game_asset_keys = [
    'abilities_and_impairments',
    'disorders',
    'epithets',
    'fighting_arts',
]
