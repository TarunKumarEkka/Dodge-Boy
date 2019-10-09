import cx_Freeze

executables = [cx_Freeze.Executable("1.py")]
includefiles =["11.png","22.png","bck.jpg","123.jpg"]
cx_Freeze.setup(
    name ="Dodge boy",
    version='0.1',
    description="A 2D game for dodge the object",
    author="TK EKKA",
    options={"build_exe":{"packages":["pygame"],"include_files":includefiles
                          }},
    executables =executables
    )
