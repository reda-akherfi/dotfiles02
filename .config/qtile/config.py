import os 
import subprocess

mod = "mod4"
terminal = "alacritty"


from libqtile.lazy import lazy
from libqtile.extension import WindowList
from libqtile.config import Group, ScratchPad, DropDown, Key, Screen, Match, Drag, Click, Key, KeyChord
from libqtile import bar, widget, layout, hook

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### this is pywall related stuff
clk_widg_colr="#ffffff" # "#efbc9b"
vol_widg_colr="#ffffff"# "#9cafaa"
bat_widg_colr="#ffffff" # "#ffaf45"
wifi_widg_colr="#ffffff"# "#d74b76"
net_widg_colr="#ffffff"# "#b0c5a4"
nbrwin_widg_colr="#ffffff" # "#87a922"
cpu_widg_colr="#a5dd9b"
df_widg_colr="#387adf"
thrm_widg_colr="#b5c0d0"
#winname_colr="#2d9596"
winname_colr="#ffffff"
bri_widg_colr="#ffffff" # "#836fff"
winbox_active="#ffffff"
winbox_thiscurrscreenborder="#ffffff"
winbox_inactive="#333333"
winbox_urgbord="#ffffff"
winbox_urgtext="#ff0000"
windbox_foreground="#ffffff"
float_bord_foc="#b0c5a4"
float_bord_norm="#ffaf45"
colors = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
keys = [
    # Switch between windows
    Key([mod], "h", lazy.group.prev_window(), desc="Move focus to left"),
    Key([mod], "l", lazy.group.next_window(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),



    # Navigate to the workspace on the left
    Key([mod], "Left", lazy.screen.prev_group()),
    # Navigate to the workspace on the right
    Key([mod], "Right", lazy.screen.next_group()),

    # scratchpad for cmus, thunderbird, kitty...
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('email')),
    Key([mod], "q", lazy.group['scratchpad'].dropdown_toggle('quickie')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('spotify')),
    Key([mod], "u", lazy.group['scratchpad'].dropdown_toggle('logout')),
    # Key([mod], "a", lazy.group['scratchpad'].dropdown_toggle('windows')),
]
# MOVE/RESIZE FLOATING WINDOW
for key, x, y in [
        ("Left", -30, 0),
        ("Right", 30, 0),
        ("Up", 0, -30),
        ("Down", 0, 30)]:
    keys.append(Key([mod, "control"], key, lazy.window.move_floating(x, y)))
    keys.append(Key([mod, "shift"], key, lazy.window.resize_floating(x, y)))
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
                                  'thunderbird',
                                  height= 0.94,
                                  width= 0.9,
                                  x= 0.03,
                                  y= 0.03,
                                  on_focus_lost_hide= False,
                                  warp_pointer= False
                                  ),
                              DropDown(
                                  'spotify',
                                  'spotify',
                                  height= 0.8,
                                  width= 0.6,
                                  x= 0.2,
                                  y= 0.1,
                                  on_focus_lost_hide= False,
                                  warp_pointer= False
                                  ),
                              DropDown(
                                  'logout',
                                  'alacritty --class "logout menu" -e  ~/dotfiles/bin/logout.sh',
                                  height= 0.4,
                                  width= 0.4,
                                  x= 0.3,
                                  y= 0.3,
                                  on_focus_lost_hide= False,
                                  warp_pointer= False
                                  ),
                              DropDown(
                                  'windows',
                                  'alacritty --class "current window stash" -e windows.sh',
                                  height= 0.4,
                                  width= 0.4,
                                  x= 0.3,
                                  y= 0.3,
                                  on_focus_lost_hide= False,
                                  warp_pointer= False
                                  ),
                              DropDown(
                                  'quickie',
                                  'alacritty --command tmux attach',
                                  height= 0.8,
                                  width= 0.6,
                                  x= 0.2,
                                  y= 0.1,
                                  on_focus_lost_hide= False,
                                  warp_pointer= False
                                  )])]

