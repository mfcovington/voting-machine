from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException


class PepsiVoter:

    def __init__(self, poll_url, player):
        self.poll_url = poll_url
        self.player = player

    def start_browser(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def open_voting_page(self):
        self.browser.get(self.poll_url)

    def hide_video(self):
        self.browser.execute_script(
            'document.getElementsByClassName("video-area")[0].style.display = "none";')

    def cast_vote(self):
        pick_items = self.browser.find_elements_by_class_name('pick-items')

        for pick in pick_items:
            if self.player.lower() in pick.text.lower():
                vote_check = pick.find_element_by_class_name('vote-check')
                vote_check.click()

        close_x = self.browser.find_element_by_class_name('close-x')
        close_x.click()

    def refresh_browser(self):
        self.browser.refresh()

    def close_browser(self):
        self.browser.quit()


def pepsi_auto_vote(poll_url, player, votes=-1):
    v = PepsiVoter(poll_url=poll_url, player=player)
    v.start_browser()
    v.open_voting_page()
    v.hide_video()

    vote_counter = 0
    while vote_counter < votes or votes == -1:
        try:
            v.cast_vote()
        except ElementNotVisibleException as e:
            print(e)
            print('Refreshing Browser...')
            v.refresh_browser()
            v.hide_video()
        else:
            vote_counter += 1
            print(vote_counter)

    v.close_browser()


if __name__ == '__main__':
    pepsi_auto_vote(
        poll_url='http://www.nfl.com/voting/rookies/2015/YEAR/0',
        player='Tyler Lockett', votes=10)
