screen test:

    drag:
        drag_name "say"
        yalign 1.0
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            # Ensure that the window is smaller than the screen.
            xmaximum 600

            has vbox

            if who:
                text who id "who"

            text what id "what"



screen hello_world():
    text "Hello, World."


init python:
    def detective_dragged(drags, drop):
        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True