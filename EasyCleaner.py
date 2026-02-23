import os, shutil

USELESS_EXT = {
    ".log",".tmp",".temp",".bak",".old",".cache",
    ".chk",".dmp",".err",".swp",".swo",
    ".part",".crash",".trace",".dbg",
    ".~tmp",".~lock",".ilk",".gid",
    ".ncb",".sdf",".idb",".pdb"
}

USELESS_NAMES = {"thumbs.db",".ds_store","desktop.ini"}

USELESS_DIRS = {
    "temp","tmp",
    "cache","caches",
    "log","logs",
    "__pycache__",".cache"
}

def is_useless_file(name):
    n = name.lower()
    return n in USELESS_NAMES or any(n.endswith(e) for e in USELESS_EXT)

def clean(base):
    print(f"\n📂 Working directory: {base}")

    for root, dirs, files in os.walk(base, topdown=False):

        for f in files:
            if is_useless_file(f):
                path = os.path.join(root, f)
                try:
                    os.remove(path)
                    print(f"[FILE REMOVED] {path}")
                except Exception as e:
                    print(f"[ERROR] {path} -> {e}")

        for d in dirs:
            path = os.path.join(root, d)

            if d.lower() in USELESS_DIRS:
                try:
                    shutil.rmtree(path)
                    print(f"[DIR REMOVED] {path}")
                    continue
                except Exception as e:
                    print(f"[DIR ERROR] {path} -> {e}")

            try:
                if not os.listdir(path):
                    os.rmdir(path)
                    print(f"[EMPTY DIR REMOVED] {path}")
            except:
                pass

if __name__ == "__main__":
    clean(os.path.dirname(os.path.abspath(__file__)))