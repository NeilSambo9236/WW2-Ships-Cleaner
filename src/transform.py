import pandas as pd


navy_classification = {
        "Australia": ("Royal Australian Navy", "RAN"),
        "Canada": ("Royal Canadian Navy", "RCN"),
        "China": ("Republic of China Navy", "ROCN"),
        "Finland": ("Finnish Navy", "FNM"),
        "France": ("French Navy", "MN"),
        "Germany": ("Kriegsmarine", "KM"),
        "Greece": ("Hellenic Navy", "HN"),
        "Italy": ("Regia Marina", "RM"),
        "Japan": ("Imperial Japanese Navy", "IJN"),
        "Netherlands": ("Royal Netherlands Navy", "RNN"),
        "Norway": ("Royal Norwegian Navy", "RNoN"),
        "Poland": ("Polish Navy", "PMW"),
        "Russia": ("Soviet Navy", "VMF"),
        "United Kingdom": ("Royal Navy", "RN"),
        "United States": ("United States Navy", "USN")
    }


def get_csv() :
    return pd.read_csv("data/ships.csv")


def remove_redundant_index(ships_df) :
    return ships_df.drop(columns="Unnamed: 0")
 

def remove_space(ships_df) :
    # Get all cells and remove space
    return ships_df.map(lambda x: x.strip())


def replace_null(ships_df) :
    return ships_df.map(
        # Make the cell a null if the condition is true
        lambda x: pd.NA 

        # Finds a cell that is an empty string or a space
        if x in ("", " ") else x)


def create_launch_note(ships_df) :
    # Get all the texts after the year and put it in a new column
    ships_df["Launch Note"] = ships_df["Launch Year"].str.extract(r"\d{4}\s*(.*)")

    # If an empty string was extracted, put "Actual" instead
    ships_df.loc[ships_df["Launch Note"] == "", "Launch Note"] = "Actual"

    # If Launch Year is null, input "No Data" in Launch Note column
    ships_df.loc[ships_df["Launch Year"].isna(), "Launch Note"] = "No Data"
    
    return ships_df


def clean_launch_year(ships_df) :
    # Replace the Launch Year values to be just the year
    ships_df["Launch Year"] = ships_df["Launch Year"].str.replace(r"(\d{4}).*", r"\1", regex=True)

    # If Launch Year is an empty string, put null instead
    ships_df["Launch Year"] = ships_df["Launch Year"].replace("", pd.NA)

    # Convert the year that is a string to be int
    ships_df["Launch Year"] = ships_df["Launch Year"].astype("Int64")

    return ships_df


def create_ship_type(ships_df) :
    # Get the ship type via extracting what's after "...-class"
    ships_df["Ship Type"] = ships_df["Class"].str.extract(r"-class (.*)")

    return ships_df


def clean_ship_type(ships_df) :
    # If it is null, put "No Classification"
    ships_df.loc[ships_df["Ship Type"].isna(), "Ship Type"] = "No Classification"

    # Arrange the column placement of "Ship Type" to be third
    ship_type = ships_df.pop("Ship Type")
    ships_df.insert(2, "Ship Type", ship_type)

    return ships_df


def create_navy(ships_df) :
    # Get the navy where the ship belonged based on navy_classification dictionary
    ships_df["Navy"] = [navy_classification[country][0] for country in ships_df["Country"]]

    # Arrange the column placement of "Navy" to be fourth
    navies = ships_df.pop("Navy")
    ships_df.insert(3, "Navy", navies)

    return ships_df


def create_navy_acronym(ships_df) :
    # Get the navy acronym based on navy_classification dictionary
    ships_df["Navy Acronym"] = [navy_classification[country][1] for country in ships_df["Country"]]

    # Arrange the column placement of "Navy Acronym" to be fifth
    navy_acronyms = ships_df.pop("Navy Acronym")
    ships_df.insert(4, "Navy Acronym", navy_acronyms)

    return ships_df