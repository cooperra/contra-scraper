from . import yaml, tsv

def load_file(filename):
    format_choices = {"yaml": yaml, "tsv": tsv}
    remaining_format_choices = set(format_choices.keys())
    format = guess_format(filename)
    remaining_format_choices.remove(format)
    while True:
        try:
            data = format_choices[format].load_file(filename)
        except Exception as e:
            if len(remaining_format_choices) > 0:
                # Load failed; try another format
                format = remaining_format_choices.pop()
            else:
                # Out of formats; fail
                raise e
        else:
            # Successful load
            break

    if format == 'tsv':
        # Do tsv-specific enhancements
        # Helps match yaml output's structure
        data = tsv.Loader.flattened_dict(data, "dances")
        data = tsv.Loader.with_field_names(data, ["code", "lo", "ti", "au", "fo", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5"], "dances")
        for dance in data["dances"]:
            # "code" is redundant
            del dance["code"]

    return data

def guess_format(filename):
    f = open(filename)
    line = f.readline()
    # Find first non-empty line
    while len(line) <= 1 and line != "":
        line = f.readline()
    if line == "":
        # Default to tsv if file empty
        return "tsv"
    elif line.startswith("#<"):
        return "tsv"
    elif line.find(":") != -1:
        return "yaml"
    else:
        # If no noticable pattern, just use tsv
        return "tsv"
