from libqtile import bar, widget
from libqtile.config import Screen

import subprocess





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
                widget.GroupBox(fontsize=24,
                                block_highlight_text_color='#ffa500',
                                borderwidth=3,
                                active="#ffffff",
                                this_current_screen_border="#111111",
                                foreground="ffa500",
                                disable_drag=True,
                                inactive="#777777",
                                rounded=False,
                                urgent_border="#000000",
                                urgent_alert_method="line",
                                fmt="{}",
                                font="Roboto Mono",
                                markup=True,
                                highlight_method="block"),
                widget.Spacer(length=20),
                widget.WindowName(
                    font="Roboto Mono",
                    fmt="<b>{}</b>",
                    parse_text=parse_windowname,
                    fontsize=19,),
                widget.Spacer(length=40),
                widget.Spacer(length=20),
                widget.WindowCount(
                                 text_format="󰣇 {num} ",
                                 show_zero=True,
                                 ),
                widget.Net(format='{down:.0f}{down_suffix}   {up:.0f}{up_suffix}',
                           ),
                widget.Wlan(format="   ",
                            interface="wlp0s20f3",
                            disconnected_message=" 󰤮 ",
                            ),
                widget.Spacer(length=20),
                widget.Backlight(backlight_name='intel_backlight',
                                 format='{percent:2.0%}',
                                 fmt='<b>󰃟 {}</b>',
                                 change_command="brightnessctl set {}",
                                 ),
                widget.Spacer(length=20),
                widget.Battery(notify_below=30,
                               full_char="󱊣",
                               discharge_char="",
                               charge_char="󰂅",
                               empty_char="",
                               format="{char}   {percent:2.0%}",
                               ),
                widget.Spacer(length=20),
                widget.Volume(step=1,
                              fmt='<b>󰕾 {}</b>',
                              ),
                widget.Spacer(length=20),
                widget.Clock(format="󰔟 %I:%M  ",
                             ),
            ],
            size=24,
            background="#00000000",
        ),



    ),
]

widget_defaults = dict(
    font="Roboto Mono",
    fontsize=19,
    padding=4,
    fmt="<b>{}</b>",
    background="#00000000",
    foreground="#ffffff"
)
extension_defaults = widget_defaults.copy()
