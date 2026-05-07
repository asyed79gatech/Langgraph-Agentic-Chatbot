# Import the module required to read the contents of a configfile
from configparser import ConfigParser

# Create a class for reading the content of the config file

class Config:
    def __init__(self, config_file_path = "src/langgraphagenticai/ui/streamlitui/uiconfigfile.ini"):
        self.config_parser = ConfigParser()
        self.config_parser.read(config_file_path)

    def get_llm_options(self):
        return self.config_parser["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def groq_model_options(self):
        return self.config_parser['DEFAULT'].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def use_case_options(self):
        return self.config_parser['DEFAULT'].get("USE_CASE_OPTIONS").split(", ")
    
    def page_title(self):
        return self.config_parser['DEFAULT'].get("PAGE_TITLE")