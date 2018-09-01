class Article:
    '''
    source class ito define source objects
    '''
    def __init__(self,author, title, description,url,urlToImage,publishedAt):
        # self.id= id
        # self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
