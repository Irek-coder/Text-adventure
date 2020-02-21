class Item():
    def __init__(self, item_name):
        self.name=item_name
        self.description=None

    def set_description(self,item_description):
        self.description=item_description

    def set_name(self,item_name):
        self.name=item_name

    def describe(self):
        print(self.description)

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def give_name(self):
        print(self.name)
        
    def get_details(self):
        self.give_name()
        self.describe()
        
