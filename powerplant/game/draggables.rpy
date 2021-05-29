init python:
    Incorrect = 0
    Correct = 1
    Completed = 2

    def detective_dragged(drags, drop):
        if not drop:
            return None

        if drags[0].drag_name.item.id != drop.drag_name.item.id:
            return Incorrect

        drags[0].drag_name.item_list.remove(drags[0].drag_name.item)
        return Correct

    class player:
        def __init__(self):
            self.availablePower = 100
            self.meltdownLevel = 0
            self.isLightMode = False
            
    class drag_context:
        def __init__(self, item, item_list):
            self.item = item
            self.item_list = item_list

    class item_location:
        def __init__(self, id, x, y, type):
            self.id = id
            self.x = x
            self.y = y
            self.type = type


    class SoftTimer:
        def __init__(self, timeout, callback, context):
            self.timeout = timeout / 50
            self.counter = 0
            self.callback = callback
            self.context = context
            self.enabled = False

        def Service(self):
            self.counter = self.counter + 1
            if self.counter >= self.timeout:
                self.callback(self.context)
                self.counter = 0


init python:
    const_l1_files = []
    const_l1_folders = []

    timers = []
    player_data = player()

    def initGame():
        initLevels()
        initPlayer()
        initTimers()

    def initLevels():
        global const_l1_files
        global const_l1_folders

        File1 = item_location(0, 300,300, "file white.png")
        Folder1 = item_location(0, 200,120, "folder white.png")

        File2 = item_location(1, 300,100, "file t2.png")
        Folder2 = item_location(1, 200,350, "folder t2.png")

        const_l1_files = [File1, File2]
        const_l1_folders = [Folder1, Folder2]
        return

    def initPlayer():
        global player_data
        player_data = player()

    def initTimers():
        global timers
        global player_data
        timers.append( SoftTimer(1000, PowerTimerCallback, player_data) )


    def PowerTimerCallback(context):
        #context.availablePower = context.availablePower - 1
        pass

    def periodic_callback():
        for i, timer in enumerate(timers):
            timer.Service()



    def show_countdown(st, at):
        if st > 5.0:
            return Text("0.0"), None
        else:
            d = Text("{:.1f}".format(5.0 - st))
            return d, 0.1
