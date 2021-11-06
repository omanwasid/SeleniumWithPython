from selenium import webdriver
driver = webdriver.Chrome()

#save the url to navigate to
url = 'file:///C:/Users/45422/PycharmProjects/selenium/checkbox_radio.html'

#Navigate to the url
driver.get(url)

def assert_element_is_checkbox(element):

    my_element_type = element.get_attribute('type')

    if my_element_type != 'checkbox':
        raise AssertionError('The passed is not a checkbox')

    return

def is_checkbox_selected(element):

    assert_element_is_checkbox(element)

    if element.is_selected():
        return True
    else:
        return False

def assert_checkbox_is_selected(element):

    assert_element_is_checkbox(element)

    if not is_checkbox_selected(element):
        raise  AssertionError('The element is not selected.')

    return

def assert_checkbox_is_enabled(element):

    assert_element_is_checkbox(element)

    if not element.is_enabled():
        raise  AssertionError('The checkbox is not enabled.')


# Start of function calls

java_box = driver.find_element_by_name('java')

print(is_checkbox_selected(java_box))
assert_checkbox_is_enabled(java_box)

php_box = driver.find_element_by_name('php')
print(php_box.is_enabled())
