# Scheme of future endpoints:
"""
/files-list: Returns list of files in dict() type. Format:
    file = {
        "file_name": "something" (both sides converted to string())
        "contains": "something^2 I think?" (also string, if availble (scripts, .txt files,  .sh, .zshrc, .config, .toml, etc), else BINARY (.exe, etc)
        "size": 1024 (just  count it by 1024 bytes until you have whole size)
        "original_location": "/mnt/Games/Temp/Cute_carpets.mp5" (PATH, gonna figure out how to make it properly)

    }

example:
    {
    'Welcome_to':
        'Liveriev',
        "size": 5120,
        "original_location": "/home/USER/Videos/cute_cats_video.txt"
    }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/files-upload: sends request to ./core/upload.py, format:
    file = {
        "file_id": UID from DB, to avoid any issues like:

        File to upload: Cat_Photo_of_me_yes.mp10
        Selected file by error: Cat_Photo_of_me_yes.png
        instead, we just use UID
        (yes I know it won't fix naming  of my files and what, but:
            it'll just make percentage of "I uploaded wrong file" much lower cuz it'll just remove
                wrong/incorrect UID's on uploading stage)

    }
"""
