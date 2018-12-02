from cx_Freeze import setup, Executable


setup(
    name = "Форсаж",
    version = "0.1",
    description = "Robot",
    executables = [Executable("contoller.py")]
)