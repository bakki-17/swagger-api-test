from faker import Faker
from faker.providers import DynamicProvider



class DataGenerator:
    def __init__(self) -> None:
        dynamicToolsName = DynamicProvider(
            provider_name="tool_name",
            elements=["Bosch ", "Dewalt", "Stanley", "Makita", "Milwaukee", "Craftsman"],
            )
        dynamicToolsName2 = DynamicProvider(
            provider_name="tool_name2",
            elements=["Tools 1", "Tools 2", "Tools 3", "Tools 4", "Tools 5"],
            )
        self.fake = Faker()
        self.fake.add_provider(dynamicToolsName)
        self.fake.add_provider(dynamicToolsName2)


    def generate_new_brand(self):
        return { "name": self.fake.tool_name() + " " + self.fake.tool_name2(),
                "slug": self.fake.bothify(text='????-???##', letters='ABCDE') 
                }
