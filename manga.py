import requests


class VkManga:

    def __init__(self, domain):
        self.domain = domain
        self.token = "#"
        self.version = 5.131
        self.offset = 1
        self.response = None
        self.links = []

    def get_data(self):
        response = requests.get(
            "https://api.vk.com/method/wall.get",
            params={
                "access_token": self.token,
                "v": self.version,
                "domain": self.domain,
                "offset": self.offset
            }
        )

        self.response = response.json()['response']['items']

    def get_links(self):
        import time
        time = int(time.time())
        for link in self.response:
            if time - link['date'] < 345_600 and len(link['attachments']) == 3 and link['donut']['is_donut'] == False:
                self.links.append(link['attachments'][2]['link']['url'])
            elif time - link['date'] > 345_600:
                break


    def check_attachments(self):
        if self.domain == 'darkfraction':
            import time
            time = int(time.time())
            for link in self.response:
                if time - link['date'] < 345_600 and len(link['attachments'])==1:
                    self.links.append(link['attachments'][0]['link']['url'])



    def get_text_links(self):

        with open("manga4.html", "a") as file:
            file.writelines(f"{link} \n" for link in self.links)






if __name__ == "__main__":
    groups = ("#", "#", "#")
    for group in groups:
        post = VkManga(group)
        post.get_data()
        post.check_attachments()
        post.get_links()
        post.get_text_links()


