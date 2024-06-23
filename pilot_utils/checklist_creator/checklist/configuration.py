from typing import Dict, Union
from reportlab.lib.pagesizes import A5

PAGE_SIZES_DICT = {'A5': A5}

class ChecklistConfiguration:
    def __init__(self):
        """
            Class that contains all configuration values
            and defaults for them.
        """
        # Border margins
        self.border_left = 80
        self.border_right = 50
        self.border_top = 80
        self.border_bottom = 80
        # Fonts and font sizes
        self.font_name_item = "Helvetica"
        self.font_name_bold_item = "Helvetica-Bold"
        self.font_size_item = 6
        self.font_name_section_name = "Helvetica-Bold"
        self.font_size_section_name = 9
        self.font_name_header_footer = "Helvetica-Bold"
        self.font_size_header_footer = 6
        # Space between different elements
        self.space_after_header = 30
        self.space_between_sections = 32
        self.space_section_to_item = 20
        self.space_between_items = 10
        self.space_for_enumerations = 10
        self.space_before_footer = 0
        # Page size
        self.page_size = PAGE_SIZES_DICT["A5"]
        # For real world usage?
        self.real_world_clearance = False


    def update_configuration(self,
                             new_config: Dict[str, Union[int, str]],
                             print_missing_elements: bool = True
                             ):
        """
            Updates the configuration with values from the provided dictionary.
            Attributes that are not present in the configuration are ignored and
            printed at the end if print_missing_elements is True.

        Params
        ------
            new_config (Dict[str, Union[int, str]]):
                Dictionary that contains the new configuration values
            print_missing_elements (bool):
                Whether configuration elements from new-config that were ignored
                should be printed at the end. Defaults to True
        """
        missing_elements = []
        for key, value in new_config.items():
            if hasattr(self, key):
                if key == 'page_size':
                    if value not in PAGE_SIZES_DICT.keys():
                        raise ValueError(f"The requested page_size {value} is not supported. Currently supported are: {list(PAGE_SIZES_DICT.keys())}")
                    self.page_size = PAGE_SIZES_DICT[value]
                elif key == 'real_world_clearance':
                    if value.lower() == "false":
                        self.real_world_clearance = False
                    else:
                        self.real_world_clearance = True
                else:
                    setattr(self, key, value)
            else:
                missing_elements.append(key)
        if print_missing_elements and len(missing_elements) > 0:
            print(f"The following configuration elements were ignored: {missing_elements}")