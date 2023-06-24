import os
import platform
import shutil
from tqdm import tqdm


def clear_screen():
    system = platform.system()

    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class FileOrganizer:
    def __init__(self):
        self.start = True
        self.ignore_paths = ['file_organizer.py']
        self.folder_paths = self.get_default_folder_paths()
        self.extensions_data = (
            (
                ("documents", (
                    "conf", "xml", "kdenlive", "yaml", "log", "json", "iml", "mdb", "accdb", "chm", "pub", "pubx",
                    "csv", "h",
                    "hpp", "hxx", "ini", "java", "lua", "mht", "hteml", "odt", "pdf", "potx", "potm", "ppam", "ppsm",
                    "ppsx",
                    "pps", "ppt", "pptm", "pptx", "rtf", "sldm", "sldx", "thmx", "txt", "vsd", "wpd", "wps", "wri",
                    "xlam", "xls",
                    "xlsb", "xlsm", "xlsx", "xltm", "xltx")
                 )
            ),
            (
                "fonts", (
                    "fon", "ttf", "ttc", "fnt", "otf", "woff2")
            ),
            (
                "adobe", (
                    "3dxml", "prc", "u3d", "dwg", "jt", "xvl", "stl", "dxf", "indd", "ai", "psd")
            ),
            (
                "scripts", (
                    "sh", "sql", "go", "sum", "py", "cpp", "cxx", "doc", "docm", "docx", "dot", "dotm", "dotx", "cmd",
                    "ps1",
                    "bat")
            ),
            (
                "video", (
                    "3g2", "3gp", "3gp2", "3gpp", "amr", "amv", "asf", "avi", "bdmv", "bik", "d2v", "divx", "drc",
                    "dsa", "dsm",
                    "dss", "dsv", "evo", "f4v", "flc", "fli", "flic", "flv", "hdmov", "ifo", "ivf", "m1v", "m2p", "m2t",
                    "m2ts",
                    "m2v", "m4b", "m4p", "m4v", "mkv", "mp2v", "mp4", "mp4v", "mpe", "mpeg", "mpg", "mpls", "mpv2",
                    "mpv4", "mov",
                    "mts", "ogm", "ogv", "pss", "pva", "qt", "ram", "ratdvd", "rm", "rmm", "rmvb", "roq", "rpm", "smil",
                    "smk",
                    "swf", "tp", "tpr", "ts", "vob", "vp6", "webm", "wm", "wmp", "wmv")
            ),
            (
                "audio", (
                    "aac", "ac3", "aif", "aifc", "aiff", "au", "cda", "dts", "fla", "flac", "it", "m1a", "m2a", "m3u",
                    "m4a",
                    "mid", "midi", "mka", "mod", "mp2", "mp3", "mpa", "ogg", "ra", "rmi", "spc", "rmi", "snd", "umx",
                    "voc",
                    "wav", "wma")
            ),
            (
                "archives", (
                    "7z", "ace", "arj", "bz2", "cab", "gz", "gzip", "jar", "r00", "r01", "r02", "r03", "r04", "r05",
                    "r06", "r07",
                    "r08", "r09", "r10", "r11", "r12", "r13", "r14", "r15", "r16", "r17", "r18", "r19", "r20", "r21",
                    "r22", "r23",
                    "r24", "r25", "r26", "r27", "r28", "r29", "rar", "tar", "tgz", "z", "zip")
            ),
            (
                "programs", (
                    "AppImage", "exe", "msi", "msp", "scr", "deb")
            ),
            (
                "applications", (
                    "apk", "xapk", "aab", "apks", "apkm", "obb", "jar", "dex", "so")
            ),
            (
                "iso", (
                    "img", "iso", "bin", "nrg", "mdf", "cue", "ccd", "dmg", "b6t")
            ),
            (
                "photos", (
                    "webp", "svg", "bmp", "gif", "ico", "jpe", "jpeg", "jpg", "pcx", "png", "tga", "tif", "tiff", "wmf")
            ),
            (
                "web app", (
                    "htm", "html", "css", "js", "mhtml")
            ),
            (
                "system", (
                    "spec", "dll", "reg")
            )
        )

    def block_path(self, path_analysis):
        system = platform.system()
        if system == "Windows":
            system_folders = [
                os.path.expanduser("~"),
                os.path.expandvars(os.path.join("%WINDIR%", "Win32")),
                os.path.expandvars(os.path.join("%WINDIR%", "System32"))
            ]
        elif system == "Linux":
            system_folders = [
                os.path.expanduser("~"),
                "/usr/bin",
                "/usr/sbin",
                "/usr/lib",
                "/etc",
                "/var",
                "/"
            ]
        elif system == "Darwin":  # macOS
            system_folders = [
                os.path.expanduser("~"),
                "/System",
                "/Applications",
                "/Library",
                "/usr/bin",
                "/usr/sbin",
                "/usr/lib",
                "/etc",
                "/var",
                "/"
            ]
        else:
            raise NotImplementedError("מערכת הפעלה לא מזוהה: " + system)

        for folder in system_folders:
            if os.path.commonpath([path_analysis, folder]) == os.path.normpath(folder):
                return True

        return False

    def get_default_folder_paths(self):
        system = platform.system()
        paths = {
            "Documents": "",
            "Downloads": "",
            "Videos": "",
            "Music": "",
            "Pictures": ""
        }

        if system == "Windows":
            paths["Documents"] = os.path.expanduser("~\\Documents")
            paths["Downloads"] = os.path.expanduser("~\\Downloads")
            paths["Videos"] = os.path.expanduser("~\\Videos")
            paths["Music"] = os.path.expanduser("~\\Music")
            paths["Pictures"] = os.path.expanduser("~\\Pictures")
        elif system in ("Linux", "Darwin"):
            paths["Documents"] = os.path.expanduser("~/Documents")
            paths["Downloads"] = os.path.expanduser("~/Downloads")
            paths["Videos"] = os.path.expanduser("~/Videos")
            paths["Music"] = os.path.expanduser("~/Music")
            paths["Pictures"] = os.path.expanduser("~/Pictures")
        else:
            raise NotImplementedError("מערכת הפעלה לא מוכרת: " + system)

        return paths

    def get_files_to_move(self, folder_path):
        list_files = os.listdir(folder_path)
        files_to_move = []
        for file in list_files:
            if os.path.isfile(os.path.join(folder_path, file)) and file not in self.ignore_paths:
                files_to_move.append(file)
        return files_to_move

    def move_files(self, folder_path, extensions):
        files_to_move = self.get_files_to_move(folder_path)
        total_files = len(files_to_move)
        if total_files > 0:
            progress_bar = tqdm(total=total_files, desc='מעביר קבצים', unit='file')
            for file in files_to_move:
                if file not in self.ignore_paths:
                    extension = file.split('.')[-1]
                    for category, ext_list in extensions:
                        if extension.lower() in ext_list:
                            folder_to_move = os.path.join(folder_path, category)
                            if not os.path.exists(folder_to_move):
                                os.makedirs(folder_to_move)
                            else:
                                if not os.path.isdir(folder_to_move):
                                    try:
                                        os.makedirs(folder_to_move)
                                    except (OSError, PermissionError, Exception) as error:
                                        print(f'שגיאה: {error}')
                                        continue
                            try:
                                file_to_move = os.path.join(folder_to_move, file)
                                src_path_file = os.path.join(folder_path, file)
                                shutil.move(src_path_file, folder_to_move)
                            except shutil.Error as e:
                                print(f'ERROR: {e}')
                progress_bar.update(1)
            progress_bar.close()
            input('הפעולה בוצע בהצלחה הקלד משהו להמשך...')
            clear_screen()
        else:
            clear_screen()
            input('לא נמצאו קבצים להעברה להמשך הקלד משהו...')

    def analyze_folder(self, folder_path):
        if os.path.isdir(folder_path):
            self.move_files(folder_path, self.extensions_data)
        else:
            print('נתיב תקייה לא חוקי.')
            clear_screen()

    def select_option(self):
        folder_mapping = {
            '1': 'Documents',
            '2': 'Downloads',
            '3': 'Videos',
            '4': 'Music',
            '5': 'Pictures'
        }

        while True:
            print('בחר אחת מהאפשרויות:')
            print('[1] תיקיית מסמכים')
            print('[2] תיקיית הורדות')
            print('[3] תיקיית וידאו')
            print('[4] תיקיית מוזיקה')
            print('[5] תיקיית תמונות')
            print('[6] נתיב מותאם אישית')
            print('[7] יציאה')

            try:
                option = input('נא לבחור מספר [1-7]: ')
            except (ValueError, TypeError, KeyboardInterrupt):
                exit()

            if option == '6':
                folder_organize = input('הזן נתיב: ')
                if not os.path.isdir(folder_organize):
                    print('נא להזין נתיב של תקיה שקיימת')
                    continue

                if self.block_path(folder_organize):
                    input('שגיאה זוהי תקיית מערכת הקלד משהו להמשך')
                    clear_screen()
                    continue

                self.analyze_folder(folder_organize)
            elif option == '7':
                exit()
            elif option in folder_mapping:
                folder_organize = self.folder_paths[folder_mapping[option]]
                self.analyze_folder(folder_organize)
            else:
                print('אופציה לא קיימת נא לבחור שוב.')

    def main(self):
        while True:
            print('')
            self.select_option()


if __name__ == '__main__':
    file_organizer = FileOrganizer()
    file_organizer.main()
