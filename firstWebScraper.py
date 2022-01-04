rom selenium import webdriver
from selenium.webdriver.support.select import By # This is the new 'standard'

url = 'https://www.youtube.com/c/KalleHallden/videos'
browser = webdriver.Chrome()
browser.get(url)
#browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

browser.find_element(By.XPATH, '//*[@id="video-title"]').click() # You can also just do the one below. This way just finds the id via an xpath, which is more complicated.
# browser.find_element(By.ID, "video-title").click()

# browser.find_element_by_xpath('//*[@id="img"]').click()  <-- this didn't work either



# def openPage(url):
#     '''
#     Features to add for this function for gfuture projects:
#         1)Use of proper error checking in pythin
#         2) Check the format of the URL

    
    
#     '''
#     if not isinstance(url,str) or url is None:
#         print("invalid input")
#         return

#     print("We are going to open a webpage")
#     browser = webdriver.Chrome()
#     browser.get(url)

#     #" Error when I used the wrong xpath =   find_element_by_* commands are deprecated. Please use find_element() instead
#     #   browser.find_element_by_xpath('//*[@id="img"]').click()"
#     # This was the code that I used that created  the problem
#         #    browser.find_element_by_xpath('//*[@id="img"]').click()

    
#     # string = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/ytd-thumbnail/a'
#     string = '//*[@id="thumbnail"]'
#     browser.find_element(string).click()

    
    
#     # browser.find_element('//*[@id="thumbnail"]').click()





# if __name__ == '__main__':
#     print("Hello world") #this was necessary 
#     url = 'https://www.youtube.com/c/KalleHallden/videos'
#     openPage(url)
