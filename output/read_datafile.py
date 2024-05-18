def read_datafile(filepath):
    from initial.read_data import ReadLmpData
    Tot_data = ReadLmpData(filepath)
    Tot_data.run_read()
    return Tot_data