from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class QuizizzUploader:
    def __init__(self, username, password, file_path):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.file_path = file_path
    
    def login(self):
        self.driver.get('https://quizizz.com/')
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-top-nav"]')
        login_button.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 10)
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-0"]/div/div[2]/div[2]/section/section/section/section[1]/section/section[2]/section[1]/button[2]')))
        next_button.click()
        time.sleep(3)

        username_field = self.driver.find_element(By.XPATH, '//*[@id="email-field-input"]')
        username_field.send_keys(self.username)
        time.sleep(3)

        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-0"]/div/div[2]/div[2]/section/section/section/section[1]/div/form/button[2]/span')))
        continue_button.click()
        time.sleep(3)

        password_field = self.driver.find_element(By.XPATH, '//*[@id="password-field-input"]')
        password_field.send_keys(self.password)
        time.sleep(3)

        password_field.send_keys(Keys.RETURN)
        time.sleep(4)

    def upload_quiz(self, quiz_name, button_xpath, file_path):
        create_content_button = self.driver.find_element(By.XPATH, '//*[@id="base-0"]/div/div[1]/div/header/div/div/button')
        create_content_button.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="base-0"]/div/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/div[2]/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="base-0"]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[4]').click()
        time.sleep(3)
        file_input = self.driver.find_element(By.XPATH, '//*[@id="quiz-editor"]/div[2]/div/div/div[3]/div/input')
        file_input.send_keys(file_path)
        time.sleep(3)
        button_selector = '//*[@id="quiz-editor"]/div[2]/div/div/div[4]/div[2]/button[2]' 
        button = self.driver.find_element(By.XPATH, button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.perform()
        button.click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, '//*[@id="score-container"]/div/div[1]/button[2]/div').click()
        time.sleep(3)
        quiz_name_field = self.driver.find_element(By.XPATH, '//*[@id="modal-layer-2"]/div/div/div/body/div/section[1]/div[1]/div[1]/input')
        quiz_name_field.send_keys(quiz_name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="modal-layer-2"]/div/div/div/footer/div/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="quiz-editor-header"]/div[2]/button[3]').click()
        time.sleep(3)

    def close(self):
        self.driver.quit()