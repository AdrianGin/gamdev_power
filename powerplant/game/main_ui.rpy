screen volume_controls():
    frame:
        has vbox

        bar value Preference("sound volume")
        bar value Preference("music volume")
        bar value Preference("voice volume")


