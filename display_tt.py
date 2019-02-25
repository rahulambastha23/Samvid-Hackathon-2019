from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x200")

timeTable_4A = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]


frame = Frame(root)
frame.pack()

tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6), height = 10, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="Column 1")
tree.heading(2, text="Column 2")
tree.heading(3, text="Column 3")
tree.heading(4, text="Column 4")
tree.heading(5, text="Column 5")
tree.heading(6, text="Column 6")

tree.column(1, width = 100)
tree.column(2, width = 100)
tree.column(3, width = 100)
tree.column(4, width = 100)
tree.column(5, width = 100)
tree.column(6, width = 100)
for val in timeTable_4A:
    tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6]) )

root.mainloop()