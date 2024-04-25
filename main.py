import tkinter as tk

root = tk.Tk()
root.title("chocoladde ladder man")
#widthxheight+pad 50px from left+ pad 50px from top
#if you do -, then its reverse, right <-> bottom
root.geometry('600x400+50+50')
root.resizable(False, False)

#this grabs the current screen's dimension
curScreenWidth = root.winfo_screenwidth()
curScreenHeight = root.winfo_screenheight()

#find the center point (for centering the window on execution)
#centerX = int(curScreenWidth/2 - window_width/2)
#centerY = int(curScreenHeight/2 - window_height/2)
#root.geometry(f'{window_width}x{window_height}+{centerX}+{centerY}')


#root is the window where you want to place the Label
message = tk.Label(root, text="Hello, World!")
#pack positions Label onto the root window, if not called, label not visible
message.pack()
try:
    #windll is only for windows, since we are working on linux subsystem, no work
    #hahahahahahhah L bozo
    #anyways the purpose of this to make the ui and stuff not blurry .-.
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    #keeps window rendered on screen
    root.mainloop()

