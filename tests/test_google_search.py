from selene.support.shared import browser
from selene import be, have


def test_positive(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))
    print('Positive test successful')


def test_negative(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ng').press_enter()
    browser.element("[id='result-stats']").should(have.text('По запросу ng ничего не найдено.'))
    print('Negative test passed')
