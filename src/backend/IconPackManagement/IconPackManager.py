"""
Author: Core447
Year: 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This programm comes with ABSOLUTELY NO WARRANTY!

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

# Import Python modules
import json
import os
import shutil

# Import own modules
from src.backend.IconPackManagement.IconPack import IconPack

class IconPackManager:
    def __init__(self):
        self.packs = {}

    def get_icon_packs(self) -> dir:
        packs = {}
        for pack in os.listdir("icons"):
            packs[pack] = IconPack(os.path.join("icons", pack))
        return packs

    def get_pack_icons(self, icon_pack: dict):
        path = icon_pack.get("path")
        icons_path = os.path.join(path, "icons")

        icons = {}
        if os.path.exists(icons_path):
            for icon in os.listdir(icons_path):
                icons.setdefault(icon, {})
                icons[icon] =  self.get_icon_attribution(icon_pack.get("attribution"), icon)

        return icons
    
    def get_icon_attribution(self, attribution:dict, icon_name: str) -> dict:
        if icon_name in attribution:
            # Use specific
            return attribution[icon_name]
        else:
            # Use default
            return attribution.get("generic", attribution.get("default", attribution.get("general")))
            
    def prepare_icon_packs(self):
        return
        packs = self.get_icon_packs()

        prepared_packs = {}

        for pack in packs:
            prepared_packs[pack] = self.get_pack_icons(packs[pack])

        return prepared_packs