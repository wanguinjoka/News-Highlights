class Article:
    '''
    source class ito define source objects
    '''
    def __init__(self,source,author, title, description,url,urlToImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    '''
    source class ito define source objects
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id= id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
