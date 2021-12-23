from more_itertools import chunked


class Bingo():

    def __init__(self, input_data):
        self.tables = []
        self.shadow_tables = []
        self.entries = []

        data = input_data.split('\n')
        entries = data[0].rstrip().split(',')
        self.entries = [int(x) for x in entries]
        del(data[0])
        data = [d for d in data if d]
        data = list(chunked(data, 5))

        for line in data:
            table = []
            s_table = []
            for row in line:
                values_row = row.split(' ')
                table.append([int(v) for v in values_row if v])

            self.tables.append(table)

        for tbl in self.tables:
            table = [[0] * len(_) for _ in tbl]
            self.shadow_tables.append(table)
    
    def mark_shadow(self, entry):
        for tbl, table in enumerate(self.tables):
            for rw, row in enumerate(table):
                if entry in row:
                    col = row.index(entry)
                    self.shadow_tables[tbl][rw][col] = 1
    
    def run_entries(self):
        for entry in self.entries:
            self.mark_shadow(entry)
            if self.bingo():
                return self.get_value()
        
        return False

    def bingo(self):
        for table in self.shadow_tables:
            for row in table:
                if all(row):
                    return True
                
        columns = [list(x) for x in zip(*self.shadow_tables)]
        columns = [[_[0]][0] for _ in columns]
        
        for col in columns:
                if all(col):
                    return True
        
        import ipdb; ipdb.set_trace()
        return False
    
    
    def get_value(self):
        pass
