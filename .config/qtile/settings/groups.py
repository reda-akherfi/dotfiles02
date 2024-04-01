from libqtile.config import Group, ScratchPad, DropDown, Key
from .keys import mod, keys
from libqtile.lazy import lazy

from libqtile import hook


scratch_dict = {'height': 0.8,
                'width': 0.6,
                'x': 0.2,
                'y': 0.1,
                'on_focus_lost_hide': False,
                'warp_pointer': False}

scratchpads = [ScratchPad('scratchpad',
                          [
                              DropDown(
                                  'email',
                                  'alacritty -e neomutt',
                                  **scratch_dict),
                              DropDown(
                                  'spotify',
                                  'spotify',
                                  **scratch_dict),
                              DropDown(
                                  'quickie',
                                  'alacritty --command tmux attach',
                                  **scratch_dict)])]

groupies = [# Group(i) for i in ["  ", "  󱨠", "  ", "  ", "  "],
            Group(name="1", label=" 1 ", layout="max"),
            Group(name="2", label=" 2 ", layout="max"),
            Group(name="3", label=" 3 ", layout="max"),
            Group(name="4", label=" 4 ", layout="max"),
            Group(name="5", label=" 5 "),
            Group(name="6", label=" 6 "),
            Group(name="7", label=" 7 "),
            ]

groups = scratchpads + groupies


for group in groupies:
    keys.extend(
        [
            # mod1 + group number = switch to group
            #Key(
            #    ["mod1"],
            #    group.name,
            #    lazy.group[group.name].toscreen(),
            #    desc="Switch to group {}".format(group.name),
            #),
            Key(
                [mod],
                group.name,
                lazy.screen.toggle_group(group_name=group.name),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            # Key(
            #    [_mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)),
        ]
    )

