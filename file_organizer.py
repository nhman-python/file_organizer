import os
import platform
import shutil
from tqdm import tqdm


def clear_screen():
    input('להמשך הקלד משהו...')
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        term = os.environ.get("TERM")
        if term:
            os.system("clear")


class FileOrganizer:
    def __init__(self):
        self.start = True
        self.ignore_paths = ['file_organizer.py', 'extensions.json']
        self.folder_paths = self.get_default_folder_paths()
        self.extensions_data = {
            "documents": [
                "conf",
                "xml",
                "kdenlive",
                "yaml",
                "log",
                "json",
                "iml",
                "mdb",
                "accdb",
                "chm",
                "pub",
                "pubx",
                "csv",
                "h",
                "hpp",
                "hxx",
                "ini",
                "java",
                "lua",
                "mht",
                "hteml",
                "odt",
                "pdf",
                "potx",
                "potm",
                "ppam",
                "ppsm",
                "ppsx",
                "pps",
                "ppt",
                "pptm",
                "pptx",
                "rtf",
                "sldm",
                "sldx",
                "thmx",
                "txt",
                "vsd",
                "wpd",
                "wps",
                "wri",
                "xlam",
                "xls",
                "xlsb",
                "xlsm",
                "xlsx",
                "xltm",
                "xltx"
            ],
            "fonts": [
                "fon",
                "ttf",
                "ttc",
                "fnt",
                "otf",
                "woff2"
            ],
            "adobe": [
                "3dxml",
                "prc",
                "u3d",
                "dwg",
                "jt",
                "xvl",
                "stl",
                "dxf",
                "indd",
                "ai",
                "psd"
            ],
            "scripts": [
                "sh",
                "sql",
                "go",
                "sum",
                "py",
                "cpp",
                "cxx",
                "doc",
                "docm",
                "docx",
                "dot",
                "dotm",
                "dotx",
                "cmd",
                "ps1",
                "bat"
            ],
            "video": [
                "3g2",
                "3gp",
                "3gp2",
                "3gpp",
                "amr",
                "amv",
                "asf",
                "avi",
                "bdmv",
                "bik",
                "d2v",
                "divx",
                "drc",
                "dsa",
                "dsm",
                "dss",
                "dsv",
                "evo",
                "f4v",
                "flc",
                "fli",
                "flic",
                "flv",
                "hdmov",
                "ifo",
                "ivf",
                "m1v",
                "m2p",
                "m2t",
                "m2ts",
                "m2v",
                "m4b",
                "m4p",
                "m4v",
                "mkv",
                "mp2v",
                "mp4",
                "mp4v",
                "mpe",
                "mpeg",
                "mpg",
                "mpls",
                "mpv2",
                "mpv4",
                "mov",
                "mts",
                "ogm",
                "ogv",
                "pss",
                "pva",
                "qt",
                "ram",
                "ratdvd",
                "rm",
                "rmm",
                "rmvb",
                "roq",
                "rpm",
                "smil",
                "smk",
                "swf",
                "tp",
                "tpr",
                "ts",
                "vob",
                "vp6",
                "webm",
                "wm",
                "wmp",
                "wmv"
            ],
            "audio": [
                "aac",
                "ac3",
                "aif",
                "aifc",
                "aiff",
                "au",
                "cda",
                "dts",
                "fla",
                "flac",
                "it",
                "m1a",
                "m2a",
                "m3u",
                "m4a",
                "mid",
                "midi",
                "mka",
                "mod",
                "mp2",
                "mp3",
                "mpa",
                "ogg",
                "ra",
                "rmi",
                "spc",
                "rmi",
                "snd",
                "umx",
                "voc",
                "wav",
                "wma"
            ],
            "archives": [
                "7z",
                "ace",
                "arj",
                "bz2",
                "cab",
                "gz",
                "gzip",
                "jar",
                "r00",
                "r01",
                "r02",
                "r03",
                "r04",
                "r05",
                "r06",
                "r07",
                "r08",
                "r09",
                "r10",
                "r11",
                "r12",
                "r13",
                "r14",
                "r15",
                "r16",
                "r17",
                "r18",
                "r19",
                "r20",
                "r21",
                "r22",
                "r23",
                "r24",
                "r25",
                "r26",
                "r27",
                "r28",
                "r29",
                "rar",
                "tar",
                "tgz",
                "z",
                "zip"
            ],
            "programs": [
                "AppImage",
                "exe",
                "msi",
                "msp",
                "scr",
                "deb"
            ],
            "applications": [
                "apk",
                "xapk",
                "aab",
                "apks",
                "apkm",
                "obb",
                "jar",
                "dex",
                "so"
            ],
            "iso": [
                "img",
                "iso",
                "bin",
                "nrg",
                "mdf",
                "cue",
                "ccd",
                "dmg",
                "b6t"
            ],
            "photos": [
                "webp",
                "svg",
                "bmp",
                "gif",
                "ico",
                "jpe",
                "jpeg",
                "jpg",
                "pcx",
                "png",
                "tga",
                "tif",
                "tiff",
                "wmf"
            ],
            "web app": [
                "htm",
                "html",
                "css",
                "js",
                "mhtml"
            ],
            "system": [
                "spec",
                "dll",
                "reg"
            ]
        }

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
        paths = {}

        if system == "Windows":
            paths["Documents"] = os.path.expanduser("~\\Documents")
            paths["Downloads"] = os.path.expanduser("~\\Downloads")
            paths["Videos"] = os.path.expanduser("~\\Videos")
            paths["Music"] = os.path.expanduser("~\\Music")
            paths["Pictures"] = os.path.expanduser("~\\Pictures")
        elif system == "Linux":
            paths["Documents"] = os.path.expanduser("~/Documents")
            paths["Downloads"] = os.path.expanduser("~/Downloads")
            paths["Videos"] = os.path.expanduser("~/Videos")
            paths["Music"] = os.path.expanduser("~/Music")
            paths["Pictures"] = os.path.expanduser("~/Pictures")
        elif system == "Darwin":  # macOS
            paths["Documents"] = os.path.expanduser("~/Documents")
            paths["Downloads"] = os.path.expanduser("~/Downloads")
            paths["Videos"] = os.path.expanduser("~/Movies")
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
                    for category, ext_list in extensions.items():
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
                            except (OSError, PermissionError, Exception) as error1:
                                print(f'קיבלנו שגיאה: {error1}')
                progress_bar.update(1)
            progress_bar.close()
        else:
            clear_screen()
            print('לא נמצאו קבצים להעברה')

    def analyze_folder(self, folder_path):
        if os.path.isdir(folder_path):
            self.move_files(folder_path, self.extensions_data)
        else:
            print('נתיב תקייה לא חוקי.')
            clear_screen()

    def select_option(self):
        self.start = True
        if self.start:
            self.start = False
        else:
            clear_screen()
        print('בחר אחת מהאפשרויות:')
        print('[1] תיקיית מסמכים')
        print('[2] תיקיית הורדות')
        print('[3] תיקיית וידאו')
        print('[4] תיקיית מוזיקה')
        print('[5] תיקיית תמונות')
        print('[6] נתיב מותאם אישית')
        print('[7.] יציאה')
        try:
            option = input('נא לבחור מספר [1-7]: ')
        except (KeyboardInterrupt, SystemExit):
            exit()
        if option == '1':
            folder_organize = self.folder_paths['Documents']
            self.analyze_folder(folder_organize)
        elif option == '2':
            folder_organize = self.folder_paths['Downloads']
            self.analyze_folder(folder_organize)
        elif option == '3':
            folder_organize = self.folder_paths['Videos']
            self.analyze_folder(folder_organize)
        elif option == '4':
            folder_organize = self.folder_paths['Music']
            self.analyze_folder(folder_organize)
        elif option == '5':
            folder_organize = self.folder_paths['Pictures']
            self.analyze_folder(folder_organize)
        elif option == '6':
            folder_organize = input('הזן נתיב: ')
            if os.path.isdir(folder_organize):
                warning = self.block_path(folder_organize)
                if not warning:
                    self.analyze_folder(folder_organize)
                else:
                    input('שגיאה זוהי תקיית מערכת')
                    self.select_option()
            else:
                print('נא להזין נתיב של תקיה שקיימת')
                self.select_option()
        elif option == '7':
            exit()
        else:
            print('אופציה לא קיימת נא לבחור שוב.')
            self.select_option()

    def main(self):
        while True:
            print('')
            self.select_option()


if __name__ == '__main__':
    file_organizer = FileOrganizer()
    file_organizer.main()
