from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select

# GLOBALS
BLANK_CARD_TEMPLATE = "https://www.makeplayingcards.com/design/custom-blank-card.html"
PAPER_TYPE_DROPDOWN = "dro_paper_type"
DECK_SIZE_DROPDOWN  = "dro_choosesize"
FOIL_DROPDOWN       = "dro_product_effect"
FOIL_FINISH_VALUE   = "EF_055"

SCRIPTS = {
    'personalize': "doPersonalize('https://www.makeplayingcards.com/products/pro_item_process_flow.aspx')",
    '': ""
}

def js(k):
    return f"javascript:{SCRIPTS.get(k)}"


class MPC_API:
    def fill_cards(bar: tqdm, root):
        """
        TODO: Add desc
        """
        # Navigate to Game Cards (63mm x 88mm) page
        self.driver.get(BLANK_CARD_TEMPLATE)


        # Select card stock and deck size
        c_count, dk_size, p_type, is_foil = root[0]

        type_drp = Select(self.driver.find_element_by_id(PAPER_TYPE_DROPDOWN))
        type_drp.select_by_visible_text(p_type.text)

        size_drp = Select(self.driver.find_element_by_id(DECK_SIZE_DROPDOWN))
        size_drp.select_by_visible_text(dk_size.text)

        if is_foil.text == "true":
            foil_drp = Select(self.driver.find_element_by_id(FOIL_DROPDOWN))
            foil_drp.select_by_value(FOIL_FINISH_VALUE)

        self.driver.execute_script(js('personalize'))


    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_options
        )
        self.driver.set_window_size(1200, 900)
        self.driver.implicitly_wait(5)

