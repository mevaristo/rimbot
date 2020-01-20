class Worker:
    """
    Class used to represent a working robot and all of 
    the attributes for it to work. 

    ...

    Attributes
    ----------
    url : str
        lorem ipsum
    hash : str
        dolor sit amet

    Methods
    -------
    getHash(url=url)
        consectetur
    """

    url = ""
    hash = ""


    def __init__(self, url: str, hash = ""):
        """
        """
        super().__init__()

        self.url = url
        self.hash = hash
    
    
    def getHash(self, url = url):
        """
        """
        pass