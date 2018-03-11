def sort_contacts(contacts):
    updated_contacts=[]
    function_keys=contacts.keys()

    for key in sorted(function_keys):
        data = (key, contacts[key][0], contacts[key][1])
        updated_contacts.append(data)

    return updated_contacts


