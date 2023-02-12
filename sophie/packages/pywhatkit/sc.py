import os
import platform

try:
    import winerror
except ImportError or ModuleNotFoundError:
    pass

osname = platform.system()


def shutdown(time: int = 20) -> None:
    """Schedules a Shutdown after the Specified Time"""

    if "linux" in osname.lower():
        cont = f"shutdown -h {time}"
        os.system(cont)
        print(f"Your System will Shutdown in {time} Minutes!")

    else:
        raise Warning(
            f"Available on Windows, Mac and Linux only, can't Execute on {osname}"
        )


def cancel_shutdown() -> None:
    """Cancels the Scheduled Shutdown"""

    if "linux" in osname.lower():
        os.system("shutdown -c")
        print("Shutdown has been Cancelled!")

    else:
        raise Warning(
            f"Available on Windows, Mac and Linux only, can't Execute on {osname}"
        )
