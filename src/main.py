from transform import (
    get_csv, 
    remove_redundant_index,
    remove_space, 
    replace_null, 
    create_launch_note, 
    clean_launch_year, 
    create_ship_type, 
    clean_ship_type, 
    create_navy, 
    create_navy_acronym
)


def convert_to_csv(ships_df) :
    ships_df.to_csv("output/ww2_ships.csv", index=False)


def print_summary(ships_df) :
    print(ships_df.describe(include="all"))


def main() :
    ships_df = get_csv()

    # Clean the existing df
    ships_df = remove_redundant_index(ships_df)
    ships_df = remove_space(ships_df)
    ships_df = replace_null(ships_df)


    # New Columns
    ships_df = create_launch_note(ships_df)
    ships_df = clean_launch_year(ships_df)

    ships_df = create_ship_type(ships_df)
    ships_df = clean_ship_type(ships_df)

    ships_df = create_navy(ships_df)
    ships_df = create_navy_acronym(ships_df)

    print_summary(ships_df)
    convert_to_csv(ships_df)


if __name__ == "__main__" :
    main()