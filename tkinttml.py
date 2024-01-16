from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label
my_label = HTMLLabel(root, html="""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScEEVT8UZ4YsJ7Fhe_PgGqgk8QrCeUoJ8QALFTzjsMiBNUkTg/viewform?embedded=true" width="640" height="382" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """)
 
# Adjust label
my_label.pack(pady=20, padx=20)
 
# Execute Tkinter
root.mainloop()