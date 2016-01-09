from selenium import webdriver


class Voter:

    def start_browser(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def open_voting_page(self):
        self.browser.get('http://www.nfl.com/voting/rookies/2015/YEAR/0')

    def hide_video(self):
        self.browser.execute_script(
            'document.getElementsByClassName("video-area")[0].style.display = "none";')

    def vote_for_lockett(self):
        pick_items = self.browser.find_elements_by_class_name('pick-items')

        for pick in pick_items:
            if 'TYLER LOCKETT' in pick.text:
                vote_check = pick.find_element_by_class_name('vote-check')
                vote_check.click()

        close_x = self.browser.find_element_by_class_name('close-x')
        close_x.click()

    def close_browser(self):
        self.browser.quit()


if __name__ == '__main__':
    v = Voter()
    v.start_browser()
    v.open_voting_page()
    v.hide_video()

    vote_counter = 0
    while True:
        v.vote_for_lockett()
        vote_counter += 1
        print(vote_counter)

    v.close_browser()
