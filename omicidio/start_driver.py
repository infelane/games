from selenium import webdriver


from omicidio.config import keys

def main():
    driver = webdriver.Chrome('./chromedriver')     # python
    
    driver.get(keys['url'])

    url = driver.command_executor._url  # "http://127.0.0.1:60622/hub"
    session_id = driver.session_id  # '4e167f26-dc1d-4f51-a207-f761eaf73c31'

    print(url)  # http://127.0.0.1:58260
    print(session_id)   # b598cdaae97a1172be93edd1d0b20dad

    print("Please login")

    input('Enter anything to stop')


if __name__ == '__main__':
    main()