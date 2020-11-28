import Auto_async
import Xl_Automatic
import Run_macros
import sftp_fileShare
import UI_Automation


if __name__ == '__main__':
    Auto_async.session_met(concurrency=1000,
                           duration=1000,
                           timeout=1000)

    Xl_Automatic.handel_XL()

    Run_macros.macro_run()

    sftp_fileShare.share_file()

    UI_Automation.automate()
