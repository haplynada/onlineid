import pandas as pd


def check_country(country_provided: str):
    file_path = "/Users/bjarke/Documents/Noroff/DF1/0. Studio/OnlineID/test/country_and_zip_code/country_codes.xlsx"
    df = pd.read_excel(file_path)
    country = country_provided.capitalize()
    guery_text = "country == ['"+country+"']"
    query = str(guery_text)
    code = df.query(query).head()
    code_string = str(code)
    country = code_string.split(" ")
    return country[7], country[18]


def check_zip_code(country_provided: str, zip_code: int):
    country = country_provided.capitalize()
    path = "/Users/bjarke/Documents/Noroff/DF1/0. Studio/OnlineID/test/country_and_zip_code/"+country+".xlsx"
    df = pd.read_excel(str(path))
    city = df.loc[df["zip_code"] == zip_code]
    comparison = (((str(city.isin([zip_code]))).strip(" ")).split(" "))
    if comparison[0] != "Empty":
        if comparison[9] == "True":
            return True
        else:
            return False
    else:
        return "No such zip-code"


if __name__ == "__main__":
    print(check_country("DENMARK"))
    print(check_zip_code("DENMARK", 9000))