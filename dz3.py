class City:
    def __init__(self, name, region, country, inhabitants, postal_code, area_code):
        self.name = name
        self.region = region
        self.country = country
        self.inhabitants = inhabitants
        self.postalCode = postal_code
        self.areaCode = area_code

    def info(self):
        print(f"name:{self.name}")
        print(f"region:{self.region}")
        print(f"country:{self.country}")
        print(f"inhabitants:{self.inhabitants}")
        print(f"postal_code:{self.postalCode}")
        print(f"area_code:{self.areaCode}")

inf = City(name="Ivano-Frankivsk", region="Ivano-Frankivsk", country="Ukraine", inhabitants="230 507", postal_code="76-78xxx", area_code="+380-34")
inf.info()