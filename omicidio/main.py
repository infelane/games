import os
import time

from scipy import ndimage
from io import BytesIO
import numpy as np
from PIL import Image
from selenium import webdriver

from config import keys

import matplotlib.pyplot as plt


def supreme_bot():

    # will cookies improve load time?
    # options = webdriver.ChromeOptions()
    # options.add_argument('user-data-dir=www.supremenewyork.com')

    @timeme
    def order():
        # add to cart
        driver.find_element_by_name('commit').click()

        # wait for checkout button element to load
        time.sleep(.5)
        checkout_element = driver.find_element_by_class_name('checkout')
        checkout_element.click()

        # fill out checkout screen fields
        driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
        driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
        driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
        driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
        driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
        driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
        driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
        driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])

        process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
        process_payment.click()

    if __name__ == '__main__':
        # load chrome

        # get product url
        driver.get(keys['product_url'])
        order()


def reopen_sess():
    """
    https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
    :return:
    """

    # executor_url = driver.command_executor._url
    # session_id = driver.session_id
    
    url = 'http://127.0.0.1:61208'
    session_id = 'a2d2a063a92deb957cf6a3cec41fce30'
    
    from selenium.webdriver.remote.webdriver import WebDriver

    def attach_to_session(executor_url, session_id):
        original_execute = WebDriver.execute

        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)

        # Patch the function before creating the driver object
        WebDriver.execute = new_command_execute
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver.session_id = session_id
        # Replace the patched function with original function
        WebDriver.execute = original_execute
        return driver

    bro = attach_to_session(url, session_id)

    return bro


def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime) / 1000, 's')
        return result

    return wrapper


def captch_solver(img):
    img = img[:, :, :3]

    def cleanup(im):

        if 0: dist = np.sqrt(np.mean(np.square(im - 0), axis=-1))

        else:
            dist = np.sqrt(np.mean(np.abs(im - 0), axis=-1))

        result = ndimage.median_filter(dist, size=3)

        # Grayscale


        # b = []
        # for i in range(3):
        #     b.append(im[..., 0] < .1 * 255)
        #
        # bo = np.logical_and(np.logical_and(b[0], b[1]), b[2])
        # c = np.zeros(shape=im.shape[:2], dtype=im.dtype)
        # c[bo] = 255

        if 0:
            plt.imshow(result,  vmin=result.min(), vmax=result.max())

        return result

    def threeLetters(im):

        w = im.shape[1]
        w_single = w//3

        im_crops = []

        for i in range(3):
            im_crop = im[:, w_single*i:w_single*(i+1), ...]

            im_crop = (im_crop - im_crop.min())/(im_crop.max() - im_crop.min())

            im_crops.append(im_crop)

        plt.figure()
        for i, im_crop in enumerate(im_crops):
            plt.subplot(1, 3, i+1)
            plt.imshow(im_crop, vmin=im_crop.min(), vmax=im_crop.max(), cmap='gray')
        plt.show(True)

        return im_crops

    def recog(im_letters):

        import pytesseract
        """
        https://github.com/UB-Mannheim/tesseract/wiki
        https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
        """
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Laurens_laptop_w\AppData\Local\Tesseract-OCR\tesseract.exe'

        guess = []
        for im_letter in im_letters:



            plt.imshow(arr)
            plt.show()

            b = cleanup(arr)
            plt.imshow(b)
            plt.show()

            im = Image.fromarray((im_letter*255).astype(np.uint8))
            im = im.convert('1', dither=Image.NONE)

            pytesseract.image_to_string(im,
                                        # lang='fra'
                                        )

            guess.append(None)  # TODO
        print(guess)
        return

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(img, vmin=0, vmax=255)
    plt.subplot(1, 2, 2)
    im1 = cleanup(img)
    plt.imshow(im1, vmin=im1.min(), vmax=im1.max())
    plt.show(True)



    l = threeLetters(im1)

    recog(l)

    return input('TODO, now input captcha code')


def main():
    # screenGrab()  # Probably not gonna do it like that for now.


    # Do one

    # Later: Repeat?

    # supreme_bot()

    driver = reopen_sess()
    driver.implicitly_wait(1)

    # Switch to Misdaden (don't know which one yet)
    if 1:
        # TODO not this url, but instead "click" it?

        # #driver.find_element_by_xpath('//*[@id="Misdaad"]')#.click()
        # xpath = '/html/body/div/div[8]/div/a[4]'
        # driver.find_element_by_xpath(xpath)
        #
        # driver.find_element_by_name('Misdaad').click()

        # Go to *Misdaad*

        url_crime = 'http://www.omicidio.nl/crime.php'
        if driver.current_url != url_crime:
            driver.get(url_crime)

    if 0:
        """
        Click highest percentage
        """
        # TODO Find highest:
        el_button = driver.find_element_by_xpath('//*[@id="chk4"]')
        el_button.click()

    if 1:
        # If you have to wait, don't try anything
        el_waiting = '/html/body/center/table/tbody/tr[2]/td'
        while len(driver.find_elements_by_xpath(el_waiting)):
            driver.implicitly_wait(1)

        # driver.find_elements_by_tag_name("img")   # Also works
        p_captcha1 = '/html/body/form/table/tbody/tr[8]/td/div/fieldset/div[1]/div/label/img'
        p_captcha2 = '/html/body/form/table/tbody/tr[10]/td/div/fieldset/div[1]/div/label/img'

        def try_xpahts(lst):
            for xpath in lst:
                if len(driver.find_elements_by_xpath(xpath)):
                    return driver.find_element_by_xpath(xpath)

            raise ValueError()

        el_captcha = try_xpahts([p_captcha1, p_captcha2])

        if 0:
            # Might not work as it updates constantly
            img_url = el_captcha.get_attribute('src')
        elif 0:
            filename_captcha_temp = 'C:/Users/Laurens_laptop_w/Downloads/captcha_temp.png'
            el_captcha.screenshot(filename_captcha_temp)
        else:
            png = el_captcha.screenshot_as_png
            im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
            arr = np.asarray(im)

        s_captcha = captch_solver(arr)

        # TODO put in and press enter

        if 1:
            el_captcha_input = '//*[@id="code"]'
            driver.find_element_by_xpath(el_captcha_input).send_keys(s_captcha)

        if 1: # Press enter
            p_submit1 = '/html/body/form/table/tbody/tr[8]/td/div/fieldset/div[2]/div/input[2]'
            p_submit2 = '/html/body/form/table/tbody/tr[10]/td/div/fieldset/div[2]/div/input[2]'

            el_submit = try_xpahts([p_submit1, p_submit2])

            el_submit.click()

        import pytesseract
        """
        https://github.com/UB-Mannheim/tesseract/wiki
        https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
        """
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Laurens_laptop_w\AppData\Local\Tesseract-OCR\tesseract.exe'

        plt.imshow(arr)
        plt.show()

        b = cleanup(arr)
        plt.imshow(b)
        plt.show()

        pytesseract.image_to_string(im,
                                    #lang='fra'
                                     )


        # Fill in Captcha
        
        # Captcha solver
        if 1:
            from captcha_solver import CaptchaSolver

            solver = CaptchaSolver('browser')
    
            # raw_data = open(img_url, 'rb').read()

            import requests
            response = requests.get(img_url)
            response.content
            print(solver.solve_captcha( response.content))

        # Click *Do it*


if __name__ == '__main__':
    main()