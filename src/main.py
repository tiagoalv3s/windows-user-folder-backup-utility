from pathlib import Path
import shutil

main_path = Path.home()
backups = Path.home() / 'backups'

directories = [ 
    'Downloads', 
    'Desktop', 
    'Pictures', 
    'Videos', 
    'Music', 
    'Other'
    ]

for item in directories:
    if not Path(backups/item).is_dir():
        Path(backups/item).mkdir(parents=True, exist_ok=True)