groupies = [# Group(i) for i in ["  ", "  󱨠", "  ", "  ", "  "],
            Group(name="1", label=" 1 ", layout="max", matches=[Match(wm_class=["qutebrowser"])]),
            Group(name="2", label=" 2 ", layout="max"),
            Group(name="3", label=" 3 ", layout="max", matches=[Match(wm_class=["mpv"])]),
            Group(name="4", label=" 4 ", layout="max"),
            Group(name="5", label=" 5 ", layout="max", matches=[Match(wm_class=["thunderbird"])], spawn="thunderbird"),
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
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

layouts = [
    layout.Columns(border_width=3, 
                   border_focus="#ffffff",
                   margin=5),
    layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(border_focus=colors[0]),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Floating(border_focus=colors.green, border_normal=colors.red, border_width=3)
]

floating_layout = layout.Floating(
    border_focus=float_bord_foc,
    border_normal=float_bord_norm,
    border_width=3,
    width=1000,
    height=500,
    float_rules=[
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='ranger_qtbr_file_picker_alacritty'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(func=lambda c: c.has_fixed_size()),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
    ]
)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






# xdotool func for parsing the window class or name
def xdotool_parse_window_name(text):
    window_class = subprocess.run(["xdotool", "getwindowfocus", "getwindowclassname"], capture_output=True)
    return window_class.stdout.decode("utf-8")

def parse_windowname(text):
    """Return parsed window name for WindowName widget."""
    text_lst = text.split()
    if len(text_lst) > 2:
        #  text = text_lst[-1] + " : " + " ".join(text_lst[:-2])
        text = f"{text_lst[-1]} : {' '.join(text_lst[:-2])}"
    return text.replace("—", "-")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fontsize=20,
                                block_highlight_text_color="#ffffff",
                                borderwidth=3,
                                active=winbox_active,
                                this_current_screen_border=winbox_thiscurrscreenborder,
                                foreground=windbox_foreground,
                                disable_drag=True,
                                inactive=winbox_inactive,
                                rounded=False,
                                urgent_border=winbox_urgbord,
                                urgent_text=winbox_urgtext,
                                urgent_alert_method="line",
                                fmt="{}",
                                font="Roboto Mono",
                                markup=True,
                                highlight_method="line"),
                widget.Spacer(length=20),
                widget.WindowName(
                    font="Roboto Mono",
                    fmt="<b>{}</b>",
                    parse_text=parse_windowname,
                    foreground=winname_colr,
                    fontsize=19),
                widget.Spacer(length=40),
                widget.Spacer(length=20),
                widget.WindowCount(
                                 text_format="󰣇 {num} ",
                                 show_zero=True,
                                 foreground=nbrwin_widg_colr
                                 ),
                widget.Net(format='{down:.0f}{down_suffix}   {up:.0f}{up_suffix}',
                                 foreground=net_widg_colr
                           ),
                # widget.Wlan(fmt="  {}",
                #             format="<b>{essid} {percent:2.0%}</b>",
                #             interface="wlp0s20f3",
                #             disconnected_message=" 󰤮 ",
                #             foreground=wifi_widg_colr
                #             ),
                widget.Spacer(length=20),
                widget.Backlight(backlight_name='intel_backlight',
                                 format='{percent:2.0%}',
                                 fmt='<b>󰃟 {}</b>',
                                 change_command="brightnessctl set {}",
                                 foreground=bri_widg_colr
                                 ),
                # widget.Battery(notify_below=30,
                #                full_char="󱊣",
                #                discharge_char="",
                #                charge_char="󰂅",
                #                empty_char="",
                #                format="{char}   {percent:2.0%}",
                #                foreground=bat_widg_colr
                #                ),
                widget.Spacer(length=20),
                # widget.Volume(step=1,
                #               fmt='<b>󰕾 {}</b>',
                #               foreground=vol_widg_colr
                #               ),
                widget.Systray(padding=10,
                               icon_size=25),
                widget.Spacer(length=20),
                widget.Clock(format="󰔟 %I:%M  ",
                             foreground=clk_widg_colr
                             ),
            ],
            size=30,
            background="#000000",
            opacity=0.9,
            margin=3,
        ),
    ),
]

widget_defaults = dict(
    font="Roboto Mono",
    fontsize=19,
    padding=4,
    fmt="<b>{}</b>",
    background="#000000",
    foreground=clk_widg_colr
)
extension_defaults = widget_defaults.copy()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
