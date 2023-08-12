def split_string(stringsplit):

    parts = stringsplit.split('_')

    if len(parts) != 3:
        raise ValueError("Encoded string must contain exactly 3 parts separated by underscores.")

    dom_dict = {
        "name": parts[0],
        "domain": parts[1],
        "register_number": parts[2]
    }

    return dom_dict

encoded_string = "Ansh_UniversityManagementSystem_2347212"
dec_dict = split_string(encoded_string)
print(dec_dict)

